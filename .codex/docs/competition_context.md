# Deep Past Challenge（Translate Akkadian to English）コンペコンテキスト

<!-- コンペの前提知識をまとめ、実験設計・ノート要約の基準に使う。 -->

## 基本情報

- **コンペ名**: Deep Past Challenge - Translate Akkadian to English
- **Host**: Deep Past Initiative
- **Kaggle URL**: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation
- **開始日**: 2025-12-16
- **重要日程（UTC 23:59）**:
  - **Entry/Team Merger 締切**: 2026-03-09
  - **最終提出締切**: 2026-03-23
- **賞金**: 総額 $50,000（上位6位まで: 15k/10k/8k/7k/5k/5k）
- **目的**: 旧アッシリア語（アッカド語の方言）の**転写（transliteration）→英訳**の機械翻訳モデルを作る（`train.csv` は 1,561 ペア。追加で公開テキスト/辞書/OCR資源が同梱）

### 公式説明の「難しさ」の解釈（低資源 + 形態論が複雑）

Kaggle概要の “Akkadian is a low-resource, morphologically complex language where a single word can encode what takes multiple words in English.” は、主に次の難点を指す。

- **低資源（low-resource）**: 教師データが少なく、単語形（活用形）の種類に対して観測回数が足りない → 長尾の語形が多く、汎化が難しい。
- **形態論が複雑（morphologically complex）**: 1語に「語幹 + 複数の文法情報（人称/数/性/格/時制/法/接辞代名詞など）」が乗りやすく、英語では複数語（主語・助動詞・目的語・前置詞など）で表す内容が、入力側では1トークン相当に圧縮され得る → アライメントや分割（tokenization）が難しくなる。

## 評価指標（要点）

- **スコア**: `sqrt(BLEU * chrF++)`（BLEU と chrF++ の**幾何平均**）
- **集計方法**: それぞれの指標の十分統計量を**コーパス全体で集計（micro-average）**してから算出
- **実装の指針**: SacreBLEU を参照（Kaggle側の公式評価スクリプト/実装ノートに準拠する）

### BLEU と chrF++ を「どう読めばいいか」

- **BLEU**: *単語 n-gram* の一致度合いを見る指標（ざっくり「単語列としてどれだけ同じか」）。語順・助動詞・前置詞・冠詞・句読点の差でも落ちやすい。
- **chrF++**: *文字 n-gram* の一致度合いを見る指標（ざっくり「綴りとしてどれだけ似ているか」）。固有名詞・地名・数字・表記揺れ（ハイフン/アポストロフ/特殊文字）の影響を強く受ける。
- **幾何平均（`sqrt(BLEU * chrF++)`）の意味**: 片方だけ良くても、もう片方が低いとスコアが伸びにくい（両方の底上げが必要）。

### micro-average（コーパス集計）の注意

- **文ごとに平均するのではなく**、全テキストをまとめた統計量で算出される想定。短文・長文の寄与の仕方が文平均と変わるため、ローカルCVでも「公式と同じ集計」で再現するのが重要。

### 実務的に効きやすいポイント（評価指標目線）

- **表記の一貫性**: 引用符、ハイフン、アポストロフ、空白、数字表記（例: `13 1/3` vs `13.333`）は BLEU/chrF++ の両方を落としやすい。
- **固有名詞**: chrF++ は「文字が近い」ことが効くので、辞書/レキシコンの参照や copy 寄りのデコード（制約付きデコード、後処理）で伸びる余地がある。
- **デコード調整**: `num_beams`, `length_penalty`, `max_new_tokens` などは BLEU/chrF++ に直接効くので、CVでスイープしてから提出する。

## 提出形式

- **提出ファイル名**: `submission.csv`
- **列**: `id,translation`
- **要件**: test の各 `id` に対し、対応する転写の**英訳（1文）**を出力

## コード提出要件（Code Competition）

- **提出は Notebooks 経由のみ**
- **実行時間**: CPU/GPU ともに **9時間以内**
- **Internet**: **無効**
- **外部データ**: **公開で自由に利用できる外部データ/事前学習モデルは利用可**

## 運用上の制約（サブミッション/GPU枠）

- **サブミッション上限**: 1日 **5回まで**
  - **リセット**: 日本時間（JST）**毎日 09:00** に回数がリセット
- **GPU利用枠**: 週あたり **30時間**
  - **リセット**: 日本時間（JST）**毎週土曜日 09:00** に枠がリセット

