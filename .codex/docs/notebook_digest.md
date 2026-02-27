# ノート・ディスカッション Digest

<!-- 公開ノート・高評価コメントの要約。キャッチアップ時に追記する（既存は削除しない） -->

## 更新履歴

| 日付 | 追加したノート数 | 追加したコメント数 | メモ |
|------|------------------|--------------------|------|
| 2026-02-26 | 2 | 0 | Kaggle MCP が未認証/authorize エラーのため、Kaggleページのアーカイブから要約 |
| 2026-02-26 | 0 | 0 | Kaggle MCP で `search_notebooks` を試したが `Unauthenticated`（=公開ノートの一覧取得ができず）。アダプタ側の `Authorization: Bearer:` バグで失敗している可能性が高い（`public_insights.md` 参照） |
| 2026-02-26 | 20 | 0 | Kaggle MCP で `search_notebooks` / `get_notebook_info` が成功。upvote（主）+新しさ（従）で重要ノートをランキングして追記（後述）。 |

## ノート一覧

| タイトル | URL | 作者 | アップ投票 | 日付 | 手法の一言 | 要点・使えそうなアイデア | 自分用メモ |
|----------|-----|------|------------|------|------------|---------------------------|------------|
| DPC Starter (Train) | https://archive.ph/Dx7ZF | takamichitoda | （要確認） | （要確認） | ByT5 finetune + augmentation | アライン済み追加データの利用、`akk→en` と `en→akk` の双方向データ拡張（`direction` 付き） | まずはこの骨格を自前コードに写経し、前処理とCVだけ差し替える |
| DPC Baseline: train+infer | https://archive.ph/5myze | llkh0a | （要確認） | （要確認） | Starter を踏襲した train+infer | 学習〜推論〜submission 出力までの一連の流れを把握できる | 手元の提出Notebook雛形として利用 |

### 重要ノートブック（Kaggle MCP: upvote 主 + 新しさ 従 / 2026-02-26）

スコア定義（メモ）:
- 候補: `search_notebooks(sortBy="voteCount")` と `search_notebooks(sortBy="dateRun")` の上位から抜粋
- ranking: `alpha=0.8`（upvote 重視）, `half_life_days=30`（新しさの減衰）
- 出力: `skills/kaggle-mcp-notebook-scout/scripts/rank_notebooks.py`

| rank | ref | votes | last_run_time (UTC) | score | 手法の一言（推定） |
|---:|---|---:|---|---:|---|
| 1 | lgregory/akkadiam-exemple | 326 | 2026-02-25 08:27:56 | 0.9669 | MBR + 最適化推論（モデル入力） |
| 2 | kkashyap14/akkadian2eng-v1 | 151 | 2026-02-26 05:34:40 | 0.8691 | ByT5 推論 + 前後処理 |
| 3 | anthonytherrien/byt-ensemble-script | 323 | 2026-02-01 15:44:19 | 0.8588 | ByT5 推論最適化（スクリプト） |
| 4 | jiexusheng20bz/byt-ensemble | 301 | 2026-02-04 01:06:31 | 0.8568 | 2モデルアンサンブル（logit平均） |
| 5 | mattiaangeli/deep-pasta-mbr | 176 | 2026-02-19 08:37:46 | 0.8497 | MBR 推論（モデル入力） |
| 6 | baidalinadilzhan/lb-35-2-ensemble | 175 | 2026-02-19 03:55:44 | 0.8479 | 2本出力のブレンド/アンサンブル |
| 7 | qifeihhh666/dpc-starter-infer-add-sentencealign | 405 | 2025-12-19 04:03:54 | 0.8202 | starter推論 + sentence alignment |
| 8 | takamichitoda/dpc-starter-train | 370 | 2025-12-31 11:12:17 | 0.8184 | starter学習（ByT5 fine-tune） |
| 9 | nikitagajbhiye30/deep-past000 | 192 | 2026-02-09 19:35:50 | 0.8176 | 推論最適化 + 後処理（推定） |
| 10 | meenalsinha/hybrid-best-akkadian | 114 | 2026-02-19 12:45:15 | 0.7932 | 複数モデル + MBR の“候補プール” |
| 11 | takamichitoda/dpc-starter-infer | 260 | 2025-12-31 20:55:25 | 0.7719 | starter推論 |
| 12 | serariagomes/akkadian-english-byt5-optimized-again | 147 | 2026-02-02 12:45:19 | 0.7571 | ByT5 推論最適化（推定） |
| 13 | yongsukprasertsuk/deep-past-challenge-byt5-optimized | 139 | 2026-02-03 08:37:41 | 0.7522 | ByT5 推論最適化（推定） |
| 14 | assiaben/akkadian-english-inference-byt5-optimized-34x | 153 | 2026-01-29 10:33:08 | 0.7507 | ByT5 推論（optimized 34x 系） |
| 15 | junaid512/akkadian-to-english-v1 | 71 | 2026-02-22 10:47:38 | 0.7473 | ByT5 推論 + 前後処理（推定） |
| 16 | takamichitoda/dpc-infer-with-post-processing-by-llm | 173 | 2026-01-17 09:44:37 | 0.7406 | LLM 後処理の試み |
| 17 | prayagp1/adaptive-beams-test-v1 | 102 | 2026-02-01 19:52:38 | 0.7067 | adaptive beams（推定） |
| 18 | qifeihhh666/deep-past-challenge-byt5-base-inference | 124 | 2026-01-19 20:45:37 | 0.7011 | ByT5 base 推論 |
| 19 | harukiharada/byt5-optuna-tuning-chunked-beam-search | 75 | 2026-02-08 11:35:59 | 0.6884 | Optuna + chunked beam search |
| 20 | mattiaangeli/deep-pasta-mbr-v2 | 46 | 2026-02-21 16:43:02 | 0.6861 | MBR 推論（v2） |

リンク:
- Kaggle URL は `https://www.kaggle.com/code/<ref>` で参照できる（例: `https://www.kaggle.com/code/lgregory/akkadiam-exemple`）。

## ディスカッション・コメント一覧

一次メモ（手動採集した本文/要点/検証プラン）は `.codex/docs/discussion_comments.md` に記録し、ここには「一覧」と「参照」を残す。

| 内容の一言 | URL | アップ投票 | 日付 | 要点 | 自分用メモ |
|------------|-----|------------|------|------|------------|
|            |     |            |      |      |            |

## 横断メモ

（複数ノートに共通するテーマ: リーク指摘・評価指標の実装・よく使われる特徴量など）

- 
