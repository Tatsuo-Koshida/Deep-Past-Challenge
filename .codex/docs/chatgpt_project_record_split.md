# ChatGPTプロジェクト用: 長文レコード分割ブリーフ

最終更新: 2026-03-19

## このファイルの用途

- ChatGPT の「プロジェクト」に配置し、`train.curated.v002` の**長文レコードを 1024 byte 制約に収まる複数レコードへ分割**するときの共通前提として使う。
- 目的は **transliteration と translation の対応を崩さずに分割すること**であり、**翻訳の修正・意訳・要約**は目的ではない。
- PDF スクリーンショットは、**どこで切ると対応が自然か**を判断する補助証拠として使う。

## 背景

- このコンペでは ByT5 を使っており、Kaggle 実行環境では `max_source_length/max_target_length=1024` 付近が現実的な上限。
- `notebooks/EDA/train.curated.v002_バイト長分布.ipynb` とその出力 CSV によると、`train.curated.v002`（1564 件）では以下の長文が存在する。
  - `transliteration(+prefix)` が 1024 byte 超: **206件（13.17%）**
  - `translation` が 1024 byte 超: **174件（11.13%）**
  - いずれか一方が 1024 byte 超: **213件（13.62%）**
- prefix は `translate Akkadian to English: ` の **31 byte**。したがって source 側は、**生の transliteration が 993 byte を超えると危険**。
- 分位点の目安:
  - `transliteration(+prefix)`: p50=450, p90=1113, p95=1459, p98=1822, p99=2463, max=4570
  - `translation`: p50=416, p90=1068, p95=1390, p98=1750, p99=2424, max=4061

## ChatGPT にさせたい仕事

- 1件のレコードを、**意味対応のある複数ペア**へ分割する。
- 各分割後レコードは、原則として **source/target ともに 1024 byte 未満**を目指す。
- ただし ChatGPT が byte 数を厳密に数えるのは不安定なので、**安全側に倒して 900 byte 前後以下を目標**に切る。
- どうしても自然な切れ目がなく、無理に切ると対応が壊れる場合は、**分割しない**のではなく `needs_manual_review` として返す。

## 絶対ルール

1. **分割であって、書き換えではない**
   - `transliteration` と `translation` の本文は、原則として**入力文字列の部分文字列をそのまま使う**。
   - 語の補完、言い換え、現代英語としての整形、綴り修正はしない。
2. **順序を保存する**
   - 分割後レコードを上から順に連結すると、元の `transliteration` / `translation` の順序が保たれていること。
3. **対応が確認できる境界でしか切らない**
   - 優先する境界:
     - 書簡の定型句の切れ目
     - 列挙項目の切れ目
     - 命令文や叙述文の切れ目
     - 英訳側の文末記号（`.`, `;`, `:`）に対応する箇所
     - 転写側の改行・接続の切れ目・反復定型句の切れ目
4. **数値・固有名詞・品目名をまたいで切らない**
   - 銀量、shekel/mina、人物名、地名、品目列挙を途中で切らない。
5. **不確実なら “保留”**
   - 画像を見ても対応が取れない、原文と train ペアがズレている、途中欠落が疑われる場合は `needs_manual_review` を返す。

## 使ってよい判断材料

- 入力の `transliteration`
- 入力の `translation`
- PDF スクリーンショット
- このファイルに書かれたコンペ前提

使ってはいけないこと:

- 画像に基づく**翻訳の再生成**
- 入力に無い語の補完
- 「たぶんこうだろう」という推測での改変

## コンペ固有の前提

### transliteration 側

- ByT5 は byte-level なので、記号や特殊文字も長さに効く。
- determinatives は `{d}`, `{ki}` など **波括弧ごと意味の手掛かり**なので、分割時に落とさない。
- 欠損表現は `<gap>` / `<big_gap>` に寄っていることがある。これも文字列の一部として保持する。
- `:` `/` `?` `!` などの編集記号はデータ内に残っていることがあるが、この作業では**正規化しない**。

### translation 側

- train 英訳は OCR/LLM 補助由来のため、もともと途中欠落や不自然な引用符を含むことがある。
- そのため、**英訳として読みやすいか**より、**転写との対応が崩れていないか**を優先する。

## 分割判断の実務ルール

### 優先して狙う切れ目

- 挨拶・導入句の直後
  - 例: `a-na ... qí-bi-ma um-ma ... -ma`
- 命令や依頼の節の切れ目
- 品目列挙のアイテム境界
- `all this ...`, `thereof ...`, `if ... then ...` のような英訳上のまとまり
- 同じ構文の反復の境目

