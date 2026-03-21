# ノート・ディスカッション Digest

<!-- 公開ノート・高評価コメントの要約。キャッチアップ時に追記する（既存は削除しない） -->

## 更新履歴

| 日付 | 追加したノート数 | 追加したコメント数 | メモ |
|------|------------------|--------------------|------|
| 2026-03-21 | 0 | 0 | `notebooks/006/lb-35-9-ensembling-post-processing-baseline.ipynb` の推論パイプラインを整理。2つの ByT5 系モデルから **beam search 候補（`num_beam_cands`）+ top-p sampling 候補（`num_sample_cands`）** を生成し、候補を結合→`VectorizedPostprocessor` で表記ゆれ/禁則/重複を正規化→**chrF++（`sacrebleu.metrics.CHRF(word_order=2)`）の候補間合意で MBR rerank** し最終1文を選ぶ。補助機構として bucketed batching、入力長に応じた adaptive beams（短文は beams 半減）、BF16 autocast/BetterTransformer 適用、OOM バッチのスキップ、`checkpoint_freq` ごとの途中CSV保存、空出力のフォールバック文を含む。 |
| 2026-03-19 | 0 | 0 | `notebooks/002/[4-6]submit-notebook-v3.ipynb` をベースに、`notebooks/002/[2-7]dpc-starter-train-v3.ipynb` で学習したモデルを使う submit ノート `notebooks/002/[4-7]submit-notebook-v3.ipynb` を新規作成。前処理/後処理は `[2-7]` に合わせ、提出直前の scoring error 対策（空文字→`<gap>` + `validate_submission`）は `[4-6]` を踏襲。 |
| 2026-03-13 | 0 | 0 | `notebooks/006/lb-35-9-ensembling-post-processing-baseline.ipynb` の前処理/後処理の置換ルールを確認。転写（入力）側は `OptimizedPreprocessor` で `@deeppast` Entry `678899` の推奨（`<gap>` 統一、決定詞 `(d)->{d}`, `(ki)->{ki}`, `(TÚG)->TÚG`、`KÙ.B.->KÙ.BABBAR`、下付き数字→通常数字、小数→Unicode分数、長いfloat短縮、`ḫ/Ḫ->h/H`）をほぼ網羅。追加で `sz->š`, `s,->ṣ`, `t,->ṭ`, 母音+2/3→アクセント等の ASCII→ダイアクリティクス変換、`ʾ` 除去、ダッシュ統一、下付き `ₓ` 除去も実装。出力（英訳）側は `VectorizedPostprocessor` で `PN-><gap>`、月ローマ数字→整数、/による代替訳の片側除去、禁則文字除去、重複語/句の縮約などを実施。 |
| 2026-03-18 | 0 | 0 | `notebooks/002/[2-6]dpc-starter-train-v3.ipynb` から枝分かれして `notebooks/002/[2-6-2]dpc-starter-train-v3.ipynb` を作成。Discussion Entry `678899` と @engricardoperez 氏の指摘に合わせ、`-gold/-tax/-textiles` の置換を **「文字列先頭または空白直後のみ」** に限定。`import-tax` や `kutānu-textiles` のような語中ハイフンを誤置換しない ablation 用。 |
| 2026-03-13 | 0 | 0 | `notebooks/002/[2-1]dpc-starter-train-v2.ipynb` を直接編集。P100のOOM対策として `MAX_LENGTH=256` に短縮し、`gradient checkpointing` を有効化。`loss=0.0` 再発回避のため `fp16/bf16` は無効（FP32維持）。さらに `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` を追加してメモリ断片化を抑制。 |
| 2026-03-13 | 0 | 0 | `notebooks/002/[2-1]dpc-starter-train-v2.ipynb` を直接編集し、mixed precision（fp16/bf16 自動）/ gradient checkpointing / Adafactor のデフォルト有効化を **無効化（FP32 + AdamW）**。Kaggle学習ログで `loss=0.0` / `grad_norm=nan` が出たため、まずは最適化/精度設定の影響を切り分ける。 |
| 2026-03-13 | 0 | 0 | `notebooks/002/[2-1]dpc-starter-train-v1.ipynb` をコピーして `notebooks/002/[2-1]dpc-starter-train-v2.ipynb` を作成。差分は **モデルを ByT5-large（`google/byt5-large`）に切替**し、`fp16/bf16` + gradient checkpointing + Adafactor をデフォルト有効化（VRAM対策）。Kaggleで Internet OFF の場合は `/kaggle/input/...` にローカル重みを置いて `MODEL_NAME_OR_PATH` を差し替える運用を想定。 |
| 2026-03-07 | 0 | 0 | ByT5-base 改善の当面の方針メモ（`notebooks/002/[2]dpc-starter-train-v1.ipynb` 起点）: (1) `google/byt5-base` 直startより、公開で強い既学習重み（例: `byt5-akkadian-model` / `byt5-base-big-data2`）から resume/fine-tune する、(2) `en→akk`（aux）を「英語入力も正規化する」か「2段階学習で最後は `akk→en` のみに寄せる」等で効きを担保する、(3) 数値/分数・`PN/<gap>` 等の表記規約を train/infer で揃える、(4) 現行 `simple_sentence_aligner()` は現行 `train.csv` の形式だと増量になりにくいので改善 or 効果検証を前提化、(5) `fp16/bf16` や実効batchを上げて学習を安定化、(6) `published_texts.csv` を teacher（例: `final-byt5`）で擬似翻訳→蒸留してデータ量を稼ぐ案を検討。 |
| 2026-03-07 | 0 | 0 | `notebooks/002/[2]dpc-starter-train-v1.ipynb` の `simple_sentence_aligner()` が **現行の `train.csv` ではほぼ機能しない**点を確認（transliteration が改行区切りではないため、想定している “英:句点分割 vs akk:改行分割” の文数一致が起きず、実質的に分割・増量されない）。alignment を改善するか、前提を置かずに効果検証する。 |
| 2026-03-06 | 1 | 1 | `notebooks/007/akkadian-english-inference-byt5-optimized-34x.ipynb`（assiaben の推論ノート）を追記。ノートコメント欄の “public LB overfit（多数サブミットでのベスト選抜）” 示唆をメモ。 |
| 2026-03-06 | 0 | 0 | `notebooks/002/[3-5]dpc-starter-train-cv5-v1-colab.ipynb` をコピーして `notebooks/002/[3-5]dpc-starter-train-cv5-v2-colab.ipynb` を作成。差分は **観点Eの追加のみ**で、`en→akk` 側の English input にも `normalize_translation_d1()` を適用。D1 単独版（v1）との差分を `reverse input に D1 を入れるかどうか` だけに固定した ablation 用。 |
| 2026-03-06 | 0 | 0 | `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` から枝分かれして `notebooks/002/[3-5]dpc-starter-train-cv5-v1-colab.ipynb` を作成。差分は **観点D1のみ**（英訳 target / CV metric で `fem.` / `sing.` / `pl.` / `plural` / `(?)` を除去）で、`en→akk` 側の English input は未変更（= 観点Eは混ぜない）。あわせて実行不能だった `traitner` タイポを `trainer` に修正。 |
| 2026-03-06 | 0 | 0 | `notebooks/002/[2]dpc-starter-train-v1.ipynb` をコピーして `notebooks/002/[2]dpc-starter-train-v2.ipynb` を作成。`v5 → v6` の ablation メモから **観点D1のみ**を抽出し、ByT5-base の full-train notebook に実装。差分は **英訳 target の注釈除去（`fem.` / `sing.` / `pl.` / `plural` / `(?)`）**だけで、`en→akk` 側の English input は未変更（= 観点Eは切り分け）。 |
| 2026-03-05 | 0 | 0 | `notebooks/002/[3-6]dpc-starter-train-cv5-v3-colab.ipynb` をコピーして `notebooks/002/[3-6]dpc-starter-train-cv5-v4-colab.ipynb` を作成。差分は **CV評価の DataLoader を入力長でソート**して padding を減らす変更（`AdaptiveBeamSeq2SeqTrainer.get_eval_dataloader()` を上書き）。v3の **adaptive beams（`<100 -> 4`, `>=100 -> 8`）**は維持。 |
| 2026-03-05 | 0 | 0 | `notebooks/002/[3-6]dpc-starter-train-cv5-v2-colab.ipynb` をコピーして `notebooks/002/[3-6]dpc-starter-train-cv5-v3-colab.ipynb` を作成。差分は **CV評価時の生成を adaptive beams（`<100 tokens -> 4 beams`, `>=100 -> 8 beams`）に切替**する変更のみ（`Seq2SeqTrainer.prediction_step()` をサブクラスで上書き）。 |
| 2026-03-05 | 0 | 0 | 公開ノートで「短文は beam 幅を小さく、長文は大きくする（adaptive beams）」実装を確認: `prayagp1/adaptive-beams-test-v1`（`<100 tokens -> 4 beams` / `>=100 -> 8 beams`）に加え、`harukiharada/byt5-optuna-tuning-chunked-beam-search` でも同様に `lengths < 100` を閾値に `num_beams` を切替。 |
| 2026-03-05 | 0 | 0 | `notebooks/002/[3-6]dpc-starter-train-cv5-v1-colab.ipynb` をコピーして `notebooks/002/[3-6]dpc-starter-train-cv5-v2-colab.ipynb` を作成。差分は **`generation_num_beams: 3 → 4` のみ**（`Seq2SeqTrainingArguments`）。CV/推論の探索幅（品質↔計算量/時間）を1点だけ動かす ablation 用。 |
| 2026-03-05 | 0 | 0 | `notebooks/002/[3]dpc-starter-train-cv5-v6-colab.ipynb` から枝分かれして `notebooks/002/[3-6]dpc-starter-train-cv5-v1-colab.ipynb` を作成。差分は **`generation_num_beams: 2 → 3` のみ**（`Seq2SeqTrainingArguments`）。CV/推論の探索幅（品質↔計算量/時間）を1点だけ動かす ablation 用。 |
| 2026-03-05 | 1 | 0 | `notebooks/006/lb-34-9-ensembling-post-processing-baseline.ipynb` を確認。**2モデルの候補（beam + sampling）を合流 → chrF++ の MBR で“合意に近い”1本を選ぶ**推論ノート。`deep-pasta-mbr-v2` 系の前処理（ダイアクリティクス、`(d)->{d}`、`<gap>` 正規化、小数/分数、下付き数字など）と後処理（`PN→<gap>`、月ローマ数字→整数、重複語/句の縮約、禁則文字除去。ただし `/` は保持）を適用。BetterTransformer（optimum）/ BF16 AMP / length bucketing / 適応 beam / OOM バッチスキップ / 200件ごと checkpoint 付きで `submission.csv` を生成。 |
| 2026-03-04 | 0 | 0 | `notebooks/005/lb-28-1-dpc-byt5-large-inference.ipynb` を確認。ByT5-large 推論の**最小構成**で、`model.eval()` / `torch.no_grad()` 以外の省メモリ工夫（FP16/8bit 量子化、`device_map` 分割、dynamic padding、`use_cache` 制御など）は未導入。OOM 時は `BATCH_SIZE` / `num_beams` / 生成長（`max_new_tokens` 等）を下げる、FP16 を検討。 |
| 2026-03-04 | 0 | 0 | 公開ノートの generation 設定（ByT5）観測: `num_beams=2`（`pheezzyy/byt5-genreprocess-2beams-512`）、`num_beams=4`（`llkh0a/dpc-baseline-train-infer` 推論部）、`num_beams=5`（`kiza123123/trinity-akkadian-sota-v2-0-beam-search-upgrade`）、`num_beams=8`（`prayagp1/adaptive-beams-test-v1`。短文は4/長文は8に切替）。 |
| 2026-03-04 | 0 | 0 | `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` をコピーして `notebooks/002/[3]dpc-starter-train-cv5-v6-colab.ipynb` を作成。Entry: `678899` の推奨に合わせ、**translation 側の正規化（fem./sing./pl./plural/(?) 除去、`PN→<gap>`、小数→Unicode分数、month ローマ数字→整数など）**と、**transliteration 側の gap/決定詞（(d)->{d}, (ki)->{ki} など）正規化**を追加。CV 評価時も `normalize_translation()` を preds/labels に適用。ついでに `traitner` タイポを `trainer` に修正。 |
| 2026-03-04 | 0 | 0 | `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` の **前処理/後処理（評価時）** を棚卸し。文分割アライン（英: 句読点、akk: 改行）、transliteration の NFKC + 下付き数字→通常数字 + `<gap>` 正規化（`…` / `x` 系）までで、推論/提出用の後処理はほぼ無し（decode→strip 程度）。 |
| 2026-03-03 | 0 | 0 | `notebooks/002/[3]dpc-starter-train-cv5-v4-colab.ipynb` をコピーして `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` を作成。`notebooks/004/dpc-baseline-train-infer.ipynb` の実装に合わせ、**train を `akk→en` + `en→akk` の prefix multi-task で2倍化**（val は `akk→en` のみで評価）。Fold 内で `Dataset.from_pandas` して `input_text/target_text` を作る方式に変更。 |
| 2026-03-01 | 0 | 0 | `notebooks/002/dpc-starter-train-cv5.ipynb` と `notebooks/004/dpc-baseline-train-infer.ipynb` を比較して、評価が極端に低い主因として **ByT5 での生成長の未指定（`generation_max_length` / `max_new_tokens`）** が濃厚だと判明。Baseline側は `generation_max_length=512` を明示しており `eval_geo_mean` が “数十” になり得る。一方CV5側はデフォルト生成長（短い）に依存し、BLEU/chrF がほぼ 0 になって `geo_mean≈0` に落ちる可能性が高い。加えて Baseline は expanded sentence をランダム split しており、同一ドキュメント由来サンプルが train/val に跨る **リーク**で評価が過大になり得る。追記: 公開ノート側では「サブワード tokenization を自前で作る（BPE/SentencePiece）」の言及はあるが、ByT5 vs サブワードの体系的な比較（ablation）は少なく、上位ノートの主眼は前処理/推論最適化に寄っている印象。 |
| 2026-02-28 | 0 | 0 | 公開ノートで頻出の MBR（Minimum Bayes Risk）デコードを「モデルを変えずに」取り込む方針を採用。`mattiaangeli/deep-pasta-mbr` の実装（候補プール + BLEU系での rerank）を参考に、ローカル提出ノート `notebooks/003/deep-09-mbr-v1.ipynb` に decoding-only で反映（アイデアは1つに限定）。`sacrebleu` がある場合は sentence BLEU、無い場合は文字n-gram F1 で MBR スコア計算にフォールバック。 |
| 2026-02-27 | 0 | 0 | 「主に使われているモデル」観点で上位ノートを追加確認（`get_notebook_info` でソースを確認）。ByT5 系が主流で、mBART50/LLM 後処理/LLM LoRA も一部。 |
| 2026-02-26 | 2 | 0 | Kaggle MCP が未認証/authorize エラーのため、Kaggleページのアーカイブから要約 |
| 2026-02-26 | 0 | 0 | Kaggle MCP で `search_notebooks` を試したが `Unauthenticated`（=公開ノートの一覧取得ができず）。アダプタ側の `Authorization: Bearer:` バグで失敗している可能性が高い（`public_insights.md` 参照） |
| 2026-02-26 | 20 | 0 | Kaggle MCP で `search_notebooks` / `get_notebook_info` が成功。upvote（主）+新しさ（従）で重要ノートをランキングして追記（後述）。 |

