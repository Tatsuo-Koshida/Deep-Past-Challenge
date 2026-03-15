# EDA notebooks

最終更新: 2026-03-15

## `notebooks/EDA/train.curated.v002_バイト長分布.ipynb`

- 目的: `train.curated.v002.xlsx` の `transliteration(+prefix)` と `translation` の **UTF-8 バイト長分布**を可視化し、ByT5 の `max_source_length/max_target_length` の候補を決める。
- 対象データ: `data/curated/deep-past-initiative-machine-translation/train/train.curated.v002.xlsx`
- 出力:
  - 分位点（p50/p90/p95/p98/p99/max）
  - ヒストグラム（線形/対数）
  - ECDF（累積分布）
  - `max_length` 候補ごとの truncation 率
  - 最長サンプルのプレビュー（先頭/末尾）

## `notebooks/EDA/英訳冒頭脱落点検.ipynb`

- 目的: `train.csv` の `transliteration` と `translation` を突き合わせ、**英訳冒頭や定型句の脱落候補**を機械的に洗い出す。
- 対象データ: `data/kaggle/deep-past-initiative-machine-translation/train.csv`
- 主な検出対象:
  - `um-ma kà-ru-um kà-ni-iš-ma` があるのに英訳で `karum` が落ちているケース
  - `a-na ... qí-bi-ma` があるのに `Say to ...` が落ちているケース
  - `ṭup-pì-ni ta-ša-me-a-ni` があるのに `As soon as you hear our letter` が落ちているケース
  - `GÍR ša a-šur` があるのに `dagger of Aššur` が落ちているケース
  - `lá i-sa-ḫu-ur` 系があるのに「遅延禁止」命令が落ちているケース
- 実装方針:
  - 転写側の定型句と英訳側の期待表現を **対応表（初版）**としてノートブック内に保持
  - `transliteration` に定型句があるのに `translation` に期待表現が見当たらない行を候補化
  - 自動修正ではなく **review 用 shortlist 作成** が目的
- 注意:
  - 意訳・語順変更・同義表現は誤検出しうる
  - train 英訳は OCR/転記ノイズを含みうるため、確定には PDF / published_texts / 近傍の並行例での再確認が必要

## 運用メモ

- `notebooks/EDA/データの解析.ipynb` とは別用途の、**翻訳脱落検査専用**ノートブックとして追加。
- ルールを増やすときは、まず「転写側の定型句」「英訳側の最低限の期待表現」「誤検出リスク」を 1 行で説明できる形で追加する。
- 実験ログではなく、**データ点検の補助ノート**として扱う。

## `notebooks/EDA/publications候補ページ検索.ipynb`

- 目的: `publications.csv`（PDF名×ページ単位OCRテキスト）を全文検索し、各 `oare_id` に対して **候補 `pdf_name/page` を上位K件**提示する（探索支援）。
- 対象データ:
  - `data/kaggle/deep-past-initiative-machine-translation/train.csv`
  - `data/kaggle/deep-past-initiative-machine-translation/published_texts.csv`（`label`, `cdli_id` などをクエリに利用）
  - `data/kaggle/deep-past-initiative-machine-translation/publications.csv`
- 実装方針:
  - `scripts/publications_candidate_search.py` で SQLite FTS5 インデックスを作成し（`data/index/publications_fts.sqlite`）、`oare_id` ごとに OR クエリで検索して上位候補を返す
  - notebook 側は `show_candidates(oare_id)` で候補と snippet を表示し、ipywidgets が使える場合は簡易UIで **確定結果を `data/index/confirmed_oare_to_publication.csv` に追記**できる
- 注意:
  - ヒットしない/誤ヒットも普通に起きる（OCR品質・表記揺れ・PDF側に当該文字列が無い等）。**最終確定は人手**で行う。
  - `data/index/` 配下のDB/CSVは再生成可能な作業ファイル扱い（git管理しない前提）。
