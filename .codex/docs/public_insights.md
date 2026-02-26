# Deep Past Challenge（Translate Akkadian to English）公開ノート/コメントからの学び（暫定）

最終更新: 2026-02-26

> 注意: 本来は Kaggle MCP で公開ノートブック/ディスカッション/コメントを収集したいが、この環境では Kaggle MCP が `Unauthenticated` になり、`authorize` もエラーで進められない。  
> そのため本メモは、Kaggleページのアーカイブ（archive.ph 等）と外部の公開記事を一次ソースとして、現時点で再現性のある範囲だけを整理している。

追記（2026-02-26）:
- Kaggle MCP の `mcp__kaggle__search_notebooks` は `Unauthenticated` を返し、公開ノートブックのランキング/一覧を取得できない。
- `mcp__kaggle__authorize` は、この環境では tool 側のエラー（invalid_union）で実行できなかった。

---

## Kaggle MCP 認証トラブルの切り分けメモ（2026-02-26）

観測できたこと（この repo 内のログ/設定から）:

- `.codex/config.toml` では Kaggle MCP 起動時に `BEARER_TOKEN` を渡す想定（`env_vars = ["BEARER_TOKEN"]`、かつ `shell_environment_policy.ignore_default_excludes = true` / `inherit = "all"`）。
- それにも関わらず、認証が必要そうな API（例: `search_notebooks`, `list_competition_data_files`）は `Unauthenticated` になる。
- セッション開始時に作成された shell snapshot（`.codex/shell_snapshots/*.sh`）には、`BEARER_TOKEN` の export が見当たらない（= 少なくとも snapshot 作成時点では親環境に無かった可能性）。
- `npx -y @pyroprompts/mcp-stdio-to-streamable-http-adapter@0.1.0` の実装をローカルキャッシュから確認すると、Authorization ヘッダが **`Bearer: <token>`（コロン付き）**になっている（本来は `Bearer <token>`）。このままだと **トークンが正しくても `Unauthenticated` になり得る**。

次に確認したいポイント（親環境→MCP起動→リクエストのどこで落ちるか）:

1) **MCP 起動時点**で `BEARER_TOKEN` が渡っているか（= 親環境→MCP起動の問題か）
2) 渡っているのに `Unauthenticated` なら、**トークンの失効/権限不足**または **アダプタ側の仕様変更**（未ピン留め）を疑う

この repo では、MCP 起動時点の環境をログできるようにラッパーを追加した:

- `.codex/config.toml` は `bash .codex/scripts/kaggle_mcp_wrapper.sh` 経由で Kaggle MCP を起動するよう変更
- `.codex/scripts/kaggle_mcp_wrapper.sh` は `BEARER_TOKEN` の「存在有無/長さ/sha256先頭8桁（値は出さない）」を `.codex/log/kaggle-mcp-env.log` に追記してから、従来通り `npx -y @pyroprompts/mcp-stdio-to-streamable-http-adapter` を起動する
- 追加対応: 上記アダプタの **`Bearer:` バグ**を避けるため、`.codex/scripts/kaggle_mcp_wrapper.sh` 側で **キャッシュ内の `build/index.js` を一時ファイルにコピーして `Bearer: `→`Bearer ` に置換**してから起動する（キャッシュ自体は改変しない）。

運用メモ:
- 変更を反映するには Codex の再起動（= MCP サーバの再起動）が必要。
- 再起動後に `.codex/log/kaggle-mcp-env.log` の `token_present=1` なのに `Unauthenticated` のままなら、**トークン失効/権限不足の可能性が高い**（= トークン再発行を優先）。

---

## 1. これまでのコンペの「流れ」（公開物から推測できる範囲）

### フェーズA: まずは動くベースライン

- **ByT5系（文字レベル）を素直に finetune**するのが入口になっている（転写がノイジーで、サブワード分割が不利になりがち）。
- **SacreBLEU で評価を再現**し、`sqrt(BLEU * chrF++)` の方針を手元で固定する（CV/LB 乖離の原因切り分けの前提）。

### フェーズB: データの癖への対応（前処理/正規化）

- 「転写（transliteration）」側は **編集記号・欠損・区切り記号・Unicode揺れ**が精度ボトルネックになりやすい。
- 「英訳」側も **OCR + LLM 由来のノイズ**がある前提で、過学習/学習不安定の要因になる。

