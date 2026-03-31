# 2位解法の日本語要約

原文: `solutions/2nd/2nd_place_solution.md`  
参照元: <https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/writeups/2nd-place-data-centric-akkadian-nmt>

## 概要

2位チーム `wukeneth` の解法は、モデル改良ではなく **データ構築を主戦場にした ByT5-large 単騎構成** です。  
モデル自体は `google/byt5-large` のままで、スコア改善の主因は次の3点でした。

1. 公式データから sentence pair を再構成する **3段階 LLM パイプライン**
2. 公式配布外の **学術 PDF を大量に発掘して OCR/抽出**
3. 出典ごとの差が大きい転写表記を揃える **強い正規化**

提出スコアは **Public 41.9 / Private 41.0**。  
一方で、公開 LB の最高到達は 42.4 まで行ったが、private では崩れたため、最終的にはより安定な run を選んだと書かれています。

## この解法の中心

### 1. 公式データの sentence-level 再構成

このチームは、公式ファイルをそのまま full document 翻訳として学習するのではなく、sentence-level pair に落とし直しています。  
そのために published texts を3集合に分け、集合ごとに別の処理をしています。

| 集合 | 定義 | 役割 |
| --- | --- | --- |
| Breaker | `(U_train ∪ U_pub) − S_meta` | きれいな full translation を文単位に分割 |
| Fixer | `S_meta` | 既存断片の誤対応を OARE API で再アンカー |
| Generator | `U_pub − (U_train ∪ S_meta)` | 形態論情報だけから英訳を生成 |

- **Breaker**  
  `train.csv` の全文英訳と OARE API の単語位置情報を使い、LLM に sentence chunk と `word_range` を振らせる。  
  結果は **1,558 documents → 9,378 sentence pairs**。
- **Fixer**  
  `Sentences_Oare_FirstWord_LinNum.csv` の断片を信用しすぎず、OARE API の `normalized_form`, `word_index`, `line_number` を使って再構成。  
  結果は **1,416 documents → 11,302 sentence pairs**。
- **Generator**  
  形態論情報だけで pseudo translation を作る案。  
  これは **ノイズが強すぎてスコア悪化** したため破棄。

実質的に効いたのは **Breaker と Fixer** で、公式データを「文対応つきの監督データ」に変換し直したのが基盤です。

### 2. 外部学術データの大規模追加

最大の改善源はここです。  
competition 提供の PDF 群に加えて、Old Assyrian の論文・紀要・モノグラフを自前で発掘し、OCR + LLM 抽出で学習データ化しています。

- 追加ソースは **149 distinct sources**
- 追加 sentence pair は **60,654**
- 対象は AKT シリーズ、ArAn、Belleten、DTCF、ATDD/TAD、HAL、各種国際誌、モノグラフなど

特に重要なのは、**PDF 側は元から transliteration と translation が近接して載っているので、Breaker のような再分割工程が不要** という点です。  
つまり、外部データは比較的素直に sentence pair として回収でき、量の拡張に直結しています。

### 3. 非英語論文も英訳して吸収

追加ソースにはトルコ語・ドイツ語・フランス語論文が多く含まれます。  
このチームは抽出時にそれらを **直接英訳** して、最終的な学習形式を一貫して `Akkadian -> English` に揃えています。

言語別内訳は以下です。

| 言語 | sentence pairs |
| --- | --- |
| Turkish | 27,089 |
| English | 21,683 |
| French | 6,436 |
| German | 5,413 |

ただし、同じ tablet が英語論文とトルコ語/ドイツ語論文に重複する場合は、**英語版を優先して残す dedup** をしています。  
また、非英語ソースは複数回抽出して自然な言い換えの揺れを augmentation として使い、英語ソースは 2x boost して露出量を調整しています。

## 正規化

この解法では、source-side の表記ゆれ吸収をかなり重視しています。  
主なルールは以下です。

- `sz` や `s,` 系を `š` / `ṭ` に寄せる
- 母音 + `2` を acute、母音 + `3` を grave に変換
- 上付き数字 `₄₅₆...` を通常数字へ
- `ʾ`, `ʿ`, `ʼ` を削除
- `ḫ / Ḫ` を `h / H` に変換
- `(d)`, `(ki)` を `{d}`, `{ki}` へ統一

