# Task → Repo Decision Guide

> 🌐 **Language**: [🇨🇳 中文](./TASK_GUIDE.md) · **🇬🇧 English**

A task-first decision matrix across the 13 skill repos. Given a concrete AI-agent task, which repo (or stack) should you install?

- §1 — Where each repo sits on the functional map
- §2 — **AM × O × NX deep-dive**: overlaps, orthogonality, and complementary stacks (the most-asked comparison)
- §3 — Other notable overlap pairs
- §4 — Task → Repo lookup (~50 tasks across dev / AI / design / research / content / KM / data)
- §5 — Recommended stacks (solo / team / role)
- §6 — Coverage gaps (game / GPU kernel / Web3 / embedded — areas the cohort doesn't cover)

---

## 1. Functional positioning of the 13 repos

| Code | Repo | Orthogonal niche (unique value axis) |
|---|---|---|
| **AM** | `affaan-m/everything-claude-code` | **General-purpose agent harness** — 60 agents + 228 skills + commands + hooks + install; king of breadth |
| **O**  | `obra/superpowers` | **Engineering methodology** — TDD / debug / brainstorm / plan / review meta-skills; king of depth |
| **NX** | `nexu-io/open-design` | **Design output** — 19 skills + 71 design systems; multi-platform (web/desktop/mobile/slides/PDF) creative production |
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

---

## 2. AM × O × NX deep-dive

> The most-asked comparison. All three are top-tier (totals 129 / 115 / 110) but occupy different axes.

### 2.1 Core positioning

| | **AM** (everything-claude-code) | **O** (superpowers) | **NX** (open-design) |
|---|---|---|---|
| Positioning | General-purpose agent harness (capability surface) | Engineering methodology (process layer) | Design output (output layer) |
| Value axis | **Breadth** | **Depth** | **Vertical** |
| Question it answers | "What agents / skills / commands does our team install?" | "How do we work without screwing up?" | "How do we produce coherent, beautiful visuals?" |
| Content body | 228 skills + 60 agents + commands + hooks | 14 deeply-polished skills (TDD / debug / plan / brainstorm…) | 19 skills + 71 design systems |
| When to install | Team base setup | Anytime (when discipline is needed) | When you need to produce UI / visuals |
| Enforcement | Optional reference | **Mandatory workflow** (hard gates) | Optional reference |

### 2.2 Overlaps (content collision points)

| Pair | Collision zone | Specifics |
|---|---|---|
| AM ↔ O | **engineering methodology** | AM has reviewer/planner/python-reviewer agents; O has TDD/debugging/planning skills. AM bakes practices into **agents** (commitlint/ESLint/CoC), O bakes methodology **gates** into skill bodies (HARD-GATE / eval evidence required) |
| AM ↔ NX | **frontend / UI boundary** | AM has some frontend-design-related skills; NX is a global design system. AM leans "implementation"; NX leans "specification" |
| O ↔ NX | **nearly fully orthogonal** | Process layer vs output layer; minimal collision |

### 2.3 Orthogonality (independent axes — combinable)

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

### 2.4 Complementarity (recommended stack combinations)

| Stack | Use case | Synergy |
|---|---|---|
| **AM + O** | Best team baseline | AM fills the capability pool; O adds discipline gates. Agent has both capability and rigor. **Most common combo** |
| **AM + NX** | Full-stack delivery (engineering + design) | AM handles engineering; NX handles visual/UI output |
| **O + NX** | Designer who wants process discipline | O's brainstorming + writing-plans guide design decisions; NX produces |
| **AM + O + NX** | One-stop power-user | Engineering + methodology + design fully loaded. ⚠ Cost: highest context overhead, agent choice paralysis; needs careful configuration |

### 2.5 When to install only one

| Which one | Scenario |
|---|---|
| **AM only** | You want "one-click full setup," don't want to assemble. Or you're upgrading an existing harness |
| **O only** | You have an existing setup you don't want to replace, but want to add TDD/debug/plan **mandatory discipline layer** |
| **NX only** | You're a designer / marketer who doesn't need AM's 60 agents but wants design systems |

---

## 3. Other notable overlap pairs

### 3.1 A vs OAI — two official catalogs

| Common ground | Differences |
|---|---|
| Both are platform official (Anthropic vs OpenAI) | A serves Claude, OAI serves Codex; A ships PDF/theme/doc-coauthoring as cross-purpose reference skills, OAI ships skill-creator + eval tooling |

→ **Complementary**: pick by your host platform. If you use both agent platforms, install both; the specs cross-reference but implementations are separate.

### 3.2 AM vs AD — two broad-engineering repos

| Common ground | Differences |
|---|---|
| Both cover general software engineering (API / testing / perf / security / refactoring / docs) | AM is **breadth + harness** (agents + commands + hooks); AD is **depth + quality** (every skill has Verification + Red Flags sections, enforces 4 principles Specific/Verifiable/Battle-tested/Minimal) |

→ **Complementary with overlap**: use AM as team base, AD as the "quality gate" during reviews. Or pick one (overlap ~50%).

### 3.3 NL vs NX — two design repos

| Common ground | Differences |
|---|---|
| Both do design | NL is **component-level UI/UX** (buttons / forms / palettes / fonts / reasoning engine); NX is **system-level + multi-platform output** (71 design systems + slides/PDF/video/mobile) |

→ **Complementary**:
- Single-platform UI component-level → **NL**
- Cross-platform creative output / brand systems → **NX**
- Both component and brand → install both

### 3.4 M vs MA — two individual lenses

| Common ground | Differences |
|---|---|
| Both individual-author | M is **lightweight composable techniques** (/diagnose / /tdd / /grill-me) targeting failure modes; MA is **always-on 4 Karpathy principles** in a single file |

→ **Complementary**: MA gives base discipline; M's skills trigger on demand. Together = lightest possible solo-developer baseline.

### 3.5 C vs everyone — Awesome-list overlap

C is an awesome-list, so **it overlaps with everyone** (by aggregating their skills). The difference:
- C's SKILL.md averages just 3.4 KB (vs O's 8.2 KB, AD's 10.7 KB) — **broad but shallow**
- C has 864 SKILL.md (biggest "index" in cohort) but D10 supplementary density is just 0.03 (lowest)

→ **When to use C**: discovery / browsing the skill ecosystem to see what's possible. **Not a primary install**; once you find a direction, switch to the matching specialist.

### 3.6 V vs A vs OAI — three official authorities

| | A | OAI | V |
|---|---|---|---|
| Official for | Claude Skills spec | Codex skill catalog | Vercel deploy + React/Next.js |
| Scope | Horizontal (any domain) | Horizontal (any domain) | Vertical (web frontend / Vercel-native) |
| Strength | Spec authority | Three-tier `.system/.curated/.experimental` governance model | Live WebFetch for fresh web rules |

→ **Orthogonal**: all three cover entirely different "official" domains. V has no overlap with A/OAI; it's platform-specific authority.

---

## 4. Task → Repo lookup

> ✅ = primary · ➕ = secondary / complementary · ⚠ = cohort weak / no specialist

### 4.1 Web · Mobile · Systems development

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
| 9 | **Game development** (Web / Engine) | ⚠ no specialist | C search | ⚠ Cohort has **no game specialist**; C may have stray entries, else self-build |
| 10 | Web3 / Smart Contracts | ⚠ no specialist | C search | ⚠ Same as above |
| 11 | Embedded / Rust systems | M ✅ | MA ➕ | M's first-principles + MA's anti-pattern guard |

### 4.2 AI · ML · Agent building

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

### 4.3 Engineering methodology

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

### 4.4 Research · Experimentation

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

### 4.5 Design · Creative

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 40 | Design system | **NX ✅** | NL ➕ | NX ships 71 design systems |
| 41 | Visual mockup | NX ✅ | NL ➕ | NX is multi-platform (web/desktop/mobile) |
| 42 | Brand / Logo / CI | NX ✅ | — | NX has brand-identity + logo skills |
| 43 | Typography / color | **NL ✅** | NX ➕ | NL has 161 palettes + 57 font pairs |
| 44 | Slides / Presentation | A ✅ | NX ➕ | A's theme-factory + slide skills are canonical |
| 45 | PDF / document generation | **A ✅** | C ➕ | A's PDF skill is the standard |
| 46 | Icon | NX ✅ | NL ➕ | NX has icon-design with 15 styles |
| 47 | **Taste exploration / mood board** | **NX ✅** | A ➕ | NX's 71 design systems = 71 "taste samples"; A's theme-factory has 10 presets |
| 48 | Print / Banner / social images | NX ✅ | — | NX banner-design with 22 styles |
| 49 | UI/UX component level | **NL ✅** | NX ➕ | NL is the specialist |
| 50 | Brand voice | NX ✅ | CH ➕ | NX brand identity + CH marketing voice |

### 4.6 Content · Marketing

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 51 | Copywriting | **CH ✅** | — | CH only specialist |
| 52 | SEO | **CH ✅** | — | CH only specialist |
| 53 | **CRO / Landing page** | CH ✅ | V ➕ | CH page-cro + V web-design-guidelines (design + conversion) |
| 54 | Email marketing | CH ✅ | C ➕ | CH specialist |
| 55 | Social media | CH ✅ | C ➕ | CH + C (slack/twitter) |
| 56 | Content research | C ✅ | CH ➕ | C's content-research-writer |
| 57 | Growth analytics | CH ✅ | — | CH analytics skills |

### 4.7 Knowledge management · Notes

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 58 | **Markdown / Obsidian** | **K ✅** | — | K is Obsidian creator's repo |
| 59 | Knowledge graphs / JSON Canvas | K ✅ | — | K has Canvas skill |
| 60 | Personal notes | K ✅ | A ➕ | K Obsidian + A doc-coauthoring |
| 61 | Meeting notes | C ✅ | K ➕ | C meeting-insights-analyzer |
| 62 | Research synthesis | K ✅ | A ➕ | K notes + A doc output |

### 4.8 Productivity · Communication

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 63 | Email | C ✅ | — | C internal-comms |
| 64 | Slack / chat | C ✅ | — | C slack-gif-creator etc. |
| 65 | Project management | **O ✅** | AM ➕ | O plan management + AM commands |
| 66 | Onboarding docs | A ✅ | AM ➕ | A doc-coauthoring |

### 4.9 Data · Integration

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 67 | API integration (OAuth / REST / GraphQL) | C ✅ | AM ➕ | C's connect / connect-apps series |
| 68 | Browser automation | C ✅ | — | C has related skills |
| 69 | Web scraping | C ✅ | — | C has related skills |
| 70 | Data ETL | AD ✅ | C ➕ | AD general engineering; C scattered |

### 4.10 Meta · General

| # | Task | Primary | Secondary | Notes |
|---:|---|---|---|---|
| 71 | **5-minute drop-in CLAUDE.md** | **MA ✅** | — | Single file, zero friction |
| 72 | Browse / discover skill ecosystem | C ✅ | — | 864 SKILL.md index |
| 73 | Learn the SKILL.md spec | A ✅ | OAI ➕ | A is official authority |
| 74 | Multi-agent platform support | NX ✅ | NL ➕ V ➕ | NX covers 9 platforms |
| 75 | Solo independent engineer | M ✅ | MA ➕ | M lightweight + MA anti-pattern |
| 76 | Team / company adoption | AM ✅ | AD ➕ O ➕ | AM hooks/commitlint/CoC; AD strict quality gates; O methodology enforcement |

---

## 5. Recommended stacks

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

---

## 6. Coverage gaps (areas the cohort doesn't cover)

The 13-repo cohort has **no specialist** for these domains — opportunities for future cohort additions:

| Gap | Best fallback | Suggestion |
|---|---|---|
| **Game development** (Web / Unity / Unreal) | C search (sparse) | ⚠ Needs specialist; today rely on M's rigor + self-build |
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

> **Key observation**: the cohort is strong in *agent dev + design + web frontend + marketing + KM*; weak in *low-level systems / GPU / game / multimodal ML / cloud IaC*. This matches community velocity — current skill ecosystem energy is in *application-layer agent + content + design*; deep systems work is still self-built territory.

---

## Appendix: 13-repo functional orthogonality matrix

> Coverage strength per domain on a 1–5 scale. ✅ ≥ 4, ➕ ≥ 2, — = not covered.

| Domain \ Repo | AM | O | NX | A | NL | AD | CH | C | M | OAI | MA | K | V |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| General engineering | ✅ | ✅ | — | ➕ | — | ✅ | — | ➕ | ✅ | ✅ | ✅ | — | — |
| Web frontend | ➕ | — | — | — | ➕ | ➕ | ➕ | ➕ | — | — | — | — | **✅** |
| UI/UX design | — | — | **✅** | ➕ | **✅** | — | — | ➕ | — | — | — | — | ➕ |
| Design system / brand | — | — | **✅** | ➕ | ➕ | — | ➕ | — | — | — | — | — | — |
| Methodology (TDD/debug/plan) | ➕ | **✅** | — | ➕ | — | ➕ | — | ➕ | ➕ | ➕ | ✅ | — | — |
| AI / agent building | **✅** | ➕ | — | ✅ | — | ➕ | — | ➕ | — | ✅ | ➕ | — | — |
| Skill meta-development | ➕ | ➕ | — | **✅** | — | ➕ | ➕ | ➕ | — | **✅** | — | — | ➕ |
| Marketing / growth | — | — | ➕ | — | — | — | **✅** | ➕ | — | — | — | — | ➕ |
| Knowledge management | — | — | — | ➕ | — | — | — | — | — | — | — | **✅** | — |
| Document output | ➕ | — | ➕ | ✅ | — | ➕ | ➕ | ➕ | — | — | — | ➕ | — |
| Performance / optimization | ➕ | — | — | — | — | ✅ | — | — | ➕ | — | ➕ | — | **✅** |
| Research / eval | ➕ | **✅** | — | ➕ | — | ➕ | — | — | ✅ | — | ➕ | ➕ | — |
| Discovery / browse | — | — | — | — | — | — | — | **✅** | — | — | — | — | — |

---

_Based on §10 philosophy research + sampled docs from each repo. Task list covers AI-agent use cases including the user-requested ones (game / frontend / backend / AI GPU / research / experiments / loops / design / taste exploration) and 30+ adjacent categories. Coverage-gap section is honest about cohort limits — no forced recommendations for domains the cohort doesn't excel in._
