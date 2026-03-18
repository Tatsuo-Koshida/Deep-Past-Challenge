# Deep Past Challenge（Translate Akkadian to English）公開ノート/コメントからの学び（暫定）

最終更新: 2026-03-15

追記（2026-03-15）:
- Kaggle MCP 経由でコンペ Discussions のスレ/コメントも取得できる状態を確認し、後処理（置換）まわりの “スコアが上がる/下がる” 報告を本メモにも反映した。

> 注意: 本来は Kaggle MCP で公開ノートブック/ディスカッション/コメントを収集したいが、この環境では Kaggle MCP が `Unauthenticated` になり、`authorize` もエラーで進められない。  
> そのため本メモは、Kaggleページのアーカイブ（archive.ph 等）と外部の公開記事を一次ソースとして、現時点で再現性のある範囲だけを整理している。
>
> 手動で採集した Discussions/コメントの一次メモは `.codex/docs/discussion_comments.md` に蓄積する（ここには横断的な学びを要約する）。

追記（2026-02-27）:
- Kaggle MCP の `search_notebooks` / `get_notebook_info` は **この環境でも成功する状態を確認**（少なくとも公開ノートのメタデータ取得と、ノートブックソース（`blob.source`）の参照は可能）。
- 以下「主に使われているモデル」は、上位ノートを `get_notebook_info` で確認した内容を反映した。

追記（2026-02-26）:
- Kaggle MCP の `mcp__kaggle__search_notebooks` は `Unauthenticated` を返し、公開ノートブックのランキング/一覧を取得できない。
- `mcp__kaggle__authorize` は、この環境では tool 側のエラー（invalid_union）で実行できなかった。

---

## 0. 公開ノートで主流のモデル（2026-02-27 時点の観測）

- **主流: ByT5 系（Seq2Seq / `AutoModelForSeq2SeqLM`）**  
  - starter 系（学習/推論）を起点に、推論最適化・アンサンブル・MBR（候補生成→最終選択）へ発展している。
  - 例: `takamichitoda/dpc-starter-train`, `qifeihhh666/dpc-starter-infer-add-sentencealign`, `anthonytherrien/byt-ensemble-script`
- **補助: “翻訳→英語整形” の2段構成（LLM 後処理）**  
  - 例: `hanifnoerrofiq/dpc-byt5-base-flan-t5-base`（ByT5 の出力を Flan-T5(base) で polish）
- **別系統: LLM（CausalLM）を LoRA/SFT で直接翻訳に使う試み**  
  - 例: `rejk11/deep-past-qwen-4b-lora`（Qwen 4B + LoRA）, `xiaoleilian/deep-past-sft-gemma3-training`（Gemma3 4B IT + SFT/LoRA）
- **ByT5 以外の seq2seq も一部で検証**  
  - 例: `rifat963/offline-competition-deep-past-challenge-mbart50`（mBART50 + LoRA、オフライン前提）

### 0.2 サブワード分割（BPE/SentencePiece）に関する “公開物での扱い”

公開ノートの観測範囲では、次の 2 パターンが見られる。

1) **サブワード前提の既存翻訳モデルを使う**（= tokenizer はモデル付属の SentencePiece/BPE をそのまま使う）  
   - 例: `kayamui/starter-baseline-with-google-mt5-small`（mT5）、`kageyama/starter-t5-base-nmt-baseline(-infer)`（T5）、`riti0208/deep-past-nllb-200`（NLLB）、`rifat963/offline-competition-deep-past-challenge-mbart50`（mBART50）。
2) **Akkadian 用の subword tokenizer を自前学習/差し替えする発想**  
   - 例: `kayamui/starter-baseline-with-google-mt5-small` は “Ideas for Improvement” に **「Subword tokenization: custom BPE/SentencePiece」** を明示。  
   - 例: `zhangyue199/dpc-byt5-retrain-tokenizer` は **tokenizer 再学習**をテーマにしている（要: 内容精読）。