## 実験計画メモ: `v5 → v6` の ablation（2026-03-04）

対象（実験ログの状況）:
- `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` → `notebooks/002/[3]dpc-starter-train-cv5-v6-colab.ipynb`
- CV: `mean=18.4611, std=0.6222` → `mean=17.7535, std=0.5035`（平均↓だが安定性↑）
- Entry: `678899`（ホストの “最新データセット更新” に関する推奨）を取り込んだが、複数アイデア同時投入のため寄与が分離できない。

目的:
- **“CV が下がった要因”** と **“効いている正規化”** を切り分けて、以後は 1 観点ずつ積み上げる。

小分け観点（toggle 単位）:
- 観点A（評価だけ）: `compute_metrics()` での `normalize_translation()` 適用 **のみ**（学習データの入出力は v5 のまま）
- 観点B（alignmentだけ）: sentence align の前に translation の軽い掃除（`fem.` 等の `.` を含む注釈が sentence split を壊すのを防ぐ）**のみ**
- 観点C（transliteration 正規化）: 入力側だけ（推奨: 小→大）
  - C1: gap 表現統一（`[x]` / `(break)` 系→`<gap>`、`<gap>` 連続の dedup）
  - C2: 決定詞の整合（`(d)->{d}`, `(ki)->{ki}`, `(TÚG)->TÚG`）
  - C3: `<gap>` 周辺の記号掃除（例: `-<gap>` / `<gap>-`）※誤変換リスクがあるので後回し
