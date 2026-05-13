# Five-Model Cross-Comparison of the Cohort

> 🌐 **Language**: [🇨🇳 中文](./agent_summary.md) · **🇬🇧 English**

This document collects the cross-model summary of 5 AI models (Claude / ChatGPT / Gemini / Grok / Perplexity) independently evaluating this repo's 15 skill repos. **This is not my own scoring** (see [`EVALUATION.en.md`](./EVALUATION.en.md)) — it's a horizontal aggregation of judgments made by different models on the same cohort.

Related docs:
- Scoring detail → [`EVALUATION.en.md`](./EVALUATION.en.md) · [`scoring.ipynb`](./scoring.ipynb)
- Task → repo lookup → [`TASK_GUIDE.en.md`](./TASK_GUIDE.en.md)

---

## TL;DR

**Converged minimum viable stack** (intersection of all 5 models):

1. `anthropics/skills` (foundation)
2. `obra/superpowers` (methodology)
3. `gstack` or `everything-claude-code` (operational, pick one)
4. Add as needed: `nexu-io/open-design` (design), `vercel-labs/agent-skills` (Next.js)

Whether to add `karpathy-skills` / `addyosmani` / `mattpocock` depends on your specific stack — **there's no must-add consensus**.

---

## 1. Strong consensus (all models recommend)

Four foundational picks have essentially no debate:

| Repo | Role | All-5 consensus |
|---|---|---|
| `anthropics/skills` | Spec / foundation layer | Everyone installs it |
| `obra/superpowers` | Methodology layer (TDD, subagent-driven) | Everyone installs it |
| `gstack` **OR** `everything-claude-code` | Operational layer (pick one) | Solo → former; team/multi-harness → latter |
| `nexu-io/open-design` | Design extension | Add when design is a bottleneck |

## 2. Strong consensus (all models avoid)

| Repo | Reason |
|---|---|
| `msitarzewski/agency-agents` | 222 personality agents unanimously characterized as "**inspiration library, not infrastructure**". ChatGPT verbatim: "don't treat such a sprawling library as core"; Claude skipped it; Gemini warned about token cost and latency |
| `openai/skills` (D1=1) | Dead last, unanimously skipped |
| `kepano/obsidian-skills` | Only meaningful inside an Obsidian workflow |

## 3. Main disagreements

### 3.1 `multica-ai/andrej-karpathy-skills`

- **Claude / Gemini**: high-value drop-in given D1=9
- **ChatGPT**: "personal config, not suitable for primary lib", placed in tier C
- **Verdict**: disagreement stems from positioning — it's an **overlay, not standalone**

### 3.2 `addyosmani/agent-skills`

- **ChatGPT**: A-tier must-have
- **Grok / Claude**: not particularly emphasized
- **Differentiator**: whether you're doing production backend

### 3.3 `ComposioHQ/awesome-claude-skills`

- **Grok**: recommend as **discovery layer**
- **Others**: think meta-list depth isn't enough; doesn't belong in workflow

### 3.4 `mattpocock/skills`

- **All-5 agree**: only use in TypeScript context
- **ChatGPT**: B-tier "daily-relevant"
- **Claude**: treats it as a **vertical tool**

### 3.5 Recommendation methodology itself (meta-level disagreement)

| Model | Style |
|---|---|
| ChatGPT / Claude | Give complete stacks |
| Grok | Advocates "max 2-3 trials" |
| Gemini | No recommendation, asks back about your scenario |

## 4. Unique viewpoints / per-model differentiated insights

| Model | Unique angle |
|---|---|
| **Claude** | Only one to do **`contribs < 20 = bus factor` analysis** (betting on person vs community), and warned the whole ecosystem is <1 year old and **not yet production-tested** |
| **ChatGPT** | Only one to give a **strict 5-layer architecture**: Spec → Methodology → Operational → Engineering → Vertical |
| **Gemini** | Warned about **S-tier locking into single-community methodology** risk |
| **Grok** | Operational principle: **"fit > score"** |

## 5. Converged minimum viable stack (restated)

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

## 6. Footnote

**Perplexity didn't produce actual content this round** (only emitted its search process) — this is a known failure mode under **long prompt + tabular input**, **not a data problem**.

---

## Comparison with our internal v1.3 scoring

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

_This summary aggregates from 5 external LLM evaluations; for our scoring methodology see [`EVALUATION.en.md`](./EVALUATION.en.md) §2-§12._

---

## 7. Supplement: deep-essay "operational value" perspective (single-model detailed view)