ただし、LB 上位（ByT5 系）文脈の公開物では、**ByT5（byte-level） vs サブワード分割の体系的比較（同条件 ablation）**は前面に出ていない印象で、実務的には前処理と推論最適化（生成長・ビーム・MBR 等）に議論が集中している。

### 0.3 「このコンペで subword モデルを作る価値があるか」の暫定判断

結論（暫定）: **“上振れ狙い” の価値はあるが、優先度は高くない**。まず ByT5 系で「生成長/正規化/CVリーク無し」を固めた上で、余力があれば試すのが安全。

根拠（公開物からの推測）:
- Discussions では **subword tokenization がハイフン等で難しくなる**ことが示唆され、LB 上位は **ByT5（UTF-8 byte）**に寄っているという観測もある（`.codex/docs/discussion_comments.md` 参照）。
- 公開ノートでは mT5/T5/NLLB/mBART など subword 前提モデルの利用例や「custom BPE/SentencePiece」提案はあるが、**subword 化が ByT5 を明確に上回る**という公開ablationは目立たない。

試す価値が上がる条件:
- 入力側の表記（`<gap>`, `{d}`, `...`, ハイフン、Unicode/記号）を **正規化して subword が安定する**見込みがある。
- 追加データ（アライン済みなど）で **データ量が増え、語彙学習が効きやすい**。
- 目的が「LB 35.1 の ByT5 公開モデルを超える」で、ByT5 の改善が頭打ちになった。

最小コストの検証案（ablation）:
1) **モデルは既存 subword 系**（mT5/T5/NLLB/mBART）をそのまま使い、tokenizer も付属のまま（まずは “tokenizer学習” を後回し）。
2) 同一 split / 同一前処理 / 同一 decode 設定で ByT5 と比較（生成長を必ず固定）。
3) それでも有望なら、次に **SentencePiece を自前学習**（語彙サイズを小さめから）し、特殊記号は special token として固定して分割破綻を避ける。

### 0.1 よく出てくる “ByT5 のチェックポイント名/パス” 例（=実際にロードされているもの）

公開ノートでは、Hugging Face の “素の ByT5” というより、**fine-tune 済み重みを Kaggle Dataset / Kaggle Model として配布**し、`from_pretrained("/kaggle/input/...")` で読むケースが多い。

- `"/kaggle/input/byt5-akkadian-model"`  
  - Starter 系の学習出力を配布したチェックポイントとして頻出。  
  - 例: `jiexusheng20bz/byt-ensemble`（`MODEL2_PATH` で使用）、`qifeihhh666/dpc-starter-infer-add-sentencealign`（`byt5-akkadian-model` をロード）
- `"/kaggle/input/final-byt5/byt5-akkadian-optimized-34x"`（Dataset: `assiaben/final-byt5`）  
  - 推論最適化ノート（beam/length_penalty 等）で頻出。  
  - 例: `assiaben/akkadian-english-inference-byt5-optimized-34x`, `serariagomes/akkadian-english-byt5-optimized-again`, `yongsukprasertsuk/deep-past-challenge-byt5-optimized`
- `"/kaggle/input/byt5-base-20/byt5-base-akkadian"`  
  - `byt5-base` 系を fine-tune した派生（名称から推定）。  
  - 例: `hanifnoerrofiq/dpc-byt5-base-flan-t5-base`（Stage 1 の翻訳器として使用）
- `"/kaggle/input/dpc-byt5-large/"`（Dataset: `artemgoncarov/dpc-byt5-large`）  
  - `byt5-large` 系を使った推論ノートの例。  
  - 例: `artemgoncarov/lb-28-1-dpc-byt5-large-inference`
- `"/kaggle/input/models/mattiaangeli/byt5-akkadian-mbr-v2/pytorch/default/1"`（Kaggle Model: `mattiaangeli/byt5-akkadian-mbr-v2`）  
  - MBR（Minimum Bayes Risk）推論用にパッケージされた ByT5 派生。  
  - 例: `mattiaangeli/deep-pasta-mbr`