### 切らないほうがよい箇所

- 銀量・税率・分数・小数の途中
- 固有名詞と肩書きの途中
- `X with Y`, `belonging to Z`, `son of ...` のような連結の途中
- 引用部の開きと閉じの間

### 画像を見て確認する観点

- 転写の行まとまりと、英訳の段落・文のまとまりが対応しているか
- train の 1 レコードに、PDF 上で明確な段落切れ・列挙切れがあるか
- train 側が PDF とずれている場合、どこからどこまでなら安全に 1 ペアとして切り出せるか

## 出力フォーマット

ChatGPT には **JSON 配列だけ** を返させる。

```json
[
  {
    "record_id": "元レコードID",
    "split_id": "元ID__01",
    "status": "ok",
    "transliteration_chunk": "...",
    "translation_chunk": "...",
    "boundary_reason": "英訳の文末と転写の列挙境界が一致するため",
    "confidence": "high"
  },
  {
    "record_id": "元レコードID",
    "split_id": "元ID__02",
    "status": "ok",
    "transliteration_chunk": "...",
    "translation_chunk": "...",
    "boundary_reason": "thereof 以降で会計項目のまとまりが変わるため",
    "confidence": "medium"
  }
]
```

分割不能または危険な場合:

```json
[
  {
    "record_id": "元レコードID",
    "split_id": "元ID__00",
    "status": "needs_manual_review",
    "transliteration_chunk": "",
    "translation_chunk": "",
    "boundary_reason": "PDFを見ても 1:1 の対応境界を特定できない",
    "confidence": "low"
  }
]
```

### `status` の意味

- `ok`: 分割案を返す
- `needs_manual_review`: 人手確認が必要

### `confidence` の基準

- `high`: PDF と原文の対応が明確で、自然な境界が両側に見える
- `medium`: 境界候補は妥当だが、片側の対応がやや弱い
- `low`: train 原文自体にズレや欠落が疑われる

## ChatGPT への依頼文テンプレート

以下を各レコードごとに投げる。

```md
あなたは Deep Past Challenge 用の学習データ分割アシスタントです。

目的:
- 1件の長文レコードを、transliteration と translation の対応を保ったまま複数レコードへ分割する。
- 分割であって書き換えではない。本文は原則として入力文字列の部分文字列をそのまま使うこと。
- source/target ともに 1024 byte 未満を目指し、厳密計数に自信がない場合は安全側に倒して短めに切ること。
- 不確実なら `needs_manual_review` を返すこと。

絶対ルール:
1. 語の補完・意訳・修正をしない
2. 順序を保存する
3. 数値・固有名詞・引用部を途中で切らない
4. JSON 配列のみ返す

入力:
- record_id: {{RECORD_ID}}
- transliteration:
{{TRANSLITERATION}}

- translation:
{{TRANSLATION}}

- pdf screenshot notes:
{{SCREENSHOT_NOTES}}

出力形式:
- 既定の JSON 配列
```

## スクリーンショットの渡し方

- 1レコードにつき、可能なら **同じページの転写と英訳が見える範囲**を渡す。
- 画像が複数枚になる場合は、ChatGPT へ以下を明記する。
  - `image_1`: 転写上段
  - `image_2`: 英訳上段
  - `image_3`: 下段の続き
- 画像に行番号や段落番号が見える場合は、テキストでも補足する。

推奨する補助メモ:

```md
- PDF: CCT 5, p.123
- 上段左: 転写 1-18 行
- 下段右: 英訳 1-2 段落
- train translation は引用符が崩れている可能性あり
```

## 人手レビューに回すべき典型例

- train の英訳が明らかに途中で切れている
- PDF 上で 1 文に見えるのに train 側だけ複数の話題が混ざっている
- 転写と英訳の item 数が大きくずれる
- OCR 由来と思われる引用符崩れ、重複、欠落が強い
- 1024 byte 未満に収めようとすると、どうしても数値列や固有名詞列を破壊してしまう

## ローカルで後続チェックする項目

- `split_id` ごとの `transliteration_chunk` / `translation_chunk` が空でないか
- byte 長が本当に 1024 未満か
- 分割後チャンクを連結したとき、元文字列の順序が大きく崩れていないか
- `needs_manual_review` の件数が異常に多くないか

## 関連資料

- 長さ分布の根拠: `notebooks/EDA/train.curated.v002_バイト長分布.ipynb`
- 公式の整形方針: `.codex/docs/dataset_instructions.md`
- コンペ制約と評価: `.codex/docs/competition_context.md`
- train 品質改善の全体方針: `.codex/docs/data_quality_playbook.md`
