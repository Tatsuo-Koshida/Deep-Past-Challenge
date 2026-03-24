I joined this competition late, and up until three days before the submission deadline I was mostly focused on cleaning up and curating `train.csv`.
Because of that, I didn’t have enough time to properly verify local CV, and in the end I had to rely on LB score and gut feeling, which is something I regret.

# Cleaning up `train.csv`
The original `train.csv` had 1,561 records, but after doing the following work I expanded it to 2,600 records in the end:

- I visually inspected the PDF page by page and added transliteration/translation pairs that were missing from `train.csv` (I found 27 missing items).
- I split texts that were too long to fit into the ByT5 input window, while paying attention to the alignment between the transliteration and the translation (I did this after fixing the issues in `train.csv` described below).

I also fixed issues like the following in `train.csv`:

- PDF OCR mistakes (cases where either the transliteration or the translation was completely wrong)
- I restored records where the transliteration text was truncated in the host-provided `train.csv` (this was relatively easy to recover by comparing with `published_texts.csv`).
- I excluded some long records with so many `<gap>` tokens that splitting the transliteration and translation was not feasible, since they were likely harmful for model training (surprisingly, I found only 3 such records).

I also found issues like the following in many places, but since the volume was too large and I suspected that similar issues existed in `test.csv` used for the final evaluation, I intentionally left them as-is:

- Italic text in the PDF was not captured by OCR

For fixing `train.csv` using the PDF, I used a very primitive method: taking screenshots of the relevant parts and having ChatGPT transcribe them.

*For transcription*
````markdown
> NOTE: The original version of this prompt was written in Japanese. The text below is an English translation.

# Purpose (request to you)
The **screenshot images** I’m going to send contain **Akkadian transliteration** on the left (or top) and the corresponding **English translation** on the right (or bottom).  
Please **transcribe both accurately** and return them in a format that is **easy to copy & paste into a spreadsheet**.

In some cases, a single screenshot might not be enough and the content may be split across multiple screenshots. In that case, please infer the correct order of the screenshots and transcribe accordingly.

---

## Response format (copy/paste first)
In principle, please reply every time with the following 2-line set (no extra explanation needed):

transliteration (Akkadian text) <newline>
<separator>
translation (English text)

- `<newline>` means a line break in the ChatGPT UI; `<separator>` also means a line break in the ChatGPT UI.
- Keep the Akkadian text and the English text to **one line each**.

---

## Handling body text vs. notes (important)
- The image may contain lines other than the “body text” (e.g., notes, headings, layout notes, page numbers, line numbers), such as `Seal A`, `rev.`, `obv.`, `(remainder obv. missing)`, `(3.5 cm un-inscribed)`, etc.
- Please **extract only the body text** and **exclude note-like lines** from the transcription output.

Example output (when NOTE-like lines are present):
Akkadian: transcribed transliteration (body) <newline>
<newline>
English: transcribed translation (body)

---

## Transcription rules (important)
### 1) Normalization / replacements (required)
For expressions indicating missing/damaged/illegible text, if the meaning is the same, **unify everything to `<gap>`**.

- `x` → `<gap>`
- `[x]` → `<gap>`
- `…` (ellipsis) → `<gap>`
- `(break)` → `<gap>`
- `(large break)` → `<gap>`
- `(n broken lines)` → `<gap>` (it’s OK to use `<gap>` even when `n` is a number)
- If `<gap>` appears multiple times consecutively, merge into one; i.e., `<gap> <gap>` → `<gap>`
- **Any other “missing/broken/unreadable” indicators** → `<gap>`

For determinatives, normalize as follows:

- `(d)` → `{d}`
- `(ki)` → `{ki}`

For parenthesized words:

- `(TÚG)` → `TÚG` (remove the parentheses)

---

## 2) Things to keep as-is
- Keep uppercase/lowercase, apostrophes, hyphens, subscript numerals (e.g., `₂`), special characters (e.g., `š ṣ ṭ ḫ`), accents, etc. **exactly as shown**
- Keep symbols/separators (like `-` and `.`) **as in the image**, except where the replacement rules apply
- `<gap>` must always be exactly `<gap>` in **lowercase**

---

## 3) Uncertainty
- If there is a character/word you truly cannot identify, you may replace that part with `<gap>`
- However, preserve whatever you can read (don’t turn everything into `<gap>`)

---

## Minimal competition context (for clarity)
- Input: Akkadian (cuneiform) transliteration = transliteration
- Output: its English translation = translation
- The goal is to create transliteration → English pairs, so please extract them as **two columns of text**

---

