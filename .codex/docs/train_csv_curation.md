# train.csv 品質改善：運用台帳（SSOT）

`train.csv` の品質改善（ノイズ削減・修正・除外）の意思決定と、更新版 `train.csv`（curated）の置き場所を **再現可能に管理**するためのドキュメント。

- 関連プレイブック: `.codex/docs/data_quality_playbook.md`
- “怪しい行” の自動スキャン: `scripts/scan_train_quality.py`

## 方針（原則）

- **公式配布の `train.csv` は不変（raw 扱い）**：上書きしない
- curated は **常に raw から再生成できる** 形を目指す（最初は手作業でもOK。後で自動化できる余地を残す）
- 変更は「直す」だけでなく、まず **除外（drop）/重み下げ（weight）** も選択肢にする
- 変更理由は **`oare_id` 単位**で追えるように残す（後で取り消せることが重要）

## ファイル配置（推奨）

### 公式データ（raw）

- `data/kaggle/deep-past-initiative-machine-translation/train.csv`

### 更新版（curated）

- 置き場所: `data/curated/deep-past-initiative-machine-translation/train/`
- Git 管理: **各バージョンのCSVを追跡する**

推奨ファイル名（どれかに統一）:

- 日付ベース: `train.curated.2026-03-11.csv`
- 連番ベース: `train.curated.v001.csv`

運用上のおすすめ（Git運用）:

- **WIPの固定名は作らず**、小さくても `vNNN`（または日付）で都度コミットして差分を残す

## 記録の置き場所

- curated の変更履歴（人間が追える台帳）: `.codex/docs/train_csv_curation_log.md`
- 実験結果（CV/LBなど）: `.codex/docs/experiments_log.md`（※ここはユーザー手動更新）
- サブミット履歴: `.codex/docs/submission.md`

## “品質改善” の作業単位（おすすめ）

1. `scripts/scan_train_quality.py` で **レビュー対象候補を作る**
2. 上位から `oare_id` を見て、次のどれかに分類して決める
   - 修正（fix）: 明確に誤りで、正解が確定できる
   - 除外（drop）: 取り違え/欠落が濃厚だが、正解確定が難しい
   - 保留（hold）: 情報不足（原典が引けない、判断不能）
3. curated を更新し、`train_csv_curation_log.md` に **理由と影響範囲**を残す
4. 同じ設定で学習/評価して “効いたか” を確認（結果は experiments_log へ）

## 最低限残すメタ情報（推奨）

- curated ファイル名（スナップショット名）
- raw の参照元（`data/kaggle/.../train.csv` の更新日やzip名）
- 変更件数（fix / drop の件数）
- 変更カテゴリ（truncation / mismatch / gap 正規化 / 数値正規化 など）
- 影響（学習データ件数、平均長、簡易な指標の変化など）