- `".../byt5-base-akkadian_gap3"` のような “gap” 派生  
  - `<gap>` 等の欠損表現の扱い（正規化/タグ化）を意識した派生名が見られる。  
  - 例: `jorapro/nllb-200-simple-training-lb-30`（`model_path` に `byt5-base-akkadian_gap3` が登場）

## 1. これまでのコンペの「流れ」（公開物から推測できる範囲）

### フェーズA: まずは動くベースライン

- **ByT5系（文字レベル）を素直に finetune**するのが入口になっている（転写がノイジーで、サブワード分割が不利になりがち）。
- **SacreBLEU で評価を再現**し、`sqrt(BLEU * chrF++)` の方針を手元で固定する（CV/LB 乖離の原因切り分けの前提）。

### フェーズB: データの癖への対応（前処理/正規化）

- 「転写（transliteration）」側は **編集記号・欠損・区切り記号・Unicode揺れ**が精度ボトルネックになりやすい。
- 「英訳」側も **OCR + LLM 由来のノイズ**がある前提で、過学習/学習不安定の要因になる。

### フェーズC: データ量の実質増量（augmentation / multi-task）

公開ノートでは、以下のような増量が明確に提案されている。

- **アラインされた追加データの取り込み**（トレーニング用ペアを増やす）。
- **双方向データ拡張**（`akk → en` だけでなく `en → akk` も学習させる）  
  - 例: 追加行として `{"translation": transliteration, "transliteration": translation, "direction": "en_akk"}` を作り、`direction` を入力に埋め込む。

### フェーズD: 推論の最適化（ビーム/後処理/アンサンブル）

ノート由来の一般的な到達点は次の通り（本コンペ特有の制約を踏まえる）。

- **ByT5 の生成長は「必ず明示」する**  
  - `Seq2SeqTrainer(predict_with_generate=True)` の評価/推論が `generate` のデフォルトに依存すると、ByT5（byte-level）では出力が極端に短くなって BLEU/chrF がほぼ 0 → `geo_mean≈0` に落ちることがある。  
  - 公開ノート（例: `notebooks/004/dpc-baseline-train-infer.ipynb`）では `generation_max_length=512`（または `max_new_tokens`）を明示している。
- **ビーム探索 + 長さ正規化**（短文/欠損表現が混ざると極端に短い出力に寄りがち）。
- **軽い後処理**（空白/句読点/記号の正規化、`<gap>` 的な表現を導入した場合の整形）。
- **複数 seed / 複数 fold のアンサンブル**（LB 安定化と底上げ）。
- **“英訳の置き換え/言い換え” は LB を下げやすい**（読みやすさ↑でも surface match↓）  
  - Discussions「Post-processing by LLM」では、LLM で英訳を自然な英語にリライトすると **LB が改善せず、むしろ悪化することが多い**という共有がある（例: 単複や言い回しの “正しさ” が BLEU/chrF++ の一致を崩す）。  
  - 参考: `https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664079`
- **数値表記の置換（小数→Unicode分数）は、少なくとも public LB では “ほぼ変わらない/小さい” 報告がある**  
  - 「Unicode Fractions vs Decimals」では、小数→分数の後処理で **LB が変わらない（または僅差で見えにくい）**というやり取りがある（LB 表示の丸め/同点ソートの話も含む）。  
  - 参考: `https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101`
- **固有名詞レキシコン（`OA_Lexicon_eBL.csv`）での “正規化置換” は注意**  
  - lexicon の `norm` が train の英訳表記と一致しない例が多く、host 側も「表記揺れ（transliteration/normalization の両方）がある」と明言しているため、機械的に置換すると **スコアが下がる方向に働く**可能性がある（“正す”＝“一致する”ではない）。  
  - 参考: `https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664905`

---

## 2. 精度改善の方向性（優先度つきの実験アイデア）

### Priority 0: public LB への “最適化” を疑う/避ける