## Requests to make the work faster and more accurate
- If possible, extract the “transliteration part” and the “English translation part” separately so they **don’t get mixed**
- Since punctuation and missing closing parentheses are common errors, do a quick check that the left/right (or top/bottom) alignment hasn’t drifted before you output
- The output is intended to be pasted into a spreadsheet, so please **avoid extra decoration** (bullets, block quotes, etc.)
````

*For splitting long texts with alignment preserved*
````markdown
> NOTE: The original version of this prompt was written in Japanese. The text below is an English translation.

# Purpose (request to you)

The text and screenshot images I’m going to send are candidate training data for the Kaggle competition **Deep Past Challenge - Translate Akkadian to English**.  
For a single long record, please split it into **a small number (around 2–5) of independent records**, while being careful not to break the alignment between the **Akkadian transliteration** and the **English translation**.

The goal is to make each record easier to handle with a ByT5 model by keeping it **under 1024 bytes**.  
However, if splitting would likely break the alignment, it is better to return it as “cannot split” than to over-split.

---

## Most important policy (v2: don’t over-split)

- Target number of splits: **2–5** (prefer **2–4** if possible)
- Split only when necessary
  - Add extra split boundaries only when they are truly needed to keep chunks under 1024 bytes or to preserve alignment
- Avoid producing many very short chunks
  - If you can’t count bytes exactly, err on the safe side, but **don’t mass-produce tiny chunks**
  - As a rough guide, aim for **large chunks (roughly 700–1000 bytes)** when possible
- If it still won’t fit within 5 splits or alignment would break, return `needs_manual_review` (do not force 6+ splits)

---

## Background (minimal)

- In this competition, we train a model to generate English translations from Akkadian transliterations.
- ByT5 is byte-level, so **UTF-8 byte length** matters more than character count.
- On the source side, we usually add the prefix `translate Akkadian to English: `.
- In practice, we want both source and target to be **under 1024 bytes** per record.
- You don’t need to compute byte length perfectly every time. If unsure, make it a bit shorter for safety.

---

## What I want you to do

1. Read the given `transliteration` and `translation`
2. Refer to the screenshot images if needed
3. Find only a small number of boundaries where the **semantic alignment is clear** (don’t add too many)
4. Split the record into **2–5** `transliteration_chunk` / `translation_chunk` pairs (choose the minimum split that works)
5. If splitting is risky, return `needs_manual_review`

---

## Absolute rules

### 1) This is “splitting”, not “editing”

- For the body text, use the input text as-is and, in principle, only take **substrings** from the provided `transliteration` / `translation`
- Do not fill in missing text, paraphrase, summarize, or re-translate
- Even if you notice OCR mistakes or unnatural English, **do not fix them in this task**

### 2) Preserve the order

- When you stack the chunks from top to bottom, they must preserve the original order of the `transliteration` / `translation`

### 3) Only cut at boundaries visible on both sides

- Sentence/clause boundaries on the English side
- Boundaries between itemized lists
- Breaks in letter templates / formulaic phrases
- Breaks between imperative/conditional sections
- Clear line-group boundaries on the transliteration side

Only cut at places where a coherent “unit” is visible on both sides.

### 4) Do not cut in the middle of these

- Numbers, fractions, decimals, tax rates
- Amount expressions like shekel / mina groupings
- Personal names, divine names, place names
- Phrases like `son of ...` or `belonging to ...`
- Inside quotation marks
- Inside an item name

### 5) If it’s not safe, hold it

In the following cases, do not force a split; return `needs_manual_review`:

- Even with the images, the aligned boundary cannot be determined
- The English translation in train looks broken in the middle
- The source/target are misaligned and 1:1 correspondence is unclear
- Keeping it within 2–5 splits would inevitably break numeric/proper-noun sequences

---

## How to use the images

Use the screenshots to decide **where to cut so that transliteration and translation stay aligned**.

Important:

- The Akkadian and English text in the PDF may not exactly match the text provided in the chat.
- This may be because the chat text has already been normalized (e.g., `<gap>` replacements, symbol cleanup, etc.).
- Therefore, use the PDF as a reference to find alignment boundaries, but for the final output body text, **prefer the chat-provided text**.
- Do not rewrite the body text to match the PDF’s visual appearance.

Priority when using images:

1. Verify alignment boundaries between `transliteration` and `translation`
2. Resolve ambiguous boundaries that are hard to see from text alone
3. Decide what spans form a coherent aligned unit

Do not create new translations even if you use the images.

---

## Boundary heuristics (for a small number of splits)

### Good candidates (high priority)

- After an introductory formula like `a-na ... qí-bi-ma um-ma ...` (but don’t split into a tiny chunk just for the intro)
- English expressions that indicate a section change, e.g. `all this ...`, `thereof ...`, `therefore ...`, `if ... then ...`
- Places where a large block of an item list changes (avoid splitting each small item)
- Where repetition of the same pattern ends as a block

