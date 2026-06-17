# 五个模型对 cohort 的评测总结 / Five-Model Cross-Comparison

> 🌐 **Language**: **🇨🇳 中文** · [🇬🇧 English](./agent_summary.en.md)

本文档收录了 5 个不同 AI 模型（Claude / ChatGPT / Gemini / Grok / Perplexity）独立评估本仓库 15 个 skill repos 后的对比总结。**这不是我自己产出的评分**（评分见 [`EVALUATION.md`](./EVALUATION.md)），而是把不同模型在面对同一份 cohort 数据时给出的判断做了横向汇总。

> ⏱️ **快照说明（v1.5 更新）**：本五模型对比基于 **15-repo cohort**（v1.3 时期）采集,**早于 v1.5 的 21-repo 扩容**（新增 UA/OS/CO/TS/L30）。这 5 个新 repo 未纳入本次跨模型评测;它们的本仓库自评分见 [`EVALUATION.md §14`](./EVALUATION.md)。重跑五模型对比是后续工作。

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

---

## 7. 补充：以"实战价值"视角的深度评测（单模型详细版）

> 不同于 §1-§6 的"5 模型横向交集"，本节是**另一个独立 LLM**从"实战价值"出发的详细分类 + 排名。
> 提供：分类学（系统型 / 官方标准型 / 垂直增强型 / 清单型）+ 5 步评价法 + 详细分档表 + 最终排名。
> 注：原文含若干外链 citation 经判断为 AI 生成的伪引用（target 与论点无对应），**已移除**以避免误导。

按**实战价值**而不是单纯星数看，这 15 个 skills set 里，真正有长期复用价值的主要分成 **4 类**：系统型、官方标准型、垂直增强型、清单型。

> **本视角核心结论**：S 档里最强的是 `gstack` 和 `open-design`，A 档里最稳的是 `anthropics/skills`，B 档里最值得按场景选的是 `openai/skills`、`vercel-labs/agent-skills`、`mattpocock/skills`。

### 7.1 评价 5 步法

1. 先看"**这是不是一个系统**"，不是看星数；能不能覆盖从规划、实现、评审、测试到交付，决定上限。
2. 再看"**是不是官方或接近标准**"；官方仓库通常更适合作为底座，社区仓库更适合做加速层。
3. 再看"**是不是垂直专精**"；设计、前端、营销、开发体验这类 repo，往往单点强，但不适合拿来当总框架。
4. 最后才看本仓库的指标；`Total` 决定综合质量，`D1` 决定第一印象，`Stars/day` 看热度，`Forks/Contribs` 看生态深度。
5. 所以最重要的问题不是"谁最火"，而是"**你要拿它做操作系统、模板库，还是灵感库**"。

### 7.2 分档判断

| Repo | 优点 | 缺点 | 判断 |
|---|---|---|---|
| **garrytan/gstack** | 体系最完整，角色分工清晰，覆盖规划到上线 | 太重、太强势、学习成本高 | 最强系统型 |
| **affaan-m/everything-claude-code** | 热度高、贡献者多、像资源中枢 | 容易杂，方法论不一定统一 | 强资源型，不一定强系统 |
| **nexu-io/open-design** | D1 满分，设计导向非常明确 | 偏设计侧，不一定适合全栈流程 | 设计方向很强 |
| **obra/superpowers** | 方法论感强，适合增强 agent 能力 | 可能偏抽象，落地闭环弱于 gstack | 好的增强层 |
| **msitarzewski/agency-agents** | 覆盖面超广，222 agents 很吸睛 | "人格代理"容易虚胖，一致性风险高 | 广而不一定深 |
| **anthropics/skills** | 官方、规范、适合作为基线 | 更像参考实现，不像战斗工作流 | 最稳底座 |
| **addyosmani/agent-skills** | 工程化导向强，生产环境友好 | 范围偏窄，像工程增强包 | 适合工程团队 |
| **mattpocock/skills** | 面向工程师，实操味道强 | 贡献者少，作者风格浓 | 适合 TS/工程开发者 |
| **openai/skills** | 官方背书，便于理解 skill 抽象 | Codex 导向，不是 Claude 最佳实践中心 | 值得参考，不是主框架 |
| **ComposioHQ/awesome-claude-skills** | 适合发现项目 | 清单本身不提供方法论 | 只能当导航站 |
| **coreyhaines31/marketingskills** | 细分场景明确 | 太垂直，通用性弱 | 适合营销团队 |
| **nextlevelbuilder/ui-ux-pro-max-skill** | UI/UX 场景强 | 容易停留在视觉层 | 适合补设计短板 |
| **vercel-labs/agent-skills** | Web/Next.js/Vercel 场景很实用 | 技术栈绑定明显 | 适合前端产品团队 |
| **multica-ai/andrej-karpathy-skills** | 理念强、规则感强 | 更像原则集，不是完整技能系统 | 适合当 CLAUDE.md 思想源 |
| **kepano/obsidian-skills** | Obsidian 用户会很受用 | 场景窄，通用价值低 | 典型 niche repo |

