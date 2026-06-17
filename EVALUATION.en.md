# Skill Collection Evaluation

> 🌐 **Language**: [🇨🇳 中文](./EVALUATION.md) · **🇬🇧 English**

> Evaluation date: **2026-06-17** (v1.5 · baseline v1.0 was 2026-05-13)
> Current snapshot: **v1.5** — **21-repo cohort × 21 dims** (v1.0 / v1.1 / v1.2 / v1.3 / v1.4 retained in `scoring.ipynb` history)
> Scoring scale: **1–10** (10 = best in cohort)
> Max total: **210** (21 dims × 10)
> ⚠ **Reading guide (read this first)**
>
> 1. **Current authoritative data = §14 (v1.5) + [`scoring.ipynb`](./scoring.ipynb).** The **§3 / §4 / §5 tables here are a v1.1 historical snapshot (13 repos, max 150), kept for context only — the numbers are stale**; do not read them as current rankings (e.g. §5 shows AM=129 on the old scale; current §14 has AM=154, max 210). Section history: §11→v1.2 (D16-D19 social), §12→v1.3 (D20-D21 task quality), §13→v1.4 (CV), **§14→v1.5 (adds UA/OS/CO/TS/L30)**.
> 2. **The 5 new v1.5 repos' scores are provisional**: subjective dims (D14/D15) and the 1-10 rank calibration were assigned in a single pass; and **Reddit was unreachable (HTTP 403) at eval time, so their D16/D17 are unmeasured and floored to 1** (`-1` sentinel in `raw_metrics`). The new repos are therefore biased low on the two social dims and **not fully comparable** to the existing 16 — treat their ranks as directional, not definitive.
> 3. **Mixed collection dates**: the 16 existing repos' metrics are from **2026-05-13**; the 5 new repos from **2026-06-17**.

## 1. Cohort