- 公開モデルや公開ノートの上振れは、public LB に対する **多数試行→ベスト選抜**（いわゆる leaderboard overfitting / probing）で起きる可能性がある。
- 例: `assiaben/akkadian-english-inference-byt5-optimized-34x` のコメント欄で、`@samson8 (tg @pansh1n)` が「1日5 submissions で ~33.6LB のモデル群の重みを tuning し続ければ、運が良ければ public LB に overfit できる」と示唆（学習レシピの公開は無し）。
- 対策: **CV の安定性**（GroupKFold、時代/出版物/ジャンルでの分割など）を優先し、public LB だけを見た微調整は最小化する（`.codex/docs/discussion_comments.md` の “Public LB ≠ Private LB” 系メモも参照）。

### Priority 1: 正規化を「固定」してからモデル比較

- **Unicode 正規化**（NFKC + 独自の置換テーブル）を先に決め、転写表記の揺れを抑える。
- **下付き数字（sign index）は“脚注ではなく意味を持つ表記”として残す**  
  - 例: `qí-bi4-ma` は `qí-bi₄-ma`（`₄ → 4`）のプレーンテキスト表現。`bi4` を `bi` に落とすのは情報落ちになり得る。  
  - 方針: Unicode 下付き数字（`₀-₉`）は **通常数字に正規化**し、数字自体は除去しない（Dataset Instructions / Discussion Entry `678899` の “subscript normalization” に整合）。
- **英訳側には OCR/転記由来の脱落が残ることがある**  
  - 例: `um-ma kà-ru-um kà-ni-iš-ma` に対して train の英訳が `Thus Kaniš, ...` となっている行があり、`karum` が落ちている可能性が高い。  
  - 同系統の近傍行では同じ冒頭に対して `Thus karum Kanesh, ...` と訳されており、表記揺れというより **訳語脱落** と見る方が自然。  
  - 方針: PDF/原文スクリーンショットで語が見える場合は、train 英訳を鵜呑みにせず、`oare_id`・出版物・近傍並行例で照合する。
- **「正しい修正」が LB で有利とは限らない**  
  - test / private data にも train と同系統の OCR・転記・整形ノイズが残っている可能性があるため、**学術的に正す補正**は評価分布をずらすリスクがある。  
  - 実務上は、train 修正を次の 2 種類に分けて扱うのが安全:
  - **形式整合**: `<gap>` 統一、`(ki)->{ki}`、下付き数字→通常数字、長い float の短縮など。これは **host 推奨の test 整合**なので比較的安全。
  - **内容補正**: 訳抜け補完、PDF を見ての手修正、固有名詞や制度語の復元など。これは **LB 悪化の可能性があるため ablation 前提**で扱う。
  - 推奨比較:
  - `A`: 生データそのまま
  - `B`: host 推奨の形式整合のみ
  - `C`: 内容補正も含む
  - 同一 split / 同一評価条件で `A/B/C` を比較し、**CV と LB の両方**で採否を判断する。`C` が CV 改善でも LB 悪化なら、evaluation data も noisy である可能性を優先して疑う。
- **編集記号の扱い**を固定する（除去/タグ化/ギャップ置換）。  
  - 単純除去は入力情報を落とすリスクがあるため、まずは「置換タグ化（`<gap>`, `<big_gap>` など）」を比較対象に入れる。
- **determinatives（`{d}` など）**は、全除去より「タグとして残す」方向が安全（固有名詞/地名の手掛かりになり得る）。
- **host（@deeppast）推奨の“test 整合”置換（Discussion Entry `678899`, 2026-02-26）**  
  - Gap 統一: `x`, `[x]`, `…`, `(break)`, `(large break)`, `(n broken lines)` → `<gap>`（重複する `<gap>` も 1 個に正規化）
  - 決定詞の表記合わせ: `(d)` → `{d}`, `(ki)` → `{ki}`, `(TÚG)` → `TÚG`
  - 長い小数の短縮: `1.3333300000000001` → `1.3333`（小数点以下 4 桁）
  - （任意）音価記号の単純化: `Ḫ` → `H`, `ḫ` → `h`
  - （任意）略記の展開: `KÙ.B.` → `KÙ.BABBAR`
  - （任意）Unicode 下付き数字: `₀..₉` → `0..9`
  - （任意）小数→分数: `0.5`→`½`, `0.25`→`¼`, `0.3333`→`⅓`, `0.8333`→`⅚`, `0.625`→`⅝`, `0.6666`→`⅔`, `0.75`→`¾`, `0.1666`→`⅙`
  - 注意: `-gold/-tax/-textiles` の語彙補完は **単純な全文置換を避ける**。Entry `678899` のコメントどおり、`import-tax` や `kutānu-textiles` のような語中ハイフンを壊すため、少なくとも **文字列先頭または空白直後にある `-gold/-tax/-textiles` だけ** を対象にする。