> Unlike §1-§6 (the 5-model horizontal intersection), this section is **another independent LLM's** detailed taxonomy + ranking through the "operational value" lens.
> Provides: taxonomy (systemic / official-standard / vertical-augment / catalog) + 5-step evaluation + per-repo table + final ranking.
> Note: the original text includes a few external citations that look like LLM-generated hallucinations; **preserved verbatim** — not ground-truth references.

Looking through the **operational value** lens (not star count alone), of these 15 skill sets the truly long-term-reusable ones fall into **4 categories**: systemic, official-standard, vertical-augment, and catalog.

> **Bottom line of this perspective**: in S-tier the strongest are `gstack` and `open-design`; in A-tier the steadiest is `anthropics/skills`; in B-tier the most situationally valuable are `openai/skills`, `vercel-labs/agent-skills`, `mattpocock/skills`.

### 7.1 5-step evaluation

1. First ask "**is this a system?**", not the star count; whether it covers planning, implementation, review, testing, delivery determines the ceiling.
2. Then ask "**is this official or near-standard?**"; official repos are better as a foundation, community repos better as an acceleration layer.
3. Then ask "**is this vertically specialized?**"; design / frontend / marketing / DX repos are often strong at one point but unsuitable as overall framework.
4. Only then look at our scoring metrics; `Total` determines composite quality, `D1` determines first impression, `Stars/day` shows heat, `Forks/Contribs` shows ecosystem depth.
5. So the most important question isn't "who's the most popular" — it's "**are you using it as an OS, a template library, or an inspiration library?**"

### 7.2 Per-repo evaluation table

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

### 7.3 Key evaluations

1. **`gstack`**: if you want an "AI software factory", it looks more like a complete product than a skill example; the repo positions itself as 23 specialists + 8 power tools, organized as a full pipeline from thinking → planning → building → review → testing → delivery.[^nngroup-en]
2. `gstack`'s problem is exactly its completeness: strongly tied to the author's methodology, command system, and rhythm. Small teams ramp up fast; big teams will face governance cost to standardize.
3. **`anthropics/skills`**: most suitable as an "official baseline"; explicitly the Claude-skills public reference + sample library — includes spec, template, examples across categories, plus an explicit note that much content is for demonstration/education.[^reddit-en]
4. `anthropics/skills` downside: more "standard reference + sample repo" than an OS for running a complete R&D process.
5. **`openai/skills`**: value lies in clear official abstraction; positioned as the Codex skills catalog, with skills defined as discoverable, composable, self-contained folders.[^github-en]
6. `openai/skills` downside: ecosystem signals and Claude-compatibility mindshare are both weaker than Anthropic's side, so good for structural reference, not for primary framework on Claude.

[^nngroup-en]: Original cites https://www.nngroup.com/articles/why-repositories-fail/ — link's actual content has no apparent relation to gstack evaluation; suspected LLM-hallucinated citation.
[^reddit-en]: Original cites reddit.com/r/programming — same as above, likely hallucinated.
[^github-en]: Original cites github.com/openai/skills/pulls — link is valid but loosely tied to the argument.

### 7.4 Recommended selection

1. If you want a "**main workflow**", pick `gstack`; it most resembles a system that can be deployed directly.
2. If you want a "**standard foundation**", pick `anthropics/skills`; it most resembles official spec, samples, templates.
3. If you're **design-driven product**, add `open-design` or `ui-ux-pro-max-skill`.
4. If you're a **Next.js / Vercel team**, add `vercel-labs/agent-skills`.
5. If you're a **multi-model team**, keep `openai/skills` for compatibility thinking, not as the sole source.

### 7.5 Final ranking (by "long-term reusability")

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

### 7.6 §7 vs §1-§6 contrast

| Lens | §1-§6 (5-LLM horizontal intersection) | §7 (single-LLM operational-value view) |
|---|---|---|
| Top operational layer recommendation | `gstack` OR `everything-claude-code` | **`gstack` only** (ECC drops to #9) |
| Top foundation | `anthropics/skills` | Same |
| `obra/superpowers` positioning | Must-have methodology layer | **Downgraded to #8 "augmentation"** |
| `everything-claude-code` positioning | Operational layer alternative | **#9 "resource hub, not necessarily systemic"** |
| `addyosmani` | Disagreement | **#4 engineering augment** (explicit eng-team recommendation) |
| **Biggest divergence** | Whether obra & ECC are core layer | §7 thinks only gstack is the core system; everything else is auxiliary |

**Interpretation**: §7's "systemic" perspective is more **confident in declaring gstack as the sole primary workflow** than §1-§6's "consensus" view; §1-§6 leans toward "obra is must-have" as a mandatory methodology layer, §7 downgrades obra. That itself is an interesting meta-data — **different LLMs disagree on what counts as a "production-ready framework" standard**.
