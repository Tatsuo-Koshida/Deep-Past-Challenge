# Dataset Instructions (Kaggle Overview Digest)

Source: Kaggle competition overview page (“Dataset Instructions”).  
Captured: 2026-03-01 (JST).  
Goal: Keep dataset-specific formatting pitfalls + normalization suggestions in one place for preprocessing / tokenization / evaluation consistency.

---

## English Summary

### Why this matters
- Akkadian / Old Assyrian data quality is heavily affected by **formatting** in both transliteration and translation (“garbage in, garbage out”).
- Formatting issues can break ML steps from **tokenization → transformation → embedding**.

### Texts in transliteration: main challenges
- **Specialist marks**: beyond standard hyphenated syllables, texts include **superscripts, subscripts, and specialist punctuation** (see “Complete Transliteration Conversion Guide” referenced on Kaggle).
- **Capitalization encodes meaning (two ways)**:
  - `CapitalizedFirstLetter` → proper noun (personal/place name).
  - `ALL CAPS` → Sumerian logogram used instead of Akkadian syllabic spelling.
- **Determinatives**:
  - Printed like superscripts near nouns; Kaggle retains **curly brackets** around them to avoid confusion (e.g. `a-lim{ki}`, `A-mur-{d}UTU`).
  - Kaggle notes curly brackets are used **only** for determinatives in transliteration.
- **Broken text / lacunae**:
  - Suggest standardizing breaks using two markers:
    - single-sign small break: `<gap>`
    - multi-sign to large breaks: `<big_gap>`

### Texts in translation: main challenges
- No complete database of translations (especially for Old Assyrian); translations were digitized via **OCR + LLM corrections**, and still contain formatting issues.
- Proper noun capitalization is typically retained; proper nouns are a common failure point for ML.
- Dataset includes a **lexicon of proper nouns** normalized by specialists to help with these issues.

### Modern scribal notations you may see
- **Line numbers**: often `1, 5, 10, 15, ...`; broken lines add trailing apostrophes like `1'` and `1''` (not quotation marks; an editorial convention).
- Other notations (appear in transliteration and/or translation):
  - `!` certain reading
  - `?` uncertain reading
  - `/` signs belonging to a line found below the line
  - `:` Old Assyrian word divider sign
  - `( )` comments for breaks/erasures
  - `< >` scribal insertions (corrections)
  - `<< >>` demarcation of erroneous signs
  - `˹ ˺` half brackets for partially broken signs
  - `[ ]` square brackets for clearly broken signs/lines
  - `{ }` curly brackets for determinatives

### Formatting suggestions (normalization recipe)

**Remove (modern scribal notations)**:
- `!`, `?`, `/`
- `:` **or** `.` (word divider)
- `˹ ˺` (remove partially broken sign markers from transliteration)
- `[ ]` (remove at document level; example: `[KÙ.BABBAR]` → `KÙ.BABBAR`)

**Keep text but remove surrounding markers**:
- `< >` (scribal insertions): remove brackets but keep the inserted text

**Replace / standardize**:
- `[x]` → `<gap>`
- `…` → `<big_gap>`
- `[… …]` → `<big_gap>`
- Superscript/subscript normalization examples:
  - superscript place marker like `ki` → `{ki}` (full list below)
  - subscript numerals: normalize e.g. `il₅` → `il5` (same idea for any subscript number)

### Additional characters & formats (CDLI / ORACC / Unicode)

Note: training/publication data may include `Ḫ ḫ` while test data may use only `H h`. Kaggle suggests a simple substitution: `Ḫ ḫ` → `H h` (Akkadian has only one “H” phoneme here).

| Character (seen) | CDLI | ORACC | Unicode (note) |
|---|---|---|---|
| `á` | `a2` | `a₂` | subscript digits used |
| `à` | `a3` | `a₃` |  |
| `é` | `e2` | `e₂` |  |
| `è` | `e3` | `e₃` |  |
| `í` | `i2` | `i₂` |  |
| `ì` | `i3` | `i₃` |  |
| `ú` | `u2` | `u₂` |  |
| `ù` | `u3` | `u₃` |  |
| `š` | `sz` | `š` | `U+0161` |
| `Š` | `SZ` | `Š` | `U+0160` |
| `ṣ` | `s,` | `ṣ` | `U+1E63` |
| `Ṣ` | `S,` | `Ṣ` | `U+1E62` |
| `ṭ` | `t,` | `ṭ` | `U+1E6D` |
| `Ṭ` | `T,` | `Ṭ` | `U+1E6C` |
| `‘` | `‘` | `ʾ` | `U+02BE` |
| `0-9` | `0-9` | subscript `₀-₉` | `U+2080–U+2089` |
| `xₓ` | `Xx` | subscript `ₓ` | `U+208A` |
| `ḫ` | `h` | `h` | `U+1E2B` |
| `Ḫ` | `H` | `H` | `U+1E2A` |

