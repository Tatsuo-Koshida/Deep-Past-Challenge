# 実験ログ

> このファイルはユーザーが手動で更新します。Codex（エージェント）は参照のみ（書き込み禁止）。

## 実験一覧

| 実験ID | ノートブック名 | ノートブックのバージョン | LBのスコア | CVのスコア | 公開ノートブックか否か | 備考 |
|---|---|---|---|---|---|
| 003 | deep-09 | 2 | 33.0  | N/A | Yes | |
| 003-1 | [1]deep-09-mbr-v1 | 2 | 33.2 | N/A | No | 003を元に改修。MBR (Minimum Bayes Risk) rerank
beam と sampling で複数候補を生成 → 候補同士の類似度で 最終1本を選ぶ（mattiaangeli/deep-pasta-mbr 系の発想を decoding-only で移植）
sacrebleu が使えれば sentence BLEU、無ければ 文字n-gram F1 でスコア計算にフォールバック |
| 002-1 | [1]dpc-starter-train-cv5 | 5 | N/A | 0.0052 | No | サブミットに利用するモデルの学習 ,ByT5-smallのCV計算, max_new_tokens 未指定, gradient_accumulation_steps=2, (train/test)batch_size=4, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, epochs=20 |
| 002-2 | [2]dpc-starter-train-v1 | 1 | N/A | N/A | No |  ,ByT5-base, max_new_tokens=512, gradient_accumulation_steps=8, (train/test)batch_size=1, epochs=20 |
| 002-3-4 | [3]dpc-starter-train-cv5-v4-colab | 1 | N/A | mean=16.7967, std=0.7955 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, epochs=10 |
| 002-3-5 | [3]dpc-starter-train-cv5-v5-colab | 1 | N/A | mean=18.4611, std=0.6222 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, epochs=10 |
| 002-3-5-1 | [3-5]dpc-starter-train-cv5-v1-colab | 1 | N/A | mean=18.4316, std=0.3241 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, 観点D1(fem. / sing. / pl. / plural / (?) を英訳 target から除去、ただしen→akk 側は今回あえて未変更), epochs=10 |
| 002-3-6 | [3]dpc-starter-train-cv5-v6-colab | 1 | N/A | mean=17.7535, std=0.5035 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用,epochs=10 |
| 002-3-6-1 | [3-6]dpc_starter_train_cv5_v1_colab | 1 | N/A | mean=18.1280, std=0.6474 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用, generation_num_beams=3, epochs=10 |
| 002-3-6-2 | [3-6]dpc_starter_train_cv5_v2_colab | 1 | N/A | mean=18.2521, std=0.5509 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用, generation_num_beams=4, epochs=10 |
| 002-3-6-3 | [3-6]dpc-starter-train-cv5-v3-colab | 1 | N/A | mean=18.2609, std=0.5988 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用, バッチ内の最長100未満ならgeneration_num_beams=4で最長100以上でgeneration_num_beams=8, epochs=10 |
| 002-3-6-4 | [3-6]dpc-starter-train-cv5-v4-colab | 1 | N/A | mean=18.1896, std=0.6562 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, train を `akk→en` + `en→akk` の prefix multi-task で2倍化, normalize_transliteration(), normalize_translation(), compute_metrics() 内で decoded の preds/labels 両方に normalize_translation() を適用, バッチ内でソートした上で最長100未満ならgeneration_num_beams=4で最長100以上でgeneration_num_beams=8, epochs=10 |