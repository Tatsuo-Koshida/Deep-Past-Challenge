# サブミット履歴

> このファイルはユーザーが手動で更新します。Codex（エージェント）は参照のみ（書き込み禁止）。

## サブミット一覧
| サブミットID | ノートブック名 | ノートブックのバージョン | LBのスコア | CVのスコア | 公開ノートブックか否か | 備考 |
|---|---|---|---|---|---|
| 1-1 | [1]deep-09-mbr-v1 | 2 | 33.2 | N/A | No | MBR (Minimum Bayes Risk) rerank
beam と sampling で複数候補を生成 → 候補同士の類似度で 最終1本を選ぶ（mattiaangeli/deep-pasta-mbr 系の発想を decoding-only で移植）
sacrebleu が使えれば sentence BLEU、無ければ 文字n-gram F1 でスコア計算にフォールバック |
| 4-1 | [4]submit-notebook-v1 | 2 | 28.9 | N/A | No | [2]dpc-starter-train-v1で学習したByT5-baseで推論(ただしbeams=4) |
| 4-2 | [4]submit-notebook-v2 | 1 | 28.2 | N/A | No | [2]dpc-starter-train-v2で学習したByT5-baseで推論(ただしbeams=4) |
| 4-1-1 | [4-1]submit-notebook-v1 | 1 | 31.6 | N/A | No | final-byt5で推論(ただしbeams=4) |