- **CV の split はリークしない形を優先**  
  - sentence alignment / 文分割で 1 doc から複数サンプルを作る場合、ランダム split すると同一 doc 由来サンプルが train/val に跨り、評価が過大になりやすい。`oare_id` 等で GroupKFold するのが無難（ただし LB との乖離が減るとは限らないので要検証）。

### Priority 2: 「方向」トークンを入れた multi-task を標準化

- 公開ノートで明示されている **`direction` 付きの双方向学習**は、少ない変更で効く可能性が高い。
- `akk_en` / `en_akk` を prefix token で入れるか、専用 special token を追加して一貫運用する。

### Priority 3: 外部データ/事前学習の活用（オフライン前提）

コンペはインターネット無効だが、**事前にダウンロードしてノートに同梱**すれば外部データ/モデルは使える。

- **関連コーパス（ORACC 等）で追加事前学習**し、DPC train で finetune。
- **翻訳の style を揃える**（句読点・固有名詞の表記揺れ）ため、英語側の正規化や簡易な再整形を検討。
- **`published_texts.csv`（転写のみ）を “強い翻訳器” で擬似ラベル化して蒸留（teacher→student）**する案は有望だが、運用/規約の注意が多い。
  - 規約面: Overview の “Freely & publicly available external data is allowed” に厳密に合わせるなら、擬似ラベル（翻訳結果）も **第三者が自由に入手できる形**（例: 公開 Kaggle Dataset 等）で用意するのが安全。個人環境で生成して私有のまま持ち込むのは解釈が割れ得る。
  - 実装面: サブミット用ノート内で外部API（GPT等）は呼べない（Internet disabled）。**事前生成→ノートで読み込み**が前提。
  - 品質面: “確度の高いものだけ” を選ぶなら、単発の自己申告 confidence より **自己一貫性/合意**（例: 低温度で複数回翻訳して一致度が高い、別プロンプトでも安定、別モデルでも近い）でフィルタするのが堅い。長さ比/禁止文字/記号崩れ/固有名詞の扱いなどの簡易ヒューリスティックも併用する。
  - 学習面: 擬似データはラベルノイズを含むため、(a) 本物 `train.csv` を常に高比率で混ぜる、(b) 擬似データの loss weight を下げる、(c) curriculum（擬似→本物の順）を比較する、等で “悪化” を避ける。
  - 代替（低リスク）: 翻訳を作らずに `published_texts.csv` で **転写側の追加事前学習（DAPT / continued pretraining）→ supervised finetune**は、規約・品質・再現性の観点で取り回しが良い（公開ノートにも例あり）。

#### 参考: 公開ノートでの `published_texts.csv` の使われ方（2026-03-03 時点の観測）

Kaggle公開ノートのソース確認（Kaggle MCP）で、`published_texts.csv` は主に次の用途で使われていた。

- **(A) 転写コーパスとしての DAPT / continued pretraining**  
  - 例: `kageyama/akkadian-language-modeling-continued-pre-training`（`published_texts.csv` の転写をサンプルして self-supervised 学習）。
- **(B) `AICC_translation` を起点に “追加の並列データ” を作る**  
  - 例: `zhangyue199/dpc-ai-translation-dataset`（aicuneiform.com から英訳を抽出して CSV 化）。  
  - 例: `akkmit/allcaps`（ノート内で “AICC_translation由来のペア” を収集して学習に利用する意図が見える）。
