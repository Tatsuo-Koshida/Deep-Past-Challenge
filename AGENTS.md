# AGENTS.md (Repo-wide)

このリポジトリは Kaggle コンペ「Deep Past Challenge - Translate Akkadian to English」向けの実験管理用です。  
目的は **公開Notebook/コメントのキャッチアップ → 要点の構造化 → 実験実行 → 結果の蓄積 → 次の実験設計** を、`.codex/docs` 配下の Markdown を“作業台帳”として回し続けることです。

## 最優先の原則（この repo での Codex の振る舞い）

- **`.codex/docs` を一次情報の置き場所（Single Source of Truth）として扱う**  
  口頭の説明で終わらせず、必ず該当する Markdown に反映して「次回の自分/別エージェントが追える状態」にする。
- **`.codex/docs/experiments_log.md` はユーザーが手動で更新する（Codex は参照のみ・書き込み禁止）**
- **変更は最小・再現性は最大**  
  実験・前処理・評価は再実行できる粒度で記録する（後追いで “なぜ効いた/効かなかった” が説明できること）。
- **新しい知見は “比較可能な形” に揃える**  
  同じ指標、同じデータ分割、同じ前処理（差分があるなら差分を明記）で比較できるように書く。

## `.codex/docs` の運用ルール

この repo では、以下のファイル（または同等の追加ドキュメント）を更新して知見を蓄積する。

- `.codex/docs/competition_context.md`  
  コンペ仕様（評価指標/提出形式/制約/データ注意点）の要約。**仕様に関わる前提**が変わったらここを先に直す。
- `.codex/docs/dataset_instructions.md`  
  Kaggle Overview タブの “Dataset Instructions” の原文（手動コピー＆ペーストした内容）を Markdown 体裁で配置したもの。**前処理やtokenizationの判断**はまずここを参照する。
- `.codex/docs/kaggle_original_index.md`  
  Kaggle の Overview/Data タブ原文の参照先まとめ（原文 Markdown の入口）。
- `.codex/docs/kaggle_overview_original.md`  
  Kaggle Overview タブの原文（Dataset Instructions を除く）。
- `.codex/docs/kaggle_data_original.md`  
  Kaggle Data タブの原文。
- `.codex/docs/notebook_digest.md`  
  公開Notebook/ディスカッションの要点（何が効くか、再現のコツ、落とし穴、引用元のメモ）。  
  “読むだけ” で終わらせず、**次の実験に落とす仮説**まで書く。
- `.codex/docs/experiments_log.md`  
  Kaggleの精度改善に直結する実験台帳（いつ、何を、どう変えて、どうなったか）。**次の一手**を必ず残す。  
  ※ MCP/認証/環境などの運用ログはここに書かない（`.codex/docs/ops_log.md` に記録する）。
- `.codex/docs/submission.md`  
  Kaggleへサブミットした結果の履歴（提出日時、提出物、スコア、メモ、対応する実験/Notebook など）。
- `.codex/docs/ops_log.md`  
  MCP・認証・データ取得・実行環境など「運用/インフラ」系の記録（再現に必要な手順や詰まりどころのメモ）。
- `.codex/docs/public_insights.md`  
  公開Notebook/コメント（または代替ソース）から得た**横断的な学び**の要約。  
  「コンペの流れ」「精度改善の方向性」「参照元リンク」「取得できなかった場合の理由/代替策」をここに集約する。
- `.codex/docs/discussion_comments.md`  
  Kaggle Discussions/コメントを**手動採集**した一次メモ（スレ/コメントのURL、要点、検証プラン、起票先）。  
  参照性のため **Entry** を付け、派生の要約からも ID で参照する。
- `.codex/docs/eda_notebooks.md`  
  `notebooks/EDA/` 配下の**データ点検・探索用ノートブックの索引**。  
  目的、検出対象、運用メモをまとめ、Codex が既存の EDA ノートブックを再利用・拡張しやすいようにする。

### 追記する時の書式（推奨）

- 日付は `YYYY-MM-DD`（必要なら `YYYY-MM-DD HH:MM`）で統一
- 1エントリは「目的 → 変更点 → 実行条件 → 結果 → 学び → 次」を基本形にする
- “良かった/悪かった” だけで終わらせず、**再現に必要な条件**（seed、データ分割、正規化、学習設定の要点）を残す

## キャッチアップ（公開Notebook/コメント）方針

- まず **「何が新規性か」** を抽出し、`.codex/docs/notebook_digest.md` に要点化する
- Discussions/コメントは、本文やスレッド構造が散逸しやすいので、手動採集した一次情報はまず `.codex/docs/discussion_comments.md` に記録する
- その後、**自分のパイプラインに入れるとしたらどこか**（前処理/モデル/学習/推論/後処理/評価）に紐付けて仮説を書く
- すぐ試せる「精度改善のための施策」は `.codex/docs/notebook_digest.md` / `.codex/docs/public_insights.md` に “次の実験候補” としてメモし、`.codex/docs/experiments_log.md` への反映はユーザーが行う
- MCP/認証/環境などの検証メモは `.codex/docs/ops_log.md` に残す（実験ログに混ぜない）

## 実験ログ（必須で残す情報）

