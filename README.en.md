# skill-obs

> 🌐 **Language**: [🇨🇳 中文](./README.md) · **🇬🇧 English**

> **Skill Observatory** — a meta-repository that benchmarks the current Agent Skills / Claude Skills ecosystem.
> 12 of the most active skill-collection repos are vendored in as **git submodules**, scored across **15 dimensions**, visualized in a notebook, and tracked over time via append-only snapshots.

[![Eval baseline](https://img.shields.io/badge/eval-2026--05--13-blue)](./EVALUATION.en.md)
[![Notebook](https://img.shields.io/badge/notebook-scoring.ipynb-orange)](./scoring.ipynb)
[![Cohort size](https://img.shields.io/badge/repos-13-green)](./.gitmodules)
[![Dimensions](https://img.shields.io/badge/dimensions-15-purple)](./EVALUATION.en.md#2-15-evaluation-dimensions)
[![Snapshots](https://img.shields.io/badge/snapshots-v1.0_·_v1.1-yellow)](./scoring.ipynb)

---

## 🎯 What is this

There are dozens of "Skills" repos in the wild, but they vary wildly in **coverage depth, originality, engineering hygiene, and portability**. This repo's purpose:

1. **Centralized observation** — pull the most-starred, most-representative skill-collection repos together as **git submodules** for side-by-side inspection.
2. **Unified scoring** — score all repos across 15 dimensions (including the user-requested ⭐ **star velocity**); conclusions are reproducible and re-scorable.
3. **Longitudinal tracking** — each evaluation records **submodule SHA + timestamp + raw metrics + 1-10 scores** as an append-only snapshot, enabling drift detection and historical comparison.

This is **not** an awesome-list (`ComposioHQ/awesome-claude-skills` already does pure-link indexing well); it's a **scored, observable, reproducible** evaluation substrate.

## 🚀 Quick Start

```bash
# 1. Clone with submodules (the --recurse-submodules flag is required)
git clone --recurse-submodules https://github.com/host452b/skill-obs.git
cd skill-obs

# 2. If you already cloned without submodules
git submodule update --init --depth 1

# 3. Read the scoring (static markdown)
$EDITOR EVALUATION.en.md      # or EVALUATION.md for 中文

# 4. View the visualization (renders directly on GitHub, no execution needed)
#    https://github.com/host452b/skill-obs/blob/main/scoring.ipynb
#
#    Locally:
jupyter notebook scoring.ipynb
#    Or static HTML:
jupyter nbconvert --to html scoring.ipynb && open scoring.html
```

> ⚠️ Shallow clones: each submodule uses `--depth 1`; total ~225 MB on disk (largest: `nexu-io/open-design` at 137 MB).

## 📂 Repo Layout

```
skill-obs/
├── README.md                          ← 中文 readme
├── README.en.md                       ← you are here
├── EVALUATION.md                      ← Full evaluation (中文)
├── EVALUATION.en.md                   ← Full evaluation (English)
├── scoring.ipynb                      ← Pre-rendered visualization (GitHub-renderable)
├── build_scoring_notebook.py          ← Source-of-truth: data + HTML generation
├── .gitmodules                        ← 12 submodule registrations
└── skills/                            ← Each submodule (shallow clone)
    ├── affaan-m__everything-claude-code/
    ├── anthropics__skills/
    ├── ComposioHQ__awesome-claude-skills/
    ├── coreyhaines31__marketingskills/
    ├── kepano__obsidian-skills/
    ├── mattpocock__skills/
    ├── multica-ai__andrej-karpathy-skills/
    ├── nextlevelbuilder__ui-ux-pro-max-skill/
    ├── nexu-io__open-design/
    ├── obra__superpowers/
    ├── openai__skills/
    ├── addyosmani__agent-skills/
    └── vercel-labs__agent-skills/
```

## 🏆 Top-line Findings (latest snapshot **v1.1** · 2026-05-13)

| Rank | Repo | Score /150 | Tier | Δ vs v1.0 | Tagline |
|---:|---|---:|:---:|---:|---|
| 🥇 1 | [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) | **129** | S | 0 | Comprehensive — de-facto standard |
| 🥈 2 | [`obra/superpowers`](https://github.com/obra/superpowers) | 115 | S | −1 | Original methodology — deepest thinking |
| 🥉 3 | [`nexu-io/open-design`](https://github.com/nexu-io/open-design) | 110 | S | 0 | Ate the design lane in 15 days |
| 4= | `anthropics/skills` | 93 | A | −1 | Official spec |
| 4= | `nextlevelbuilder/ui-ux-pro-max-skill` | 93 | A | −1 | UI/UX product polish |
| 6 | `addyosmani/agent-skills` | 90 | A | 0 | Production-grade engineering |
| 7 | `coreyhaines31/marketingskills` | 85 | A | −1 | Marketing-specialized |
| 8 | `ComposioHQ/awesome-claude-skills` | 80 | B | 0 | Volume champion (864 SKILL.md) |
| 9 | `mattpocock/skills` | 76 | B | 0 | TS engineering lens |
| **10** | **[`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills)** | **75** | **B** | 🆕 | **Vercel official — #1 on D10 supp. density** |
| 11 | `openai/skills` | 72 | B | −1 | Codex companion |
| 12 | `multica-ai/andrej-karpathy-skills` | 69 | B | −1 | Single-file drop-in |
| 13 | `kepano/obsidian-skills` | 50 | C | 0 | Obsidian-specialized |

> **v1.0 → v1.1 change**: added `vercel-labs/agent-skills` (13-repo cohort). V is #1 on D10 (supplementary material density: 19.3 supp. docs per skill), displacing OAI from 10 → 9 and dragging 5 other incumbents down by 1 on D10. Six repos lose 1 total point. Full Δ-diff in `scoring.ipynb` cell 7.

Full score matrix, by-domain recommendations, methodology, and caveats: **[`EVALUATION.en.md`](./EVALUATION.en.md)**.

## 📐 15 Evaluation Dimensions

Brief (full definitions in [`EVALUATION.en.md §2`](./EVALUATION.en.md#2-15-evaluation-dimensions)):

| Category | Dimensions |
|---|---|
| User-required ⭐ | **D1 Star Velocity** (stars/day since creation) |
| Community heat | D1, D2 Total Stars, D4 Watchers |
| Engineering signal | D3 Forks, D5 Commit Recency, D6 Commit Cadence, D7 Contributors |
| Content | D8 Skill Volume, D9 Skill Depth, D10 Supp. Material Density |
| Engineering hygiene | D11 Doc Quality, D12 Eng. Hygiene |
| Portability | D13 Multi-Agent Portability |
| Strategic value | D14 Domain Breadth, D15 Originality / Authority |

## 🎨 Notebook Layout

`scoring.ipynb` is **pre-rendered** — each code cell source is just `# Title` and the visualization is baked into `outputs[].data['text/html']`. **GitHub renders it directly without a kernel.**

| Cell | Purpose |
|:---:|---|
| 0 | Intro markdown |
| 1 | **Overall Ranking** — 9 cols (rank, repo, tier, total, D1, stars, stars/day, forks, contribs, description), per-column colored, column-best **bolded** |
| 2 | **Full Score Matrix** — 12 repos × 15 dimensions + Total, per-dimension normalized coloring |
| 3 | **Raw Metrics Snapshot** — stars/forks/watchers/contribs/skill-counts/days-alive/cadence/platforms, per-column normalized |
| 4 | **Submodule Snapshot & Drift** — recorded SHAs vs current HEAD, color-coded status |
| 5 | **Best Repo by Domain** — 12 domains → recommended skill repo with tier badge |
| 6 | **Δ-diff** (auto-renders when ≥2 snapshots exist) — per-dimension score changes |
| 7 | Maintenance instructions (markdown) |

Color encoding: `rgba(220,60,60,0.35)` (worst) → `rgba(220,220,60,0.35)` (mid) → `rgba(40,200,100,0.35)` (best), linearly interpolated across each column's min/max.

## 🔄 Long-term Maintenance

To re-score, append a new dict to the `EVALUATIONS` list in `build_scoring_notebook.py`:

```python
EVALUATIONS.append({
    'eval_date':      '2026-MM-DDTHH:MM:SSZ',
    'version':        '1.1',
    'note':           '...',
    'submodule_shas': {...},   # from `git submodule status`
    'raw_metrics':    {...},   # from `gh repo view --json ...`
    'scores':         {...},   # rank-based 1-10
})
```

Then re-run: `python3 build_scoring_notebook.py`. The notebook regenerates with the new snapshot as latest; if a previous snapshot exists, the Δ-diff cell auto-renders.

**Principles**:
- ✅ append-only — never modify historical snapshots
- ✅ submodule SHA + raw_metrics must be captured together (the SHA anchors the baseline; raw_metrics let you re-score under a new methodology later)
- ❌ don't bake "what good skills look like" into any single file — write it into `EVALUATIONS` and let history speak

## 🤔 Caveats (read me)

1. **Velocity dimension favors new repos**: `nexu-io/open-design` has only 15 days of life and tops D1; the launch-peak rate can't be extrapolated 6 months out. Read D1 alongside D2 (absolute stock).
2. **"SKILL.md count" is a double-edged sword**: `ComposioHQ` stacks an awesome-list-style 864 SKILL.md files, but average size is only 3.4 KB and supplementary-doc density is 0.03. D9/D10 together neutralize this bias.
3. **Semi-objective dimensions (D11/D12/D14/D15) involve human sampling judgment**: there will be error. Push back on specific scores via PR.
4. **`forrestchang/andrej-karpathy-skills` redirects to `multica-ai/andrej-karpathy-skills`** (owner rename); merged as one entry.

## 🔗 Current Cohort / Submodules

| Submodule | Stars | Created | License |
|---|---:|---|---|
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | 180,838 | 2026-01-18 | MIT |
| [obra/superpowers](https://github.com/obra/superpowers) | 188,498 | 2025-10-09 | MIT |
| [anthropics/skills](https://github.com/anthropics/skills) | 133,251 | 2025-09-22 | — |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 127,547 | 2026-01-27 | — |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 77,723 | 2025-11-30 | MIT |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 77,173 | 2026-02-03 | MIT |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 59,518 | 2025-10-17 | — |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 40,580 | 2026-02-15 | MIT |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | 38,735 | 2026-04-28 | Apache-2.0 |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 30,825 | 2026-01-02 | MIT |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 28,215 | 2026-01-15 | MIT |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 26,494 | 2025-12-08 | — |
| [openai/skills](https://github.com/openai/skills) | 18,982 | 2025-11-25 | — |

Snapshot date: **2026-05-13**. For current numbers, see each repo's GitHub page or the `raw_metrics` block in `scoring.ipynb`.

## 📜 Adding a Repo to the Cohort

```bash
# 1. Add as submodule
git submodule add --depth 1 https://github.com/<owner>/<repo>.git skills/<owner>__<repo>

# 2. Collect raw metrics (see EVALUATION.en.md §3)
gh repo view <owner>/<repo> --json stargazerCount,forkCount,createdAt,pushedAt,description

# 3. Register the new code in REPOS list (build_scoring_notebook.py)
# 4. Score it on 15 dims in the new snapshot
# 5. Re-run build script, commit + push
```

## 📝 License

The evaluation code and docs in this repo are MIT-licensed (when a LICENSE file is added). Each submodule has its own license — see its LICENSE file (per-repo summary in §9.1 of [`EVALUATION.en.md`](./EVALUATION.en.md)).

Data source: GitHub API (`gh repo view`) + each repo's public content. All scores are **snapshot judgments as of 2026-05-13** — not a final verdict on any project.

---

_This project welcomes challenges. Pointing out a specific score that's wrong, or proposing a new dimension, is far more useful than abstract debate._