- **(C) 既存の翻訳ソース（PDF/OCR等）と突合して train を拡張**  
  - 例: `seraquevence/dpc-increase-the-train-data-v02`（`published_texts` の転写と翻訳を `excavation_no` などで突合して `train_plus.csv` を作る）。
- **(D) EDA / retrieval の参照コーパス**  
  - 例: `leiwong/deep-past-challenge-eda-extended-dataset`（統計・品質指標・拡張データの提案）。  
  - 例: `hanifnoerrofiq/machine-translation-starter-notebook`（翻訳メモリ/retrieval に `published_texts` を混ぜる設計がある）。

#### 参考: 公開ノートでの `publications.csv` の使われ方（2026-03-03 時点の観測）

`publications.csv` は「PDF を OCR/LLM 補正したページ単位テキスト（`pdf_name,page,page_text,has_akkadian`）」で、**そのままでは転写↔英訳が整列していない**。公開ノートでは主に次の方向で使われていた。

- **(A) 追加の並列データ（転写↔英訳）を“抽出して増やす”発想**  
  - 例: `rohanrk1813/translator-comp-0-30` は「Extract additional training data from publications.csv」を明記し、`publications.csv` と `published_texts.csv` を読み込んで `extract_parallel_texts_from_publications(...)` を呼ぶ構成を含む。  
  - 例: `seraquevence/dpc-increase-the-train-data-v02` は `publications.csv` を読み込み、`published_texts.csv` の転写と、別途用意した翻訳（PDF確認）を突合して `train_plus.csv` を作る方針を示す。
  - 注意: いずれも “突合キー（`pdf_name` / `excavation_no` / 各種ID）” と “ノイズ除去（OCR崩れ/改行/多言語/脚注）” が肝で、雑に混ぜるとラベルノイズで悪化しやすい。
- **(B) EDA/品質把握（どのPDFにどれだけテキストがあるか）**  
  - 例: `angantyr/deep-past-2025-data-analysis-and-cleaning`, `gpreda/akkadian-for-accountants`, `mpwolke/akkadian-by-the-river-of-babylon` は `publications.csv` を読み込み、分布や欠損・重複等を確認する文脈がある。
- **(C) “将来的に抽出できるかも” の提案止まり**  
  - 例: `eunicetu/dataset-overview-starter-baselines` は `publications.csv` からの抽出・アラインを “High impact” として推奨するが、ノート内で実装しているわけではない（紹介/方針提示）。

補足（2026-02-27 / ローカルに保存した公開ノートより）:
- `notebooks/001/akkadian-language-modeling-continued-pre-training.ipynb` は、**翻訳の前に T5-base をアッカド語転写でドメイン適応**させる発想（continued pre-training）。determinatives（`{d}` 等）や `<gap>` を special token にして “分割されにくくする” のは再現しやすい。
- ただしノート内の「span corruption」実装は、T5 の sentinel token を用いた本来の denoising objective ではなく、**入力を壊さず labels 側だけを疎にする**実装に近い（Trainer に投げても学習が意図通りにならない可能性がある）。再実装するなら `DataCollatorForT5MLM` 相当の方式で sentinel 化まで含めて合わせる。

### Priority 4: レキシコン（固有名詞）を「生成時」に効かせる

- データ同梱の固有名詞レキシコンを、推論時に **後処理で置換**するだけでなく、
  - 入力に **候補列を付与**（retrieval augmentation）
  - もしくは **copy 寄り**になる学習（タグ化）で拾いやすくする
 などの方針を比較する。

### Priority 5: 推論チューニング（スコア最適化）

