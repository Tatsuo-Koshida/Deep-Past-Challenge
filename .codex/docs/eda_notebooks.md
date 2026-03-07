# EDA notebooks

最終更新: 2026-03-07

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