### フェーズC: データ量の実質増量（augmentation / multi-task）

公開ノートでは、以下のような増量が明確に提案されている。

- **アラインされた追加データの取り込み**（トレーニング用ペアを増やす）。
- **双方向データ拡張**（`akk → en` だけでなく `en → akk` も学習させる）  
  - 例: 追加行として `{"translation": transliteration, "transliteration": translation, "direction": "en_akk"}` を作り、`direction` を入力に埋め込む。

### フェーズD: 推論の最適化（ビーム/後処理/アンサンブル）

ノート由来の一般的な到達点は次の通り（本コンペ特有の制約を踏まえる）。

- **ビーム探索 + 長さ正規化**（短文/欠損表現が混ざると極端に短い出力に寄りがち）。
- **軽い後処理**（空白/句読点/記号の正規化、`<gap>` 的な表現を導入した場合の整形）。
- **複数 seed / 複数 fold のアンサンブル**（LB 安定化と底上げ）。

---

## 2. 精度改善の方向性（優先度つきの実験アイデア）

### Priority 1: 正規化を「固定」してからモデル比較

- **Unicode 正規化**（NFKC + 独自の置換テーブル）を先に決め、転写表記の揺れを抑える。
- **編集記号の扱い**を固定する（除去/タグ化/ギャップ置換）。  
  - 単純除去は入力情報を落とすリスクがあるため、まずは「置換タグ化（`<gap>`, `<big_gap>` など）」を比較対象に入れる。
- **determinatives（`{d}` など）**は、全除去より「タグとして残す」方向が安全（固有名詞/地名の手掛かりになり得る）。

### Priority 2: 「方向」トークンを入れた multi-task を標準化

- 公開ノートで明示されている **`direction` 付きの双方向学習**は、少ない変更で効く可能性が高い。
- `akk_en` / `en_akk` を prefix token で入れるか、専用 special token を追加して一貫運用する。

### Priority 3: 外部データ/事前学習の活用（オフライン前提）

コンペはインターネット無効だが、**事前にダウンロードしてノートに同梱**すれば外部データ/モデルは使える。

- **関連コーパス（ORACC 等）で追加事前学習**し、DPC train で finetune。
- **翻訳の style を揃える**（句読点・固有名詞の表記揺れ）ため、英語側の正規化や簡易な再整形を検討。

### Priority 4: レキシコン（固有名詞）を「生成時」に効かせる

- データ同梱の固有名詞レキシコンを、推論時に **後処理で置換**するだけでなく、
  - 入力に **候補列を付与**（retrieval augmentation）
  - もしくは **copy 寄り**になる学習（タグ化）で拾いやすくする
 などの方針を比較する。

### Priority 5: 推論チューニング（スコア最適化）

- `num_beams`, `length_penalty`, `max_new_tokens` をメトリクス（BLEU/chrF++）で最適化。
- n-best を保存して、**chrF++ 寄りの rerank**（文字一致が効きやすい）を試す価値がある。

---

## 3. 参照した公開ノート/資料（一次ソース）

> Kaggle本体ページはアクセス制限で取得が不安定なため、アーカイブを優先している。

### 公開ノートブック（アーカイブ）

- DPC Starter (Train): `https://archive.ph/Dx7ZF`
  - ByT5 での学習、評価の再現、データ拡張（双方向/アラインメント）の雛形が確認できる。
- DPC Baseline: train+infer: `https://archive.ph/5myze`
  - Starter を参照した train+infer 一体のベースライン（実行の骨格を把握する用途）。

### コンペ外の参考（背景/既存のアッカド語NLP）

- Deep Past Initiative の発表（コンペ背景）: `https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/overview/deep-past-challenge`
- Akkademia（既存のアッカド語→英語モデル/プロジェクト例）: `https://huggingface.co/datasets/Babelscape/akkademia`

---

## 4. 次にやる（このリポジトリでの作業に落とし込む）

1. 前処理の「規約」候補を 2〜3 パターンに固定（`normalize_v1/v2/...`）して ablation 可能にする
2. ByT5 ベースで `direction` multi-task の最小実装を作る（学習/推論/投稿まで）
3. CV の切り方（ランダム vs 類似度グルーピング）を決め、LB 乖離を減らす
