---
name: kaggle-official-primary-reader
description: Use when asked to retrieve/verify Kaggle competition official primary info (Overview/Data/Dataset Instructions) for “Deep Past Challenge - Translate Akkadian to English”. Answers must be grounded in the repo-captured originals in `.codex/docs/kaggle_overview_original.md`, `.codex/docs/kaggle_data_original.md`, and `.codex/docs/dataset_instructions.md` (use `.codex/docs/kaggle_original_index.md` as the entry point).
---

# Kaggle Official Primary Reader (repo-captured)

## Purpose

Provide *Kaggle公式の一次情報*（Overview / Data / Dataset Instructions）を、このリポジトリに手動保存された原文 Markdown から取得して回答する。

## Primary sources (must read first)

Use these files as the single source of truth:

- `.codex/docs/kaggle_original_index.md` (index / entry point)
- `.codex/docs/kaggle_overview_original.md` (Overview tab original)
- `.codex/docs/kaggle_data_original.md` (Data tab original)
- `.codex/docs/dataset_instructions.md` (Dataset Instructions original)

If the user asks about *summary* docs, still verify against the originals above before answering.

## Non-negotiables

- Do not browse the web for these questions unless the user explicitly asks to (the repo already contains the captured originals).
- Keep content faithful to the originals: **do not “improve” wording**; quote small, relevant excerpts when accuracy matters.
- Do **not** write `.codex/docs/experiments_log.md` (user updates it manually).
- If something is not in the captured originals, say so explicitly and point to which file(s) you checked.

## Quick workflow

### 1) Classify the question → pick the file

- Metric / evaluation / submission format / timeline / code requirements → `kaggle_overview_original.md`
- Dataset files / columns / “dummy test.csv” note / supplemental data list → `kaggle_data_original.md`
- Normalization / notation / `<gap>` / determinatives / Unicode / “Ḫ ḫ vs H h” → `dataset_instructions.md`

### 2) Locate the exact passage (fast search)

Use `rg` first, then open the surrounding section:

```bash
rg -n "Evaluation|BLEU|chrF|SacreBLEU|Submission File|Timeline|Code Requirements" .codex/docs/kaggle_overview_original.md
rg -n "train\\.csv|test\\.csv|published_texts\\.csv|publications\\.csv|OA_Lexicon_eBL\\.csv" .codex/docs/kaggle_data_original.md
rg -n "<gap>|<big_gap>|Determinatives|Curly brackets|Unicode|Ḫ|\\{ki\\}|\\{d\\}" .codex/docs/dataset_instructions.md
```

### 3) Answer with “original-first” grounding

When responding:

- Prefer verbatim short quotes (≤1–3 lines) for load-bearing requirements (deadline, submission format, metric definition, constraints).
- Always name the source file(s) you used (paths), and if helpful mention the section header you read.
- If the user wants a structured summary, give a summary **plus** a short “原文抜粋” block for the key constraints.

### 4) Optional: keep internal summaries consistent (only when asked)

If the user requests updates to internal summaries, reflect changes into:

- `.codex/docs/competition_context.md` (spec summary)
- `.codex/docs/public_insights.md` / `.codex/docs/notebook_digest.md` (insight organization)

But never modify the “original” files to add commentary; add commentary only to the summary docs.