- 観点D（translation 正規化）: 目的変数（英訳）だけ（推奨: 小→大）
  - D1: `fem./sing./pl./plural/(?)` 除去（ホストが “test に無い” と明言）
  - D2: literal `PN -> <gap>`
  - D3: 小数→Unicode分数、`month V -> month 5`（表記ゆれ吸収）
  - D4: 辞書的置換（`-gold/-tax/-textiles` や shekel 定型変換）※分布を変えるので後回し
  - D5: スラッシュ代替の片寄せ（`you / she`→片方）※最も事故りやすいので最後
- 観点E（reverse 方向の影響）: `en→akk` 側で translation 正規化を input に使う/使わない（multi-task の入力分布が変わる）

推奨の実施順（最短で原因切り分け）:
1) **A 単独**（“学習が悪化” か “評価の数え方が変わっただけ” かを切る）
2) **D1 → C1 → C2**（Entry: `678899` の趣旨に直結し、比較的低リスク）
3) それでも平均が下がる場合は **E** と **D4** を単独で ON/OFF（影響が大きい可能性）

## メモ: `notebooks/002/[3]dpc-starter-train-cv5-v5-colab.ipynb` の前処理/後処理

### 前処理（データ）

- Train の augmentation は **「英訳の文分割」×「akk の改行分割」**の簡易アラインのみ。英訳を `(?<=[.!?])\\s+` で文分割し、akk を改行で分割して **文数が一致したときだけ** 1:1 のペアに展開（不一致なら元の doc ペアのまま）。展開時は `len(s)>3 and len(t)>3` の最低限フィルタ。
- CV は `GroupKFold` を `oare_id` grouping として使い、doc 単位リークを避ける（=分割の “後処理” ではなく split 設計）。