### Akkadian determinatives in curly brackets
- `{d}` = dingir “god, deity” — `d` preceding non-human divine actors
- `{mul}` = “stars” — `MUL` preceding astronomical bodies and constellations
- `{ki}` = “earth” — `KI` following a geographical place name or location
- `{lu₂}` = `LÚ` preceding people and professions
- `{e₂}` = `{É}` preceding buildings/institutions (temples, palaces)
- `{uru}` = `(URU)` preceding settlement names (villages, towns, cities)
- `{kur}` = `(KUR)` preceding lands/territories/mountains
- `{mi}` = munus (f) preceding feminine personal names
- `{m}` = `(1 or m)` preceding masculine personal names
- `{geš}` / `{ĝeš}` = `(GIŠ)` preceding trees and wooden objects
- `{tug₂}` = `(TÚG)` preceding textiles / woven objects
- `{dub}` = `(DUB)` preceding clay tablets / documents / legal records
- `{id₂}` = `(ÍD)` preceding canal/river names (or alone = divine river)
- `{mušen}` = `(MUŠEN)` preceding birds
- `{na₄}` = `(na4)` preceding stone
- `{kuš}` = `(kuš)` preceding (animal) skin/fleece/hides
- `{u₂}` = `(Ú)` preceding plants

---

## 日本語まとめ

### なぜ重要か
- アッカド語/古アッシリア語の機械翻訳では、**表記ゆれ・注記・欠損表現**が多く、入力整形の良し悪しが性能に直結します（tokenization〜embedding まで影響）。

### 音写（transliteration）の主な課題
- 通常の「音節をハイフンでつなぐ」表記に加え、**上付き/下付き/専門家向けの句読点**が入りやすい。
- **大文字小文字が意味を持つ**:
  - 先頭のみ大文字 → 人名/地名などの固有名詞
  - 全部大文字 → シュメール語ロゴグラム（表記上の置換）
- **限定詞（determinatives）**:
  - 名詞の近くに付く分類記号。Kaggleでは混同回避のため **`{ }` で囲って保持**（例: `a-lim{ki}`）。
  - Kaggleの説明では、音写中の `{ }` は **限定詞用途のみ**。
- **欠損（破損・欠落）**:
  - 破損を2種類のマーカーに揃える提案:
    - 1字程度の小欠損: `<gap>`
    - 複数字〜大きい欠損: `<big_gap>`

### 訳文（translation）の主な課題
- 古代楔形文字文書の訳文DBが不十分で、特に古アッシリアでは資料が散在。書籍/論文から **OCR + LLM補正**でデータ化したため、なお整形ノイズが残る。
- 固有名詞の大文字表記は基本維持され、ここがMLで崩れやすい。
- 対策として、専門家が正規化した **固有名詞レキシコン**がデータセットに含まれる。

### 現代の編集注記（scribal notations）
- **行番号**: `1, 5, 10, ...` のような飛び番。破損行があると `1'`、さらに別の破損ブロックがあると `1''` のようにアポストロフィが付く（引用符ではなく編集慣習）。
- 他にも `! ? / : ( ) < > << >> ˹ ˺ [ ] { }` などが出現し、確信度・行区切り・語区切り・挿入/誤記・破損などを表す。

### 正規化の提案（前処理の目安）
- **削除**: `!`, `?`, `/`, `:` または `.`, `˹ ˺`, `[ ]`（ドキュメントレベルでは角括弧自体を外し、中身は残す）
- **括弧は外すが中身は残す**: `< >`（挿入語は残す）
- **欠損の置換**: `[x]` → `<gap>`, `…` / `[… …]` → `<big_gap>`
- **上付き/下付きの表記統一**:
  - 地名などの `ki` を `{ki}` に寄せる（限定詞として統一）
  - 下付き数字は通常数字へ（例: `il₅` → `il5`）
- **文字種の揺れ**: `Ḫ ḫ` が `H h` と混在する可能性があるため、必要なら `Ḫ ḫ` → `H h` に揃える（Kaggleの注記）。