上記の制約を前提に、**ローカル/CVでの検証を主戦場にして提出は絞る**、**GPUジョブはまとめて回して待ち時間と再実行を減らす**など、効果的・効率的に実験を設計する必要がある。

## 公式データ（Data タブで配布されるCSVの意味）

この節は Kaggle MCP と、ローカルに保存した公式データ（`data/kaggle/deep-past-initiative-machine-translation/`、スナップショット: 2026-02-27 時点）を一次情報として整理した。

> 注意: このコンペは **Code Competition** のため、提出時の評価に使われるテストデータは Notebook 実行環境内の「Hidden data」で処理される。`test.csv` / `sample_submission.csv` はフォーマット確認用のサンプルに過ぎない（行数が極端に少ない）。

### 提出に直接関係するファイル

- `train.csv`（1561行 + header）
  - **目的**: 監督学習用（転写→英訳）
  - **列**:
    - `oare_id`: 文/資料単位のID（UUID）
    - `transliteration`: 旧アッシリア語の転写（モデル入力）
    - `translation`: 英訳（教師ラベル）
- `test.csv`（4行 + header）
  - **目的**: 提出フォーマット検証用のサンプル入力（※評価本体は hidden）
  - **列**:
    - `id`: 提出用の行ID（整数）
    - `text_id`: 参照する資料ID（短いID文字列）
    - `line_start`, `line_end`: 該当行範囲
    - `transliteration`: 入力となる転写（抜粋）
- `sample_submission.csv`（4行 + header）
  - **目的**: 提出CSVの雛形
  - **列**: `id,translation`

### 追加データ（辞書・レキシコン・メタデータ）

- `published_texts.csv`（7991行 + header）
  - **目的**: 公開テキスト（楔形文字資料）のメタデータと転写（追加学習/参照用）
  - **主な列**:
    - `oare_id`: OARE上の資料ID（`train.csv` の `oare_id` と同系統）
    - `online transcript`: OARE上のトランスクリプトURL
    - `cdli_id`: CDLI ID（例: `P361099`）
    - `aliases`, `label`, `publication_catalog`, `description`, `genre_label` など（資料説明）
    - `AICC_translation`: AICC（aicuneiform）側の参照URL
    - `transliteration_orig`: 原転写（ギャップなどの表記が生）
    - `transliteration`: 正規化済みらしき転写（モデル入力候補）
- `eBL_Dictionary.csv`（19215行 + header）
  - **目的**: eBL（electronic Babylonian Library）由来の辞書（語→定義）
  - **列**: `word,definition,derived_from`
- `OA_Lexicon_eBL.csv`（39331行 + header）
  - **目的**: Old Assyrian lexicon（語形・正規化・辞書リンク等）
  - **列**:
    - `type`: エントリ種別（例: `word`）
    - `form`: 表層形（転写表記）
    - `norm`: 正規化形
    - `lexeme`: レキシーム
    - `eBL`: eBL辞書へのURL
    - `I_IV`, `A_D`, `Female(f)`, `Alt_lex`: 追加属性（語形分類/派生等）
- `Sentences_Oare_FirstWord_LinNum.csv`（9782行 + header）
  - **目的**: OAREの文分割・行位置・先頭語（索引/特徴量づくり用）
  - **列**:
    - `display_name`: 資料表示名
    - `text_uuid`, `sentence_uuid`: UUID
    - `sentence_obj_in_text`, `first_word_obj_in_text`: テキスト内オブジェクト番号
    - `translation`: 当該文の英訳（ある場合）
    - `first_word_transcription`, `first_word_spelling`, `first_word_number`
    - `line_number`, `side`, `column`: 行番号/面/列

### 出版物/OCRテキスト（追加学習・参照用）

- `bibliography.csv`（907行 + header）
  - **目的**: `publications.csv` に対応するPDFの書誌情報
  - **列**: `pdf_name,title,author,author_place,journal,volume,year,pages`
- `publications.csv`（216602行 + header）
  - **目的**: 出版物PDFの OCR テキストを「ページ単位」で保持（追加学習/検索用）
  - **列**:
    - `pdf_name`: PDFファイル名（`bibliography.csv` とキーで対応）
    - `page`: ページ番号
    - `page_text`: OCR結果（長文）
    - `has_akkadian`: アッカド語っぽい文字列を含むかのフラグ（`true/false`）
- `resources.csv`（291行 + header）
  - **目的**: 研究資源（論文/データ/プロジェクト等）一覧（メタデータ）
  - **列**: `Authors ...`, `Year`, `Title`, `Topics`, `Language/dialect`, `Methods`, `URL`, `Peer-reviewed`, `Type` など（全16列）

