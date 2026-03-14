# 実験ログ

> このファイルはユーザーが手動で更新します。Codex（エージェント）は参照のみ（書き込み禁止）。

## 実験一覧

| 実験ID | ノートブック名 | ノートブックのバージョン | LBのスコア | CVのスコア | 公開ノートブックか否か | 備考 |
|---|---|---|---|---|---|
| 002-1 | [1]dpc-starter-train-cv5 | 5 | N/A | 0.0052 | No | サブミットに利用するモデルの学習 ,ByT5-smallのCV計算, max_new_tokens 未指定, gradient_accumulation_steps=2, (train/test)batch_size=4, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, epochs=20 |
| 002-2 | [2]dpc-starter-train-v1 | 1 | N/A | N/A | No |  ,ByT5-base, max_new_tokens=512, gradient_accumulation_steps=8, (train/test)batch_size=1, epochs=20 |
| 002-3-4 | [3]dpc-starter-train-cv5-v4-colab | 1 | N/A | mean=16.7967, std=0.7955 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, epochs=10 |
| 002-3-5 | [3]dpc-starter-train-cv5-v5-colab | 1 | N/A | mean=18.4611, std=0.6222 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, epochs=10 |
| 002-3-5-1 | [3-5]dpc-starter-train-cv5-v1-colab | 1 | N/A | mean=18.4316, std=0.3241 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, 観点D1(fem. / sing. / pl. / plural / (?) を英訳 target から除去、ただしen→akk 側は今回あえて未変更), epochs=10 |
| 002-3-5-2 | [3-5]dpc-starter-train-cv5-v2-colab | 1 | N/A | mean=18.2390, std=0.6694 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, 観点D1(fem. / sing. / pl. / plural / (?) を英訳 target から除去、en→akk 側も変更), epochs=10 |
| 002-3-5-3 | [3-5]dpc-starter-train-cv5-v3-colab | 1 | N/A | mean=17.0542, std=0.5552 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, 学習を2段階に変更: Phase1 は従来どおり akk→en + en→akk の multi-task、Phase2 は akk→en のみで追加学習, epochs=10 |
| 002-3-6 | [3]dpc-starter-train-cv5-v6-colab | 1 | N/A | mean=17.7535, std=0.5035 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用,epochs=10 |
| 002-3-6-1 | [3-6]dpc_starter_train_cv5_v1_colab | 1 | N/A | mean=18.1280, std=0.6474 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用, generation_num_beams=3, epochs=10 |
| 002-3-6-2 | [3-6]dpc_starter_train_cv5_v2_colab | 1 | N/A | mean=18.2521, std=0.5509 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用, generation_num_beams=4, epochs=10 |
| 002-3-6-3 | [3-6]dpc-starter-train-cv5-v3-colab | 1 | N/A | mean=18.2609, std=0.5988 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用, バッチ内の最長100未満ならgeneration_num_beams=4で最長100以上でgeneration_num_beams=8, epochs=10 |
| 002-3-6-4 | [3-6]dpc-starter-train-cv5-v4-colab | 1 | N/A | mean=18.1896, std=0.6562 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用, バッチ内でソートした上で最長100未満ならgeneration_num_beams=4で最長100以上でgeneration_num_beams=8, epochs=10 |

## 学習データのキュレーション
| データセットID | ファイル名 | 修正内容 | 備考 |
|---|---|---|---|
| 1 | train.csv | - | Kaggleから提供されたオリジナルの学習データ。ノイズが大量に入っている。|
| 2 | train.curated.v001.xlsx | オリジナルのtrain.csvに、参考情報などを付与しキュレーション作業をしやすくした。| ノイズの修正自体は行なっていない。 |
| 3 | train.curated.v002.xlsx | 6eのPDFの英訳文の抜け落ちの修正、全く異なる転写・英訳文が記入されている場合の修正、一部のイタリック抜けの修正。その他、<gap>抜けや文字起こしミスの修正。 | イタリック抜けの修正に関しては、test.csvも同様な穴抜けがある可能性を考慮すると、修正しない方が良いかもしれない。|

## モデルの学習
### ByT5-base
| 学習ID | ノートブック名 | ノートブックのバージョン | loss | エポック数 | 学習バッチサイズ | GradientAccumulationSteps | 備考 |
|---|---|---|---|---|---|---|---|
| 2-1 | [2]dpc-starter-train-v1 | 5 | 0.189 | 20 | 1 | 8 | train.csvを使った学習。最低限の前処理|
| 2-3 | [2]dpc-starter-train-v3 | 2 | 0.1646 | 20 | 1 | 8 | train.curated.v002.xlsxを使った学習。前処理として、Gap 統一, 連続 <gap> の縮約, 長い小数の短縮, Unicode 下付き数字の正規化を実装。後処理として、注釈除去, PN → <gap>, <gap> の縮約を適用|
| 2-4 | [2]dpc-starter-train-v4 | 1 | 0.1583 | 20 | 1 | 8 | 2-3に加えて、前処理に小数→Unicode分数変換を追加、決定詞正規化 (d)->{d}, (ki)->{ki} と大文字決定詞の括弧除去の追加、略記展開 KÙ.B. -> KÙ.BABBAR、音価記号単純化 Ḫ/ḫ -> H/h の追加、訳文側の / 代替処理（分数は保持）と month ローマ数字→整数化を追加 |
