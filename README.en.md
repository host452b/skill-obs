# skill-obs

> 🌐 **Language**: [🇨🇳 中文](./README.md) · **🇬🇧 English**

> **Skill Observatory** — a meta-repository that benchmarks the current Agent Skills / Claude Skills ecosystem.
> 21 skill-collection repos are vendored in as **git submodules**, scored across **21 dimensions**, visualized in a notebook, and tracked over time via append-only snapshots.

[![Eval baseline](https://img.shields.io/badge/eval-2026--06--17-blue)](./EVALUATION.en.md)
[![Notebook](https://img.shields.io/badge/notebook-scoring.ipynb-orange)](./scoring.ipynb)
[![Notebook 中文](https://img.shields.io/badge/notebook-scoring.cn.ipynb-orange)](./scoring.cn.ipynb)
[![Task Guide](https://img.shields.io/badge/task→repo-EVALUATION_Appx_A-red)](./EVALUATION.en.md#task-guide)
[![5-Model Summary](https://img.shields.io/badge/5_AI_model_xref-EVALUATION_Appx_B-blueviolet)](./EVALUATION.en.md#agent-summary)
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

A task-first decision matrix (which repo for which AI-agent task?) — see **[`EVALUATION.en.md` Appendix A](./EVALUATION.en.md#task-guide)** (AM × O × NX overlap/orthogonality/complementarity deep-dive + ~50 task lookup + recommended stacks + coverage gaps).

**Cross-comparison summary of how 5 AI models (Claude / ChatGPT / Gemini / Grok / Perplexity) independently evaluated the cohort** — see **[`EVALUATION.en.md` Appendix B](./EVALUATION.en.md#agent-summary)** — covers strong consensus picks (4 must-have / 3 avoid), main disagreements, the minimum viable stack, and a comparison with our internal v1.3 scoring.

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

## 🧪 Skill Validation / Testing / Regression — cross-study (v1.5 appendix · unscored)

> None of the 21 scored dimensions directly measures whether a repo **validates skill behavior/effect or guards against behavioral regression** — `D12 Engineering Hygiene` lumps tests/CI/validators into one engineering signal. This section is a dedicated traversal of all 21 repos, proposed as **D22 Skill-Behavior Validation Rigor** (kept unscored, honoring the "don't bake judgments into a single file" principle).
>
> **The key distinction**: most repos test their *supporting scripts* or *lint frontmatter*; very few **actually run the skill and score its output/effect**.

### Testing frameworks used & how they're implemented

There is **no** standardized "skill-testing framework." The real stack falls into four buckets:

| Category | Tooling | Who · how it's implemented |
|---|---|---|
| Generic code test runner | **Vitest** / **Pytest** / bespoke Node runner | UA·OS·NX·GS use vitest; L30·AM use pytest (`uv run pytest`); CO uses a homegrown `test-all.mjs` (no framework, counts pass/fail itself); AM uses `node tests/run-all.js`. **Tests scripts, never prose** |
| LLM-as-judge behavior eval (**all bespoke, no shared lib**) | `claude -p` / Anthropic SDK / Gemini REST + scoring | **GS** `test/helpers/llm-judge.ts`+`benchmark-judge.ts` run `claude -p` vs `eval-baselines.json`; **anthropics** `skill-creator` uses `run_eval.py`+`grader.md`/`comparator.md` judge subagents; **L30** `evaluate_search_quality.py` calls Gemini as judge for Precision@5/nDCG; **caveman** `llm_run.py` runs 3 arms + tiktoken token counting |
| Structure / frontmatter validator (shape, not effect) | `agentskills/skills-ref` · `Flash-Brew-Digital/validate-skill` · `claude plugin validate` · homegrown sh | **CH** dual validators (homegrown + official skills-ref); **AD** uses `claude plugin validate` + real install; **AA** `lint-agents.sh`; **OAI** `quick_validate.py` |
| AI review bot / visual regression | CodeRabbit · `claude-code-action` · Playwright | **CO·OS** wire `.coderabbit.yaml`; **NL** wires the `/code-review` bot; **NX** uses Playwright `toHaveScreenshot` baselines (for the app UI, not skill output) |

> **Closest thing to a reusable skill-testing framework**: `affaan-m/everything-claude-code` ships `eval-harness` (an eval-driven-development framework), `agent-eval` (pass@k + YAML task defs), and `skill-comply` (tests whether the agent still obeys SKILL.md under a neutral prompt) — but these are tools **shipped to users**, not wired into its own CI gate.

### L0–L5 validation ladder

| Layer | Meaning |
|---|---|
| **L0** | No validation (pure curated prose) |
| **L1** | CHANGELOG / version discipline only |
| **L2** | Supporting-**code** tests (script unit/integration — **never skill prose**) |
| **L3** | **Skill-behavior** eval (eval / LLM-judge / golden transcript / contract test on skill I/O) |
| **L4** | **CI regression gate** (blocking on PR/push) |
| **L5** | **Meta-skill** that prescribes how to author/test/verify a skill |

### Master table (21 repos)

| Repo | Layers hit | Tests skill *behavior*? | Regression-prevention core |
|---|---|---|---|
| **GS** gstack | L1·L2·L3·L4·L5 | ✅ only full loop | `eval-baselines.json` + regression judge + version/docs gates |
| **L30** last30days | L1·L2·L3·L4 | ✅ most complete two-tier | blocking contract suite + cross-git-ref LLM-judge A/B |
| **caveman** | L1·L2·L3 | ✅ tests token *effect* | committed `snapshots/results.json` + `skill_md_sha256` pin |
| **A** anthropics | L3·L5 | ✅ statistical (not committed) | old-vs-new snapshot head-to-head + train/test split |
| **O** superpowers | L1·L2·L3·L5 | ✅ adversarial behavioral TDD | verify-before-done + re-runnable behavior tests + 94% PR rejection |
| **OAI** openai | L2·L3\*·L5 | ◑ golden (not gated) | eval JSON + QA rubric (manual rerun) |
| **CH** marketingskills | L1·L2·L3\*·L4 | ◑ designed, not gated | per-skill SemVer + frontmatter CI (197 evals not in gate) |
| **AM** affaan-m | L1·L2·L4·L5 | ✖ eval tooling shipped to users | matrix CI guards code + metadata only |
| **UA** Understand-Anything | L2·L3·L4 | ◑ script golden | byte-level **determinism** assert + blocking CI |
| **OS** OpenSpec | L1·L2·L3·L4 | ◑ tests **delivery/install** | **migration + drift** tests |
| **CO** career-ops | L1·L2·L3\*·L4 | ◑ grep prose contract | blocking CI + branch protection + CodeRabbit |
| **NX** open-design | L1·L2·L3·L4·L5\* | ✖ tests engine/UI | 240 tests + Playwright screenshot baselines |
| **AD** addyosmani | L2·L4·L5 | ✖ guards packaging/install | `claude plugin validate` + real install |
| **V** vercel-labs | L2·L4·L5 | ✖ guards rules build | path-filtered single-skill gate |
| **AA** agency-agents | L2·L4 | ✖ frontmatter lint | `lint-agents.sh` blocks PR |
| **NL** ui-ux-pro-max | L1·L2 | ✖ conda CI near-no-op | `skill.json` version + LLM-reviewer bot |
| **C** ComposioHQ | L4 | ✖ guards list hygiene | diff-aware PR gate (bounded README region) |
| **M** mattpocock | L1·L5 | ✖ | `write-a-skill` checklist + `deprecated/` folder lifecycle |
| **TS** taste-skill | L1 | ✖ human/observational | failures → named bans + pre-flight checklist |
| **MA** karpathy | L0 | ✖ | none (only a subjective README "how to know it's working") |
| **K** obsidian | L0 | ✖ | none |

> `*` = L3\* eval suite designed but not in CI; L5\* is informal (review-lane / red-spec docs rather than a meta-skill). ◑ = present but non-blocking / only code-or-contract level. ✖ = layer absent or guards packaging only.

### The few that truly test "skill behavior" (by rigor)

1. **GS gstack** — the only full loop, gated in CI: `skill-e2e-*.test.ts` actually runs the skill via `claude -p`/Agent SDK against golden fixtures; `llm-judge.ts` scores 1–5 + a **planted-bug detection rate**; `evals.yml` runs a 12-suite matrix in Docker and posts a pass/fail+cost PR comment (diff-selection keeps it ~$4/run).
2. **L30 last30days** — deterministic contract suite blocks in CI + an **offline** Gemini-judge A/B (cross-git-ref, Precision@5/nDCG@5), with an ADR explicitly arguing why the judge eval **stays out** of the blocking gate (cost / judge non-determinism → flaky).
3. **caveman** — the only one testing *effect*: three arms `baseline`/`terse`/`skill`, with the honest metric being **skill−terse** (strips credit for generic terseness); commits the result snapshot + `skill_md_sha256` pinned to an exact SKILL.md.
4. **anthropics `skill-creator`** — same-turn with/without (or new/old-snapshot) paired subagents + a judge subagent + mean±stddev + a 60/40 train/test split against overfitting (author-time tool, not committed or gated).
5. **obra/superpowers** — adversarial TDD-for-skills: let a fresh subagent *without* the skill fail under pressure → log its rationalizations verbatim → write the minimal skill to close them → rerun; real behavior tests plant a SQL-injection bug and assert the skill triggers and the bug is caught (no CI; enforced via 94% PR rejection governance).
6. **OAI / CH** — golden-transcript eval JSON (query + expected_behavior + success_criteria / assertion checklist), **well-designed but not wired into CI**.

### Regression-prevention toolbox

| Mechanism | Who | One-liner |
|---|---|---|
| **Baseline-comparison eval** | GS·A·L30·caveman | Quantifies "did this version get worse?" — the hardest guard |
| **CI blocking gate** | GS·L30·OS·UA·CO·AM·NX·AD·V·AA·C | But most gate code/packaging/frontmatter; only GS·L30 gate to **behavior** |
| **Determinism / golden pinning** | UA (byte-level) · caveman (snapshot+sha) · L30 (mock-JSON) | Same input must yield same output; logic drift shows as a diff |
| **Migration + drift tests** | OS (best) | Tests "are the skill files on disk still correct after an upgrade" |
| **Prose-contract assertions** | CO (grep gate phrases) · GS (command existence) · AD (hook JSON) | Stops load-bearing SKILL.md instructions from being silently edited |
| **Version / CHANGELOG discipline** | GS · OS (changesets) · CO (Release-Please) · CH | Every fix traces to the test that locks it |
| **Governance gate (human)** | O (94% PR rejection + mandatory eval evidence) · anthropics | Editing the Red-Flags table requires before/after eval evidence |
| **Accumulated anti-pattern list** | TS | A prose repo's guard: each stumble becomes a permanent named ban |

### Worth stealing (especially for regression-testing your own skills)

- Steal **GS**: representative prompts → golden fixtures → run via `claude -p` → LLM-judge → store a baseline → compare new vs baseline, with diff-selection + a cost cap, in CI.
- Steal **caveman's control arm**: measure the **marginal** difference of "with the skill vs an equivalent terse instruction" so you don't credit the skill for what the model already does.
- Steal **L30's ADR discipline**: deterministic contracts in the blocking gate; expensive/non-deterministic LLM-judge evals kept manual via `workflow_dispatch`.
- Steal **OpenSpec's migration + drift tests**: treat "the skill files that end up on the user's disk after an upgrade" as a tested contract.

> 📄 The full "patterns + starter template" (7 design principles, LLM-judge skeleton, minimal layout, two-tier CI, decision table, anti-patterns, source map): **[`skill_test.md`](./skill_test.md)**.

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
