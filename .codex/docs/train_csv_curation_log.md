# train.csv 品質改善ログ（curation log）

目的: `train.csv` の修正・除外・正規化を **後から再現/取り消し**できる形で記録する。

- 方針・置き場所: `.codex/docs/train_csv_curation.md`

## エントリ書式（テンプレ）

### YYYY-MM-DD Entry: <短いタイトル>

- 対象: `oare_id`（複数なら範囲/リスト）
- 目的:
- 変更種別: fix / drop / normalize / investigate
- 変更内容（要点）:
- 根拠（原典/外部ソース/差分の理由）:
- curated 出力:
  - ファイル: `data/curated/deep-past-initiative-machine-translation/train/<name>.csv`
  - 件数: fix=? / drop=? / total=?

---