### 前処理（テキスト正規化/入力整形）

- transliteration のみ `normalize_transliteration()` で正規化:
  - Unicode 正規化 `NFKC`
  - 下付き数字 `₀..₉` → 通常数字 `0..9`
  - 欠損/ギャップ表現の統一: `…` と単独の `x` / `X` 連続（正規表現 `\\b[xX]{1,}\\b`）を ` <gap> ` に寄せる
  - 連続空白を潰して strip
- 入力は自然言語 prefix を付与:
  - `akk→en`: `"translate Akkadian to English: " + normalized_transliteration`
  - `en→akk`: `"translate English to Akkadian: " + translation`
- train は **双方向（`akk→en` + `en→akk`）**で 2 倍化して shuffle（val は `akk→en` のみ）。

### 後処理（評価時）

- `compute_metrics()` 内で、生成 `preds` の異常値対策（logits→argmax、負値→pad、`[0, vocab_size-1]` に clip）→ decode（`skip_special_tokens=True`）→ `.strip()`。
- それ以外の提出用/推論用の整形（記号正規化や `<gap>` 変換、句読点処理など）は入っていない（このノートは train+CV のみ）。

## ローカル派生ノート（ablation）

### `[2-9]dpc-starter-train-v2-colab.ipynb`（`notebooks/002/[2-9]dpc-starter-train-v2-colab.ipynb`）

