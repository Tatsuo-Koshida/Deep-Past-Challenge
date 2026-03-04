# ノート・ディスカッション Digest

<!-- 公開ノート・高評価コメントの要約。キャッチアップ時に追記する（既存は削除しない） -->

## 更新履歴

| 日付 | 追加したノート数 | 追加したコメント数 | メモ |
|------|------------------|--------------------|------|
| 2026-03-04 | 0 | 0 | `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` をコピーして `notebooks/002/[3]dpc-starter-train-cv5-v6-colab.ipynb` を作成。Entry: `678899` の推奨に合わせ、**translation 側の正規化（fem./sing./pl./plural/(?) 除去、`PN→<gap>`、小数→Unicode分数、month ローマ数字→整数など）**と、**transliteration 側の gap/決定詞（(d)->{d}, (ki)->{ki} など）正規化**を追加。CV 評価時も `normalize_translation()` を preds/labels に適用。ついでに `traitner` タイポを `trainer` に修正。 |
| 2026-03-04 | 0 | 0 | `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` の **前処理/後処理（評価時）** を棚卸し。文分割アライン（英: 句読点、akk: 改行）、transliteration の NFKC + 下付き数字→通常数字 + `<gap>` 正規化（`…` / `x` 系）までで、推論/提出用の後処理はほぼ無し（decode→strip 程度）。 |
| 2026-03-03 | 0 | 0 | `notebooks/002/[3]dpc-starter-train-cv5-v4-colab.ipynb` をコピーして `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` を作成。`notebooks/004/dpc-baseline-train-infer.ipynb` の実装に合わせ、**train を `akk→en` + `en→akk` の prefix multi-task で2倍化**（val は `akk→en` のみで評価）。Fold 内で `Dataset.from_pandas` して `input_text/target_text` を作る方式に変更。 |
| 2026-03-01 | 0 | 0 | `notebooks/002/dpc-starter-train-cv5.ipynb` と `notebooks/004/dpc-baseline-train-infer.ipynb` を比較して、評価が極端に低い主因として **ByT5 での生成長の未指定（`generation_max_length` / `max_new_tokens`）** が濃厚だと判明。Baseline側は `generation_max_length=512` を明示しており `eval_geo_mean` が “数十” になり得る。一方CV5側はデフォルト生成長（短い）に依存し、BLEU/chrF がほぼ 0 になって `geo_mean≈0` に落ちる可能性が高い。加えて Baseline は expanded sentence をランダム split しており、同一ドキュメント由来サンプルが train/val に跨る **リーク**で評価が過大になり得る。追記: 公開ノート側では「サブワード tokenization を自前で作る（BPE/SentencePiece）」の言及はあるが、ByT5 vs サブワードの体系的な比較（ablation）は少なく、上位ノートの主眼は前処理/推論最適化に寄っている印象。 |
| 2026-02-28 | 0 | 0 | 公開ノートで頻出の MBR（Minimum Bayes Risk）デコードを「モデルを変えずに」取り込む方針を採用。`mattiaangeli/deep-pasta-mbr` の実装（候補プール + BLEU系での rerank）を参考に、ローカル提出ノート `notebooks/003/deep-09-mbr-v1.ipynb` に decoding-only で反映（アイデアは1つに限定）。`sacrebleu` がある場合は sentence BLEU、無い場合は文字n-gram F1 で MBR スコア計算にフォールバック。 |
| 2026-02-27 | 0 | 0 | 「主に使われているモデル」観点で上位ノートを追加確認（`get_notebook_info` でソースを確認）。ByT5 系が主流で、mBART50/LLM 後処理/LLM LoRA も一部。 |
| 2026-02-26 | 2 | 0 | Kaggle MCP が未認証/authorize エラーのため、Kaggleページのアーカイブから要約 |
| 2026-02-26 | 0 | 0 | Kaggle MCP で `search_notebooks` を試したが `Unauthenticated`（=公開ノートの一覧取得ができず）。アダプタ側の `Authorization: Bearer:` バグで失敗している可能性が高い（`public_insights.md` 参照） |
| 2026-02-26 | 20 | 0 | Kaggle MCP で `search_notebooks` / `get_notebook_info` が成功。upvote（主）+新しさ（従）で重要ノートをランキングして追記（後述）。 |