### 7.3 重点评价

1. **`gstack`**：如果你要的是"AI 软件工厂"，它最像完整产品而不是 skill 样例；仓库把自己定义成 23 个 specialist 加 8 个 power tools，并把流程组织成从思考、规划、构建、评审、测试到交付的完整链路。
2. `gstack` 的问题也正因为它太完整：强依赖作者的方法论、命令体系和工作节奏，小团队上手会快，大团队统一采用会有治理成本。
3. **`anthropics/skills`**：这是最适合拿来当"官方基线"的仓库；它明确是 Claude skills 的公开实现和示例库，包含 spec、template、不同类别的示例技能，还特别说明很多内容主要用于演示和教育。
4. `anthropics/skills` 的缺点是：它更像"标准参考 + 样例仓库"，不是帮你直接跑完整研发流程的操作系统。
5. **`openai/skills`**：价值在于官方抽象清晰，定位是 Codex 的 skills catalog，并把 skills 定义成可发现、可组合的自包含文件夹。
6. `openai/skills` 的缺点是生态信号和 Claude 兼容心智都不如 Anthropic 这边强，所以更适合借鉴结构，不适合直接拿来当 Claude 主框架。

### 7.4 推荐选择

1. 如果你要一个"**主工作流**"，选 `gstack`；它最像可直接投入实战的系统。
2. 如果你要一个"**标准底座**"，选 `anthropics/skills`；它最像官方规范、示例和模板库。
3. 如果你是**设计驱动产品**，额外叠加 `open-design` 或 `ui-ux-pro-max-skill`。
4. 如果你是 **Next.js / Vercel 团队**，叠加 `vercel-labs/agent-skills`。
5. 如果你是**多模型团队**，保留 `openai/skills` 作为兼容层思路，而不是唯一来源。

### 7.5 最终排名（按"长期可用性"）

| Rank | Repo | 视角 |
|---:|---|---|
| 1 | `garrytan/gstack` | 重型作战系统 |
| 2 | `anthropics/skills` | 官方标准件 |
| 3 | `nexu-io/open-design` | 设计特种兵 |
| 4 | `addyosmani/agent-skills` | 工程增强包 |
| 5 | `vercel-labs/agent-skills` | Vercel/Next.js 实战 |
| 6 | `mattpocock/skills` | TS 工程师工具箱 |
| 7 | `openai/skills` | Codex 兼容参考 |
| 8 | `obra/superpowers` | 方法论增强层 |
| 9 | `everything-claude-code` | 资源中枢（不一定系统）|
| 10 | `andrej-karpathy-skills` | CLAUDE.md 思想源 |
| 11 | `awesome-claude-skills` | 发现导航 |
| 12 | `ui-ux-pro-max-skill` | UI 视觉补丁 |
| 13 | `marketingskills` | 营销垂直 |
| 14 | `agency-agents` | 灵感库（不建议主用）|
| 15 | `obsidian-skills` | Niche |

> **一句话总结**：`gstack` 是"重型作战系统"，`anthropics/skills` 是"官方标准件"，`open-design` 是"设计特种兵"，其余大多是**增强包或导航包**。

### 7.6 §7 与 §1-§6 的对比

| 视角 | §1-§6 (5-LLM 横向交集) | §7 (单 LLM 实战价值视角) |
|---|---|---|
| 推荐 #1 实战层 | `gstack` 或 `everything-claude-code` | **`gstack` 一票**（ECC 跌到 #9）|
| 推荐 #1 底座 | `anthropics/skills` | 一致 |
| `obra/superpowers` 定位 | 必装方法论层 | **降至 #8 "增强层"** |
| `everything-claude-code` 定位 | 实战层备选 | **#9 "资源中枢，不一定系统"** |
| `addyosmani` | 分歧 | **#4 工程增强包**（明确推荐工程团队）|
| **最大分歧点** | obra & ECC 是否核心层 | §7 认为只有 gstack 是核心系统，其他都是辅助 |

**判读**：§7 的"系统主义"视角比 §1-§6 的"合议式"视角更**自信地把 gstack 定为唯一主工作流**；§1-§6 倾向"obra 必装"作为方法论强制层，§7 把 obra 降级。这本身就是一个有意思的元数据 —— 不同 LLM 对"什么算 production-ready 框架"的标准本身有分歧。