- 目的: ByT5-base の「どれだけ学習すべきか」を手動で決めずに済むよう、**検証 split（hold-out）で学習量を見積もってから full train** する。
- 骨格: `notebooks/002/[2-9]dpc-starter-train-v1-colab.ipynb` をベースに、train の一部を `oare_id` グループ単位で hold-out して `eval_loss` を監視し、`EarlyStoppingCallback`（patience 既定 `2`）で停止。
- 学習量の決め方: 推定フェーズの `best_step / steps_per_epoch` を `best_epoch_equiv` として算出し、full train の `steps_per_epoch_full` に掛けて `max_steps` を決定（= full train は epoch ではなく step で止める）。
- 出力: 推定用チェックポイントは `Config.OUTPUT_DIR_ESTIMATE`、最終 full-train は `Config.OUTPUT_DIR_FULL` に保存。

### `[2-10]dpc-starter-train-v3-colab.ipynb`（`notebooks/002/[2-10]dpc-starter-train-v3-colab.ipynb`）

- 目的: `notebooks/002/[2-10]dpc-starter-train-v2-colab.ipynb` で得た early-stopping の推定学習量を、**通常の full-train ノートへ固定値として反映**する。
- 反映内容: `v2` 実行結果の `best_step=3000`、`best_epoch_equiv≈9.585`、full-train 換算 `max_steps=3134` を `Config` に転記し、学習は `max_steps=3134` で終了するように変更。
- 意図: early-stopping 用の hold-out / checkpoint 管理を本番学習ノートへ持ち込まず、`v1` 系の単純な full-data 学習を維持したまま学習量だけ最適化する。