### Tempting but usually forbidden

- Splitting every English sentence (often creates too many chunks)
- Splitting every small list item (avoid)

---

## Output format (strict)

Return **only a JSON array**. No extra explanation text.

### When splitting is possible (2–5 chunks)

```json
[
  {
    "record_id": "original record id",
    "split_id": "original record id__01",
    "status": "ok",
    "transliteration_chunk": "split transliteration chunk (must be a substring of the input)",
    "translation_chunk": "corresponding translation chunk (must be a substring of the input)",
    "boundary_reason": "one sentence describing why you cut here (alignment rationale)",
    "confidence": "high"
  }
]
```

### When splitting is risky

```json
[
  {
    "record_id": "original record id",
    "split_id": "original record id__00",
    "status": "needs_manual_review",
    "transliteration_chunk": "",
    "translation_chunk": "",
    "boundary_reason": "cannot cut into 2–5 chunks without breaking alignment",
    "confidence": "low"
  }
]
```

---

## `confidence` guide

- `high`: boundaries are very clear from both images and text
- `medium`: mostly reasonable, but alignment is slightly weak on one side
- `low`: the original train text may be missing/broken/misaligned

---

## When you receive an actual request, always follow these

- Return only a JSON array
- Strongly prefer 2–5 splits and do not add too many boundaries
- Remember this is splitting, not editing
- Do not add words that are not in the provided body text, even if you look at images
- If unsure, return `needs_manual_review`
````

At first I tried to clean up `train.csv` using Codex agents and the skills feature, but I couldn’t control it well, and in the end I did it manually.

# Final submission pipeline
I started from the public notebook “LB 35.9 Ensembling & Post Processing Baseline”, then increased the number of models and made small changes to preprocessing and postprocessing.
The last two submissions differed only in the number of training epochs; despite concerns about overfitting, the one trained for more epochs achieved a higher Private LB score.

## Preprocessing / Postprocessing
### Preprocessing
Both preprocessing and postprocessing are differences from “LB 35.9 Ensembling & Post Processing Baseline” (only the differences are listed here).

- Expanded fraction/decimal normalization (replacing baseline `_EXACT_FRAC_RE` + `_canon_decimal(float)`):
  - Convert fraction expressions like `1/2` and `2 1/2` into Unicode vulgar fractions (e.g., `½`)
  - For decimals, map them to Unicode fractions using a “4-digit truncated representation” as the key (e.g., `0.16666...` → `⅙`)
  - Keep `.5` values like `2.5` as-is (by design)
  - Shorten long floats by truncating to 4 digits after the decimal point (truncate, not round)
- Expanded the set of supported Unicode vulgar fractions (more than baseline)

### Postprocessing
Postprocessing and the final submission formatting are also differences from “LB 35.9 Ensembling & Post Processing Baseline” (only the differences are listed here).

- Fixed the replacement for `5/12 shekel(s)`: baseline `⅔ shekel 15 grains` → `⅓ shekel 15 grains`
- Unified fraction/decimal normalization with the same logic as preprocessing (`1/2` / `2 1/2` / decimals → Unicode fractions)
- Improved removal of slash-based alternatives:
  - For patterns like `you / she`, keep the left side (`you`) and drop the right side (`she`)
  - Changed the regex to avoid breaking fraction expressions like `1/2`
- Do not delete curly quotes (“ ” ‘ ’); normalize them to straight quotes (`"` / `'`) instead (baseline deletes them)
- Adjusted the forbidden-character deletion target (unlike baseline, do not delete all `()` in bulk)
- Removed additional stray marks (`..` / `xx...`, etc.), and as a safeguard normalized `ḫ/Ḫ` to `h/H`
- Safety checks (right before submission):
  - Force empty/None generations to `<gap>`
  - Use `validate_submission` to check columns/row count/empty translations/duplicate ids (baseline mainly logs the number of empty outputs)

## Models used
- ByT5-small (downloaded from Hugging Face and trained on the expanded `train.csv`; input length 1024, output length 1024)
- ByT5-base (downloaded from Hugging Face and trained on the expanded `train.csv`; input length 1024, output length 1024)
- ByT5-large (downloaded from Hugging Face and trained on the expanded `train.csv`; input length 1024, output length 1024)
- Public model: byt5 akkadian mbr v2 (input length 512, output length 384)
- Public model: final-byt5 (input length 512, output length 384)
- Public model: byt5 akkadian mbr v2 (additional fine-tuning on the expanded `train.csv`; input length 1024, output length 1024)
- Public model: final-byt5 (additional fine-tuning on the expanded `train.csv`; input length 1024, output length 1024)
