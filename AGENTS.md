# skill-obs — Agent Guide

> **Skill Observatory**: a meta-repo that scores **21** Agent-Skill / Claude-Skill collection repos (vendored as shallow git submodules under `skills/`) across **21 dimensions**, with **append-only** snapshot history.
>
> This file is the **single source of truth for agent rules**. `CLAUDE.md` just imports it (`@AGENTS.md`); other tools (Codex, Cursor, …) read this file directly. Edit rules here, not in `CLAUDE.md`.

## Structure

- `build_scoring_notebook.py` — **source of truth**: the `REPOS` registry + the append-only `EVALUATIONS` list. Canonical scores = `EVALUATIONS[-1]`. Running it regenerates the notebooks.
- `scoring.ipynb` (en) / `scoring.cn.ipynb` (zh) — **generated**, pre-rendered (GitHub renders them without a kernel). Never hand-edit.
- `EVALUATION.md` / `EVALUATION.en.md` — full report. The former TASK_GUIDE and agent_summary now live here as **Appendix A** (anchor `#task-guide`) and **Appendix B** (anchor `#agent-summary`).
- `README.md` / `README.en.md` — overview + the "Top-line Findings" leaderboard + the skill-testing (D22) section.
- `skill_test.md` — skill-testing design playbook (the proposed, unscored D22 axis).
- `check_consistency.py` — cross-document drift guard. `scan_lessons.py` / `sample_social.py` — metric collectors. `lessons_sample.json` / `social_sample.json` — their sample output.
- `skills/` — the 21 cohort repos as **shallow, read-only git submodules**.

## Commands

```bash
# Regenerate both notebooks from the source of truth (also runs _self_check())
python3 build_scoring_notebook.py

# Cross-document consistency guard — MUST exit 0 before committing score/doc changes
python3 check_consistency.py

# Init / refresh the cohort submodules (shallow)
git submodule update --init --depth 1 --jobs 10
```

## Rules — CRITICAL (do not violate)

1. **Scores live in ONE place**: `EVALUATIONS[-1]` inside `build_scoring_notebook.py`. Never hand-edit scores in the notebooks or in markdown.
2. **Append-only**: never modify a historical snapshot in `EVALUATIONS`. Add a new dict (`eval_date`, `version`, `note`, `submodule_shas`, `raw_metrics`, `scores`).
3. **Capture `submodule_shas` + `raw_metrics` with every snapshot** — the SHA anchors the baseline; raw_metrics let you re-score under a new methodology later.
4. **Notebooks are generated** — edit `build_scoring_notebook.py` and re-run it; never hand-edit `scoring*.ipynb`.
5. **Leaderboards must match canonical scores**: the README "Top-line Findings" table and `EVALUATION` §14.1 are hand-maintained markdown guarded by `check_consistency.py`. If scores change, update **both**, then run the guard.
6. **Bilingual parity**: keep `README.md` ↔ `README.en.md` and `EVALUATION.md` ↔ `EVALUATION.en.md` in sync (content **and** structure). Do **not** recreate `TASK_GUIDE*.md` / `agent_summary*.md` as standalone files — they are EVALUATION appendices reached via `#task-guide` / `#agent-summary`.
7. **Don't bake "what good skills look like" into prose** — encode judgments in `EVALUATIONS` and let snapshot history speak.
8. **`skills/` is read-only** — those are upstream submodules. Never edit files inside them; only add/update/remove the submodule pointer.

## Workflow: re-score or add a repo

**Re-score** → append a snapshot to `EVALUATIONS` → `python3 build_scoring_notebook.py` → `python3 check_consistency.py` (exit 0) → update the README + EVALUATION §14.1 leaderboards if ranks changed → commit.

**Add a repo to the cohort**:
```bash
git submodule add --depth 1 https://github.com/<owner>/<repo>.git skills/<owner>__<repo>
gh repo view <owner>/<repo> --json stargazerCount,forkCount,createdAt,pushedAt,description
```
→ register the new code in `REPOS` → give it scores in the new snapshot → regenerate → guard → commit. (Full steps: README "Adding a repo" / EVALUATION §3.)

## Data sources (per dimension)

D1–D7 via `gh` repo API; D8/D9/D13/D20 via local submodule scan; D21 via `scan_lessons.py`; D18/D19 via HN Algolia. **D16/D17 (Reddit) currently return HTTP 403** → recorded as `-1` sentinel in `raw_metrics`, floored to 1; don't treat new-repo social scores as comparable to the older cohort until re-collected.

## CI

`.github/workflows/consistency.yml` runs on every PR and push to `main`:
1. `python3 build_scoring_notebook.py` — `_self_check()` fails on score-sum vs `# total` drift, bad dimensions, or `DOMAIN_RECS` en/zh skew, then regenerates the notebooks.
2. `python3 check_consistency.py` — README top-line + EVALUATION §14.1 must match canonical scores.

Run both locally before pushing; keep CI green.

## Commits

- Repo owner is **`host452b`** → commit as `host452b <32806348+host452b@users.noreply.github.com>` (repo-local `git config` only; never touch global config).
- Branch off `main` for changes; open a PR. Don't commit score/doc changes unless `check_consistency.py` exits 0.
- **Don't commit**: `*.html`, `__pycache__/`, `.ipynb_checkpoints/`, `.understand-anything/` (local tool output).
