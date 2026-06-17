# skill-obs

> 🌐 **Language**: [🇨🇳 中文](./README.md) · **🇬🇧 English**

> **Skill Observatory** — a meta-repository that benchmarks the current Agent Skills / Claude Skills ecosystem.
> 21 skill-collection repos are vendored in as **git submodules**, scored across **21 dimensions**, visualized in a notebook, and tracked over time via append-only snapshots.

[![Eval baseline](https://img.shields.io/badge/eval-2026--06--17-blue)](./EVALUATION.en.md)
[![Notebook](https://img.shields.io/badge/notebook-scoring.ipynb-orange)](./scoring.ipynb)
[![Notebook 中文](https://img.shields.io/badge/notebook-scoring.cn.ipynb-orange)](./scoring.cn.ipynb)
[![Task Guide](https://img.shields.io/badge/task→repo-TASK__GUIDE-red)](./TASK_GUIDE.en.md)
[![5-Model Summary](https://img.shields.io/badge/5_AI_model_xref-agent__summary-blueviolet)](./agent_summary.en.md)
[![Cohort size](https://img.shields.io/badge/repos-21-green)](./.gitmodules)
[![Dimensions](https://img.shields.io/badge/dimensions-21-purple)](./EVALUATION.en.md#2-15-evaluation-dimensions)
[![Snapshots](https://img.shields.io/badge/snapshots-v1.0_→_v1.5-yellow)](./scoring.ipynb)
[![Social signals](https://img.shields.io/badge/Reddit_+_HN-30d_sampled-orange)](./scoring.ipynb)
[![Quality signals](https://img.shields.io/badge/D20_Decomp_+_D21_Lessons-v1.3-pink)](./EVALUATION.en.md)

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
├── scoring.ipynb                      ← Pre-rendered visualization (English, GitHub-renderable)
├── scoring.cn.ipynb                   ← Pre-rendered visualization (Chinese, same source)
├── build_scoring_notebook.py          ← Source-of-truth: data + bilingual HTML generation
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
    ├── vercel-labs__agent-skills/
    ├── garrytan__gstack/                       ← 🆕 v1.2
    ├── msitarzewski__agency-agents/            ← 🆕 v1.2
    ├── juliusbrussee__caveman/                 ← 🆕 v1.4 (token-efficient)
    ├── Egonex-AI__Understand-Anything/          ← 🆕 v1.5 (codebase→knowledge graph)
    ├── Fission-AI__OpenSpec/                     ← 🆕 v1.5 (spec-driven dev)
    ├── santifer__career-ops/                     ← 🆕 v1.5 (job-search automation)
    ├── Leonxlnx__taste-skill/                    ← 🆕 v1.5 (design taste)
    └── mvanhorn__last30days-skill/               ← 🆕 v1.5 (trend research)
```

## 🏆 Top-line Findings (latest snapshot **v1.5** · 2026-06-17 · max **210**)

| Rank | Repo | Score / 210 | Tier | Tag |
|---:|---|---:|:---:|---|
| 🥇 1 | [`garrytan/gstack`](https://github.com/garrytan/gstack) | **156** | S | Garry Tan setup — D9=10 (52KB deepest) + D21=8 |
| 🥈 2 | [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) | 154 | S | All-in-one — de-facto standard |
| 🥉 3 | [`nexu-io/open-design`](https://github.com/nexu-io/open-design) | 152 | S | Design track + D20=9 |
| 4 | [`obra/superpowers`](https://github.com/obra/superpowers) | 150 | S | Original methodology — D21=7 |
| 5 | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) | 146 | S | "AI agency" — 222 agents across 18 domains |
| 6 | [`juliusbrussee/caveman`](https://github.com/juliusbrussee/caveman) | 137 | A | "talk caveman, save 65% tokens" — token-efficient prompt engineering |
| 7 | `anthropics/skills` | 136 | A | Official spec |
| 8 | `addyosmani/agent-skills` | 128 | A | Production-grade — D21=9 |
| **9** | **[`Egonex-AI/Understand-Anything`](https://github.com/Egonex-AI/Understand-Anything)** | **117** | B | 🆕 v1.5 · codebase→interactive knowledge graph; D5=10/D6=9/D12=9/D13=8 (multi-platform), 661 stars/day |
| 10 | `mattpocock/skills` | 114 | B | TS lens — D20=9 |
| 11 | `openai/skills` | 113 | B | Codex companion — D21=8 |
| **12** | **[`santifer/career-ops`](https://github.com/santifer/career-ops)** | **113** | B | 🆕 v1.5 · job-search/career automation; D12=10 (strongest eng hygiene) + D3=7 (10.7k forks) + 13-language READMEs, 734 stars/day |
| 13 | `ComposioHQ/awesome-claude-skills` | 111 | B | D21=10 (with awesome-list noise caveat) |
| 14 | `coreyhaines31/marketingskills` | 103 | B | Marketing vertical |
| 15 | `nextlevelbuilder/ui-ux-pro-max-skill` | 102 | B | UI/UX productized |
| 16 | `vercel-labs/agent-skills` | 101 | B | Vercel official |
| **17** | **[`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill)** | **98** | C | 🆕 v1.5 · last-30-day trend research; D9=10 (single 140KB SKILL.md, deepest in cohort) but D20=1 (one giant skill) |
| **18** | **[`Fission-AI/OpenSpec`](https://github.com/Fission-AI/OpenSpec)** | **97** | C | 🆕 v1.5 · spec-driven development; 0 SKILL.md (spec tool) but D12=9 + 517 docs |
| 19 | `multica-ai/andrej-karpathy-skills` | 92 | C | D20=10 + D21=9 but low elsewhere |
| **20** | **[`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill)** | **84** | C | 🆕 v1.5 · design "taste" skill; D21=9 (41.4% lesson density, highest among newcomers) + D9=9 (13 skills avg 23KB) but low community/contributors |
| 21 | `kepano/obsidian-skills` | 72 | D | Obsidian vertical |

> **v1.4 → v1.5 changes**:
> 1. Cohort **16 → 21 repos**: added `Egonex-AI/Understand-Anything` (UA), `Fission-AI/OpenSpec` (OS), `santifer/career-ops` (CO), `Leonxlnx/taste-skill` (TS), `mvanhorn/last30days-skill` (L30). Total dims 21 unchanged; max 210 unchanged.
> 2. **Real data** (collected 2026-06-17): D1-D7 via `gh` API; D8/D9/D13/D20 via local structural scan; D21 via `scan_lessons.py`; D18/D19 via HN Algolia.
> 3. ⚠️ **Reddit unreachable** (HTTP 403): D16/D17 for the 5 new repos are unmeasured, floored to 1 (recorded as `-1` sentinel in `raw_metrics`). The existing 16 repos retain their v1.4 Reddit data.
> 4. Best newcomers: **UA #9 (B)** — engineering + multi-platform + high velocity; **CO #12 (B)** — strongest D12 hygiene + 13-language i18n.
> 5. Extremes: **L30** has a single **140KB** SKILL.md (deepest in cohort → D9=10, but D20=1); **TS** has **41.4%** lesson density (highest among newcomers → D21=9).
> 6. Full v1.4 → v1.5 Δ-diff in `scoring.ipynb` cell 7.

Full score matrix, by-domain recommendations, methodology, and caveats: **[`EVALUATION.en.md`](./EVALUATION.en.md)**.

A task-first decision matrix (which repo for which AI-agent task?) — see **[`TASK_GUIDE.en.md`](./TASK_GUIDE.en.md)** (AM × O × NX overlap/orthogonality/complementarity deep-dive + ~50 task lookup + recommended stacks + coverage gaps).

**Cross-comparison summary of how 5 AI models (Claude / ChatGPT / Gemini / Grok / Perplexity) independently evaluated the cohort** — see **[`agent_summary.en.md`](./agent_summary.en.md)** — covers strong consensus picks (4 must-have / 3 avoid), main disagreements, the minimum viable stack, and a comparison with our internal v1.3 scoring.

## 📐 21 Evaluation Dimensions

Brief (full definitions in [`EVALUATION.en.md §2`](./EVALUATION.en.md#2-15-evaluation-dimensions) + [`§11`](./EVALUATION.en.md#11-v12-snapshot--d16-d19-social-signals--gs--aa) + [`§12`](./EVALUATION.en.md#12-v13-snapshot--d20-d21--task-decomposition--lesson-encoded-quality)):

| Category | Dimensions |
|---|---|
| User-required ⭐ | **D1 Star Velocity** (stars/day since creation) |
| Community heat | D1, D2 Total Stars, D4 Watchers |
| Engineering signal | D3 Forks, D5 Commit Recency, D6 Commit Cadence, D7 Contributors |
| Content | D8 Skill Volume, D9 Skill Depth, D10 Supp. Material Density |
| Engineering hygiene | D11 Doc Quality, D12 Eng. Hygiene |
| Portability | D13 Multi-Agent Portability |
| Strategic value | D14 Domain Breadth, D15 Originality / Authority |
| Social signals (v1.2) | **D16 Reddit Heat** (30d posts + comments) · **D17 Reddit Sentiment** (30d avg upvote) · **D18 HN Heat** (30d stories + comments) · **D19 HN Sentiment** (30d avg points) |
| **🆕 Task-quality signals (v1.3)** | **D20 Task Decomposition** (inverse of avg SKILL.md bytes — smaller = better; theory: each skill should focus on one task) · **D21 Lesson-Encoded Quality** (% of *.md with anti-pattern / red-flag / lessons-learned / version / context markers — proxy for "valuable skills should contain model-unknown knowledge + env context + real-failure lessons") |

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
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 96,620 | 2025-10-13 | MIT |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | 95,212 | 2026-03-11 | MIT |
| **[juliusbrussee/caveman](https://github.com/juliusbrussee/caveman)** 🆕 v1.4 | 60,365 | 2026-04-04 | MIT |
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
