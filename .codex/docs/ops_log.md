# Ops / Infra ログ

<!--
このファイルは「環境・運用・インフラ」系（MCP、認証、データ取得、実行環境の差異、再現性のための手順）の記録用。
Kaggleの精度改善に直結する実験ログは .codex/docs/experiments_log.md に書く。
-->

## エントリ一覧

| ID | 日付 | 種別 | 概要 | 状態 |
|----|------|------|------|------|
| ops-001 | 2026-02-26 | Kaggle MCP | 認証/接続の疎通確認 | done |

---

## 詳細

### ops-001 Kaggle MCP 認証/接続の疎通確認（2026-02-26）

- **目的**: Kaggle MCP の認証が必要な操作が実行できるかを確認する。
- **変更点**: なし（MCP 経由で API 呼び出しのみ）。
- **実行条件**:
  - `mcp__kaggle__authorize()` を呼ぶ → `Unexpected response type` で失敗
  - 代替として、認証が必要になり得る `mcp__kaggle__list_competition_data_files(competitionName="deep-past-initiative-machine-translation")` を呼ぶ
- **結果**:
  - `list_competition_data_files` は成功し、データファイル一覧（`train.csv`, `test.csv`, `sample_submission.csv` など）を取得できた
- **学び**:
  - 少なくとも現環境では、Kaggle MCP 経由でコンペデータのメタ情報取得は可能（= 認証情報が既に有効になっている可能性が高い）
  - `authorize` エンドポイントはツール実装/レスポンス型の不整合で失敗している可能性がある（要切り分け）
- **次**:
  - 認証が必須の操作として `mcp__kaggle__download_competition_data_files` も試して、実データの DL 可否を確認する