## ノート一覧

| タイトル | URL | 作者 | アップ投票 | 日付 | 手法の一言 | 要点・使えそうなアイデア | 自分用メモ |
|----------|-----|------|------------|------|------------|---------------------------|------------|
| DPC Starter (Train) | https://archive.ph/Dx7ZF | takamichitoda | （要確認） | （要確認） | ByT5 finetune + augmentation | アライン済み追加データの利用、`akk→en` と `en→akk` の双方向データ拡張（`direction` 付き） | まずはこの骨格を自前コードに写経し、前処理とCVだけ差し替える |
| DPC Baseline: train+infer | https://archive.ph/5myze | llkh0a | （要確認） | （要確認） | Starter を踏襲した train+infer | `generation_max_length=512` を明示（ByT5 で重要）。train 側は `akk→en` に加え `en→akk` を混ぜる双方向データ（multi-task）で増量。 | `notebooks/004/dpc-baseline-train-infer.ipynb` は `byt5-base` + 既学習重み（`/kaggle/input/byt5-akkadian-model`）から再学習。expanded sentence をランダム split して val を作るため、同一 doc 由来の分割サンプルが train/val を跨るリークで評価が過大になり得る点に注意。 |
| Akkadian language modeling (continued pre-training) | notebooks/001/akkadian-language-modeling-continued-pre-training.ipynb | （不明） | （不明） | 2025-12-18 | T5-base 追加事前学習（ドメイン適応） | `published_texts.csv` の転写（最大8000件）で self-supervised 学習。determinatives（`{d}` 等）や `<gap>` を special token として追加し、マスク対象から除外 | 「T5のspan corruption」をうたうが、実装は sentinels を使う本来の denoising ではなく “ランダムtokenマスク＋その位置だけ損失” に近い。cleaning 関数がノート内に無い点も注意 |
| DPC-AI-translation-dataset | https://www.kaggle.com/code/zhangyue199/dpc-ai-translation-dataset | zhangyue199 | 16 | 2026-01-06 | `published_texts.csv` から並列データ生成 | `published_texts.csv` の `AICC_translation`（aicuneiform.com 検索URL）を起点に、aicuneiform 側の JSON/HTML を `requests + bs4` で取得して英訳（obverse/reverse）を抽出し、追加の並列CSVを作る | インターネット有効ノート（データ生成用）。提出ノートでは再現できないので、成果物を公開Dataset化して使う想定 |
| DPC \| Increase the Train data V02 | https://www.kaggle.com/code/seraquevence/dpc-increase-the-train-data-v02 | seraquevence | 15 | 2026-02-09 | 翻訳を別ソースから回収して train を拡張 | `published_texts.csv` の転写と、`publications.csv` / PDF 由来の翻訳を `excavation_no` 等で突合して `train_plus.csv` を作る | 参照元と突合キー（`excavation_no`）が肝。重複/スタイル差の扱いが難所 |
| Machine Translation: starter notebook | https://www.kaggle.com/code/hanifnoerrofiq/machine-translation-starter-notebook | hanifnoerrofiq | 99 | 2025-12-17 | retrieval ベースの翻訳 | `published_texts.csv` を読み込み、`train.csv` の翻訳メモリ（TF-IDF/文字・単語類似 + SequenceMatcher）と組み合わせる設計（フラグで切替） | 翻訳モデル無しでの強いベースライン発想。`published_texts` の “翻訳がどこから来るか” を自分のパイプラインに合わせて要確認 |
| AllCaps | https://www.kaggle.com/code/akkmit/allcaps | akkmit | 72 | 2026-01-04 | `AICC_translation` 起点の追加データ化 + 学習 | `published_texts.csv` を起点に “AICC_translation由来のペア” を収集して学習データを増やすコードが含まれる（ノート内で集計/重複除去） | 中身の取得方法（スクレイピング/既存データセット参照）と再現性を要確認（source が長いので必要箇所だけ精読） |
| translator_comp 0.30 | https://www.kaggle.com/code/rohanrk1813/translator-comp-0-30 | rohanrk1813 | 51 | 2026-01-02 | `publications.csv` から追加学習データ抽出（主張） | ノート冒頭で「Extract additional training data from publications.csv」を掲げ、`publications.csv` と `published_texts.csv` を読み込んで `extract_parallel_texts_from_publications(...)` を呼ぶ分岐を持つ | 実際の抽出品質/突合ロジックは精読が必要（関数定義が長い）。提出ノートで回すなら時間制約に注意 |
| Deep Past 2025 - data analysis and cleaning | https://www.kaggle.com/code/angantyr/deep-past-2025-data-analysis-and-cleaning | angantyr | 24 | 2026-01-14 | EDA（データ品質） | `publications.csv` を含む複数CSVをロードし、重複や長さ分布などの品質チェックを行う | 追加学習データ化は目的ではなく、どこが壊れているか/クリーニング方針を得る用途 |


