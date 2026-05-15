# Skill Collection Evaluation

> 🌐 **Language**: [🇨🇳 中文](./EVALUATION.md) · **🇬🇧 English**

> Evaluation date: **2026-05-13**
> Current snapshot: **v1.4** — **16-repo cohort × 21 dims** (v1.0 / v1.1 / v1.2 / v1.3 retained in `scoring.ipynb` history)
> Scoring scale: **1–10** (10 = best in cohort)
> Max total: **210** (21 dims × 10)
> ⚠ Note: §3/§4/§5 tables in this markdown still show v1.1 baseline for context. Latest v1.4 data (including GS / AA / CV / D16-D21) lives in `scoring.ipynb`. §11 covers v1.2 (D16-D19 social signals); §12 covers v1.3 (D20-D21 task-quality signals); **§13 covers v1.4 (CV caveman addition)**.

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

### 13.5 Comparison with `agent_summary.en.md` 5-model evaluation

CV is too new (created 2026-04-04), so **the 5-model evaluation in §1-§6 (collected before v1.2) does not cover CV**. To do a v1.4 full LLM re-evaluation, you'd need to re-prompt all 5 models on CV's operational value. The current v1.4 #6 is **this repo's internal scoring** — not the 5-model consensus.

> For the full 21-dim × 16-repo colored matrix + Δ v1.3→v1.4: open `scoring.ipynb` (renders directly on GitHub, no execution needed).
