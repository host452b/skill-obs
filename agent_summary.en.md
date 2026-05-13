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
