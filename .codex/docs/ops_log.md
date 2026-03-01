# Ops log

## 2026-02-28

### Added a Codex skill to mine captured Discussions

- Skill: `skills/discussion-insights-miner/`
- Purpose: triage + extract experiment-ready insights from `.codex/docs/discussion_comments.md`, optionally persisting summaries into `.codex/docs/public_insights.md` / `.codex/docs/notebook_digest.md`
- Helper script: `python3 skills/discussion-insights-miner/scripts/summarize_discussion_comments.py .codex/docs/discussion_comments.md --format md --top-k 50`

## 2026-02-27

### Kaggle official data download (Deep Past Challenge)

- Competition: `deep-past-initiative-machine-translation`
- Destination: `data/kaggle/deep-past-initiative-machine-translation/`
- Method: Kaggle MCP to obtain a signed download URL, then `curl` to fetch `archive.zip` and `unzip` it locally.
- Note: In the default sandboxed shell, DNS/network access was unavailable; the download required running `curl` with escalated permissions.

## 2026-03-01

### ByT5 CV notebook decode crash in Kaggle

- Symptom: running `notebooks/002/[3]dpc-starter-train-cv5-v3.ipynb` hit `ValueError: chr() arg not in range(0x110000)` during evaluation after ~40 minutes.
- Cause: `compute_metrics` called `tokenizer.batch_decode(preds)` with invalid ids (e.g., logits array, negative ids, or out-of-vocab ids). ByT5’s decode path can raise when given out-of-range values (internally uses `chr()`).
- Mitigation: created `notebooks/002/[4]dpc-starter-train-cv5-v4.ipynb` with a defensive `compute_metrics` that (a) converts logits via `argmax` when `preds.ndim==3` and (b) casts to `int64`, replaces negatives, and clips ids to `[0, vocab_size-1]` before decoding.