### `[3-6]dpc-starter-train-cv5-v2-colab.ipynb`（`notebooks/002/[3-6]dpc-starter-train-cv5-v2-colab.ipynb`）

- 目的: `generation_num_beams` を 1点だけ動かして、**CV の `geo_mean`（BLEU×chrF の幾何平均）**と計算量のトレードオフを見る（評価時に `predict_with_generate=True` を使うため、beam は CV に直撃する）。
- 差分: `notebooks/002/[3-6]dpc-starter-train-cv5-v1-colab.ipynb` → `generation_num_beams: 3 → 4`（他は据え置き）。
- 学習骨格: ByT5（`google/byt5-small`）+ sentence align（英: 句読点、akk: 改行。文数一致時のみ分割）+ `oare_id` GroupKFold（5-fold）+ train を双方向（`akk→en` + `en→akk`）に 2x 化（val は `akk→en` のみ）。
- 正規化: Discussion Entry `678899` に基づく翻訳/転写の軽い正規化（`<gap>`、決定詞 `(d)->{d}`、`PN→<gap>`、小数→Unicode分数、month ローマ数字→整数、`fem./sing./pl./plural/(?)` 除去など。フラグでON/OFF）。
- 主要ハイパラ（抜粋）: `MAX_LENGTH=512`、`epochs=10`、`lr=2e-4`、`weight_decay=0.01`、`per_device_{train,eval}_batch_size=16`、`grad_accum=2`、`bf16=True`（A100想定）、`tf32=True`、`generation_max_length=512`、`generation_num_beams=4`。
- 再現メモ: Colab 上で `transformers==4.57.1` を明示インストール。出力先は Colab の notebook path を拾って timestamp 付き `OUTPUT_DIR` を作り、`{OUTPUT_DIR}/cv5/fold_k/model` と `cv_results.csv` を保存。

