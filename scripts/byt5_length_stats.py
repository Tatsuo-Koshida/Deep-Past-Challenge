#!/usr/bin/env python3
"""
ByT5 用の長さ分布をざっくり把握するユーティリティ。

- ByT5 は（概ね）UTF-8 の「バイト列」を token として扱うため、
  `len(text.encode("utf-8"))` が token 数の近似になる。
- 本スクリプトは `train.csv` の source/target の byte 長を集計し、
  max_length 候補ごとの truncation 率を出す。

NOTE:
- transformers を使わない（オフライン前提・依存最小）
- 近似なので、厳密には special token（eos など）分だけズレることがある
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


def _byte_len(s: str) -> int:
    return len(s.encode("utf-8"))


def _nearest_rank_quantile(sorted_vals: Sequence[int], p: float) -> int | None:
    if not sorted_vals:
        return None
    if p <= 0:
        return sorted_vals[0]
    if p >= 1:
        return sorted_vals[-1]
    k = int(round((len(sorted_vals) - 1) * p))
    return sorted_vals[k]


def _format_int(x: int | None) -> str:
    return "NA" if x is None else str(int(x))


def _ceil_to_multiple(x: int, m: int) -> int:
    if m <= 0:
        raise ValueError("m must be positive")
    return ((x + m - 1) // m) * m


@dataclass(frozen=True)
class LengthStats:
    name: str
    vals: list[int]

    def summarize(self) -> dict[str, int]:
        v = sorted(self.vals)
        qs = {
            "p50": _nearest_rank_quantile(v, 0.50),
            "p90": _nearest_rank_quantile(v, 0.90),
            "p95": _nearest_rank_quantile(v, 0.95),
            "p98": _nearest_rank_quantile(v, 0.98),
            "p99": _nearest_rank_quantile(v, 0.99),
            "max": v[-1] if v else None,
        }
        return {k: int(qs[k]) for k in qs if qs[k] is not None}

    def truncation_rate(self, max_len: int) -> float:
        if not self.vals:
            return 0.0
        return sum(v > max_len for v in self.vals) / len(self.vals)


def _read_lengths(
    csv_path: Path,
    source_col: str,
    target_col: str,
    source_prefix: str,
) -> tuple[LengthStats, LengthStats]:
    src_vals: list[int] = []
    tgt_vals: list[int] = []

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in (source_col, target_col) if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"Missing columns in {csv_path}: {missing}")

        for row in reader:
            src = (row.get(source_col) or "").strip()
            tgt = (row.get(target_col) or "").strip()
            src_vals.append(_byte_len(source_prefix + src))
            tgt_vals.append(_byte_len(tgt))

    return LengthStats(f"{source_col} (+prefix)", src_vals), LengthStats(target_col, tgt_vals)


def _suggest_src_max(src: LengthStats, multiple: int) -> int:
    if not src.vals:
        return 0
    return _ceil_to_multiple(max(src.vals), multiple)


def _suggest_tgt_max(tgt: LengthStats, p: float, multiple: int) -> int:
    if not tgt.vals:
        return 0
    v = sorted(tgt.vals)
    q = _nearest_rank_quantile(v, p)
    assert q is not None
    return _ceil_to_multiple(q, multiple)


def main(argv: Iterable[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--train-csv",
        type=Path,
        default=Path("data/kaggle/deep-past-initiative-machine-translation/train.csv"),
        help="train.csv のパス",
    )
    ap.add_argument("--source-col", default="transliteration")
    ap.add_argument("--target-col", default="translation")
    ap.add_argument(
        "--source-prefix",
        default="translate Akkadian to English: ",
        help="学習時に source の先頭に付ける prefix（byte長も上限に効く）",
    )
    ap.add_argument(
        "--candidates",
        default="512,768,1024,1280,1536,2048",
        help="max_length 候補（カンマ区切り）",
    )
    ap.add_argument(
        "--round-multiple",
        type=int,
        default=128,
        help="推奨値を丸める単位（例: 128 / 256）",
    )
    ap.add_argument(
        "--target-quantile",
        type=float,
        default=0.95,
        help="target の推奨 max_length を決める分位（例: 0.95 or 0.98）",
    )
    args = ap.parse_args(list(argv) if argv is not None else None)

    src, tgt = _read_lengths(
        csv_path=args.train_csv,
        source_col=args.source_col,
        target_col=args.target_col,
        source_prefix=args.source_prefix,
    )

    print(f"train_csv: {args.train_csv}")
    print(f"rows: {len(src.vals)}")
    print(f"source_prefix_bytes: {_byte_len(args.source_prefix)}")
    print("")

    for st in (src, tgt):
        s = st.summarize()
        print(f"[{st.name}] byte length summary (approx. ByT5 tokens)")
        print(
            "  "
            + ", ".join(
                [
                    f"p50={_format_int(s.get('p50'))}",
                    f"p90={_format_int(s.get('p90'))}",
                    f"p95={_format_int(s.get('p95'))}",
                    f"p98={_format_int(s.get('p98'))}",
                    f"p99={_format_int(s.get('p99'))}",
                    f"max={_format_int(s.get('max'))}",
                ]
            )
        )
        print("")

    cand = [int(x.strip()) for x in args.candidates.split(",") if x.strip()]
    print("[truncation rate by max_length]")
    for L in cand:
        sr = src.truncation_rate(L)
        tr = tgt.truncation_rate(L)
        print(f"  L={L:4d}  source_trunc={sr:6.1%}  target_trunc={tr:6.1%}")

    print("")
    rec_src = _suggest_src_max(src, multiple=args.round_multiple)
    rec_tgt = _suggest_tgt_max(tgt, p=args.target_quantile, multiple=args.round_multiple)
    print("[suggested max_length (rule of thumb)]")
    print(f"  max_source_length ~= {rec_src}  (ceil(max(source)) to multiple={args.round_multiple})")
    print(
        f"  max_target_length ~= {rec_tgt}  (ceil(p{int(args.target_quantile*100)}(target)) to multiple={args.round_multiple})"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