少なくとも次を記録する（未確定なら TODO で明示）。

- データ版（ダウンロード日・ファイル名・前処理の差分）
- 評価方法（指標、tokenization、micro/macro、CV方法）
- 主要ハイパラ（モデル、max_len、batch、lr、epoch、dropout、decoding設定など“比較に効く”部分）
- 使った外部リソース（公開モデル/辞書/正規化表など。利用条件があればメモ）
- 結果（CV/LB、定性例、失敗例）

## ファイル作成・命名

- 新規ドキュメントは基本 `.codex/docs/` 配下に追加する
- 追加する場合は **目的が伝わるファイル名**にし、既存ファイルにリンクを張る（孤立ドキュメントを作らない）
- `notebooks/` は `001/` や `002/` のように番号で子フォルダを切り、**元になった公開ノートブック単位**で整理する

## `solutions/` の扱い

- `solutions/` には、**上位者が共有してくれた解法一式**を整理して置く
- 格納対象には、Markdown 形式の解説テキスト、メモ、実際に使われたノートブック、補助スクリプト、設定ファイルなどを含めてよい
- `solutions/` 配下のファイルは、**Kaggle 上で共有された内容の保管・参照が主目的**であり、この repo の実行系コードや標準ディレクトリ構成に無理に合わせない
- ユーザーから **特定の Kaggle writeup / notebook / solution URL** が与えられ、その内容の記録を求められた場合は、**要約を `.codex/docs` に書くのではなく、まず `solutions/<順位>/` 配下に原文に近い形で Markdown / notebook / script として保管する**  
  可能な限り **見出し・表・画像リンク・関連リンク・注記の流れを保持**し、`solutions/3rd/3rd_place_solution.md` のような「参照元の保全」を優先する
- この場合、`solutions/<順位>/` には **`1st_place_solution.md` のような順位ベースの名前**で格納し、内容は「要約」ではなく **できるだけそのままの転載/整形**を基本とする
- そのうえで必要なら、`.codex/docs/public_insights.md` や `.codex/docs/notebook_digest.md` には **参照先リンクと最小限の横断メモだけ**を追記する
- Kaggle から取得したノートブックやスクリプトに、Kaggle 環境前提の入力パス・出力パス・データセット参照パスがそのまま記載されていても、それは**共有物の原状を保持したもの**として扱う
- そのため、`solutions/` 配下のノートブックやスクリプトに書かれたパスは、**このリポジトリのフォルダ構成と一致しなくてよい**。参照目的で保管している段階では、ローカル都合でパスを書き換えない
- `solutions/` 配下の共有物をベースに自分用の実験を起こす場合は、元ファイルを直接編集せず、必要に応じて `notebooks/` 配下など適切な場所へコピーしてから作業する

## 公式データ（Kaggle）

- 公式データの配置先: `data/kaggle/deep-past-initiative-machine-translation/`（コンペslug: `deep-past-initiative-machine-translation`）
- データ本体は大きいので git 管理しない（`.gitignore` で `data/**` を無視。`data/**/README.md` は追跡してメモだけ残す）
- 収録ファイル/メモ: `data/kaggle/deep-past-initiative-machine-translation/README.md`
- 再ダウンロード手順・詰まりどころ: `.codex/docs/ops_log.md`

## コード変更時の注意

- 目的に直結しないリファクタは避ける（台帳運用が主目的の repo）
- 実験用コード/ノートブックは “再現性” を優先（実行コマンド/依存/入出力を明確に）
- 可能なら小さな検証（軽いスクリプト、assert、サンプル入出力）を添える
- **評価指標の実装ノートブック:** `notebooks/000/dpi-bleu-chrf.ipynb`（このコンペの評価指標（BLEU/chrF 等）の実装・検証用。指標まわりはまずこれを参照）
- `solutions/` 配下の共有ノートブック/共有スクリプトは、**参照元の原状保持を優先**し、パス修正やローカル向けの整形を前提にしない
- **ノートブック改修ルール（必須）**
  - 既存 `.ipynb` を**直接編集しない**（常にコピー運用）。
  - 改修前に、同じフォルダにコピーを作成してから編集する。
  - コピー命名は連番/版を明示する（例: `xxx-v2.ipynb`, `xxx-cv5-v2.ipynb`, `xxx-r01.ipynb`）。
  - `notebooks/` 配下の命名規則（`[<lineage_id>]...-v<version>` や枝分かれの表記）は `.codex/docs/notebook_naming_rules.md` を参照し、必ず従う。
  - 実験結果として回収・報告する対象は、**コピーした新しいノートブック**に統一する。
  - どのファイルを元にコピーしたかを `.codex/docs/experiments_log.md` に記録する。
- ノートブック内のパスは Kaggle 環境のフォルダパスを前提にハードコードされていても、ローカルリポジトリのパスに合わせて書き換えず Kaggle 環境のパスのままにする
- コメントやdocstringなどは日本語で書く

## この環境（Codex）固有の注意

- 端末での検索は `rg` を優先
- ユーザーが明示しない限り `git commit` や破壊的操作（`rm`, `reset` 等）はしない
- ネットワーク制約がある前提で、**取得できない情報は “取得できなかった理由” と “代替策” を明記**する