## データの性質（このコンペで効く前処理の論点）

### 1) 転写（Transliteration）側のノイズ

- ハイフンで区切られた音節表記に加え、研究者向けの**上付き/下付き/各種記号**が混ざる
- Kaggle側で「Complete Transliteration Conversion Guide」を参照する前提の記載あり

### 2) 英訳（Translation）側のノイズ

- 既存出版物の翻訳・注釈を OCR + LLM でデジタイズした経緯があり、**フォーマット崩れ**が残る
- 固有名詞の正規化が難所になりやすく、対策として**固有名詞レキシコン**が同梱されている（と説明されている）

### 3) モダン注記（翻刻・編集記号）の扱い（除去/置換の推奨）

Kaggleの「Dataset Instructions」には、翻刻・編集由来の記号について以下のような扱い方の提案がある（モデル入力の正規化候補）。

- **除去候補**: `!`（確読）, `?`（不確読）, `/`（行区切り）, `:` や `.`（単語区切り）, `˹ ˺`（部分欠損）, `[ ]`（欠損）など
- **保持しつつ括弧のみ除去候補**: `< >`（挿入）
- **ギャップ表現の置換例**: `[x] -> <gap>`, `… -> <big_gap>`, `[… …] -> <big_gap>`

#### なぜ「正規化/タグ化」で精度が上がり得るか（直感）

- **語彙の分裂を防ぐ**: `’` と `'`、`–` と `-`、`₂` と `2` のように「見た目は同じ/近い」差があると、サブワード分割や学習上は別トークンになりやすく、データ（`train.csv` 1561ペア）が小さいほど学習信号が散って不利になる。
- **同種パターンの“見え方”を揃える**: 欠損表現が `[x]`, `[...]`, `…` のように複数あると、それぞれの出現頻度が下がって学習しにくい。`<GAP>` のような **一貫したプレースホルダ**に寄せると、「欠損がある文」の一般的な翻訳挙動を学びやすい。
- **評価指標への直接効果**: chrF++ は文字 n-gram に敏感なので、不要な記号や表記揺れはそれだけで一致率を落とし得る（BLEU もトークン化のブレで n-gram が壊れる）。

### 4) 文字種の揺れ（Unicode正規化）

データ上に、アッカド語転写でよく使われる拡張ラテン文字・下付き数字などが出現する（例: `š/Š/ṣ/ṭ/ḫ`、下付き `₀-₉`、アポストロフ系文字など）。
同一文字の表記体系（CDLI/ORACC/Unicode）揺れがあり得るため、**正規化テーブルで寄せる**のが基本方針になりそう。

### 5) determinatives（波括弧の決定詞）

波括弧 `{ }` による決定詞（例: `{d}`, `{ki}`, `{lu₂}` 等）があり、意味的に重要な可能性がある。
「除去」するか「タグ化して保持」するかは要検討（ルールベースで一律に落とすと固有名詞・地名等の情報が消える可能性）。

## ベースライン案（ここから実験設計）

### CV 実験の比較ルール（重要）

- **CVの精度比較は、原則として「同じ更新回数」になるように `max_steps` を固定**する（ノートブック間で比較可能にするため）。
- ノートブック改修時に `max_steps` が意図せず変わりやすい（例: `num_train_epochs` へ切替、データ分割/学習データ量の変更、`batch_size` や `gradient_accumulation_steps` の変更で “1epochあたりのstep数” が変化）ため、**改修のたびに `max_steps` が維持されているか確認**する。

- **モデル候補**: 文字レベルに強い ByT5 / mT5 / encoder-decoder 系、または強力な事前学習MTモデルの転移（外部モデル可）
- **前処理**: 編集記号の正規化（除去/置換）、Unicode正規化、ギャップ表現統一、決定詞の扱い方針決め
- **CV**: まずは `id` 単位でランダム分割（リークが疑われる場合はテキスト類似度でグルーピング分割を検討）
- **メトリクス**: SacreBLEU で `sqrt(BLEU * chrF++)` を再現し、コーパス集計（micro-average）で一致確認

## TODO（データ入手後に追記）

- （必要に応じて）`published_texts.csv` の `transliteration` がどの程度「正規化済み」かを定量確認（例: 記号除去率、語彙サイズ差分）
- Kaggle公式のメトリクス実装ノート（BLEU/chrF++のtokenization設定やchrF++の詳細）を手元コードに反映
