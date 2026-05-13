# Skill Collection Evaluation

> 🌐 **Language**: [🇨🇳 中文](./EVALUATION.md) · **🇬🇧 English**

> Evaluation date: **2026-05-13**
> Cohort: 12 Agent Skills / Claude Skills / Skill-adjacent repos (vendored as git submodules)
> Scoring scale: **1–10** (10 = best in cohort)
> Max total: **150** (15 dims × 10)

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
| OAI| [`openai/skills`](https://github.com/openai/skills) | 18,982 | 1,259 | 2025-11-25 | 2026-05-12 | Codex skills catalog |

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
| OAI| 169 | 112.3 | 18,982 | 1,259 | 110 | 1  | 0.64 | 34  | 43  | 9,435 | **11.33** | 1 |

> **D1 caveat**: NX (`nexu-io/open-design`) is only 15 days alive — its velocity score of 2,582 stars/day includes early-peak bias and cannot be extrapolated 6 months out.

## 4. Score Matrix

```
Column order: AM | O | NX | A | NL | AD | CH | C | M | OAI | MA | K
```

| Dim | Description | AM | O | NX | A | NL | AD | CH | C | M | OAI | MA | K |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| D1  | Star Velocity ⭐ | 9 | 8 | **10** | 6 | 5 | 5 | 3 | 4 | 7 | 1 | 9 | 2 |
| D2  | Total Stars | 9 | **10** | 4 | 9 | 7 | 4 | 2 | 5 | 6 | 1 | 8 | 3 |
| D3  | Forks | **10** | 9 | 3 | 8 | 6 | 4 | 4 | 5 | 5 | 1 | 7 | 2 |
| D4  | Watchers | **10** | 8 | 2 | 9 | 5 | 3 | 4 | 5 | 6 | 1 | 7 | 2 |
| D5  | Commit Recency | **10** | **10** | **10** | 8 | 2 | 8 | 6 | 7 | 9 | 9 | 4 | 7 |
| D6  | Commit Cadence | 9 | 7 | **10** | 1 | 6 | 7 | 8 | 3 | 5 | 4 | 2 | 3 |
| D7  | Contributors | 9 | 7 | **10** | 3 | 6 | 4 | 4 | 5 | 1 | 8 | 2 | 3 |
| D8  | Skill Volume | 9 | 3 | 8 | 3 | 2 | 4 | 6 | **10** | 5 | 7 | 1 | 1 |
| D9  | Skill Depth | 6 | 5 | 3 | 9 | **10** | 8 | 9 | 3 | 2 | 7 | 1 | 4 |
| D10 | Supp. Material Density | 5 | 7 | 4 | 7 | 9 | 3 | 7 | 1 | 2 | **10** | 8 | 2 |
| D11 | Doc Quality | **10** | 8 | **10** | 6 | 9 | 9 | 8 | 8 | 7 | 3 | 7 | 4 |
| D12 | Eng. Hygiene | **10** | 9 | **10** | 6 | 8 | 8 | 9 | 4 | 6 | 3 | 3 | 3 |
| D13 | Multi-Agent Portability | 8 | 7 | **10** | 1 | 9 | 8 | 6 | 8 | 2 | 1 | 2 | 4 |
| D14 | Domain Breadth | **10** | 9 | 8 | 8 | 4 | 8 | 4 | 9 | 6 | 7 | 1 | 3 |
| D15 | Originality / Authority | 5 | 9 | 8 | **10** | 6 | 7 | 6 | 3 | 7 | **10** | 8 | 7 |
| **Σ** | **Total (out of 150)** | **129** | **116** | **110** | **94** | **94** | **90** | **86** | **80** | **76** | **73** | **70** | **50** |

## 5. Overall Ranking

### 5.1 Equal-weighted (default)

| Rank | Repo | Score | Tier |
|---:|---|---:|---|
| 🥇 1 | `affaan-m/everything-claude-code` | **129** | S |
| 🥈 2 | `obra/superpowers` | 116 | S |
| 🥉 3 | `nexu-io/open-design` | 110 | S |
| 4 | `anthropics/skills` | 94 | A |
| 4 | `nextlevelbuilder/ui-ux-pro-max-skill` | 94 | A |
| 6 | `addyosmani/agent-skills` | 90 | A |
| 7 | `coreyhaines31/marketingskills` | 86 | A |
| 8 | `ComposioHQ/awesome-claude-skills` | 80 | B |
| 9 | `mattpocock/skills` | 76 | B |
| 10 | `openai/skills` | 73 | B |
| 11 | `multica-ai/andrej-karpathy-skills` | 70 | B |
| 12 | `kepano/obsidian-skills` | 50 | C |

### 5.2 Velocity-emphasized (D1 weighted ×3)

If D1 (star velocity, the user-emphasized dimension) is weighted ×3 while others stay at ×1:

| Rank | Repo | Adj. Score |
|---:|---|---:|
| 🥇 1 | `affaan-m/everything-claude-code` | 147 |
| 🥈 2 | `obra/superpowers` | 132 |
| 🥉 3 | `nexu-io/open-design` | 130 |
| 4 | `anthropics/skills` | 106 |
| 5 | `nextlevelbuilder/ui-ux-pro-max-skill` | 104 |
| 6 | `addyosmani/agent-skills` | 100 |
| 7 | `coreyhaines31/marketingskills` | 92 |
| 8 | `mattpocock/skills` | 90 |
| 9 | `ComposioHQ/awesome-claude-skills` | 88 |
| 9 | `multica-ai/andrej-karpathy-skills` | 88 |
| 11 | `openai/skills` | 75 |
| 12 | `kepano/obsidian-skills` | 54 |

> Top-3 is invariant; middle-tier shuffles modestly. The velocity dimension is robust to weighting.

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
| **openai/skills** (B) | Official Codex skill catalog | ✅ Highest supplementary density (D10=10) + official authority; ⚠ Codex-only, small community |
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
| Marketing / Growth | `coreyhaines31/marketingskills` |
| Research / knowledge worker | `kepano/obsidian-skills` + `anthropics/skills` (doc-coauthoring etc.) |
| AI tool / skill builder | `anthropics/skills` (spec) + `affaan-m/everything-claude-code` (reference impl) |
| Quick trial (5-min onboarding) | `multica-ai/andrej-karpathy-skills` (single-file drop-in) |

---

_All raw queries are reproducible via `gh repo view --json` + local `find`; submodules are shallow-cloned at `skills/<owner>__<repo>/`. Reproduction recipe: see this repo's `.gitmodules` and rank-based equal-weighted methodology in §7._
