# 実験ログ

> このファイルはユーザーが手動で更新します。Codex（エージェント）は参照のみ（書き込み禁止）。

## 実験一覧

| 実験ID | ノートブック名 | ノートブックのバージョン | LBのスコア | CVのスコア | 公開ノートブックか否か | 備考 |
|---|---|---|---|---|---|
| 003 | deep-09 | 2 | 33.0  | N/A | Yes | |
| 003-1 | [1]deep-09-mbr-v1 | 2 | 33.2 | N/A | No | 003を元に改修。MBR (Minimum Bayes Risk) rerank
beam と sampling で複数候補を生成 → 候補同士の類似度で 最終1本を選ぶ（mattiaangeli/deep-pasta-mbr 系の発想を decoding-only で移植）
sacrebleu が使えれば sentence BLEU、無ければ 文字n-gram F1 でスコア計算にフォールバック |
| 002-1 | [1]dpc-starter-train-cv5 | 1 | N/A | 0.0052 | No | 学習でエラーができないか確認用 ,ByT5-smallのCV計算, max_new_tokens 未指定, gradient_accumulation_steps=2, (train/test)batch_size=4, epochs=20 |
| 002-3 | [3]dpc-starter-train-cv5 | 1 | N/A | mean=16.7967, std=0.7955 | No | ByT5-smallのCV計算, max_new_tokens=512, gradient_accumulation_steps=2, (train/test)batch_size=16, epochs=10 |