## 横断メモ

（複数ノートに共通するテーマ: リーク指摘・評価指標の実装・よく使われる特徴量など）

- 主流モデルは **ByT5（`AutoModelForSeq2SeqLM`）の finetune / 推論最適化 / アンサンブル**。例: `takamichitoda/dpc-starter-train`, `qifeihhh666/dpc-starter-infer-add-sentencealign`, `anthonytherrien/byt-ensemble-script`（いずれも ByT5 系モデルをロードして推論）。
- サブワード分割（BPE/SentencePiece）については、mT5/NLLB/mBART のような **サブワード系の既存翻訳モデルをそのまま使う**ノートや、「Akkadian 用に SentencePiece を自前学習する」方向性の言及がある。一方で、LB 上位で「サブワード化が効いた」を主張する決定的な公開比較は（少なくとも上位ノートの文脈では）見当たりにくい。
- 推論側の代表的なスコア押し上げアイデアとして **MBR（Minimum Bayes Risk）デコード**が見られる（候補を複数生成し、候補同士の類似度（BLEU/chrF など）で rerank）。例: `mattiaangeli/deep-pasta-mbr`, `mattiaangeli/deep-pasta-mbr-v2`。
- よく参照される ByT5 チェックポイント（fine-tune 済み配布物）の例:
  - `"/kaggle/input/byt5-akkadian-model"`（Starter 系の出力として頻出）
  - `"/kaggle/input/final-byt5/byt5-akkadian-optimized-34x"`（`assiaben/final-byt5`。推論最適化ノートで頻出）
  - `"/kaggle/input/dpc-byt5-large/"`（`byt5-large` 系の例）
  - `"/kaggle/input/models/mattiaangeli/byt5-akkadian-mbr-v2/pytorch/default/1"`（MBR 用の ByT5 派生）
- 「LLM 後処理（polish）」は補助的に使われることがある。例: `hanifnoerrofiq/dpc-byt5-base-flan-t5-base` は **ByT5 翻訳 → Flan-T5(base) で英語整形**の2段。
- 「LLM を主モデルにする」系の試みもあるが、主流とは別系統（計算資源/実装コストが増える）。例: `rejk11/deep-past-qwen-4b-lora`（Qwen 4B + LoRA）、`xiaoleilian/deep-past-sft-gemma3-training`（Gemma3 4B IT + SFT/LoRA）。
- ByT5 以外の seq2seq も一部で検証される。例: `rifat963/offline-competition-deep-past-challenge-mbart50`（mBART50 + LoRA、オフライン実行前提）。