- `num_beams`, `length_penalty`, `max_new_tokens` をメトリクス（BLEU/chrF++）で最適化。
- 公開ノートの観測レンジ（ByT5）: `num_beams=2/4/5/8` が使われている（例: `pheezzyy/byt5-genreprocess-2beams-512`, `llkh0a/dpc-baseline-train-infer`, `kiza123123/trinity-akkadian-sota-v2-0-beam-search-upgrade`, `prayagp1/adaptive-beams-test-v1`）。まずは **4（標準）→ 5（微増）**、計算制約が強ければ **2**、長文で伸びるなら **短文4/長文8** のような適応も候補。
- n-best を保存して、**chrF++ 寄りの rerank**（文字一致が効きやすい）を試す価値がある。
- 公開ノートの実装例では、候補を「beam + sampling」でプールし、**候補同士の sentence-level BLEU（`sacrebleu`）で MBR rerank**する構成がある（例: `mattiaangeli/deep-pasta-mbr`）。モデルを固定したまま取り込める改善として、ローカル提出ノート `notebooks/003/deep-09-mbr-v1.ipynb` に decoding-only で反映（`sacrebleu` が無い場合は文字n-gram F1 にフォールバック）。

#### n-best / MBR rerank（Minimum Bayes Risk）の要点

このコンペ文脈で言われる **n-best/MBR rerank** は、ざっくり「候補を複数出して、候補集合の“合意に近い”1本を選ぶ」推論テクニック。

- **n-best**: `generate()` で最終1本だけでなく **上位 n 個の候補（n-best list）**を返すこと。
  - Hugging Face の例（概念）: `num_beams=B`, `num_return_sequences=n`（通常 `n<=B`）。
- **MBR rerank**: 候補 `y1..yn` を用意し、各 `yi` が他候補とどれだけ似ているか（chrF++ / BLEU 等）を平均して、**平均類似度が最大の候補**を採用する（=候補集合の“代表”を選ぶ）。
  - 直感: 「他の候補たちと最も一致する文は、モデル分布の中心に近い」→ 外れ候補を避けやすい。

注意点:
- 追加コストは概ね **候補生成コスト（n倍近い） + rerank の O(n^2)**（n が大きいと重い）。
- `num_beams` と強く相互作用するので、まずは `max_new_tokens` を固定し、`num_beams`/`n`/`length_penalty` を小さめから調整すると安全。

参考（一次メモ）:
- `.codex/docs/discussion_comments.md` に MBR decoding の言及（例: 「候補を多数生成して chrF++ で合意選択」）を採録済み。

### Priority 6: スロット置換（名詞入れ替え）によるデータ増量（慎重に）

- 2026-03-03 メモ: **安全なスロット（固有名詞・地名・人名・数詞など）に限定し、かつアラインメント高信頼のものだけ**置換して増量するなら試す価値あり。一般名詞の広い入れ替えは（アッカド語側の形態/表記揺れ・英語側の文法/照応崩れで）ラベルノイズ化しやすいので避ける。

---

## 3. 参照した公開ノート/資料（一次ソース）

> Kaggle本体ページはアクセス制限で取得が不安定なため、アーカイブを優先している。

### 公開ノートブック（アーカイブ）

- DPC Starter (Train): `https://archive.ph/Dx7ZF`
  - ByT5 での学習、評価の再現、データ拡張（双方向/アラインメント）の雛形が確認できる。
- DPC Baseline: train+infer: `https://archive.ph/5myze`
  - Starter を参照した train+infer 一体のベースライン（実行の骨格を把握する用途）。

### コンペ外の参考（背景/既存のアッカド語NLP）

- Deep Past Initiative の発表（コンペ背景）: `https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/overview/deep-past-challenge`
- Akkademia（既存のアッカド語→英語モデル/プロジェクト例）: `https://huggingface.co/datasets/Babelscape/akkademia`

---

## 4. 次にやる（このリポジトリでの作業に落とし込む）

1. 前処理の「規約」候補を 2〜3 パターンに固定（`normalize_v1/v2/...`）して ablation 可能にする
2. ByT5 ベースで `direction` multi-task の最小実装を作る（学習/推論/投稿まで）
3. CV の切り方（ランダム vs 類似度グルーピング）を決め、LB 乖離を減らす