| Code | Repo | Stars | Forks | Created | Last push | Theme |
|---|---|---:|---:|---|---|---|
| AM | [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) | 180,838 | 27,876 | 2026-01-18 | 2026-05-13 | Agent harness perf framework |
| O  | [`obra/superpowers`](https://github.com/obra/superpowers) | 188,498 | 16,759 | 2025-10-09 | 2026-05-13 | Agentic skill framework |
| A  | [`anthropics/skills`](https://github.com/anthropics/skills) | 133,251 | 15,715 | 2025-09-22 | 2026-05-09 | Official Anthropic spec |
| MA | [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | 127,547 | 12,958 | 2026-01-27 | 2026-04-20 | Karpathy-derived CLAUDE.md |
| NL | [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 77,723 | 7,977 | 2025-11-30 | 2026-04-03 | UI/UX design skill |
| M  | [`mattpocock/skills`](https://github.com/mattpocock/skills) | 77,173 | 6,656 | 2026-02-03 | 2026-05-12 | "Skills for Real Engineers" |
| C  | [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | 59,518 | 6,462 | 2025-10-17 | 2026-05-07 | Awesome list / curated index |
| AD | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 40,580 | 4,472 | 2026-02-15 | 2026-05-10 | Production-grade engineering |
| NX | [`nexu-io/open-design`](https://github.com/nexu-io/open-design) | 38,735 | 4,403 | 2026-04-28 | 2026-05-13 | OSS Claude Design alternative |
| K  | [`kepano/obsidian-skills`](https://github.com/kepano/obsidian-skills) | 30,825 | 2,100 | 2026-01-02 | 2026-05-07 | Obsidian-native skills |
| CH | [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) | 28,215 | 4,550 | 2026-01-15 | 2026-05-06 | Marketing / CRO / SEO |
| **V** | **[`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills)** | **26,494** | **2,416** | **2025-12-08** | **2026-05-07** | **Vercel deploy + React/Next.js skills (🆕 v1.1)** |
| OAI| [`openai/skills`](https://github.com/openai/skills) | 18,982 | 1,259 | 2025-11-25 | 2026-05-12 | Codex skills catalog |
| **UA** 🆕 | **[`Egonex-AI/Understand-Anything`](https://github.com/Egonex-AI/Understand-Anything)** | **62,155** | **5,129** | **2026-03-15** | **2026-06-16** | **Codebase → interactive knowledge graph (🆕 v1.5)** |
| **OS** 🆕 | **[`Fission-AI/OpenSpec`](https://github.com/Fission-AI/OpenSpec)** | **55,241** | **3,866** | **2025-08-05** | **2026-06-13** | **Spec-driven dev workflow for AI agents (🆕 v1.5)** |
| **CO** 🆕 | **[`santifer/career-ops`](https://github.com/santifer/career-ops)** | **54,306** | **10,774** | **2026-04-04** | **2026-06-16** | **Job-search / career automation (🆕 v1.5)** |
| **TS** 🆕 | **[`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill)** | **45,534** | **3,169** | **2026-02-19** | **2026-06-12** | **Design "taste" — steers off generic output (🆕 v1.5)** |
| **L30** 🆕 | **[`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill)** | **43,681** | **3,592** | **2026-01-23** | **2026-06-17** | **Last-30-day trend research (🆕 v1.5)** |

> Note: `forrestchang/andrej-karpathy-skills` is redirected by GitHub to `multica-ai/andrej-karpathy-skills` (owner rename/transfer); merged as a single entry.

## 2. 15 Evaluation Dimensions

These 15 dimensions are distilled from CHAOSS OSS-health metrics + awesome-list quality rubrics + Claude Skills spec elements. **D1 is the user-required dimension** (stars/day = total stars ÷ days since creation).

| #   | Dimension | Type | Measurement |
|----:|---|---|---|
| **D1**  | **Star Velocity** ⭐ (stars/day since creation) | Objective | `stargazerCount / days_since_created` — user-required |
| D2  | Total Stars | Objective | Absolute popularity / mindshare |
| D3  | Fork Volume | Objective | Replication / serious users |
| D4  | Watcher Count | Objective | Deeply subscribed users |
| D5  | Commit Recency | Objective | `days_since_pushed` (inverted; lower is better) |
| D6  | Commit Cadence | Objective | `total_commits / days_since_created` — sustained development |
| D7  | Contributor Diversity | Objective | Distinct contributors (incl. anonymous) |
| D8  | Skill Volume | Objective | Count of `SKILL.md` files |
| D9  | Skill Depth | Objective | Average `SKILL.md` bytes |
| D10 | Supplementary Material Density | Objective | `(*.md − SKILL.md) / SKILL.md` — supporting docs per skill |
| D11 | Documentation Quality | Semi-objective | README size + top-level docs (CHANGELOG, CONTRIBUTING, AGENTS, CLAUDE, …) |
| D12 | Engineering Hygiene | Semi-objective | LICENSE, tests, hooks, validators, CI, install scripts, CoC, changelog |
| D13 | Multi-Agent Portability | Objective | # of agent platforms named in README (Claude / Codex / Cursor / Gemini / Copilot / OpenCode / Qwen / Windsurf / Kimi …) |
| D14 | Domain Coverage Breadth | Semi-objective | Topical breadth (generalist vs niche) |
| D15 | Originality / Authority | Semi-objective | First-mover/official vs derivative aggregation |

**Why these 15:**

| Selection principle | Dimensions covered |
|---|---|
| User-required | D1 |
| Community heat (short-term, long-term, depth) | D1, D2, D4 |
| Engineering signal (real use vs hype-watching) | D3, D5, D6, D7 |
| Content side (volume vs quality vs supplementary) | D8, D9, D10 |
| Engineering maturity (consumability) | D11, D12 |
| Ecosystem portability (avoid vendor lock-in) | D13 |
| Strategic value (breadth + differentiation) | D14, D15 |

## 3. Key Raw Metrics

> As of 2026-05-13. All numbers reproducible via `gh repo view <owner>/<repo> --json …`.

| Repo | Days alive | Stars/day (D1) | Stars | Forks | Watchers | Last push (d ago) | Commits/day | Contribs | SKILL.md | Avg SKILL bytes | Supp. docs/skill | Multi-agent count |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AM | 115 | **1,572.5** | 180,838 | 27,876 | 899 | 0  | **14.82** | 183 | 572 | 8,847 | 2.0  | 7 |
| O  | 216 | 872.7 | 188,498 | 16,759 | 753 | 0  | 2.04 | 33  | 14  | 8,168 | 4.0  | 6 |
| A  | 233 | 571.9 | 133,251 | 15,715 | 865 | 4  | 0.15 | 13  | 18  | 10,995 | 3.94 | 1 |
| MA | 106 | 1,203.3 | 127,547 | 12,958 | 671 | 23 | 0.26 | 7   | 1   | 2,518 | 5.0  | 2 |
| NL | 164 | 474.0 | 77,723 | 7,977 | 381 | 40 | 0.82 | 31  | 7   | 12,272 | 8.29 | 8 |
| M  | 99 | 779.5 | 77,173 | 6,656 | 532 | 1  | 0.78 | 2   | 28  | 3,321 | 1.14 | 2 |
| C  | 208 | 286.1 | 59,518 | 6,462 | 399 | 6  | 0.34 | 26  | **864** | 3,444 | 0.03 | 7 |
| AD | 87 | 466.4 | 40,580 | 4,472 | 255 | 3  | 2.0  | 23  | 22  | 10,703 | 1.45 | 7 |
| NX | 15 | **2,582.3** | 38,735 | 4,403 | 142 | 0  | **42.5** | **186** | 218 | 3,438 | 1.86 | **9** |
| K  | 131 | 235.3 | 30,825 | 2,100 | 185 | 6  | 0.30 | 13  | 5   | 6,040 | 1.2  | 3 |
| CH | 118 | 239.1 | 28,215 | 4,550 | 288 | 7  | 2.21 | 16  | 41  | 11,443 | 4.02 | 5 |
| **V** | **156** | 169.8 | 26,494 | 2,416 | 114 | 6 | 1.27 | 21 | 7 | 7,224 | **19.3** | 4 |
| OAI| 169 | 112.3 | 18,982 | 1,259 | 110 | 1  | 0.64 | 34  | 43  | 9,435 | 11.33 | 1 |

> **D1 caveat**: NX (`nexu-io/open-design`) is only 15 days alive — its velocity score of 2,582 stars/day includes early-peak bias and cannot be extrapolated 6 months out.

## 4. Score Matrix (Snapshot **v1.1** · 13 repos)

```
Column order: AM | O | NX | A | NL | AD | CH | C | M | V | OAI | MA | K
```

| Dim | Description | AM | O | NX | A | NL | AD | CH | C | M | **V** | OAI | MA | K |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| D1  | Star Velocity ⭐ | 9 | 8 | **10** | 6 | 5 | 5 | 3 | 4 | 7 | 2 | 1 | 9 | 2 |
| D2  | Total Stars | 9 | **10** | 4 | 9 | 7 | 4 | 2 | 5 | 6 | 2 | 1 | 8 | 3 |
| D3  | Forks | **10** | 9 | 3 | 8 | 6 | 4 | 4 | 5 | 5 | 3 | 1 | 7 | 2 |
| D4  | Watchers | **10** | 8 | 2 | 9 | 5 | 3 | 4 | 5 | 6 | 2 | 1 | 7 | 2 |
| D5  | Commit Recency | **10** | **10** | **10** | 8 | 2 | 8 | 6 | 7 | 9 | 7 | 9 | 4 | 7 |
| D6  | Commit Cadence | 9 | 7 | **10** | 1 | 6 | 7 | 8 | 3 | 5 | 6 | 4 | 2 | 3 |
| D7  | Contributors | 9 | 7 | **10** | 3 | 6 | 4 | 4 | 5 | 1 | 4 | 8 | 2 | 3 |
| D8  | Skill Volume | 9 | 3 | 8 | 3 | 2 | 4 | 6 | **10** | 5 | 2 | 7 | 1 | 1 |
| D9  | Skill Depth | 6 | 5 | 3 | 9 | **10** | 8 | 9 | 3 | 2 | 5 | 7 | 1 | 4 |
| D10 | Supp. Material Density | 5 | 6 | 4 | 6 | 8 | 3 | 6 | 1 | 2 | **10** | 9 | 7 | 2 |
| D11 | Doc Quality | **10** | 8 | **10** | 6 | 9 | 9 | 8 | 8 | 7 | 8 | 3 | 7 | 4 |
| D12 | Eng. Hygiene | **10** | 9 | **10** | 6 | 8 | 8 | 9 | 4 | 6 | 6 | 3 | 3 | 3 |
| D13 | Multi-Agent Portability | 8 | 7 | **10** | 1 | 9 | 8 | 6 | 8 | 2 | 5 | 1 | 2 | 4 |
| D14 | Domain Breadth | **10** | 9 | 8 | 8 | 4 | 8 | 4 | 9 | 6 | 4 | 7 | 1 | 3 |
| D15 | Originality / Authority | 5 | 9 | 8 | **10** | 6 | 7 | 6 | 3 | 7 | 9 | **10** | 8 | 7 |
| **Σ** | **Total (out of 150)** | **129** | **115** | **110** | **93** | **93** | **90** | **85** | **80** | **76** | **75** | **72** | **69** | **50** |

> **v1.0 → v1.1 Δ**: V (vercel-labs) added. V displaces OAI atop D10 (supp. material density 19.3); OAI/O/A/NL/CH/MA each drop 1 on D10 due to cohort re-rank; six repos lose 1 total point. v1.0 baseline preserved in `scoring.ipynb`.

## 5. Overall Ranking

### 5.1 Equal-weighted (default)

| Rank | Repo | Score | Tier | Δ vs v1.0 |
|---:|---|---:|---|---:|
| 🥇 1 | `affaan-m/everything-claude-code` | **129** | S | 0 |
| 🥈 2 | `obra/superpowers` | 115 | S | −1 |
| 🥉 3 | `nexu-io/open-design` | 110 | S | 0 |
| 4 | `anthropics/skills` | 93 | A | −1 |
| 4 | `nextlevelbuilder/ui-ux-pro-max-skill` | 93 | A | −1 |
| 6 | `addyosmani/agent-skills` | 90 | A | 0 |
| 7 | `coreyhaines31/marketingskills` | 85 | A | −1 |
| 8 | `ComposioHQ/awesome-claude-skills` | 80 | B | 0 |
| 9 | `mattpocock/skills` | 76 | B | 0 |
| **10** | **`vercel-labs/agent-skills`** | **75** | **B** | **🆕** |
| 11 | `openai/skills` | 72 | B | −1 |
| 12 | `multica-ai/andrej-karpathy-skills` | 69 | B | −1 |
| 13 | `kepano/obsidian-skills` | 50 | C | 0 |

### 5.2 Velocity-emphasized (D1 weighted ×3)

If D1 (star velocity, the user-emphasized dimension) is weighted ×3 while others stay at ×1 — i.e. total + 2×D1:

| Rank | Repo | Adj. Score |
|---:|---|---:|
| 🥇 1 | `affaan-m/everything-claude-code` | 147 |
| 🥈 2 | `obra/superpowers` | 131 |
| 🥉 3 | `nexu-io/open-design` | 130 |
| 4 | `anthropics/skills` | 105 |
| 5 | `nextlevelbuilder/ui-ux-pro-max-skill` | 103 |
| 6 | `addyosmani/agent-skills` | 100 |
| 7 | `coreyhaines31/marketingskills` | 91 |
| 8 | `mattpocock/skills` | 90 |
| 9 | `ComposioHQ/awesome-claude-skills` | 88 |
| 9 | `multica-ai/andrej-karpathy-skills` | 87 |
| 11 | `vercel-labs/agent-skills` | 79 |
| 12 | `openai/skills` | 74 |
| 13 | `kepano/obsidian-skills` | 54 |

> Top-3 invariant; V at #11 even with velocity emphasis. The velocity dimension is robust to weighting.

## 6. One-liner per Repo

| Repo | One-liner | Highlights / Risks |
|---|---|---|
| **affaan-m/everything-claude-code** (S) | The de-facto-standard agent-harness optimization toolkit — comprehensive | ✅ Top engineering completeness; ⚠ originality low (largely integration of community assets) |
| **obra/superpowers** (S) | Original "superpowers" methodology — TDD/debugging/planning meta-skills | ✅ Strongest in thinking; ⚠ low SKILL.md count (14), depth over volume |
| **nexu-io/open-design** (S) | OSS Claude Design alternative; ate the design lane in 15 days | ✅ Best engineering + i18n + broadest platform compatibility (9 agents); ⚠ velocity has early-peak bias |
| **anthropics/skills** (A) | Official spec — defines the SKILL.md standard | ✅ Authority + quality baseline; ⚠ single platform, slow cadence, small volume |
| **nextlevelbuilder/ui-ux-pro-max-skill** (A) | Most product-like UI/UX kit | ✅ Avg skill 12 KB, rich docs; ⚠ ~40 days since last update |
| **addyosmani/agent-skills** (A) | "Production-grade" general engineering skills | ✅ Clean structure, author authority; ⚠ medium volume |
| **coreyhaines31/marketingskills** (A) | Vertical marketing / CRO / SEO skills | ✅ Good engineering, validators; ⚠ narrow domain |
| **ComposioHQ/awesome-claude-skills** (B) | Large awesome-list / index (864 SKILL.md) | ✅ Volume crushes; ⚠ near-zero supplementary docs (D10=1), highly homogeneous |
| **mattpocock/skills** (B) | TypeScript guru's "skills engineers actually use" | ✅ Distinct personal voice; ⚠ only 2 contributors, narrow platform |
| **vercel-labs/agent-skills** (B · 🆕 v1.1) | Vercel official — deploy + React/Next.js engineering skills | ✅ #1 on D10 supp. density (19.3) + official authority; ⚠ only 7 skills, web-only, no LICENSE |
| **openai/skills** (B) | Official Codex skill catalog | ✅ Second-highest supp. density (D10=9) + official authority; ⚠ Codex-only, small community |
| **multica-ai/andrej-karpathy-skills** (B) | A CLAUDE.md based on Karpathy's observations | ✅ Extreme velocity; ⚠ single file, single point of value |
| **kepano/obsidian-skills** (C) | Obsidian / Markdown / Canvas vertical | ✅ Authoritative creator; ⚠ smallest volume, narrow coverage |

## 7. Methodology & Caveats

**Scoring mapping**: per dimension, rank the 12 repos and assign 1-10 (rank 1 → 10, rank 12 → 1, evenly distributed; ties average). Objective dimensions use direct numerical ranking; semi-objective dimensions (D11, D12, D14, D15) are judged by manual sampling of READMEs, directory structure, CONTRIBUTING, and validators.

**Caveats**:

1. **Velocity dimension favors new repos**: NX (15 days alive) maxes D1/D6 on early-peak rates that can't be extrapolated. Pair with D2 (absolute stock).
2. **"SKILL.md count" is double-edged**: ComposioHQ stacks 864 SKILL.md awesome-list-style, but each averages 3.4 KB with supplementary-doc density of 0.03 — a volume trap. D9 (depth) + D10 (supplementary) together neutralize this bias.
3. **Frontmatter compliance ≈ 100%**: An earlier detection script had an `xargs` parsing bug and falsely reported all repos at 0%. Corrected check shows every repo's SKILL.md follows the basic `name:` + `description:` frontmatter (already a community-converged standard); that dimension lost discriminating power and was replaced with D10 (supplementary density).
4. **Multi-agent support inferred from README keyword mentions**: may be over-counted (mentioned but not actually supported); D13 deserves manual verification.
5. **AM and NX both score 10 on Engineering Hygiene**: their hygiene directions differ (AM leans into hooks/scripts/install/lint; NX leans into multi-language docs + e2e + Nix); both tied at cohort top.
6. **MA = multica-ai is the forrestchang redirect**: GitHub did an owner rename/transfer, so the two are equivalent; canonical name is multica-ai here.

## 8. TL;DR (one-line per use case)

- **For "de-facto standard / highest total"**: `affaan-m/everything-claude-code`
- **For "original methodology / depth of thinking"**: `obra/superpowers`
- **For "official spec / learning how to write a SKILL.md"**: `anthropics/skills`
- **For "design lane / broadest multi-platform support"**: `nexu-io/open-design`
- **For "vertical domain reference"**: `coreyhaines31/marketingskills` (marketing) · `nextlevelbuilder/ui-ux-pro-max-skill` (UI/UX) · `kepano/obsidian-skills` (Obsidian)
- **For "wide net / one-stop index"**: `ComposioHQ/awesome-claude-skills`
- **For "official Codex companion"**: `openai/skills`

## 9. By Domain & By Persona

### 9.1 By Use Case

| # | Domain / Use case | Best repo | Key reason (dim refs) |
|---:|---|---|---|
| 1 | **Learning the SKILL.md spec** (writing your own) | [`anthropics/skills`](https://github.com/anthropics/skills) | Only official authority; defines the frontmatter standard; D15(originality)=10 |
| 2 | **OpenAI Codex users** | [`openai/skills`](https://github.com/openai/skills) | Official Codex companion; D10(supp. material)=10 — 11+ supporting docs per skill |
| 3 | **Comprehensive agent engineering framework** | [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) | Overall #1 (129); commands + hooks + plugins + install scripts in one stop |
| 4 | **Methodology / meta-skills** (TDD, debugging, planning, brainstorming) | [`obra/superpowers`](https://github.com/obra/superpowers) | Original "superpowers" framework; D15=9; deepest thinking |
| 5 | **Production-grade software engineering** (general) | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Author authority + clean structure; D14(domain breadth)=8 |
| 6 | **TypeScript / individual engineer efficiency** | [`mattpocock/skills`](https://github.com/mattpocock/skills) | Matt Pocock's TS-first lens; "Skills for Real Engineers" pre-filters |
| 7 | **UI / UX component design** | [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | D9(skill depth)=10; most detailed color/font/product-type recipes |
| 8 | **Design systems + multi-platform creative output** (slides/HTML/PDF/video) | [`nexu-io/open-design`](https://github.com/nexu-io/open-design) | 19 skills + 71 design systems; D13(multi-agent)=10 (9 platforms) |
| 9 | **Marketing / CRO / SEO / Growth** | [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) | Only marketing-specialized repo; ships `validate-skills.sh` |
| 10 | **Obsidian / Markdown knowledge management** | [`kepano/obsidian-skills`](https://github.com/kepano/obsidian-skills) | Obsidian creator (kepano) maintains personally; only repo covering Canvas / Bases / JSON Canvas |
| 11 | **Zero-friction CLAUDE.md drop-in** | [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | Single-file drop-in; Karpathy's LLM-coding anti-patterns |
| 12 | **Browsing / discovery of the skill ecosystem** | [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | 864 SKILL.md index; biggest awesome-list |
| **13** | **Vercel / Next.js / React production engineering** | [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | Vercel official; 40+ React perf rules; #1 on D10 (supp. density) across cohort |

### 9.2 Cross-cutting Needs

| Need | Recommendation |
|---|---|
| Broadest agent platform compatibility (9: Claude/Codex/Cursor/Gemini/Copilot/OpenCode/Qwen/Windsurf/Kimi) | `nexu-io/open-design` |
| Spec + real-world examples paired | `anthropics/skills` (spec) + `obra/superpowers` (examples) |
| Chinese / multi-language i18n friendly | `nexu-io/open-design` (zh/ja/pt/de/fr CONTRIBUTING) + `multica-ai` (includes README.zh) |
| Personal + team both | `affaan-m/everything-claude-code` (hooks + commitlint + ESLint, team-deployable) |

### 9.3 By Persona

| Role | Recommended combo |
|---|---|
| Backend / DevOps engineer | `obra/superpowers` (methodology) + `addyosmani/agent-skills` (engineering practice) |
| Frontend / designer | `nextlevelbuilder/ui-ux-pro-max-skill` (component-level) + `nexu-io/open-design` (design systems) |
| **Vercel / Next.js / React engineer** | **`vercel-labs/agent-skills` (official deploy + 40+ React perf rules)** |
| Marketing / Growth | `coreyhaines31/marketingskills` |
| Research / knowledge worker | `kepano/obsidian-skills` + `anthropics/skills` (doc-coauthoring etc.) |
| AI tool / skill builder | `anthropics/skills` (spec) + `affaan-m/everything-claude-code` (reference impl) |
| Quick trial (5-min onboarding) | `multica-ai/andrej-karpathy-skills` (single-file drop-in) |

## 10. Philosophy · Skill Validity · Long-term Iteration

> **User questions**: For each repo, what's the author's philosophy? How do they ensure skill validity along [Anthropic's two axes](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills):
> 1. **Output quality** — given the skill is active, does it give good answers?
> 2. **Trigger precision** — does Claude activate the skill when it should, and **only** then?
>
> And: how do they decide to *add vs remove* skills over time?

This section is based on careful reading of each of the 13 repos' README / AGENTS.md / CLAUDE.md / CONTRIBUTING / sampled SKILL.md files.

### 10.1 "What a skill IS" — five paradigms

| Paradigm | Representative repos | Core tenet |
|---|---|---|
| **Mandatory workflow** | `obra/superpowers` (O), `addyosmani/agent-skills` (AD) | "If a task matches a skill, you MUST invoke it" — hard-gates prevent agents from skipping steps; O's TDD skill literally says _"NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"_ |
| **Optional reference** | `anthropics/skills` (A), `openai/skills` (OAI), `affaan-m/everything-claude-code` (AM), `mattpocock/skills` (M), `kepano/obsidian-skills` (K) | "Skills are tools Claude **can choose** when relevant" — capability offered, not enforced; OAI's three-tier `.system / .curated / .experimental` lets users opt in by tier |
| **Composable artifact** | `nexu-io/open-design` (NX) | Skills + Design Systems + Craft form a layered capability stack; each skill answers "what to produce", design systems answer "how it should look" |
| **Domain-expert workflow** | `coreyhaines31/marketingskills` (CH), `vercel-labs/agent-skills` (V), `nextlevelbuilder/ui-ux-pro-max-skill` (NL) | Skill = packaged domain decision tree (CH: marketing CRO/SEO frameworks; V: 40+ React rules sorted by Impact; NL: CSV-backed BM25 reasoning engine) |
| **Behavioral directive** | `multica-ai/andrej-karpathy-skills` (MA) | No "activation timing" — 4 Karpathy principles always-on (Don't assume / Simplicity first / Surgical changes / Goal-driven) |
| **Aggregated index** | `ComposioHQ/awesome-claude-skills` (C) | Awesome-list-style governance; PR reviewer judges "real use / tested / attributable"; admission = approval |

### 10.2 Output Quality strategy (how skills give good answers when active)

| Repo | Strategy | Source |
|---|---|---|
| **O** | **Eval evidence required for PRs**: must submit a transcript proving "input 'Let's make a react todo list' triggers brainstorming skill"; ~94% PR rejection rate | `CONTRIBUTING.md`: reject "compliance changes without eval evidence" |
| **AD** | **Forced internal structure**: every SKILL.md has Verification section + exit criteria + Red Flags table + Common Rationalizations; CONTRIBUTING enforces four principles (Specific / Verifiable / Battle-tested / Minimal) | `docs/skill-anatomy.md`; `CONTRIBUTING.md` "Don't add skills that are vague advice" |
| **AM** | **Structure + bundled resources**: every SKILL.md has "When to Activate" + code examples + anti-patterns + cross-platform mapping; scripts/ and references/ enable progressive context loading | `CONTRIBUTING.md` "Skill Development Guide"; 500-line cap |
| **NX** | **Per-skill independent checklists**: P0/P1/P2 gates in `references/checklist.md`; "honesty rules" (release-notes skill must write "None" rather than fabricate); live-artifact preview validation pre-emit | per-skill `references/` directories |
| **NL** | **CSV-driven reasoning**: BM25 ranking + 161 industry-specific decision rules + 20+ pre-delivery checklist (contrast ≥4.5:1, cursor-pointer on clickables, hover 150–300ms, etc.) | `src/ui-ux-pro-max/data/*.csv`; README §"Pre-delivery checklist" |
| **CH** | **Automated `validate-skills.sh`**: enforces frontmatter, 500-line hard cap, trigger-phrase presence, related-skill references; CONTRIBUTING includes "Skill Quality Checklist" | `validate-skills.sh`; `CONTRIBUTING.md` |
| **V** | **Priority matrix + per-rule files**: rules/ contains separate `Explanation / Incorrect Example / Correct Example / Context`; `web-design-guidelines` uses `WebFetch` for fresh rules instead of vendoring | `skills/react-best-practices/rules/`; `skills/web-design-guidelines/SKILL.md` |
| **A** | **Official spec + template**: `template/SKILL.md` shows minimal frontmatter; progressive disclosure (metadata always / SKILL.md body when triggered / bundled resources unlimited) | `template/`; agentskills.io spec |
| **OAI** | **Degrees of Freedom design**: high-freedom text instructions / medium pseudocode / low-freedom scripts; "context window is a public good" — large references must include TOC + grep patterns | `.system/skill-creator/SKILL.md` |
| **M** | **Anti-failure-mode design**: each skill targets a specific agent failure (/grill-me fixes alignment, /diagnose fixes feedback loops, /tdd fixes test quality); CONTEXT.md + ADRs ground skills in project vocabulary | README "Why These Skills Exist" |
| **K** | **Specification completeness**: every skill includes `references/*.md` exhaustively covering one Obsidian format (properties / embeds / callouts), loaded on-demand by the agent | `skills/obsidian-markdown/references/` |
| **MA** | **Four negative principles**: Don't assume / Simplicity first / Surgical changes / Goal-driven; README "How to Know It's Working" gives meta-criteria (smaller diffs, fewer rewrites) | `CLAUDE.md`; README |
| **C** | **PR authenticity proof**: must be "based on a real use case, not hypothetical"; must "be tested across Claude.ai, Claude Code, and API"; attribution traceable | `CONTRIBUTING.md` |

### 10.3 Trigger Precision strategy (correct activation)

| Repo | Strategy | Typical execution |
|---|---|---|
| **CH** | **Exhaustive enumeration**: single skill description lists 15+ trigger phrase variations ("CRO" / "conversion rate optimization" / "this page isn't converting" / "bounce rate is too high" ...) | `page-cro` skill description |
| **NL** | **Mega-description**: 200+ phrases / projects / elements / topics packed into one description (actions × projects × elements × topics) | `SKILL.md` frontmatter `description` field |
| **NX** | **Frontmatter `triggers:` array**: 4-6 variants per skill; `od:mode / od:scenario` extension fields distinguish intent (prototype vs workflow) | `od:` frontmatter |
| **AD** | **Positive + negative boundaries**: every skill has "Use when" + explicit "When NOT to use" (e.g. "Single-line fixes, typo corrections") to exclude false positives; AGENTS.md maps intents → skills explicitly | `skill-anatomy.md` §Frontmatter |
| **O** | **Prescriptive imperatives**: description directly says _"You MUST use this before any creative work"_, _"Use when implementing any feature or bugfix, before writing implementation code"_ | brainstorming / TDD skills |
| **V** | **"Use when:" + task conditions**: description includes trigger phrases ("Deploy my app") and task types ("when asked to review UI code for Web Interface Guidelines compliance") | per-skill SKILL.md |
| **K** | **Specific format terminology**: description embeds Obsidian-specific terms ("wikilinks" / "callouts" / "properties") so agents trigger by exact word | `obsidian-markdown` description |
| **M** | **Multi-faceted description**: trigger scenarios × user phrasings (e.g. /tdd: "Use when user wants to build features or fix bugs using TDD, mentions 'red-green-refactor', wants integration tests, or asks for test-first development") | per-skill descriptions |
| **AM** | **"When to Activate" section**: required in every skill; description specifies both "what" and "when"; related-skills links cascade contextual activation | `docs/SKILL-DEVELOPMENT-GUIDE.md` |
| **A / OAI** | **Minimal precision**: "Default assumption: Codex is already very smart" — description carries only name + key scenarios; trust the model to judge intent | `template/SKILL.md` |
| **C** | **Problem-statement style**: 1-2 sentences focus on "what problem" not exhaustive phrases; categorization guides discovery (Business & Marketing / Communication & Writing) | README §Categorization |
| **MA** | **Implicit / global trigger**: CLAUDE.md applies to all coding work after install; no fine-grained triggering | single-file design |

### 10.4 Long-term iteration / Add vs Remove

| Repo | Admission gate | Removal / deprecation |
|---|---|---|
| **O** | ⛔ Strictest: ~94% PR rejection; require eval evidence + one-problem-per-PR + human reviewed complete diff | Not explicit, but CONTRIBUTING rejects "compliance changes" |
| **AD** | CONTRIBUTING four principles; vague advice rejected outright; new skills must reference existing ones to avoid duplication | Not explicit; once added, treated as permanent |
| **AM** | "Skill Adaptation Policy": copy ideas not product identity; new skills must be single-domain with examples, anti-patterns, tested | Not explicit |
| **NX** | PR against "Common rejection patterns"; design systems must meet 5-point bar (9 sections present / hex verifiable / no marketing fluff / ASCII slug / etc.) | CHANGELOG accretion (v0.6.0 = 136 PRs), no removal pattern |
| **NL** | npm CLI (`uipro-cli`) + semver; changes via CSV row addition; source-of-truth `src/ui-ux-pro-max/`, symlinks auto-sync | "Continuous data enhancement" — no skill add/remove, just CSV row changes |
| **CH** | `validate-skills.sh` auto PR validation; CONTRIBUTING enforces PR templates (new-skill.md / skill-update.md) + Skill Quality Checklist; version metadata | Not explicit; via fork / selective install |
| **V** | AGENTS.md mandates: kebab-case directory / SKILL.md required / scripts/ required / .zip package / **500-line cap** | Not explicit, but "End-User Installation" distinguishes stable vs experimental |
| **A** | No CONTRIBUTING; strict curation of demo examples; THIRD_PARTY_NOTICES.md for license rigor | No retirement policy; "demonstration purposes only" |
| **OAI** | 12-line CONTRIBUTING.md ("Be kind and inclusive"); low technical bar; skill-creator includes eval scripts (`generate_review.py`, `eval-viewer`) | Three tiers `.system / .curated / .experimental` ≈ stable / mature / preview |
| **M** | No formal CONTRIBUTING; **directory segregation**: `engineering/ productivity/ misc/` must register in README + plugin.json; `in-progress/ personal/ deprecated/` do not | **`deprecated/` directory** preserves history without recommending — graceful retirement |
| **K** | No CONTRIBUTING; points to agentskills.io spec | Static references, only updated when Obsidian adds new syntax |
| **MA** | Single-file, read-only | "These guidelines are designed to be merged" — no external skill intake |
| **C** | PR must be "based on a real use case, not hypothetical" + tested across Claude.ai / Claude Code / API + attribution traceable | No removal; relies on category organization (Business / Communication / ...) |

### 10.5 Cross-cutting insights

**Three philosophical poles**:

| Pole | Repos | Stance |
|---|---|---|
| Enforce | O, AD | "If it matches, you **must** use it" |
| Offer | A, OAI, AM, M, K, V | "I provide capability; you choose" |
| Always-on | MA | "This is how you code, period" |

**Two QA paradigms**:

| Paradigm | Repos | Tooling |
|---|---|---|
| Mechanical / automated | CH, O, V, NX, NL | shell scripts / eval transcripts / 500-line caps / P0-P2 checklists / 20-test pre-delivery |
| Judgment / manual review | C, A, MA | PR reviewer judges authenticity / official curation / immutable principles |

**Trigger strategy spectrum**:

```
High recall ←———————————————————————→ High precision
Enumeration       Positive+Negative     Minimal description
(CH / NL)         boundary (AD)          (A / OAI)
```

CH/NL's 200+ phrase enumeration maximizes recall (no missed activations) but risks over-triggering. A/OAI's minimal descriptions trust the model's judgment (more model-quality-sensitive). AD's "Use when X / When NOT to use Y" gives both positive and negative boundaries — currently the most balanced approach.

**Iteration governance spectrum**:

```
Heavy gates ←————————————————————→ Light governance
O / AD     CH / V     NX / NL      C       MA / K / OAI
eval req   validator  CHANGELOG    PR attest  ~no gate
```

**Best practices for the user's two questions**:

1. **Output Quality**: the strongest pattern is **"structure inside the skill body"** + **"PR-time verification"** as double insurance. AD's Verification + Red Flags + Use When structure plus O's eval transcript requirement is the combination that works.
2. **Trigger Precision**: **positive + negative boundaries** beats **pure enumeration**. AD's "When NOT to use" sections suppress false positives more than CH's 15-phrase enumeration. But for domains with high linguistic variation (marketing users phrase requests many ways), CH's approach remains effective.

**Decision signals for long-term add/remove**:

| Signal | Implies | Action |
|---|---|---|
| Skill has no eval evidence | "May never trigger when it should" | **Reject / remove** |
| Skill triggers overlap with existing skills | False positives / mis-fires | **Merge or add "see X" boundary clause** |
| Skill body > 500 lines | High context cost; dilutes instruction weight | **Split / move to `references/`** |
| Skill content stales easily (e.g. SDK versions) | Vendored content rots | **Switch to live `WebFetch`** (V's approach) |
| Skill can't go cross-platform | Claude-only | **Downgrade to `experimental/`** (OAI's 3-tier) |
| Skill seldom triggers | Users don't actually need it | **Move to `deprecated/`** (M's directory segregation) |

> **Conclusion**: comparing the 13 repos reveals a counter-intuitive fact — **community popularity does not correlate with governance rigor**. The strictest O (~94% rejection) and the lightest MA (single-file, read-only) both sit in the cohort top tier; the largest C (864 skills) has the lowest D10 supp. density (0.03). Both "strict" and "loose" can work — what *doesn't* work is **strict-on-paper-but-not-enforced**: claiming high gates but waving things through.

---

_All raw queries are reproducible via `gh repo view --json` + local `find`; submodules are shallow-cloned at `skills/<owner>__<repo>/`. Reproduction recipe: see `.gitmodules` and rank-based equal-weighted methodology in §7. §10 philosophy archaeology is based on sampled docs from all 13 repos._

## 11. v1.2 Snapshot — D16-D19 (social signals) + GS + AA

### 11.1 New dimensions

| Dim | Name | Measurement | Source |
|---|---|---|---|
| **D16** | **Reddit Heat (30d)** | `posts + comments/10` last 30 days | Reddit public search.json API (`t=month`) |
| **D17** | **Reddit Sentiment (30d)** | Avg upvote score per post (last 30d) | Same as above |
| **D18** | **HN Heat (30d)** | `stories*10 + comments` last 30 days | HN Algolia Search API (`numericFilters=created_at_i>UNIX_30D_AGO`) |
| **D19** | **HN Sentiment (30d)** | Avg points per story | Same as above |

### 11.2 Sampling methodology

- **Queries**: 2 queries per repo: `"<owner> <repo>"` and `"github.com/<owner>/<repo>"`, dedup by ID then union.
- **Window**: 30 days back from sample time (2026-05-13T09:08 UTC).
- **Tool**: `sample_social.py` (in repo root), stdlib `urllib.request` only, no external deps; rate-limit politeness: Reddit 1.5s between calls, HN 0.6s, 2s between repos.
- **User-Agent**: `skill-obs/1.0`.

### 11.3 Full v1.2 ranking (max 190)

| Rank | Repo | Score | Tier |
|---:|---|---:|:---:|
| 🥇 1 | **`garrytan/gstack`** 🆕 | **147** | S |
| 🥈 2 | `affaan-m/everything-claude-code` | 145 | S |
| 🥉 3 | `nexu-io/open-design` | 139 | S |
| 3= | **`msitarzewski/agency-agents`** 🆕 | 139 | S |
| 5 | `obra/superpowers` | 137 | S |
| 6 | `anthropics/skills` | 127 | A |
| 7 | `addyosmani/agent-skills` | 115 | A |
| 8 | `mattpocock/skills` | 104 | B |
| 9 | `openai/skills` | 101 | B |
| 10 | `nextlevelbuilder/ui-ux-pro-max-skill` | 98 | B |
| 11 | `coreyhaines31/marketingskills` | 95 | B |
| 12 | `ComposioHQ/awesome-claude-skills` | 93 | B |
| 13 | `vercel-labs/agent-skills` | 91 | B |
| 14 | `multica-ai/andrej-karpathy-skills` | 73 | C |
| 15 | `kepano/obsidian-skills` | 62 | D |

### 11.4 Caveats

1. **Query-string contamination**: queries like "anthropics skills" match both this repo *and* Anthropic's broader "Skills" feature discussion. **D16/D17 numbers for A/OAI include spill-over from official-feature chatter, not pure repo discussion**.
2. **GS / AA top Reddit avg_score 2769 / 2897 include launch-wave peaks**: launch buzz inflates upvotes — analogous to NX's early D1 velocity bias. Steady-state heat 6 months out may be much lower.
3. **HN signal is sparse**: only 7/15 repos have ≥1 HN story in 30 days. AD's 1 story got 212 comments (a viral story) — HN D18/D19 are easily dominated by single viral hits.
4. **No bot / cross-post deduping**: Reddit results include "garry tan claude code" matches that may include the author's own self-promo. Statistically this represents *propagation volume*, not strictly *organic discussion vs marketing*.
5. **D16-D19 scoring uses rank-based 1-10**: same methodology as D1-D15; 4 new dimensions integrated without re-ranking existing dim spreads.

### 11.5 Cascading effects from adding GS + AA

- **GS** (avg SKILL.md 52,730 bytes) significantly tops v1.1's D9 leader NL (12,272 bytes), pushing NL from 10 → 9.
- **AA** has 222 agents (`.md` rather than `SKILL.md`) — for methodology consistency we count `*.md` as the skill-volume metric — plus 9 platforms (tied with NX) + 18 domain directories (including game-dev).
- Both new repos take **D16/D17 top spots** (Reddit avg score 2769 / 2897 vs third-place A at 151.7) — they significantly widen the social-dim spread.

> For the full 19-dim × 15-repo colored matrix: open `scoring.ipynb` (renders directly on GitHub, no execution needed).

## 12. v1.3 Snapshot — D20-D21 (Task Decomposition + Lesson-Encoded Quality)

> **The user's two theoretical principles**:
> 1. *"Each repo splits different tasks into specific skills; theoretically, the smaller each skill's text length, the better."* → **D20 Task Decomposition**
> 2. *"Valuable skills should contain: (1) knowledge the model doesn't know, (2) environment-specific context, (3) lessons learned from real failures."* → **D21 Lesson-Encoded Quality**

### 12.1 New dimension definitions

| Dim | Name | Measurement | Theoretical premise |
|---|---|---|---|
| **D20** | **Task Decomposition** | rank-based, inverted `avg_skill_bytes` — smaller = better | "Each skill should focus on one task"; fat skills (>10KB) bundle multiple tasks together, hurting trigger precision and context cost |
| **D21** | **Lesson-Encoded Quality** | rank-based `value_density_pct` — higher = better; composite = 60% × lesson markers + 25% × version markers + 15% × context markers | A valuable skill should encode (1)+(2)+(3); keyword scan estimates this — lesson markers ≈ criterion (3), version markers ≈ (1), context markers ≈ (2) |

### 12.2 D21 marker-scan methodology

`scan_lessons.py` (committed in repo root) scans every `*.md` per submodule:

**Lesson markers (criterion #3 — real-failure lessons)**:
`anti-pattern`, `red flag`, `common mistake`, `common pitfall`, `common rationalization`, `when not to use`, `do not use`, `failure mode`, `pitfall`, `lessons learned`, `avoid this/the/using/over`, `don't do/use`, `wrong way`, `common failure/error`, `gotchas`, `caveats`, `hard-gate`, `why not`, `mistake`

**Version markers (criterion #1 — model-unknown / time-sensitive info)**:
`as of YYYY`, `since vN.N`, `api version`, `deprecated since`, version-comparison operators

**Context markers (criterion #2 — environment-specific context)**:
`export`, `process.env`, `${VAR}`, `~/.config`, `.env`, `localhost`, `127.0.0.1`, `/usr/local`, `/etc/`, `/opt/`

Per-repo output: `lesson_pct`, `version_pct`, `context_pct`, `value_density_pct` (composite).

### 12.3 D20 + D21 raw data + scoring

| Repo | avg_skill_bytes | D20 (inverted) | lesson_pct | version_pct | context_pct | value_density_pct | D21 |
|---|---:|---:|---:|---:|---:|---:|---:|
| MA | 2,518 | **10** | 66.7% | 0% | 16.7% | 42.5 | 9 |
| M | 3,321 | 9 | 6.7% | 0% | 3.3% | 4.5 | 1 |
| NX | 3,438 | 9 | 18.5% | 1.3% | 12.8% | 13.3 | 4 |
| C | 3,444 | 8 | **94.7%** ⚠ | 0.6% | 2.0% | 57.3 | **10** |
| K | 6,040 | 7 | 18.2% | 0% | 0% | 10.9 | 3 |
| V | 7,224 | 7 | 10.6% | 0% | 16.2% | 8.8 | 3 |
| O | 8,168 | 6 | 37.1% | 1.4% | 15.7% | 25.0 | 7 |
| AM | 8,847 | 5 | 10.5% | 3.2% | 28.1% | 11.3 | 4 |
| OAI | 9,435 | 4 | 41.9% | 0.4% | 42.3% | 31.6 | 8 |
| AD | 10,703 | 4 | 59.3% | 1.9% | 22.2% | 39.4 | 9 |
| A | 10,995 | 3 | 31.5% | 6.7% | 12.4% | 22.4 | 6 |
| CH | 11,443 | 3 | 18.4% | 1.0% | 14.6% | 13.5 | 5 |
| NL | 12,272 | 2 | 4.6% | 4.6% | 23.1% | 7.4 | 2 |
| AA | 12,293 | 2 | 25.2% | 2.2% | 17.7% | 18.3 | 5 |
| **GS** | **52,730** | **1** | 56.0% | 1.6% | 35.2% | 39.3 | 8 |

### 12.4 Full v1.3 ranking (max 210)

| Rank | Repo | Score | Tier | Δ vs v1.2 |
|---:|---|---:|:---:|---:|
| 🥇 1 | **`garrytan/gstack`** | **156** | S | +9 (D9+D21 strong / D20 cost) |
| 🥈 2 | `affaan-m/everything-claude-code` | 154 | S | +9 |
| 🥉 3 | `nexu-io/open-design` | 152 | S | +13 (D20=9 boost) |
| 4 | `obra/superpowers` | 150 | S | +13 |
| 5 | `msitarzewski/agency-agents` | 146 | S | +7 |
| 6 | `anthropics/skills` | 136 | A | +9 |
| 7 | `addyosmani/agent-skills` | 128 | A | +13 (D21=9 big boost) |
| 8 | `mattpocock/skills` | 114 | B | +10 (D20=9 / D21=1) |
| 9 | `openai/skills` | 113 | B | +12 |
| 10 | `ComposioHQ/awesome-claude-skills` | 111 | B | **+18** (D21=10 ⚠ with caveat) |
| 11 | `coreyhaines31/marketingskills` | 103 | B | +8 |
| 12 | `nextlevelbuilder/ui-ux-pro-max-skill` | 102 | B | +4 |
| 13 | `vercel-labs/agent-skills` | 101 | B | +10 |
| 14 | `multica-ai/andrej-karpathy-skills` | 92 | C | **+19** (D20+D21 both high) |
| 15 | `kepano/obsidian-skills` | 72 | D | +10 |

> Note: tier thresholds rescaled for max=210: S+ ≥165, S ≥145, A ≥125, B ≥100, C ≥80, D <80.

### 12.5 Caveats

1. **C's D21=10 (94.7%)**: requires careful interpretation — ComposioHQ is an awesome-list of 864 SKILL.md files, each averaging just 3.4KB (mostly short stubs). The 94.7% lesson-marker hit rate could be: (a) fragmentary keyword matches in short descriptions ("common ...", "avoid ..."), (b) genuine lessons-learned content. Regex alone **cannot** distinguish; suggest manual sampling of ~30 ComposioHQ SKILL.mds to judge real value vs noise.
2. **D21's 60/25/15 weighting**: based on the assumption "lesson markers signal 'real-world value' more strongly than version/context markers"; debatable. Equal weighting would re-rank C and OAI.
3. **D20 vs D9 (Skill Depth) are negatively correlated / directly conflicting**: D9 assumes "deep = substantive"; D20 assumes "small = focused". Both give GS extreme scores (D9=10, D20=1), net out to no change for GS; but for mid-tier repos (NL 12KB) this is a -1/-2 difference. **Why have both**: balance of evaluation lenses — D9 alone favors "broad-and-deep"; D20 alone favors "small-and-focused".
4. **value_density_pct is not absolutely comparable across repos**: 1/5 SKILL.md containing anti-pattern = 20%; 100/500 SKILL.md containing it = also 20%. But repo B has 100× absolute volume. **Ratio vs absolute** has no single right answer; we use ratio to avoid letting large repos win automatically.
5. **Theory vs reality**: D20's "smaller = better" is the user's *theoretical assumption*. GS's 52KB SKILL.md is actually a role definition (CEO/Designer/QA), not a single-task implementation. So GS D20=1 reflects **"the decomposition cost of role-style fat skills"**, not a quality judgment on GS content itself (D21=8).
6. **Runtime caveats**: v1.2 D16-D19 caveats (query contamination / launch wave / HN sparsity) still apply.

### 12.6 Major v1.3 ranking shifts

**Big climbers**:
- **MA +19**: single-file 2.5KB (D20=10 max) + Karpathy's 4 principles are all anti-pattern warnings (D21=9)
- **C +18**: D21=10 but with the awesome-list noise caveat
- **AD +13**: existing "Verifiable / Battle-tested" sections already had heavy Red Flags content
- **O +13**: original methodology already includes anti-pattern education
- **NX +13**: 3.4KB average + 13.3% value-density

**Small / unchanged**:
- **NL +4**: D20=2 + D21=2 both low; UI/UX docs lean toward components, less lessons-learned content
- **NL** still rank 12 (despite D9=9 in v1.2/v1.3)
- **M +10 but D21=1**: mattpocock uses skill names like /diagnose, /tdd rather than "anti-pattern" keywords, scan misses

**Big-picture takeaway**:
- v1.0-v1.2 emphasized popularity + engineering measurements
- v1.3 adds D20+D21, introducing a **"signal quality / lesson density"** differentiation axis — MA's 4 anti-pattern principles alone lift it to 92 vs V's 101 (close!)
- **GS's #1 is no longer popularity-only**; it's popularity + D9 (deepest) + D21 (rich lessons) combined — multi-dimensional robust win

> For the full 21-dim × 15-repo colored matrix + Δ v1.2→v1.3: open `scoring.ipynb` (renders directly on GitHub, no execution needed).

## 13. v1.4 Snapshot — added `juliusbrussee/caveman` (CV)

### 13.1 Why include CV

CV is a **single-point viral repo**:
- Concept: **"talk caveman, save tokens"** — Claude speaks in caveman style (short sentences, no filler words), cutting token consumption by 65%
- Data: 60,365 stars / 39 days alive = **1,548 stars/day** (near NX's launch peak)
- Engineering: very complete (bin/dist/commands/agents/plugins/evals/benchmarks/tests + multi-OS installer + Gemini extension)
- **Fills the "token efficiency / prompt minification" vertical** — previously uncovered in cohort

### 13.2 CV 21-dim scoring

| Dim | Score | Note |
|---|---:|---|
| D1 Star Velocity | 9 | 1,548 stars/day (launch-peak caveat) |
| D2 Total Stars | 6 | 60k (between M and C) |
| D3 Forks | 3 | 3,346 |
| D4 Watchers | 2 | 141 (low tier) |
| D5 Recency | 9 | 1 day ago |
| D6 Cadence | 9 | 4.67 commits/day (after only NX 42.5 and AM 14.82) |
| D7 Contributors | 6 | 29 |
| D8 Skill Volume | 3 | 15 SKILL.md (small) |
| D9 Skill Depth | 2 | avg 3.3KB (small) |
| D10 Supp Material | 5 | 2.93 supp/skill |
| D11 Doc Quality | 8 | 224 README + AGENTS+CLAUDE+GEMINI+INSTALL+CONTRIBUTING+docs/ |
| D12 Eng Hygiene | 9 | benchmark/evals/tests + multi-OS installer + gemini-ext |
| **D13 Multi-Agent** | **10** | **9 platforms (first to mention antigravity)** — tied with NX/AA at top |
| D14 Domain Breadth | 4 | Only prompt-engineering vertical |
| D15 Originality | 8 | Unique caveman concept + viral spread |
| D16 Reddit Heat | 9 | 105 posts + 15705 comments |
| **D17 Reddit Sentiment** | **10** | **avg 788.8** (top tier with GS 2769 / AA 2897) |
| D18 HN Heat | 6 | 3 stories + 1 comment |
| D19 HN Sentiment | 6 | avg 3.0 |
| D20 Task Decomposition | 9 | avg 3.3KB (small-and-focused tier) |
| D21 Lesson-Encoded | 4 | 22% lesson + 0% version + 6.8% context = 14.2 density |
| **Σ Total** | **137** | **Tier A, rank #6** |

### 13.3 Full v1.4 ranking (max 210)

| Rank | Repo | Score | Tier |
|---:|---|---:|:---:|
| 🥇 1 | `garrytan/gstack` | 156 | S |
| 🥈 2 | `affaan-m/everything-claude-code` | 154 | S |
| 🥉 3 | `nexu-io/open-design` | 152 | S |
| 4 | `obra/superpowers` | 150 | S |
| 5 | `msitarzewski/agency-agents` | 146 | S |
| **6** | **`juliusbrussee/caveman`** 🆕 | **137** | A |
| 7 | `anthropics/skills` | 136 | A |
| 8 | `addyosmani/agent-skills` | 128 | A |
| 9 | `mattpocock/skills` | 114 | B |
| 10 | `openai/skills` | 113 | B |
| 11 | `ComposioHQ/awesome-claude-skills` | 111 | B |
| 12 | `coreyhaines31/marketingskills` | 103 | B |
| 13 | `nextlevelbuilder/ui-ux-pro-max-skill` | 102 | B |
| 14 | `vercel-labs/agent-skills` | 101 | B |
| 15 | `multica-ai/andrej-karpathy-skills` | 92 | C |
| 16 | `kepano/obsidian-skills` | 72 | D |

### 13.4 Key caveats

1. **CV launch-wave bias**: 1,548 stars/day includes viral launch peak. **Meme-style repos** typically decay faster than tool repos; 6-month steady-state velocity will likely drop to 200-400 stars/day, dragging D1 down to 4-5.
2. **CV's D14=4 reflects a genuinely narrow positioning**: all 15 skills are about "caveman talk" prompt-style optimization — strictly a **single-trick repo**, not a framework. The #6 ranking is driven by D6/D13/D16/D17 (active + multi-platform + high social heat).
3. **CV's niche is unique**: no other prompt-engineering / token-efficiency specialist in cohort. For users specifically worried about token costs, CV is the **only option** — its value isn't strictly proportional to total score.
4. **9-platform support includes antigravity**: CV is the first repo in cohort to explicitly support antigravity. If your workflow goes through antigravity, **CV is uniquely fitting**.

### 13.5 Comparison with the Five-Model evaluation ([Appendix B](#agent-summary))

CV is too new (created 2026-04-04), so **the 5-model evaluation in §1-§6 (collected before v1.2) does not cover CV**. To do a v1.4 full LLM re-evaluation, you'd need to re-prompt all 5 models on CV's operational value. The current v1.4 #6 is **this repo's internal scoring** — not the 5-model consensus.

> For the full 21-dim × 16-repo colored matrix + Δ v1.3→v1.4: open `scoring.ipynb` (renders directly on GitHub, no execution needed).

---

## 14. v1.5 Snapshot — 5 repos added (cohort 16 → 21)

This round expands the cohort from 16 to 21 repos with five additions: **UA** `Egonex-AI/Understand-Anything`, **OS** `Fission-AI/OpenSpec`, **CO** `santifer/career-ops`, **TS** `Leonxlnx/taste-skill`, **L30** `mvanhorn/last30days-skill`. All metrics are real data collected **2026-06-17** (D1-D7 via `gh` API, D8/D9/D13/D20 via local scan, D21 via `scan_lessons.py`, D18/D19 via HN Algolia). ⚠ **Reddit-403 caveat**: Reddit's search endpoint returned HTTP 403 at eval time, so **D16/D17 are unmeasured for the 5 new repos and floored to 1** (raw_metrics store a `-1` sentinel); the existing 16 repos retain their v1.4 Reddit data.

### 14.1 Full v1.5 ranking (max 210)

| Rank | Repo | Score | Tier |
|---:|---|---:|:---:|
| 🥇 1 | `garrytan/gstack` | 156 | S |
| 🥈 2 | `affaan-m/everything-claude-code` | 154 | S |
| 🥉 3 | `nexu-io/open-design` | 152 | S |
| 4 | `obra/superpowers` | 150 | S |
| 5 | `msitarzewski/agency-agents` | 146 | S |
| 6 | `juliusbrussee/caveman` | 137 | A |
| 7 | `anthropics/skills` | 136 | A |
| 8 | `addyosmani/agent-skills` | 128 | A |
| **9** | **`Egonex-AI/Understand-Anything`** 🆕 | **117** | **B** |
| 10 | `mattpocock/skills` | 114 | B |
| 11 | `openai/skills` | 113 | B |
| **12** | **`santifer/career-ops`** 🆕 | **113** | **B** |
| 13 | `ComposioHQ/awesome-claude-skills` | 111 | B |
| 14 | `coreyhaines31/marketingskills` | 103 | B |
| 15 | `nextlevelbuilder/ui-ux-pro-max-skill` | 102 | B |
| 16 | `vercel-labs/agent-skills` | 101 | B |
| **17** | **`mvanhorn/last30days-skill`** 🆕 | **98** | **C** |
| **18** | **`Fission-AI/OpenSpec`** 🆕 | **97** | **C** |
| 19 | `multica-ai/andrej-karpathy-skills` | 92 | C |
| **20** | **`Leonxlnx/taste-skill`** 🆕 | **84** | **C** |
| 21 | `kepano/obsidian-skills` | 72 | D |

> Tier thresholds (max=210, per `tier_for_total()` in `build_scoring_notebook.py`): S+ ≥165, S ≥145, A ≥125, B ≥100, C ≥80, D <80. TS at 84 lands in **C** by this rule. CO and OAI tie at 113; OAI ranked ahead on tie-break (stable sort, existing-repo precedence).

### 14.2 New-repo profiles

- **UA — `Egonex-AI/Understand-Anything` (#9, B, 117)**: turns a codebase into an interactive knowledge graph — the most general-purpose newcomer (code-understanding / dev tooling). **Strongest**: D5=10 (pushed 1d ago), D6=9 (6.05 commits/day), D12=9 (hygiene), D13=8 (multi-platform), D15=8. **Weakest**: D8=2 (only 8 SKILL.md). Raw: 62,155★ / 5,129 forks / 200 watchers / 43 contribs / 94d alive / 661 stars-day; 8 SKILL.md @ ~10KB avg, lesson 14.2%.
- **CO — `santifer/career-ops` (#12, B, 113)**: job-search / career automation (CV, ATS, application tracking) — niche but exceptionally well-kept. **Strongest**: D12=10 (the strongest engineering hygiene in the whole cohort), D5=10, D11=9 (13-language READMEs), D7=8, D3=7 (10.7k forks — second-highest fork count in cohort). **Weakest**: D14=3 (narrow domain), D8=2. Raw: 54,306★ / 10,774 forks / 207 watchers / 93 contribs / 74d / 734 stars-day; 4 SKILL.md @ ~4KB, 110 supporting docs incl. 13-language READMEs, lesson 12.3%.
- **L30 — `mvanhorn/last30days-skill` (#17, C, 98)**: researches last-30-day trends across Reddit / X / YouTube / HN / web (trend-research niche). **Strongest**: D9=10 (its single SKILL.md is 140KB — the **deepest single skill in the entire cohort**), D5=10, D6=8, D7=7. **Weakest**: D8=1 (one skill) and D20=1 (that one giant skill is the worst-decomposed in cohort — D9/D20 directly conflict here). Raw: 43,681★ / 3,592 forks / 153 watchers / 48 contribs / 145d / 301 stars-day; 1 SKILL.md @ 140KB, lesson 14.3%.
- **OS — `Fission-AI/OpenSpec` (#18, C, 97)**: spec-driven development workflow for AI coding agents (general methodology). It is a **spec tool, not a skill pack** — 0 `SKILL.md` files but 517 supporting docs. **Strongest**: D7=8 (60 contribs — most-contributed newcomer), D10=8, D12=9 (hygiene), D15=8. **Weakest**: D8=1, D9=1 (no SKILL.md to measure), D21=3. Raw: 55,241★ / 3,866 forks / 245 watchers / 60 contribs / 316d (oldest newcomer) / 175 stars-day; lesson 5.8%.
- **TS — `Leonxlnx/taste-skill` (#20, C, 84)**: a design-"taste" skill that steers agents away from generic, templated output (niche but cross-cutting aesthetics). **Strongest**: D21=9 (lesson 41.4% — the **highest lesson density of any newcomer**), D9=9 (23KB avg — deepest newcomer skills), D15=7. **Weakest**: D7=2 (only 6 contributors) and D13=1 (single-platform). Raw: 45,534★ / 3,169 forks / 132 watchers / 6 contribs / 118d / 386 stars-day; 13 SKILL.md @ ~23KB avg, lesson 41.4%.

### 14.3 Data sources & caveats

1. **Reddit-403 → D16/D17 floored to 1 for the 5 new repos.** Reddit's `search.json` returned HTTP 403 during this collection run, so social-heat/sentiment could not be sampled for UA/OS/CO/TS/L30; their raw_metrics carry a `-1` sentinel and the dimensions are floored to 1. The original 16 repos keep their v1.4 Reddit figures, so cross-repo D16/D17 comparisons against newcomers are not meaningful this round.
2. **Data sources**: D1-D7 via `gh` API; D8/D9/D13/D20 via local submodule scan; D21 via `scan_lessons.py`; D18/D19 via HN Algolia. HN signal for newcomers is sparse (TS and L30 each have 1 story, the rest 0).
3. **OS measured as a spec tool**: with 0 `SKILL.md`, OS scores near-floor on D8/D9/D20/D21 by construction — this reflects format, not lack of value; its strength is methodology + docs (D7/D10/D12/D15).
4. **L30's D9=10 vs D20=1** is the sharpest case of the D9↔D20 conflict noted in §12.5(3): one 140KB skill is simultaneously the "deepest" and the "least decomposed."
5. **Runtime caveats from v1.2-v1.4 still apply** (query contamination, launch-wave velocity bias, HN sparsity) to the carried-over 16-repo data.

> For the full 21-dim × 21-repo colored matrix + Δ v1.4→v1.5: open `scoring.ipynb` (renders directly on GitHub, no execution needed).


---

<a id="task-guide"></a>

## Appendix A — Task → Repo Decision Guide

> 🔄 **v1.2 sync (2026-05-13)**: cohort expanded to **15 repos**, adding `garrytan/gstack` (GS) and `msitarzewski/agency-agents` (AA). See §1 bottom, §3.7-3.8, §5 recommended stacks, §6 gap update. **AA fills the game-dev gap** (20 game-dev agents).
> 🔄 **v1.5 sync (2026-06-17)**: cohort expanded to **21 repos**, adding `Egonex-AI/Understand-Anything` (UA), `Fission-AI/OpenSpec` (OS), `santifer/career-ops` (CO), `Leonxlnx/taste-skill` (TS), `mvanhorn/last30days-skill` (L30). **UA fills the "understand existing codebase" gap, CO fills the "job-search" gap, OS fills the "spec-driven development" gap.**

A task-first decision matrix across the 21 skill repos. Given a concrete AI-agent task, which repo (or stack) should you install?

- §1 — Where each repo sits on the functional map
- §2 — **AM × O × NX deep-dive**: overlaps, orthogonality, and complementary stacks (the most-asked comparison)
- §3 — Other notable overlap pairs
- §4 — Task → Repo lookup (~50 tasks across dev / AI / design / research / content / KM / data)
- §5 — Recommended stacks (solo / team / role)
- §6 — Coverage gaps (game / GPU kernel / Web3 / embedded — areas the cohort doesn't cover)

---

### 1. Functional positioning of the 21 repos

| Code | Repo | Orthogonal niche (unique value axis) |
|---|---|---|
| **GS** 🆕 | `garrytan/gstack` | **Opinionated role-based setup** — Garry Tan's actual 23-role-agent setup (CEO/Designer/Eng-Mgr/Release/Doc/QA); avg SKILL.md 52KB = cohort-deepest |
| **AM** | `affaan-m/everything-claude-code` | **General-purpose agent harness** — 60 agents + 228 skills + commands + hooks + install; king of breadth |
| **O**  | `obra/superpowers` | **Engineering methodology** — TDD / debug / brainstorm / plan / review meta-skills; king of depth |
| **NX** | `nexu-io/open-design` | **Design output** — 19 skills + 71 design systems; multi-platform (web/desktop/mobile/slides/PDF) creative production |
| **AA** 🆕 | `msitarzewski/agency-agents` | **Personality-driven multi-role agency** — 222 agents across **18 domains** (incl. game-dev / spatial / academic / finance); each agent has personality + emoji + vibe |
| **A**  | `anthropics/skills` | **Official spec + practical demos** — Defines SKILL.md standard; ships PDF / theme / doc-coauthoring reference skills |
| **NL** | `nextlevelbuilder/ui-ux-pro-max-skill` | **Component-level UI/UX** — 161 palettes + 57 font pairs + BM25 reasoning engine; visual polish |
| **AD** | `addyosmani/agent-skills` | **Production engineering** — General software practice with strict quality gates (Specific / Verifiable / Battle-tested / Minimal) |
| **CH** | `coreyhaines31/marketingskills` | **Marketing vertical** — CRO / SEO / copywriting / growth; only specialist in this lane |
| **C**  | `ComposioHQ/awesome-claude-skills` | **Awesome-list** — 864 SKILL.md index; widest discovery surface |
| **M**  | `mattpocock/skills` | **TS engineer's lens** — /diagnose / /tdd / /grill-me; anti-failure-mode design |
| **OAI**| `openai/skills` | **Codex companion catalog** — three-tier `.system / .curated / .experimental` |
| **MA** | `multica-ai/andrej-karpathy-skills` | **Single-file behavioral directive** — Karpathy's 4 LLM-coding anti-pattern principles |
| **K**  | `kepano/obsidian-skills` | **Obsidian / Markdown / Canvas** — only KM specialist |
| **V**  | `vercel-labs/agent-skills` | **Vercel deploy + React/Next.js production** — Official authority; live `WebFetch` for fresh web rules |
| **UA** 🆕 | `Egonex-AI/Understand-Anything` | **Codebase comprehension / knowledge-graph** — turns an existing codebase into an interactive knowledge graph (nodes/edges/layers/tour); only repo for *understanding existing code* (all others lean toward producing new code); multi-platform (claude/copilot/codex/opencode) |
| **OS** 🆕 | `Fission-AI/OpenSpec` | **Spec-driven development** — spec→tasks→implementation workflow ("write the spec first, then implement"); a spec tool not a skill collection (0 SKILL.md, 517 docs); complements O's process methodology |
| **CO** 🆕 | `santifer/career-ops` | **Job-search / career automation** — resume / CV / ATS / application tracking; brand-new vertical (no prior career repo); very strong engineering, 13-language READMEs |
| **TS** 🆕 | `Leonxlnx/taste-skill` | **Design taste / aesthetic judgment** — steers agents away from generic/mediocre output; orthogonal to NX (NX governs *what to produce*, TS governs *aesthetic judgment/taste*); high lesson density (41.4%) |
| **L30** 🆕 | `mvanhorn/last30days-skill` | **Recent-trend research** — last-30-day trends across Reddit / X / YouTube / HN / web; new research category; one 140KB SKILL.md |

---

### 2. AM × O × NX deep-dive

> The most-asked comparison. All three are top-tier (totals 129 / 115 / 110) but occupy different axes.

#### 2.1 Core positioning

| | **AM** (everything-claude-code) | **O** (superpowers) | **NX** (open-design) |
|---|---|---|---|
| Positioning | General-purpose agent harness (capability surface) | Engineering methodology (process layer) | Design output (output layer) |
| Value axis | **Breadth** | **Depth** | **Vertical** |
| Question it answers | "What agents / skills / commands does our team install?" | "How do we work without screwing up?" | "How do we produce coherent, beautiful visuals?" |
| Content body | 228 skills + 60 agents + commands + hooks | 14 deeply-polished skills (TDD / debug / plan / brainstorm…) | 19 skills + 71 design systems |
| When to install | Team base setup | Anytime (when discipline is needed) | When you need to produce UI / visuals |
| Enforcement | Optional reference | **Mandatory workflow** (hard gates) | Optional reference |

#### 2.2 Overlaps (content collision points)

| Pair | Collision zone | Specifics |
|---|---|---|
| AM ↔ O | **engineering methodology** | AM has reviewer/planner/python-reviewer agents; O has TDD/debugging/planning skills. AM bakes practices into **agents** (commitlint/ESLint/CoC), O bakes methodology **gates** into skill bodies (HARD-GATE / eval evidence required) |
| AM ↔ NX | **frontend / UI boundary** | AM has some frontend-design-related skills; NX is a global design system. AM leans "implementation"; NX leans "specification" |
| O ↔ NX | **nearly fully orthogonal** | Process layer vs output layer; minimal collision |

#### 2.3 Orthogonality (independent axes — combinable)

```
                  Process / Methodology (O)
                            │
                            │
  Capability ────────────── ┼────────────── Visual output
  surface (AM)              │                  (NX)
                            │
                            │
```

- **AM ⊥ NX**: engineering harness vs design production — zero conflict, frequently stacked
- **O ⊥ NX**: methodology vs output — zero conflict
- **AM ⊥ O with intersection**: the intersection is itself complementary (AM provides "capability to do things," O provides "discipline for how to do them")

#### 2.4 Complementarity (recommended stack combinations)

| Stack | Use case | Synergy |
|---|---|---|
| **AM + O** | Best team baseline | AM fills the capability pool; O adds discipline gates. Agent has both capability and rigor. **Most common combo** |
| **AM + NX** | Full-stack delivery (engineering + design) | AM handles engineering; NX handles visual/UI output |
| **O + NX** | Designer who wants process discipline | O's brainstorming + writing-plans guide design decisions; NX produces |
| **AM + O + NX** | One-stop power-user | Engineering + methodology + design fully loaded. ⚠ Cost: highest context overhead, agent choice paralysis; needs careful configuration |

#### 2.5 When to install only one

| Which one | Scenario |
|---|---|
| **AM only** | You want "one-click full setup," don't want to assemble. Or you're upgrading an existing harness |
| **O only** | You have an existing setup you don't want to replace, but want to add TDD/debug/plan **mandatory discipline layer** |
| **NX only** | You're a designer / marketer who doesn't need AM's 60 agents but wants design systems |

---

### 3. Other notable overlap pairs

#### 3.1 A vs OAI — two official catalogs

| Common ground | Differences |
|---|---|
| Both are platform official (Anthropic vs OpenAI) | A serves Claude, OAI serves Codex; A ships PDF/theme/doc-coauthoring as cross-purpose reference skills, OAI ships skill-creator + eval tooling |

→ **Complementary**: pick by your host platform. If you use both agent platforms, install both; the specs cross-reference but implementations are separate.

#### 3.2 AM vs AD — two broad-engineering repos

| Common ground | Differences |
|---|---|
| Both cover general software engineering (API / testing / perf / security / refactoring / docs) | AM is **breadth + harness** (agents + commands + hooks); AD is **depth + quality** (every skill has Verification + Red Flags sections, enforces 4 principles Specific/Verifiable/Battle-tested/Minimal) |

→ **Complementary with overlap**: use AM as team base, AD as the "quality gate" during reviews. Or pick one (overlap ~50%).

#### 3.3 NL vs NX — two design repos

| Common ground | Differences |
|---|---|
| Both do design | NL is **component-level UI/UX** (buttons / forms / palettes / fonts / reasoning engine); NX is **system-level + multi-platform output** (71 design systems + slides/PDF/video/mobile) |

→ **Complementary**:
- Single-platform UI component-level → **NL**
- Cross-platform creative output / brand systems → **NX**
- Both component and brand → install both

#### 3.4 M vs MA — two individual lenses

| Common ground | Differences |
|---|---|
| Both individual-author | M is **lightweight composable techniques** (/diagnose / /tdd / /grill-me) targeting failure modes; MA is **always-on 4 Karpathy principles** in a single file |

→ **Complementary**: MA gives base discipline; M's skills trigger on demand. Together = lightest possible solo-developer baseline.

#### 3.5 C vs everyone — Awesome-list overlap

C is an awesome-list, so **it overlaps with everyone** (by aggregating their skills). The difference:
- C's SKILL.md averages just 3.4 KB (vs O's 8.2 KB, AD's 10.7 KB) — **broad but shallow**
- C has 864 SKILL.md (biggest "index" in cohort) but D10 supplementary density is just 0.03 (lowest)

→ **When to use C**: discovery / browsing the skill ecosystem to see what's possible. **Not a primary install**; once you find a direction, switch to the matching specialist.

#### 3.7 AM vs GS — two "all-rounder" repos, opposite philosophies (v1.2 addition)

| Common ground | Differences |
|---|---|
| Both are "team production-grade" general harnesses | **AM = breadth + neutral** (228 skills + 60 agents; "fill the capability pool"); **GS = depth + opinion** (51 skills but avg 52KB; "Garry Tan's personally-vetted operational flow") |

→ **Choice**:
- Team is startup / accepts strong opinion → **GS** (copy YC-leader's setup verbatim)
- Team is enterprise / needs capability diversity → **AM** (compose your own / swap components)
- Want "AM's breadth + GS's depth" → install both: **AM as capability pool, GS as high-quality reference**

#### 3.8 AM vs AA — two "big-bag" repos, different axes (v1.2 addition)

| Common ground | Differences |
|---|---|
| Both are large-scale (AM 228 skills, AA 222 agents) | **AM = skill-centric** (each skill solves a capability); **AA = role-centric + personality** (each agent has personality + emoji + vibe, organized by *role* not *task*; 18 domains vs AM's mostly-engineering focus) |

→ **Choice**:
- You want "engineering capability pool" → **AM**
- You want "multi-role / cross-domain agency" → **AA** (covers finance/academic/spatial-computing/game-dev that AM doesn't)
- Use both? Possible, but trigger collisions may occur — set up priority / namespace ordering

#### 3.6 V vs A vs OAI — three official authorities

| | A | OAI | V |
|---|---|---|---|
| Official for | Claude Skills spec | Codex skill catalog | Vercel deploy + React/Next.js |
| Scope | Horizontal (any domain) | Horizontal (any domain) | Vertical (web frontend / Vercel-native) |
| Strength | Spec authority | Three-tier `.system/.curated/.experimental` governance model | Live WebFetch for fresh web rules |

→ **Orthogonal**: all three cover entirely different "official" domains. V has no overlap with A/OAI; it's platform-specific authority.

#### 3.9 UA vs O vs OS — three "process / understanding" axes (v1.5 addition)

| | **UA** (Understand-Anything) | **O** (superpowers) | **OS** (OpenSpec) |
|---|---|---|---|
| Axis | **Understand existing code** (read / map / onboard) | **How to build** (TDD / debug / plan methodology) | **Spec-first build** (spec → tasks → implementation) |
| Direction | Inbound: comprehend what exists | Process: discipline while building | Inbound→outbound: define intent, then implement |
| Artifact | Interactive knowledge graph (nodes/edges/layers/tour) | Meta-skills (mandatory gates) | Spec documents + task breakdown |

→ **Complementary**: UA maps an unfamiliar codebase before you touch it; OS turns a desired change into a spec; O enforces discipline while implementing. UA ⊥ NX/CO (different lifecycle stages).

---

### 4. Task → Repo lookup

> ✅ = primary · ➕ = secondary / complementary · ⚠ = cohort weak / no specialist

#### 4.1 Web · Mobile · Systems development

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 1 | **Web frontend (React/Next.js production)** | V ✅ | AD ➕ AM ➕ | V is Vercel official; 40+ React perf rules sorted by Impact |
| 2 | UI components / visual polish | NL ✅ | NX ➕ | NL ships 161 palettes + 57 fonts + BM25 reasoning |
| 3 | React Native / mobile web | V ✅ | NL ➕ | V has react-native-skills |
| 4 | iOS / Android native | NL ✅ | A ➕ | NL covers SwiftUI; A has doc-coauthoring |
| 5 | **Backend API / microservices** | AM ✅ | AD ➕ O ➕ | AM has API/data/architecture agents; O adds methodology gates |
| 6 | Database / SQL optimization | AD ✅ | C ➕ | AD strong on Verification; C has DB-specific skills |
| 7 | DevOps / CI / Deployment | AM ✅ | V ➕ | AM has hooks/commitlint/lint; V specializes in Vercel deploy |
| 8 | Cloud IaC (Terraform/K8s) | AM ⚠ | — | ⚠ Cohort weak; rely on AM general engineering |
| 9 | **Game development** (Web / Engine) | **AA ✅** (v1.2) | C search | 🆕 **AA has 20 game-development agents** (cohort previously had no game specialist; AA fills the gap) |
| 10 | Web3 / Smart Contracts | ⚠ no specialist | C search | ⚠ Same as above |
| 11 | Embedded / Rust systems | M ✅ | MA ➕ | M's first-principles + MA's anti-pattern guard |

#### 4.2 AI · ML · Agent building

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 12 | **LLM application / Agent building** | AM ✅ | OAI ➕ A ➕ | AM is the agent-harness king; OAI for Codex; A for spec |
| 13 | Prompt engineering | A ✅ | O ➕ | A has skill-creator; O's brainstorming helps prompt design |
| 14 | **Skill / Agent meta-development** (writing new skills) | A ✅ | OAI ➕ AM ➕ | A defines SKILL.md spec; AM gives reference impl |
| 15 | RAG / search systems | C search ✅ | AM ➕ | C has multiple search/research-writer skills |
| 16 | **GPU kernel (CUDA / Triton / MPS)** | ⚠ no specialist | MA + M | ⚠ Cohort has **no GPU specialist**; MA anti-pattern + M's engineering rigor as fallback |
| 17 | Model fine-tuning | AD ✅ | M ➕ | General production engineering; no specialist |
| 18 | Model evaluation / benchmarking | **O ✅** | AD ➕ | O **mandates eval evidence** (gold standard) |
| 19 | Inference optimization | AD ✅ | V (web side) | AD performance practice; V for web perf |
| 20 | Agent-harness optimization | **AM ✅** | O ➕ | AM literally describes itself as "agent harness perf framework" |

#### 4.3 Engineering methodology

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 21 | **TDD** | **O ✅** | AD ➕ | O's TDD skill is the gold standard |
| 22 | **Systematic debugging** | **O ✅** | M ➕ | O's systematic-debugging + M's /diagnose |
| 23 | Brainstorming / planning | **O ✅** | — | O's brainstorming + writing-plans suite |
| 24 | Code review | AM ✅ | AD ➕ O ➕ | AM has multiple reviewer agents |
| 25 | Refactoring | M ✅ | O ➕ MA ➕ | M minimizes unnecessary diffs; O plan-first; MA "surgical changes" |
| 26 | Large-scale migration / framework upgrades | AD ✅ | M ➕ O ➕ | AD has migration patterns; O adds plan flow |
| 27 | Performance optimization (web) | V ✅ | AD ➕ | V ships 40+ React perf rules |
| 28 | Performance optimization (general) | AD ✅ | M ➕ | AD production engineering; M first-principles feedback |
| 29 | Security audit | AM ✅ | AD ➕ | General engineering; no specialist |
| 30 | Architecture decisions | O ✅ | AD ➕ AM ➕ | O's writing-plans + brainstorming |
| 31 | Documentation writing | A ✅ | K ➕ AD ➕ | A's doc-coauthoring; K's Markdown format depth |
| 31a | **Understand / onboard onto an existing codebase** | **UA ✅** | A ➕ | 🆕 v1.5 · UA builds an interactive knowledge graph (nodes/edges/layers/onboarding tour) from existing code — only repo specialized in *reading* code |
| 31b | **Spec-driven development** (spec → tasks → implementation) | **OS ✅** | O ➕ | 🆕 v1.5 · OS writes the spec first then implements; O adds methodology gates |

#### 4.4 Research · Experimentation

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 32 | **Literature review** | K ✅ | A ➕ | K syncs Obsidian notes; A outputs docs |
| 33 | Benchmarking / evaluation | **O ✅** | M ➕ | O mandates eval evidence; M /diagnose stresses feedback loop |
| 34 | Experimental design | O ✅ | M ➕ | O's writing-plans + brainstorming |
| 35 | **All-night batch loop / autonomous runs** | **AM ✅** | O ➕ | AM has install scripts + hooks + cron-style commands; O has dispatching-parallel-agents + subagent-driven-development |
| 36 | Data analysis / EDA | A ✅ | C ➕ | A has data-analysis demo skills |
| 37 | Hypothesis testing / "running experiments" | M ✅ | O ➕ | M's /diagnose stresses first-principles; O adds discipline |
| 38 | Paper writing | A ✅ | K ➕ | A doc-coauthoring; K note sync |
| 39 | Reproducibility | O ✅ | MA ➕ | O mandates verification; MA goal-driven execution |
| 39a | **Recent-trend research** (last-30-day, Reddit/X/YouTube/HN) | **L30 ✅** | C ➕ | 🆕 v1.5 · L30 specializes in last-30-day trends across social + web; C for broader discovery |

#### 4.5 Design · Creative

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 40 | Design system | **NX ✅** | NL ➕ | NX ships 71 design systems |
| 41 | Visual mockup | NX ✅ | NL ➕ | NX is multi-platform (web/desktop/mobile) |
| 42 | Brand / Logo / CI | NX ✅ | — | NX has brand-identity + logo skills |
| 43 | Typography / color | **NL ✅** | NX ➕ | NL has 161 palettes + 57 font pairs |
| 44 | Slides / Presentation | A ✅ | NX ➕ | A's theme-factory + slide skills are canonical |
| 45 | PDF / document generation | **A ✅** | C ➕ | A's PDF skill is the standard |
| 46 | Icon | NX ✅ | NL ➕ | NX has icon-design with 15 styles |
| 47 | **Taste exploration / mood board** | **NX ✅** | TS ➕ A ➕ | NX's 71 design systems = 71 "taste samples"; 🆕 TS adds aesthetic-judgment guardrails (steers away from generic output); A's theme-factory has 10 presets |
| 48 | Print / Banner / social images | NX ✅ | — | NX banner-design with 22 styles |
| 49 | UI/UX component level | **NL ✅** | NX ➕ | NL is the specialist |
| 50 | Brand voice | NX ✅ | CH ➕ | NX brand identity + CH marketing voice |
| 50a | **Aesthetic judgment / avoid generic output** | **TS ✅** | NX ➕ | 🆕 v1.5 · TS governs *taste* (steers agents away from mediocre/generic results); NX governs *what to produce* |

#### 4.6 Content · Marketing

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 51 | Copywriting | **CH ✅** | — | CH only specialist |
| 52 | SEO | **CH ✅** | — | CH only specialist |
| 53 | **CRO / Landing page** | CH ✅ | V ➕ | CH page-cro + V web-design-guidelines (design + conversion) |
| 54 | Email marketing | CH ✅ | C ➕ | CH specialist |
| 55 | Social media | CH ✅ | C ➕ | CH + C (slack/twitter) |
| 56 | Content research | C ✅ | CH ➕ | C's content-research-writer |
| 57 | Growth analytics | CH ✅ | — | CH analytics skills |

#### 4.7 Knowledge management · Notes

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 58 | **Markdown / Obsidian** | **K ✅** | — | K is Obsidian creator's repo |
| 59 | Knowledge graphs / JSON Canvas | K ✅ | UA ➕ | K has Canvas skill; 🆕 UA builds knowledge graphs from code |
| 60 | Personal notes | K ✅ | A ➕ | K Obsidian + A doc-coauthoring |
| 61 | Meeting notes | C ✅ | K ➕ | C meeting-insights-analyzer |
| 62 | Research synthesis | K ✅ | A ➕ | K notes + A doc output |

#### 4.8 Productivity · Communication

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 63 | Email | C ✅ | — | C internal-comms |
| 64 | Slack / chat | C ✅ | — | C slack-gif-creator etc. |
| 65 | Project management | **O ✅** | AM ➕ | O plan management + AM commands |
| 66 | Onboarding docs | A ✅ | UA ➕ AM ➕ | A doc-coauthoring; 🆕 UA generates onboarding guides from the codebase |
| 66a | **Job search / resume / ATS** | **CO ✅** | — | 🆕 v1.5 · CO is the only career-automation vertical (resume/CV/ATS/application tracking) |

#### 4.9 Data · Integration

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 67 | API integration (OAuth / REST / GraphQL) | C ✅ | AM ➕ | C's connect / connect-apps series |
| 68 | Browser automation | C ✅ | — | C has related skills |
| 69 | Web scraping | C ✅ | — | C has related skills |
| 70 | Data ETL | AD ✅ | C ➕ | AD general engineering; C scattered |

#### 4.10 Meta · General

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 71 | **5-minute drop-in CLAUDE.md** | **MA ✅** | — | Single file, zero friction |
| 72 | Browse / discover skill ecosystem | C ✅ | — | 864 SKILL.md index |
| 73 | Learn the SKILL.md spec | A ✅ | OAI ➕ | A is official authority |
| 74 | Multi-agent platform support | NX ✅ | UA ➕ NL ➕ V ➕ | NX covers 9 platforms; 🆕 UA is multi-platform (claude/copilot/codex/opencode) |
| 75 | Solo independent engineer | M ✅ | MA ➕ | M lightweight + MA anti-pattern |
| 76 | Team / company adoption (general enterprise) | AM ✅ | AD ➕ O ➕ | AM hooks/commitlint/CoC; AD strict quality gates; O methodology enforcement |
| 77 | 🆕 **YC / Startup opinionated setup** | **GS ✅** | AM ➕ | 🆕 v1.2 · Garry Tan's actual role setup — copy verbatim, no component picking |
| 78 | 🆕 Multi-role / multi-domain agency-as-agents | **AA ✅** | GS ➕ AM ➕ | 🆕 v1.2 · 222 agents across 18 domains (finance / academic / spatial-computing / game-dev etc.) |
| 79 | 🆕 Deep SKILL.md template (learning to write "thick" SKILLs) | **GS ✅** | NL ➕ | 🆕 v1.2 · GS avg SKILL.md 52KB = cohort-deepest; NL 12KB is second |

---

### 5. Recommended stacks

> Don't over-install — context is a public resource. 3–4 repos is usually enough.

| Scenario | Stack | Rationale |
|---|---|---|
| **Solo indie engineer (lightweight base)** | MA + M | One-line CLAUDE.md base discipline; M's skills trigger on demand |
| **Designer / Marketer** | NX + K | NX for design output; K for notes / research |
| **Team Dev base** | **AM + O** | Capability surface + methodology gates — **most common combo** |
| **Web Product Team** (Vercel-native) | V + AD + O | V deploy + AD quality gate + O discipline |
| **Web Product Team** (full-stack with design) | AM + O + NX + V | Engineering + methodology + design + Vercel |
| **Marketing / Growth Team** | CH + V + A | CH marketing + V landing-page engineering + A document output |
| **Researcher / Academic** | K + O + A | K notes + O eval discipline + A document output |
| **AI Agent / Skill builder** | A + AM + O | A spec + AM reference impl + O methodology |
| **Try / evaluate the ecosystem** | MA + C | MA zero-friction install + C ecosystem browse |
| **Codex user** | OAI + O + A | Codex companion + methodology + spec |
| 🆕 **YC / Startup founding team (copy-paste)** | **GS** + optional O | GS gives Garry Tan's setup verbatim; O adds methodology discipline |
| 🆕 **Cross-domain studio / multi-role agency** | **AA** + AM | AA provides 18-domain role agents; AM adds engineering harness |
| 🆕 **Game development** | **AA** + M | AA has 20 game-dev agents (only v1.2 coverage); M adds engineering rigor |
| 🆕 **"Best-in-class" SKILL.md template** | **GS** + A | GS avg 52KB = deepest cohort reference; A is the spec |
| 🆕 **Inherit / onboard onto a legacy codebase** | **UA** + O | 🆕 v1.5 · UA maps the existing code into a knowledge graph; O adds discipline before you change it |
| 🆕 **Spec-first product team** | **OS** + O + AM | 🆕 v1.5 · OS defines spec→tasks; O adds gates; AM supplies the capability pool to implement |
| 🆕 **Job seeker / career automation** | **CO** + A | 🆕 v1.5 · CO handles resume/ATS/tracking; A for polished document output |

---

### 6. Coverage gaps (areas the cohort doesn't cover)

The cohort previously had **no specialist** for these domains — opportunities for future cohort additions:

> ✅ **v1.2 closed**: ~~Game development~~ — **AA ships 20 game-development agents**
> ✅ **v1.5 closed**: ~~Understand existing codebase~~ — **UA builds interactive knowledge graphs from existing code**; ~~Spec-driven development~~ — **OS ships a spec→tasks→implementation workflow**; ~~Job-search / career automation~~ — **CO is a full resume/CV/ATS/application-tracking vertical**

| Gap | Best fallback | Suggestion |
|---|---|---|
| **GPU kernel** (CUDA / Triton / MPS) | MA + M (indirect) | ⚠ Needs specialist; MA anti-pattern + M /diagnose as discipline scaffolding |
| **Web3 / Smart Contracts** | C search | ⚠ Needs specialist |
| **Cloud IaC** (Terraform / K8s / Pulumi) | AM (general) | ⚠ Missing depth; AM hooks/commands work but shallow |
| **Embedded / Rust systems** | M + MA | ⚠ Indirect via general engineering rigor |
| **Native mobile** (iOS / Android primary) | NL (some SwiftUI) | ⚠ NL leans UI; doesn't cover native API |
| **Computer vision / multimodal ML** | AD + M (general) | ⚠ No CV / multimodal specialist |
| **Data engineering at scale** (Spark / Airflow / dbt) | AD (general) + C search | ⚠ Missing specialist |
| **Database internals** (B-tree / OLAP / optimization) | AD | ⚠ Missing specialist |
| **OS / Compiler / Linker** work | M + MA (general discipline) | ⚠ Deepest systems work, cohort doesn't cover |
| **Quant / Trading algorithms** | M + AD | ⚠ Missing specialist |
| **Offensive security** (pentest / red team) | AM, AD (defensive) | ⚠ No offensive specialist |

> **Key observation (v1.5 update)**: the cohort is strong in *agent dev + design + web frontend + marketing + KM + multi-role agency (AA) + game-dev (AA) + **codebase comprehension (v1.5 UA) + spec-driven dev (v1.5 OS) + job-search (v1.5 CO) + design taste (v1.5 TS) + recent-trend research (v1.5 L30)***; weak in *low-level systems / GPU / multimodal ML / cloud IaC / smart contracts*. Deep systems / GPU / Web3 are still self-built territory.

---

### Appendix: 13-repo functional orthogonality matrix

> Coverage strength per domain on a 1–5 scale. ✅ ≥ 4, ➕ ≥ 2, — = not covered.

| Domain \ Repo | AM | O | NX | A | NL | AD | CH | C | M | OAI | MA | K | V | **GS** 🆕 | **AA** 🆕 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| General engineering | ✅ | ✅ | — | ➕ | — | ✅ | — | ➕ | ✅ | ✅ | ✅ | — | — | **✅** | ➕ |
| Web frontend | ➕ | — | — | — | ➕ | ➕ | ➕ | ➕ | — | — | — | — | **✅** | ➕ | ➕ |
| UI/UX design | — | — | **✅** | ➕ | **✅** | — | — | ➕ | — | — | — | — | ➕ | ➕ | ➕ |
| Design system / brand | — | — | **✅** | ➕ | ➕ | — | ➕ | — | — | — | — | — | — | ➕ | ➕ |
| Methodology (TDD/debug/plan) | ➕ | **✅** | — | ➕ | — | ➕ | — | ➕ | ➕ | ➕ | ✅ | — | — | ➕ | — |
| AI / agent building | **✅** | ➕ | — | ✅ | — | ➕ | — | ➕ | — | ✅ | ➕ | — | — | **✅** | **✅** |
| Skill meta-development | ➕ | ➕ | — | **✅** | — | ➕ | ➕ | ➕ | — | **✅** | — | — | ➕ | ➕ | ➕ |
| Marketing / growth | — | — | ➕ | — | — | — | **✅** | ➕ | — | — | — | — | ➕ | — | ➕ |
| Knowledge management | — | — | — | ➕ | — | — | — | — | — | — | — | **✅** | — | ➕ | ➕ |
| Document output | ➕ | — | ➕ | ✅ | — | ➕ | ➕ | ➕ | — | — | — | ➕ | — | ✅ | ➕ |
| Performance / optimization | ➕ | — | — | — | — | ✅ | — | — | ➕ | — | ➕ | — | **✅** | ➕ | — |
| Research / eval | ➕ | **✅** | — | ➕ | — | ➕ | — | — | ✅ | — | ➕ | ➕ | — | ➕ | ➕ |
| Discovery / browse | — | — | — | — | — | — | — | **✅** | — | — | — | — | — | — | ➕ |
| **Game development** 🆕 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **✅** |
| **Multi-role agency (CEO/Designer/QA/etc)** 🆕 | ➕ | — | — | — | — | — | — | — | — | — | — | — | — | **✅** | **✅** |
| **Cross-domain (academic/finance/spatial)** 🆕 | ➕ | — | — | — | — | — | — | ➕ | — | — | — | — | — | — | **✅** |

> 🆕 **v1.5 repos** (UA / OS / CO / TS / L30) open new domain rows not in the 13-repo matrix above: **codebase comprehension** (UA), **spec-driven dev** (OS), **job-search / career** (CO), **design taste** (TS), **recent-trend research** (L30). Each is the sole occupant of its column, so they are listed in §1 rather than scored here.

---

_Based on §10 philosophy research + sampled docs from each repo. Task list covers AI-agent use cases including the user-requested ones (game / frontend / backend / AI GPU / research / experiments / loops / design / taste exploration) and 30+ adjacent categories. Coverage-gap section is honest about cohort limits — no forced recommendations for domains the cohort doesn't excel in._


---

<a id="agent-summary"></a>

## Appendix B — Five-Model Cross-Comparison

This document collects the cross-model summary of 5 AI models (Claude / ChatGPT / Gemini / Grok / Perplexity) independently evaluating this repo's 15 skill repos. **This is not my own scoring** (see `EVALUATION.en.md`) — it's a horizontal aggregation of judgments made by different models on the same cohort.

> ⏱️ **Snapshot note (v1.5 update)**: This five-model comparison was collected on the **15-repo cohort** (v1.3 era), **predating the v1.5 expansion to 21 repos** (which added UA/OS/CO/TS/L30). Those 5 new repos are NOT part of this cross-model comparison; their in-repo scores live in `EVALUATION.en.md §14`. Re-running the five-model comparison is follow-up work.

Related docs:
- Scoring detail → `EVALUATION.en.md` · [`scoring.ipynb`](./scoring.ipynb)
- Task → repo lookup → Appendix A

---

### TL;DR

**Converged minimum viable stack** (intersection of all 5 models):

1. `anthropics/skills` (foundation)
2. `obra/superpowers` (methodology)
3. `gstack` or `everything-claude-code` (operational, pick one)
4. Add as needed: `nexu-io/open-design` (design), `vercel-labs/agent-skills` (Next.js)

Whether to add `karpathy-skills` / `addyosmani` / `mattpocock` depends on your specific stack — **there's no must-add consensus**.

---

### 1. Strong consensus (all models recommend)

Four foundational picks have essentially no debate:

| Repo | Role | All-5 consensus |
|---|---|---|
| `anthropics/skills` | Spec / foundation layer | Everyone installs it |
| `obra/superpowers` | Methodology layer (TDD, subagent-driven) | Everyone installs it |
| `gstack` **OR** `everything-claude-code` | Operational layer (pick one) | Solo → former; team/multi-harness → latter |
| `nexu-io/open-design` | Design extension | Add when design is a bottleneck |

### 2. Strong consensus (all models avoid)

| Repo | Reason |
|---|---|
| `msitarzewski/agency-agents` | 222 personality agents unanimously characterized as "**inspiration library, not infrastructure**". ChatGPT verbatim: "don't treat such a sprawling library as core"; Claude skipped it; Gemini warned about token cost and latency |
| `openai/skills` (D1=1) | Dead last, unanimously skipped |
| `kepano/obsidian-skills` | Only meaningful inside an Obsidian workflow |

### 3. Main disagreements

#### 3.1 `multica-ai/andrej-karpathy-skills`

- **Claude / Gemini**: high-value drop-in given D1=9
- **ChatGPT**: "personal config, not suitable for primary lib", placed in tier C
- **Verdict**: disagreement stems from positioning — it's an **overlay, not standalone**

#### 3.2 `addyosmani/agent-skills`

- **ChatGPT**: A-tier must-have
- **Grok / Claude**: not particularly emphasized
- **Differentiator**: whether you're doing production backend

#### 3.3 `ComposioHQ/awesome-claude-skills`

- **Grok**: recommend as **discovery layer**
- **Others**: think meta-list depth isn't enough; doesn't belong in workflow

#### 3.4 `mattpocock/skills`

- **All-5 agree**: only use in TypeScript context
- **ChatGPT**: B-tier "daily-relevant"
- **Claude**: treats it as a **vertical tool**

#### 3.5 Recommendation methodology itself (meta-level disagreement)

| Model | Style |
|---|---|
| ChatGPT / Claude | Give complete stacks |
| Grok | Advocates "max 2-3 trials" |
| Gemini | No recommendation, asks back about your scenario |

### 4. Unique viewpoints / per-model differentiated insights

| Model | Unique angle |
|---|---|
| **Claude** | Only one to do **`contribs < 20 = bus factor` analysis** (betting on person vs community), and warned the whole ecosystem is <1 year old and **not yet production-tested** |
| **ChatGPT** | Only one to give a **strict 5-layer architecture**: Spec → Methodology → Operational → Engineering → Vertical |
| **Gemini** | Warned about **S-tier locking into single-community methodology** risk |
| **Grok** | Operational principle: **"fit > score"** |

### 5. Converged minimum viable stack (restated)

> Intersection of all 5 models — installing this gets pushback from no one.

```
┌─────────────────────────────────┐
│ 1. anthropics/skills    (base)   │  must-have
│ 2. obra/superpowers     (method) │  must-have
│ 3. gstack OR ECC        (ops)    │  pick one
├─────────────────────────────────┤
│ 4a. open-design        (design)  │  as needed
│ 4b. vercel-labs        (Next.js) │  as needed
├─────────────────────────────────┤
│  karpathy / addyosmani / mattpocock │
│  depends on stack — no must-have    │
│  consensus                          │
└─────────────────────────────────┘
```

### 6. Footnote

**Perplexity didn't produce actual content this round** (only emitted its search process) — this is a known failure mode under **long prompt + tabular input**, **not a data problem**.

---

### Comparison with our internal v1.3 scoring

| Repo | 5-model consensus | v1.3 score /210 | v1.3 tier | Agreement |
|---|---|---:|:---:|---|
| `garrytan/gstack` | Operational (solo) | 156 | S | ✅ models' #1 & our #1 |
| `affaan-m/everything-claude-code` | Operational (team) | 154 | S | ✅ |
| `nexu-io/open-design` | Design as-needed | 152 | S | ✅ |
| `obra/superpowers` | Methodology must-have | 150 | S | ✅ |
| `msitarzewski/agency-agents` | **AVOID** | 146 | S | ⚠ we S but models avoid |
| `anthropics/skills` | Foundation must-have | 136 | A | ✅ |
| `addyosmani/agent-skills` | Disagreement | 128 | A | — |
| `mattpocock/skills` | TS-only | 114 | B | ✅ |
| `openai/skills` | **AVOID** | 113 | B | ⚠ |
| `ComposioHQ/awesome-claude-skills` | Disagreement (discovery) | 111 | B | — |
| `coreyhaines31/marketingskills` | (not called out) | 103 | B | — |
| `nextlevelbuilder/ui-ux-pro-max-skill` | (not called out) | 102 | B | — |
| `vercel-labs/agent-skills` | Next.js as-needed | 101 | B | ✅ |
| `multica-ai/andrej-karpathy-skills` | Disagreement (overlay vs standalone) | 92 | C | ✅ models disagree / we low |
| `kepano/obsidian-skills` | **AVOID** | 72 | D | ✅ |

**Key observations**:
- **Consensus picks ≈ our v1.3 S-tier** (4/5 overlap), except `agency-agents` — models call it an "inspiration library"; we gave S based on high D11/D12/D13/D14 but its D20=2 + D21=5 (medium) already hinted it isn't top-tier on the *task-quality* axis
- **`openai/skills` is in the model-consensus "avoid" set** vs our B-tier (113) — we pumped it on D10=9 (supplementary) + D21=8 (lessons), but models read D1=1 (velocity bottom) as "community doesn't want it" and treat that as a hard gate
- This is an interesting **"automated scoring vs LLM holistic judgment" divergence** — our 21-dim scoring is *feature additive*; LLM judgment is *non-linearly integrative* (e.g., "velocity too low = no investment" as a hard gate)

---

_This summary aggregates from 5 external LLM evaluations; for our scoring methodology see `EVALUATION.en.md` §2-§12._

---

### 7. Supplement: deep-essay "operational value" perspective (single-model detailed view)

> Unlike §1-§6 (the 5-model horizontal intersection), this section is **another independent LLM's** detailed taxonomy + ranking through the "operational value" lens.
> Provides: taxonomy (systemic / official-standard / vertical-augment / catalog) + 5-step evaluation + per-repo table + final ranking.
> Note: the original text included external citations judged to be LLM-hallucinated (targets had no relation to the argument); **removed** to avoid misleading readers.

Looking through the **operational value** lens (not star count alone), of these 15 skill sets the truly long-term-reusable ones fall into **4 categories**: systemic, official-standard, vertical-augment, and catalog.

> **Bottom line of this perspective**: in S-tier the strongest are `gstack` and `open-design`; in A-tier the steadiest is `anthropics/skills`; in B-tier the most situationally valuable are `openai/skills`, `vercel-labs/agent-skills`, `mattpocock/skills`.

#### 7.1 5-step evaluation

1. First ask "**is this a system?**", not the star count; whether it covers planning, implementation, review, testing, delivery determines the ceiling.
2. Then ask "**is this official or near-standard?**"; official repos are better as a foundation, community repos better as an acceleration layer.
3. Then ask "**is this vertically specialized?**"; design / frontend / marketing / DX repos are often strong at one point but unsuitable as overall framework.
4. Only then look at our scoring metrics; `Total` determines composite quality, `D1` determines first impression, `Stars/day` shows heat, `Forks/Contribs` shows ecosystem depth.
5. So the most important question isn't "who's the most popular" — it's "**are you using it as an OS, a template library, or an inspiration library?**"

#### 7.2 Per-repo evaluation table

| Repo | Strengths | Weaknesses | Verdict |
|---|---|---|---|
| **garrytan/gstack** | Most complete system, clear role split, planning → delivery coverage | Heavy, opinionated, steep learning curve | Strongest systemic |
| **affaan-m/everything-claude-code** | High heat, many contributors, resource-hub feel | Easy to become a junk drawer; methodology may not be unified | Strong resource hub, not necessarily systemic |
| **nexu-io/open-design** | D1 saturated, design-focused | Design-side bias, not full-stack | Strong design vector |
| **obra/superpowers** | Methodology-strong, good for agent capability augmentation | May be abstract; less landed than gstack | Good augmentation layer |
| **msitarzewski/agency-agents** | Super-broad, 222 agents catches the eye | "Personality agents" risk vapor; consistency risk high | Broad but not necessarily deep |
| **anthropics/skills** | Official, normative, good baseline | More reference impl than battle workflow | Steadiest foundation |
| **addyosmani/agent-skills** | Engineering-oriented, production-friendly | Range narrow, more like an engineering augment pack | Good for engineering teams |
| **mattpocock/skills** | Engineer-facing, hands-on | Few contributors, strong authorial voice | Good for TS/eng devs |
| **openai/skills** | Official endorsement, clarifies skill abstraction | Codex-oriented; not the Claude best-practice center | Worth referencing, not primary |
| **ComposioHQ/awesome-claude-skills** | Good for project discovery | Catalog itself provides no methodology | Navigation only |
| **coreyhaines31/marketingskills** | Clear sub-domain | Too vertical, weak generality | Good for marketing teams |
| **nextlevelbuilder/ui-ux-pro-max-skill** | Strong UI/UX scenarios | Tends to stay at visual layer | Patches the design gap |
| **vercel-labs/agent-skills** | Practical Web/Next.js/Vercel scenarios | Tech-stack-locked | Good for frontend product teams |
| **multica-ai/andrej-karpathy-skills** | Strong philosophy, strong rule sense | More principle-set than skill system | Good as CLAUDE.md thought source |
| **kepano/obsidian-skills** | Great for Obsidian users | Narrow scenario, low general value | Typical niche repo |

#### 7.3 Key evaluations

1. **`gstack`**: if you want an "AI software factory", it looks more like a complete product than a skill example; the repo positions itself as 23 specialists + 8 power tools, organized as a full pipeline from thinking → planning → building → review → testing → delivery.
2. `gstack`'s problem is exactly its completeness: strongly tied to the author's methodology, command system, and rhythm. Small teams ramp up fast; big teams will face governance cost to standardize.
3. **`anthropics/skills`**: most suitable as an "official baseline"; explicitly the Claude-skills public reference + sample library — includes spec, template, examples across categories, plus an explicit note that much content is for demonstration/education.
4. `anthropics/skills` downside: more "standard reference + sample repo" than an OS for running a complete R&D process.
5. **`openai/skills`**: value lies in clear official abstraction; positioned as the Codex skills catalog, with skills defined as discoverable, composable, self-contained folders.
6. `openai/skills` downside: ecosystem signals and Claude-compatibility mindshare are both weaker than Anthropic's side, so good for structural reference, not for primary framework on Claude.

#### 7.4 Recommended selection

1. If you want a "**main workflow**", pick `gstack`; it most resembles a system that can be deployed directly.
2. If you want a "**standard foundation**", pick `anthropics/skills`; it most resembles official spec, samples, templates.
3. If you're **design-driven product**, add `open-design` or `ui-ux-pro-max-skill`.
4. If you're a **Next.js / Vercel team**, add `vercel-labs/agent-skills`.
5. If you're a **multi-model team**, keep `openai/skills` for compatibility thinking, not as the sole source.

#### 7.5 Final ranking (by "long-term reusability")

| Rank | Repo | Lens |
|---:|---|---|
| 1 | `garrytan/gstack` | Heavy-duty combat system |
| 2 | `anthropics/skills` | Official standard component |
| 3 | `nexu-io/open-design` | Design special forces |
| 4 | `addyosmani/agent-skills` | Engineering augment pack |
| 5 | `vercel-labs/agent-skills` | Vercel/Next.js operational |
| 6 | `mattpocock/skills` | TS engineer's toolbox |
| 7 | `openai/skills` | Codex compatibility reference |
| 8 | `obra/superpowers` | Methodology augmentation layer |
| 9 | `everything-claude-code` | Resource hub (not necessarily systemic) |
| 10 | `andrej-karpathy-skills` | CLAUDE.md thought source |
| 11 | `awesome-claude-skills` | Discovery navigation |
| 12 | `ui-ux-pro-max-skill` | UI visual patch |
| 13 | `marketingskills` | Marketing vertical |
| 14 | `agency-agents` | Inspiration library (not recommended primary) |
| 15 | `obsidian-skills` | Niche |

> **One-liner summary**: `gstack` is the "heavy-duty combat system", `anthropics/skills` is the "official standard component", `open-design` is "design special forces"; the rest are mostly **augment packs or navigation packs**.

#### 7.6 §7 vs §1-§6 contrast

| Lens | §1-§6 (5-LLM horizontal intersection) | §7 (single-LLM operational-value view) |
|---|---|---|
| Top operational layer recommendation | `gstack` OR `everything-claude-code` | **`gstack` only** (ECC drops to #9) |
| Top foundation | `anthropics/skills` | Same |
| `obra/superpowers` positioning | Must-have methodology layer | **Downgraded to #8 "augmentation"** |
| `everything-claude-code` positioning | Operational layer alternative | **#9 "resource hub, not necessarily systemic"** |
| `addyosmani` | Disagreement | **#4 engineering augment** (explicit eng-team recommendation) |
| **Biggest divergence** | Whether obra & ECC are core layer | §7 thinks only gstack is the core system; everything else is auxiliary |

**Interpretation**: §7's "systemic" perspective is more **confident in declaring gstack as the sole primary workflow** than §1-§6's "consensus" view; §1-§6 leans toward "obra is must-have" as a mandatory methodology layer, §7 downgrades obra. That itself is an interesting meta-data — **different LLMs disagree on what counts as a "production-ready framework" standard**.
