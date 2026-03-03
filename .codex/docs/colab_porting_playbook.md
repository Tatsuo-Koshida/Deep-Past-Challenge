# Kaggle → Colab(A100) 移植・高速化プレイブック

このドキュメントは、Kaggle 環境（例: P100）で動いている Notebook を **Google Colab（例: A100 40GB）** に移植し、さらに **CV/学習の計算速度を上げる**ための「よくある改修パターン」を再利用できる形でまとめたものです。

## 0. 対象例（この repo の実例）

- Kaggle 版: `notebooks/002/[3]dpc-starter-train-cv5-v4.ipynb`
- Colab 版: `notebooks/002/[3]dpc-starter-train-cv5-v4-colab.ipynb`

Colab 版で入っている代表的な差分:

- Drive マウントセルの追加
- `INPUT_DIR` を Drive 配下に変更
- `OUTPUT_DIR` を Drive に保存できる形に変更（ノートブック名 + タイムスタンプで自動命名）
- Colab の `transformers` を Kaggle 側に寄せるためのバージョン固定（uninstall + install）
- 学習高速化のための `bf16` / `tf32` など精度・計算設定の追加
- バッチサイズ増加（例: `4 -> 16`）
- エポック数減（例: `20 -> 10`）

## 1. 原則（あとで比較しやすくする）

- **環境差分は “冒頭セル” に寄せる**（Drive、pip、パス、dtype/TF32 など）。学習ロジック本体は極力そのまま残す。
- **Kaggle 版と Colab 版を同一 lineage に置き、ファイル名で区別**する（命名規則は `.codex/docs/notebook_naming_rules.md` を参照）。
- 速度を上げる変更（bf16/バッチ/epoch など）は、**「何を変えたか」だけ追える粒度**で入れる（同時に変更しすぎない）。

## 2. 手順チェックリスト（移植）

### 2.1 Notebook のコピー作成（直接編集禁止の運用）

- Kaggle 版をコピーして Colab 版を作る（元を直接編集しない）。
- 例: `[3]...-v4.ipynb` → `[3]...-v4-colab.ipynb`（`-v<version>` は維持し、末尾で環境を示す）

### 2.2 Colab 冒頭セル（環境セットアップ）

最低限の構成:

1) Drive マウント
```python
from google.colab import drive
drive.mount("/content/gdrive")
```

2) 依存バージョン固定（Kaggle と揃える）

- Colab はプリインが変動するので、**バージョン固定は “再現性” のために必須**。
- 例（実装は `notebooks/002/[3]dpc-starter-train-cv5-v4-colab.ipynb` 参照）:
```bash
!pip uninstall transformers
!pip install transformers==<PINNED_VERSION>
!pip install evaluate sacrebleu
```

3) GPU 確認（意図した GPU か）
```python
import torch
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "NO CUDA")
```

### 2.3 パス差し替え（INPUT/OUTPUT）

**入力**（データ参照）:

- Kaggle: `/kaggle/input/...`
- Colab: Drive 配下にデータを置き、`INPUT_DIR` をそちらへ

```python
INPUT_DIR = "/content/gdrive/MyDrive/Kaggle/Deep_Past_Challenge/data"
train_df = pd.read_csv(f"{INPUT_DIR}/train.csv")
test_df  = pd.read_csv(f"{INPUT_DIR}/test.csv")
```

**出力**（モデル保存）:

- Colab はランタイムが落ちるので、基本は **Drive に保存**。
- 例: 「ノートブック名 + タイムスタンプ」で `OUTPUT_DIR` を自動生成（実例は Colab 版の `Config.OUTPUT_DIR`）。

運用のコツ:

- `OUTPUT_DIR` は **毎回ユニーク**にする（上書き事故を避ける）。
- 生成した `OUTPUT_DIR` をログに出す（あとから探索できる）。

## 3. 手順チェックリスト（高速化）

### 3.1 mixed precision（A100 前提）

Hugging Face Trainer 系の典型:

- `bf16=True`（A100 ならまずこれを試す）
- 速度寄り設定: `tf32=True`

```python
args = Seq2SeqTrainingArguments(
    ...,
    bf16=True,
    tf32=True,
    fp16=False,
)
```

注意:

- `predict_with_generate=True` + `generation_num_beams>1` は **評価が重い**（学習より遅く感じる要因になりやすい）。
- 速度優先で比較だけしたい場合は、暫定で `generation_num_beams=1` や、評価頻度（`eval_strategy`）を下げるのも手。

### 3.2 バッチサイズ（train と eval を分ける）

基本方針:

- `per_device_train_batch_size` は **上げやすい**
- `per_device_eval_batch_size` は **生成評価のVRAM/時間で詰まりやすい**ので、train より小さくしても良い

例:

- train: 16、eval: 4〜16（OOM するならまず eval を下げる）

### 3.3 エポック数（“差分検証” 用に短くする）

- 変更の効き方を見る目的なら、まず `EPOCHS` を落として「早く回す」。
- 収束不足が気になる場合は、あとで epoch を戻す（または early stopping を入れる）。

## 4. よくある落とし穴

- `pip install` 後に挙動が不安定: **Runtime の再起動**が必要なことがある（特に大きいバージョン差がある場合）。
- Drive I/O がボトルネック: ローカル `/content` に一時コピーして学習し、最後に Drive に保存する構成も検討。
- OOM の切り分け: まず `per_device_eval_batch_size` を下げる → 次に `generation_num_beams` を下げる → それでも無理なら train batch を下げる。

## 4.1 「改善が遅く見える」典型原因（epoch と step の非互換）

Kaggle 版と Colab 版で `per_device_train_batch_size` や `gradient_accumulation_steps`、`EPOCHS` を変えると、
**「1 epoch あたりの optimizer step 数」や「総 optimizer step 数」**が変わるため、ログ上の `epoch=1.0` 同士を単純比較できません。

目安:

- optimizer step/epoch はだいたい `n_train / (per_device_train_batch_size * gradient_accumulation_steps)` に比例
- 例: train batch `4`→`16`（4倍）にすると、**1 epoch の step は 1/4** になります
- さらに `EPOCHS` を `20`→`10` にすると、**総 step は 1/8** になります（= 学習更新回数が大幅に減る）

この状態だと「epoch の進み」が同じでも、Colab 版は **更新回数が少ないぶん損失/指標の改善が遅く見える**ことがあります。

比較のコツ:

- 速度比較: 「wall-clock（秒）」で、同じ step 数/同じ `max_steps` まで回す
- 学習挙動比較: できるだけ **effective batch**（`per_device_train_batch_size * gradient_accumulation_steps`）と **総 step** を揃える

## 5. “次回の改修” のための最小メモ

Colab 版を作ったら、最低限これだけ残す（Notebook 内の先頭セルに置くのがおすすめ）:

- GPU 名（`torch.cuda.get_device_name(0)`）
- `transformers` / `torch` のバージョン
- `INPUT_DIR` / `OUTPUT_DIR`
- `bf16/fp16/tf32` と train/eval の batch 設定
- epoch / beam / eval_strategy の設定