### `[4-3-4]submit-notebook-v3.ipynb`（`notebooks/002/[4-3-4]submit-notebook-v3.ipynb`）

- 目的: `notebooks/002/[2-3-4]dpc-starter-train-v3.ipynb` で学習した **ByT5-small**（`fulltrain_byt5-small_multitask`）で推論し、`submission.csv` を作る。
- 元: `notebooks/002/[4-3]submit-notebook-v3.ipynb`（`MODEL_DIR` 既定パスの系統差し替え + 前処理/後処理を train-v3（2-3-4）に一致させる）。
- 入出力: `test.csv`（`/kaggle/input/.../test.csv`）→ `submission.csv`（`/kaggle/working/submission.csv`）。

## ノート一覧

| タイトル | URL | 作者 | アップ投票 | 日付 | 手法の一言 | 要点・使えそうなアイデア | 自分用メモ |
|----------|-----|------|------------|------|------------|---------------------------|------------|
| DPC Starter (Train) | https://archive.ph/Dx7ZF | takamichitoda | （要確認） | （要確認） | ByT5 finetune + augmentation | アライン済み追加データの利用、`akk→en` と `en→akk` の双方向データ拡張（`direction` 付き） | まずはこの骨格を自前コードに写経し、前処理とCVだけ差し替える |
| DPC Baseline: train+infer | https://archive.ph/5myze | llkh0a | （要確認） | （要確認） | Starter を踏襲した train+infer | `generation_max_length=512` を明示（ByT5 で重要）。train 側は `akk→en` に加え `en→akk` を混ぜる双方向データ（multi-task）で増量。 | `notebooks/004/dpc-baseline-train-infer.ipynb` は `byt5-base` + 既学習重み（`/kaggle/input/byt5-akkadian-model`）から再学習。expanded sentence をランダム split して val を作るため、同一 doc 由来の分割サンプルが train/val を跨るリークで評価が過大になり得る点に注意。 |
| Akkadian to English Translation Inference (ByT5 optimized 34x) | https://www.kaggle.com/code/assiaben/akkadian-english-inference-byt5-optimized-34x | assiaben | （要確認） | （要確認） | `final-byt5` 推論設定の整理 | `/kaggle/input/final-byt5/byt5-akkadian-optimized-34x` をロードして推論（例: `num_beams=8`, `length_penalty=1.09`, `max_new_tokens=512`）。入力側で `.../……` を `<big_gap>`, `xx+` や ` x ` を `<gap>` に正規化する関数がある。 | 学習方法はノート内では不明。コメント欄で「学習メモ共有して？」→回答なし。別コメントで「1日5 subs で ~33.6LB モデル群の重みを tuning していると、運が良ければ public LB に overfit できる（=多数試行→ベスト選抜）」との示唆がある。 |
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
- Discussions では「英訳を LLM で自然な英語にリライトする」後処理は **LB を改善せず悪化しがち**という共有がある（読みやすさ↑でも surface match↓）。参考: `https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664079`
- 「小数→Unicode分数」など数値表記の置換は、少なくとも public LB 上は **変化が小さい/見えにくい**というやり取りがある（LB 表示の丸め/同点ソートの話を含む）。参考: `https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101`
- `OA_Lexicon_eBL.csv` を使った固有名詞の置換/検証は、lexicon `norm` と ground truth の表記が一致しない例が多く、機械的な置換は危険。参考: `https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664905`
- 「LLM を主モデルにする」系の試みもあるが、主流とは別系統（計算資源/実装コストが増える）。例: `rejk11/deep-past-qwen-4b-lora`（Qwen 4B + LoRA）、`xiaoleilian/deep-past-sft-gemma3-training`（Gemma3 4B IT + SFT/LoRA）。
- ByT5 以外の seq2seq も一部で検証される。例: `rifat963/offline-competition-deep-past-challenge-mbart50`（mBART50 + LoRA、オフライン実行前提）。
