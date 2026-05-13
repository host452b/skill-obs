# 五个模型对 cohort 的评测总结 / Five-Model Cross-Comparison

> 🌐 **Language**: **🇨🇳 中文** · [🇬🇧 English](./agent_summary.en.md)

本文档收录了 5 个不同 AI 模型（Claude / ChatGPT / Gemini / Grok / Perplexity）独立评估本仓库 15 个 skill repos 后的对比总结。**这不是我自己产出的评分**（评分见 [`EVALUATION.md`](./EVALUATION.md)），而是把不同模型在面对同一份 cohort 数据时给出的判断做了横向汇总。

相关文档：
- 评分细节 → [`EVALUATION.md`](./EVALUATION.md) · [`scoring.ipynb`](./scoring.ipynb)
- 按任务选 repo → [`TASK_GUIDE.md`](./TASK_GUIDE.md)

---

## TL;DR

**收敛后的最小可用组合**（5 模型交集）：

1. `anthropics/skills`（底座）
2. `obra/superpowers`（方法论）
3. `gstack` 或 `everything-claude-code`（实战，二选一）
4. 按需加 `nexu-io/open-design`（设计）、`vercel-labs/agent-skills`（Next.js）

要不要加 `karpathy-skills` / `addyosmani` / `mattpocock` 取决于具体技术栈，**不存在"必须加"的共识**。

---

## 1. 强共识（所有模型都认）

四个底层选择基本无争议：

| Repo | 角色 | 5 模型共识 |
|---|---|---|
| `anthropics/skills` | 规范/底座层 | 所有人都装 |
| `obra/superpowers` | 方法论层（TDD、subagent-driven） | 所有人都装 |
| `gstack` **OR** `everything-claude-code` | 实战层（二选一） | solo 选前者，团队/多 harness 选后者 |
| `nexu-io/open-design` | 设计扩展 | 在设计是瓶颈时加上 |

## 2. 强共识（所有模型都避）

| Repo | 原因 |
|---|---|
| `msitarzewski/agency-agents` | 222 个 personality agent 被一致定性为"**灵感库不是基础设施**"。ChatGPT 原话"不要把这类大而全的库当核心"；Claude 直接跳过；Gemini 警告 token 成本和延迟 |
| `openai/skills`（D1=1） | 垫底，全员共识跳过 |
| `kepano/obsidian-skills` | 只有 Obsidian 工作流才有意义 |

## 3. 主要分歧

### 3.1 `multica-ai/andrej-karpathy-skills`

- **Claude / Gemini**：看到 D1=9 觉得是高价值叠加
- **ChatGPT**：当成"个人配置不适合主库"放 C 层
- **判断**：这个分歧来自定位差异 — 它是 **overlay，不是 standalone**

### 3.2 `addyosmani/agent-skills`

- **ChatGPT**：列为 A 级必用
- **Grok / Claude**：没特别强调
- **差异点**：你是否做生产后端

### 3.3 `ComposioHQ/awesome-claude-skills`

- **Grok**：推荐用作 **发现层**
- **其他人**：觉得 meta-list 深度不够，不属于工作流

### 3.4 `mattpocock/skills`

- **全员同意**：只在 TypeScript 场景下用
- **ChatGPT**：评为 B 级"日常贴近"
- **Claude**：视作 **垂直工具**

### 3.5 推荐方法本身（meta-level disagreement）

| 模型 | 推荐风格 |
|---|---|
| ChatGPT / Claude | 给完整 stack |
| Grok | 主张"最多 2-3 个测试" |
| Gemini | 不给推荐，反问你的场景 |

## 4. 独特视角 / 各家独门洞察

| 模型 | 独有视角 |
|---|---|
| **Claude** | 唯一做了 **`contribs < 20 = bus factor` 分析**（押人 vs 押社区），并警告整个生态不到一年**没经过真实生产检验** |
| **ChatGPT** | 唯一给出**严格的五层架构**：规范 → 方法论 → 实战 → 工程 → 垂直 |
| **Gemini** | 警告 **S 层锁定单一社区方法论**的风险 |
| **Grok** | 实操原则 **"fit > score"** |

## 5. 收敛后的最小可用组合（重述）

> 5 个模型意见的交集 — 装这套不会被任何人反对。

```
┌─────────────────────────────────┐
│ 1. anthropics/skills    (底座)  │  必装
│ 2. obra/superpowers     (方法论) │  必装
│ 3. gstack OR ECC        (实战)  │  二选一
├─────────────────────────────────┤
│ 4a. open-design        (设计场景)│  按需
│ 4b. vercel-labs        (Next.js)│  按需
├─────────────────────────────────┤
│  karpathy / addyosmani / mattpocock │
│  取决于技术栈 — 不存在共识必装        │
└─────────────────────────────────┘
```

## 6. 注意

**Perplexity 这次没产出实际内容**（只输出了搜索过程）—— 这是它在 **长 prompt + 表格输入** 下经常出现的失败模式，**不是数据问题**。

---

## 与本仓库自评分的对比 / Comparison with our internal v1.3 scoring

| Repo | 5-模型共识层 | v1.3 score / 210 | v1.3 tier | 一致性 |
|---|---|---:|:---:|---|
| `garrytan/gstack` | 实战 (solo) | 156 | S | ✅ 模型 #1 & 我们 #1 |
| `affaan-m/everything-claude-code` | 实战 (团队) | 154 | S | ✅ |
| `nexu-io/open-design` | 设计按需 | 152 | S | ✅ |
| `obra/superpowers` | 方法论必装 | 150 | S | ✅ |
| `msitarzewski/agency-agents` | **避** | 146 | S | ⚠ 我们 S 但模型避 |
| `anthropics/skills` | 底座必装 | 136 | A | ✅ |
| `addyosmani/agent-skills` | 分歧 | 128 | A | — |
| `mattpocock/skills` | TS-only | 114 | B | ✅ |
| `openai/skills` | **避** | 113 | B | ⚠ |
| `ComposioHQ/awesome-claude-skills` | 分歧 (发现层) | 111 | B | — |
| `coreyhaines31/marketingskills` | （未点名） | 103 | B | — |
| `nextlevelbuilder/ui-ux-pro-max-skill` | （未点名） | 102 | B | — |
| `vercel-labs/agent-skills` | Next.js 按需 | 101 | B | ✅ |
| `multica-ai/andrej-karpathy-skills` | 分歧 (overlay vs standalone) | 92 | C | ✅ 模型分歧 / 我们偏低 |
| `kepano/obsidian-skills` | **避** | 72 | D | ✅ |

**关键观察**：
- **共识层和我们 v1.3 S-tier 高度重合** (4/5)，除了 `agency-agents` — 模型们认为它是"灵感库"，我们 v1.3 看见的是高 D11/D12/D13/D14 而给了 S，但 D20=2 + D21=5（中等）已经暗示它在"任务质量"维度并不顶尖
- **`openai/skills` 模型共识避** vs 我们 B 级（113）— 我们因 D10=9（辅料）+ D21=8（lessons）拉高，但模型们认为 D1=1（velocity 末位）说明社区不买账
- 这是有趣的**"自动评分 vs LLM 综合判断"分歧** — 我们的 21 维度评分是 *特征加和*，LLM 综合判断会做*非线性整合*（如"velocity 太低 = 不投资"作硬门）

---

_本总结收录自外部 5 个 LLM 的横向对比；具体评分方法学见 [`EVALUATION.md`](./EVALUATION.md) §2-§12。_