要するに、「論文ごとの綴り差」「OCR 後の表記差」「host の評価系とのズレ」を source 側でできるだけ減らしています。

## 学習データの作り方

学習は sentence pair だけではなく、**連続文を連結した document chunk** も混ぜています。  
chunk 長は **768 bytes** で、これは ByT5-large の `max_source_length=768` と一致するように設計されています。

この発想の狙いは次の3つです。

- 文脈を持たせる
- chunk 境界の違いを augmentation にする
- truncation なしで長さ上限を使い切る

## 学習設定

原文には 3 run の設定が書かれていますが、主な軸は共通しています。

- モデル: `google/byt5-large`
- max sequence length: `768 bytes`
- optimizer: `Adafactor`
- `group_by_length=True`
- weight decay: `0.01`

代表的な run は次の通りです。

### Run 1

- 約 **90,522 pairs**
- `lr=7e-5`
- effective batch size `128`
- `16 epochs`
- Public `41.8-41.9` / Private `40.9-41.0`
- 最終提出に採用

### Run 2

- 同じ約 **90,522 pairs**
- `lr=2e-4`
- effective batch size `256`
- `8 epochs`
- Adafactor に **`β₁=0.9`**
- Public `42.1` / Private `40.9`

### Run 3

- 約 **100,143 pairs**
- `lr=7e-5`
- effective batch size `128`
- `14 epochs`
- Public `42.4` / Private `40.4`

最良 public は Run 3 ですが、private が崩れたため、最終提出はより堅い Run 1 を選んでいます。

## `group_by_length` と学習安定化

この writeup で比較的重要なのは、`group_by_length=True` の副作用を明示している点です。  
長さが似たサンプルを同じ batch に寄せると padding は減る一方で、長い batch が続く区間では勾配スケールが偏り、loss が不安定になりやすいとしています。

それに対して、このチームは **Adafactor の `β₁=0.9` を有効化** して慣性を持たせ、勾配変動を和らげたと述べています。  
長さ bucket を使う実験では、そのまま真似する価値があります。

## 効いたもの

- **Breaker/Fixer による sentence pair 化**  
  公式データから高品質な文単位ペアを作れた。
- **学術 PDF の大規模追加**  
  追加データ量の主因で、最大のスコア改善源。
- **正規化**  
  表記ゆれを吸収し、surface noise を減らした。
- **768-byte document augmentation**  
  文脈とデータ拡張の両方に効いた。
- **Prefer-EN dedup / 非英語の英訳活用 / 英語 source の 2x boost**  
  効果は小さめだがプラス。

## 効かなかったもの

- **形態論情報だけからの Translation Generator**
- **単語辞書ペアの追加学習**
- **PN/GN の fuzzy post-process**

特に post-process については、名前表記が出典ごとに揺れ、ルールを足すほど壊しやすいので、**source OCR が正しければ後処理で直すより学習データ側で吸収すべき** という立場です。

## この解法から読み取れること

この 2位解法のメッセージはかなり明快です。

1. このコンペは **モデル競争よりデータ競争**
2. 公式データはそのまま使うより **sentence pair に再構成して価値を引き出す**
3. 外部ソース追加では、単に量を増やすだけでなく **重複除去・言語統一・表記正規化・露出量調整** が重要
4. public LB を追うと overfit しやすく、**clean で diverse な data mix** のほうが private に効く

## 実験に落とすなら

この repo 観点では、次の仮説が直接つながります。

- `train.csv` / `S_meta` / OARE API を使って **Breaker/Fixer 風の sentence realignment** を再現できないか
- 既存の PDF/OCR 抽出資産を、**英語優先 dedup + source-side normalization** 前提で再編できないか
- sentence 単位だけでなく、**768 byte 前後の chunk 学習** を混ぜたときに CV/LB がどう変わるか
- `group_by_length=True` を使うなら、**Adafactor `β₁=0.9`** の安定化効果を切り分けるべき
- pseudo translation は「何でも足す」ではなく、**形態論だけの弱い生成は切る** 前提で考えるべき
