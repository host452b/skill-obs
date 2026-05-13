# Task → Repo 决策手册 / Task → Repo Decision Guide

> 🌐 **Language**: **🇨🇳 中文** · [🇬🇧 English](./TASK_GUIDE.en.md)

从 13 个 skill repo 的**功能正交**角度，给定具体 AI agent 任务，应该装哪个 repo（或哪个组合）？本手册覆盖：

- §1 — 13 个 repo 在功能版图上的位置
- §2 — **AM × O × NX 三大代表 repo 的 overlap / 正交 / 互补**（用户重点关注）
- §3 — 其他重要 overlap pair
- §4 — 任务 → 推荐 repo lookup（~50 个任务，覆盖 dev / AI / 设计 / 研究 / 内容 / 知识管理 / 数据等）
- §5 — 推荐 stacks（个人 / 团队 / 角色组合）
- §6 — 覆盖缺口（game / GPU kernel / Web3 / embedded 等 cohort 未覆盖领域）

---

## 1. 13 个 repo 的功能正交位置 / Functional positioning

| Code | Repo | 正交位置（独占价值轴）|
|---|---|---|
| **AM** | `affaan-m/everything-claude-code` | **通用 agent harness** — 60 agents + 228 skills + commands + hooks + install 一站；breadth 之王 |
| **O**  | `obra/superpowers` | **工程方法论** — TDD / debug / brainstorm / plan / review 等元技能；depth 之王 |
| **NX** | `nexu-io/open-design` | **设计输出** — 19 skills + 71 design systems；多平台 (web/desktop/mobile/slides/PDF) creative production |
| **A**  | `anthropics/skills` | **官方规范 + 实用 demo** — SKILL.md 标准定义者；含 PDF / theme / doc-coauthoring 等 reference skills |
| **NL** | `nextlevelbuilder/ui-ux-pro-max-skill` | **UI/UX 组件级** — 161 调色板 + 57 字体 + BM25 推理引擎；component-level 视觉 polish |
| **AD** | `addyosmani/agent-skills` | **生产工程** — 通用 engineering 实践，重质量门（Specific / Verifiable / Battle-tested / Minimal）|
| **CH** | `coreyhaines31/marketingskills` | **营销垂直** — CRO / SEO / copywriting / growth；唯一专项 |
| **C**  | `ComposioHQ/awesome-claude-skills` | **Awesome-list** — 864 个 SKILL.md 索引；最广 discovery |
| **M**  | `mattpocock/skills` | **TS 工程师个人视角** — /diagnose / /tdd / /grill-me 反失败模式 |
| **OAI**| `openai/skills` | **Codex 配套 catalog** — 三层 .system / .curated / .experimental |
| **MA** | `multica-ai/andrej-karpathy-skills` | **单文件行为指令** — Karpathy 4 条 LLM coding 反 anti-pattern 原则 |
| **K**  | `kepano/obsidian-skills` | **Obsidian / Markdown / Canvas** — 知识管理唯一专项 |
| **V**  | `vercel-labs/agent-skills` | **Vercel deploy + React/Next.js 实战** — 官方权威；live `WebFetch` 取最新 web 规则 |

---

## 2. 三大代表 repo 横切对比 / AM × O × NX deep-dive

> 这是问得最多的对比 — 这三个都是 cohort 顶端（总分 129 / 115 / 110），但各占不同轴。

### 2.1 核心定位

| | **AM** (everything-claude-code) | **O** (superpowers) | **NX** (open-design) |
|---|---|---|---|
| 核心定位 | 通用 agent harness（capability surface）| 工程方法论（process layer）| 设计输出（output layer）|
| 价值轴 | **广度** breadth | **深度** depth | **垂直** vertical |
| 回答的问题 | "我们都装什么 agents / skills / commands？" | "怎么工作才不出错？" | "怎么产出好看且一致的视觉？" |
| 内容主体 | 228 skills + 60 agents + commands + hooks | 14 高度精打磨的 skills（TDD / debug / plan / brainstorm 等）| 19 skills + 71 design systems |
| 装机时机 | 团队 base setup | 任意时刻（要求纪律时）| 需要产出 UI / 视觉时 |
| 强制度 | optional reference | **mandatory workflow**（hard gates）| optional reference |

### 2.2 Overlaps（内容碰撞点）

| Pair | 碰撞区 | 具体内容 |
|---|---|---|
| AM ↔ O | **engineering methodology** | AM 含 reviewer/planner/python-reviewer 等 agents；O 含 TDD/debugging/planning skills。AM 是"装在 agent 里的"工程实践（commitlint/ESLint/CoC），O 是"写在 skill 里强制的"方法论 gates（HARD-GATE / eval evidence）|
| AM ↔ NX | **前端 / UI 边界** | AM 有些 frontend-design / UI 相关 skills；NX 是全局 design system。AM 偏 "实现"，NX 偏 "规范" |
| O ↔ NX | **几乎完全正交** | process layer 与 output layer 的关系；不太碰撞 |

### 2.3 Orthogonality（正交，独立可叠加）

```
                  Process / Methodology (O)
                            │
                            │
  Capability ────────────── ┼────────────── Visual output
  surface (AM)              │                  (NX)
                            │
                            │
```

- **AM ⊥ NX**：engineering harness vs design production —— 完全无冲突，常一起用
- **O ⊥ NX**：methodology vs output —— 完全无冲突
- **AM ⊥ O 有交集**：但交集本身是互补的（AM 提供 "做什么的能力"，O 提供 "怎么做的纪律"）

### 2.4 Complementarity（推荐叠加用法）

| Stack | 适用场景 | 协同方式 |
|---|---|---|
| **AM + O** | 团队最佳基线 | AM 装满 capability 池；O 加 discipline gates。Agent 既有能力也有纪律。**最常见组合** |
| **AM + NX** | 全栈交付（工程 + 设计） | AM 处理 engineering 实现；NX 处理视觉/UI 产出 |
| **O + NX** | 设计师 + 想要 process 纪律 | O 的 brainstorming + writing-plans 指导设计决策；NX 产出 |
| **AM + O + NX** | 一站式 power user | 工程 + 方法 + 设计全配。⚠ 代价：上下文成本最高，agent 选择困难，需要 careful 配置 |

### 2.5 何时只装其一

| 装哪个 | 场景 |
|---|---|
| **只装 AM** | 你想要 "一键全配"，不想自己挑组件。已有 harness 想升级 |
| **只装 O** | 你已有 setup 不想换，但想加 TDD/debug/plan **强制纪律层** |
| **只装 NX** | 你是设计师 / 营销人员，不需要 AM 的 60 agents 但想用 design systems |

---

## 3. 其他重要 overlap / Other notable overlap pairs

### 3.1 A vs OAI — 两个官方 spec / Two official catalogs

| 共性 | 差异 |
|---|---|
| 都是平台官方 (Anthropic vs OpenAI) | A 服务 Claude，OAI 服务 Codex；A 含 PDF/theme/doc-coauthoring 等通用 reference skills，OAI 含 skill-creator + eval 工具 |

→ **互补**：用哪个看你的 host 平台。如果两个 agent 平台都用，一并装；spec 互相参考但实现独立。

### 3.2 AM vs AD — 两个广义 engineering / Two broad-eng repos

| 共性 | 差异 |
|---|---|
| 都覆盖通用软件工程（API / 测试 / 性能 / 安全 / 重构 / 文档）| AM 是 **breadth + harness**（agents + commands + hooks）；AD 是 **depth + quality**（每个 skill 有 Verification + Red Flags 段，强制 4 原则 Specific/Verifiable/Battle-tested/Minimal）|

→ **互补 with overlap**：AM 用作团队基础，AD 用作 review/critique 时的 "质量门"。或选其一即可（重复度~50%）。

### 3.3 NL vs NX — 两个 design / Two design repos

| 共性 | 差异 |
|---|---|
| 都做设计 | NL 是 **component-level UI/UX**（按钮 / 表单 / 调色板 / 字体 / 推理引擎）；NX 是 **system-level + multi-platform output**（71 design systems + slides/PDF/video/mobile） |

→ **互补**：
- 单平台 UI 组件级 → **NL**
- 跨平台创意产出 / 品牌系统 → **NX**
- 同时做组件 + 品牌 → 一起装

### 3.4 M vs MA — 两个个人视角 / Two individual lenses

| 共性 | 差异 |
|---|---|
| 都是个人作者 | M 是 **lightweight composable techniques**（/diagnose / /tdd / /grill-me）反失败模式；MA 是 **always-on 4 条 Karpathy 原则** 单文件 |

→ **互补**：MA 装上是 base discipline；M 的 skills 按需触发。组合起来 = 个人开发者最轻量基线。

### 3.5 C vs everyone — Awesome-list 与所有人的 overlap

C 是 awesome-list，**它和谁都 overlap**（因为它聚合所有人的 skills）。差别：
- C 的 SKILL.md 平均只有 3.4KB（vs O 的 8.2KB，AD 的 10.7KB）—— **broad but shallow**
- C 含 864 个 SKILL.md，是 cohort 中最大的"目录"但 D10 辅料密度仅 0.03（最低）

→ **何时用 C**：discovery / 浏览市场上有哪些 skill 形态。**不当主装**，可以挖到具体方向后转向对应的 specialist repo。

### 3.6 V vs A vs OAI — 三个官方 / Three official authorities

| | A | OAI | V |
|---|---|---|---|
| 官方什么 | Claude Skills 规范 | Codex skill catalog | Vercel 部署 + React/Next.js |
| 范围 | 横向（任何领域） | 横向（任何领域） | 纵向（web frontend / Vercel-native） |
| 强项 | spec authority | 三层 .system/.curated/.experimental 治理模型 | live WebFetch 取最新 web 规则 |

→ **正交**：三者覆盖完全不同的官方域。V 与 A/OAI 没有 overlap，是 platform-specific authority。

---

## 4. 任务 → 推荐 repo lookup

> ✅ = primary（首选）· ➕ = secondary（次选 / 互补）· ⚠ = cohort 覆盖弱

### 4.1 Web / 移动 / 系统开发 / Web · Mobile · Systems

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 1 | **Web 前端 (React/Next.js production)** | V ✅ | AD ➕ AM ➕ | V 是 Vercel 官方；40+ React 性能规则按 Impact 排序 |
| 2 | UI 组件 / 视觉 polish | NL ✅ | NX ➕ | NL 含 161 调色板 + 57 字体 + BM25 推理 |
| 3 | React Native / 移动 web | V ✅ | NL ➕ | V 有 react-native-skills |
| 4 | iOS / Android native | NL ✅ | A ➕ | NL 含 SwiftUI 栈；A 有 doc-coauthoring |
| 5 | **后端 API / 微服务** | AM ✅ | AD ➕ O ➕ | AM 含 API/data/architecture agents；O 加方法论 gates |
| 6 | 数据库 / SQL 优化 | AD ✅ | C ➕ | AD 强 Verification；C 有 DB-specific skills |
| 7 | DevOps / CI / Deployment | AM ✅ | V ➕ | AM 含 hooks/commitlint/lint；V 专 Vercel deploy |
| 8 | 云基础设施 / IaC (Terraform/K8s) | AM ⚠ | — | ⚠ cohort 弱，靠 AM 通用工程 |
| 9 | **Game 开发** (Web / Engine) | ⚠ no specialist | C 搜 | ⚠ cohort **完全无 game 专项**；C 可能有零星，否则只能靠通用 + 自建 |
| 10 | Web3 / Smart Contracts | ⚠ no specialist | C 搜 | ⚠ 同上 |
| 11 | 嵌入式 / Rust systems | M ✅ | MA ➕ | M 的 first-principles + MA 反 anti-pattern |

### 4.2 AI / ML / Agent 建构 / AI · ML · Agent building

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 12 | **LLM 应用 / Agent 构建** | AM ✅ | OAI ➕ A ➕ | AM 是 agent harness 顶级；OAI 含 Codex 配套；A 是规范 |
| 13 | Prompt 工程 | A ✅ | O ➕ | A 含 skill-creator；O 的 brainstorming 帮设计 prompt |
| 14 | **Skill / Agent 元开发**（写新 skill） | A ✅ | OAI ➕ AM ➕ | A 定义 SKILL.md 规范；AM 给参考实现 |
| 15 | RAG / 检索系统 | C 搜 ✅ | AM ➕ | C 有多个 search/research-writer skills |
| 16 | **GPU kernel (CUDA / Triton / MPS)** | ⚠ no specialist | MA + M | ⚠ cohort **无 GPU 专项**；MA 反 anti-pattern + M 工程严谨做基础 |
| 17 | Model fine-tuning | AD ✅ | M ➕ | 通用生产工程；专项弱 |
| 18 | Model evaluation / benchmarking | **O ✅** | AD ➕ | O **强制 eval evidence**（gold standard）|
| 19 | Inference 优化 / 性能 | AD ✅ | V (web 侧) | AD 性能实践；V 含 web 性能 |
| 20 | Agent harness 优化 | **AM ✅** | O ➕ | AM 就是 "agent harness perf framework" |

### 4.3 工程方法论 / Engineering methodology

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 21 | **TDD** | **O ✅** | AD ➕ | O 的 TDD skill 是 gold standard |
| 22 | **系统性调试** (debugging) | **O ✅** | M ➕ | O systematic-debugging + M /diagnose |
| 23 | 头脑风暴 / 规划 | **O ✅** | — | O 的 brainstorming + writing-plans 套件 |
| 24 | Code review | AM ✅ | AD ➕ O ➕ | AM 含多个 reviewer agents |
| 25 | 重构 | M ✅ | O ➕ MA ➕ | M 减少 unnecessary diffs；O plan-first；MA "surgical changes" |
| 26 | 大规模迁移 / framework upgrades | AD ✅ | M ➕ O ➕ | AD 含 migration patterns；O 加 plan 流程 |
| 27 | 性能优化 (web) | V ✅ | AD ➕ | V 含 40+ React 性能规则 |
| 28 | 性能优化 (通用) | AD ✅ | M ➕ | AD 生产工程；M first-principles feedback |
| 29 | 安全审计 | AM ✅ | AD ➕ | 通用工程；专项弱 |
| 30 | 架构决策 | O ✅ | AD ➕ AM ➕ | O 的 writing-plans + brainstorming |
| 31 | 文档撰写 | A ✅ | K ➕ AD ➕ | A 含 doc-coauthoring；K 含 Markdown 格式专项 |

### 4.4 研究 / 实验 / 评测 / Research · Experimentation

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 32 | **论文 / 文献 review** | K ✅ | A ➕ | K Obsidian 笔记同步；A 输出 doc |
| 33 | Benchmarking / 评测 | **O ✅** | M ➕ | O 强制 eval evidence；M /diagnose 强调 feedback loop |
| 34 | 实验设计 | O ✅ | M ➕ | O 的 writing-plans + brainstorming |
| 35 | **整晚 batch loop / autonomous run** | **AM ✅** | O ➕ | AM 含 install scripts + hooks + cron-style commands；O 含 dispatching-parallel-agents + subagent-driven-development |
| 36 | 数据分析 / EDA | A ✅ | C ➕ | A 含 data-analysis demo skills |
| 37 | 假设测试 / "做实验" | M ✅ | O ➕ | M /diagnose 强调 first-principles；O 加纪律 |
| 38 | 论文写作 | A ✅ | K ➕ | A doc-coauthoring；K 笔记同步 |
| 39 | Reproducibility / 复现 | O ✅ | MA ➕ | O 强制 verification；MA goal-driven execution |

### 4.5 设计 / 创意 / Design · Creative

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 40 | Design system | **NX ✅** | NL ➕ | NX 含 71 design systems |
| 41 | Visual mockup / 视觉 | NX ✅ | NL ➕ | NX 多平台 (web/desktop/mobile) |
| 42 | 品牌 / Logo / CI | NX ✅ | — | NX 含 brand-identity + logo skill |
| 43 | 字体 / 配色 | **NL ✅** | NX ➕ | NL 161 调色板 + 57 字体配对 |
| 44 | 幻灯 / Presentation | A ✅ | NX ➕ | A 的 theme-factory + slide skills 是 canonical |
| 45 | PDF / Document 生成 | **A ✅** | C ➕ | A 的 PDF skill 是规范级 |
| 46 | Icon | NX ✅ | NL ➕ | NX 含 icon-design 15 styles |
| 47 | **品味探索 / 灵感 / mood board** | **NX ✅** | A ➕ | NX 71 design systems = 71 个 "品味样本"；A theme-factory 10 预设 |
| 48 | 印刷 / Banner / 社交图 | NX ✅ | — | NX banner-design 22 styles |
| 49 | UI/UX 组件级 | **NL ✅** | NX ➕ | NL component-level 最专 |
| 50 | Brand voice | NX ✅ | CH ➕ | NX brand identity + CH 营销 voice |

### 4.6 内容 / 营销 / Content · Marketing

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 51 | Copywriting | **CH ✅** | — | CH 唯一专项 |
| 52 | SEO | **CH ✅** | — | CH 唯一专项 |
| 53 | **CRO / Landing page** | CH ✅ | V ➕ | CH page-cro + V web-design-guidelines（设计 + 转化） |
| 54 | Email 营销 | CH ✅ | C ➕ | CH 专项 |
| 55 | 社交媒体 | CH ✅ | C ➕ | CH + C 含 slack/twitter |
| 56 | 内容研究 | C ✅ | CH ➕ | C 的 content-research-writer |
| 57 | Growth analytics | CH ✅ | — | CH 含 analytics skills |

### 4.7 知识管理 / 笔记 / Knowledge management

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 58 | **Markdown / Obsidian** | **K ✅** | — | K 是 Obsidian creator 维护 |
| 59 | Knowledge graphs / JSON Canvas | K ✅ | — | K 含 Canvas skill |
| 60 | 个人笔记 | K ✅ | A ➕ | K Obsidian + A doc-coauthoring |
| 61 | Meeting notes | C ✅ | K ➕ | C meeting-insights-analyzer |
| 62 | Research synthesis | K ✅ | A ➕ | K 笔记 + A 输出 doc |

### 4.8 生产力 / 沟通 / Productivity · Communication

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 63 | Email | C ✅ | — | C internal-comms |
| 64 | Slack / chat | C ✅ | — | C slack-gif-creator 等 |
| 65 | 项目管理 | **O ✅** | AM ➕ | O plan management + AM commands |
| 66 | Onboarding 文档 | A ✅ | AM ➕ | A doc-coauthoring |

### 4.9 数据 / 集成 / Data · Integration

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 67 | API 集成 (OAuth / REST / GraphQL) | C ✅ | AM ➕ | C 的 connect / connect-apps 系列 |
| 68 | 浏览器自动化 | C ✅ | — | C 含相关 skills |
| 69 | Web scraping | C ✅ | — | C 含相关 skills |
| 70 | 数据 ETL | AD ✅ | C ➕ | AD 通用工程；C 有零星 |

### 4.10 元 / 通用 / Meta · General

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 71 | **5 分钟快速 CLAUDE.md drop-in** | **MA ✅** | — | 单文件零负担 |
| 72 | 浏览 / 发现 skill 生态 | C ✅ | — | 864 SKILL.md 索引 |
| 73 | 学 SKILL.md 规范 | A ✅ | OAI ➕ | A 是官方权威 |
| 74 | 多 agent 平台兼容 | NX ✅ | NL ➕ V ➕ | NX 9 个平台覆盖最广 |
| 75 | 个人独立工程师 | M ✅ | MA ➕ | M lightweight + MA 反 anti-pattern |
| 76 | 团队 / 公司采用 | AM ✅ | AD ➕ O ➕ | AM 含 hooks/commitlint/CoC；AD 严质量门；O 强制方法论 |

---

## 5. 推荐 Stacks / Recommended combinations

> 不要装太多 — 上下文是公共资源。3-4 个 repo 通常足够。

| Scenario / 场景 | Stack | 理由 |
|---|---|---|
| **个人独立工程师 (lightweight base)** | MA + M | 一行 CLAUDE.md 加 base discipline；M 的 skills 按需触发 |
| **设计师 / 营销人员** | NX + K | NX 出设计；K 做笔记 / 研究归档 |
| **团队 Dev base** | **AM + O** | Capability surface + methodology gates — **最常见组合** |
| **Web Product Team** (Vercel-native) | V + AD + O | V 部署 + AD 工程门 + O 纪律 |
| **Web Product Team** (full-stack with design) | AM + O + NX + V | 工程 + 方法 + 设计 + Vercel 部署 |
| **Marketing / Growth Team** | CH + V + A | CH 营销实战 + V landing-page 工程 + A 文档输出 |
| **Research / 学术** | K + O + A | K 笔记 + O 评测纪律 + A 文档输出 |
| **AI Agent / Skill Builder** | A + AM + O | A 规范 + AM 参考实现 + O 方法论纪律 |
| **试水 / 评估生态** | MA + C | MA 零负担引入 + C 浏览全生态 |
| **Codex 用户** | OAI + O + A | Codex 配套 + 方法论 + spec 参考 |

---

## 6. 覆盖缺口 / Coverage gaps（cohort 未覆盖领域）

13 个 repo **没有专项覆盖**的领域 — 这是未来 cohort 扩张的方向：

| 缺口 / Gap | 当前最佳替代 | 建议 |
|---|---|---|
| **Game 开发** (Web / Unity / Unreal) | C 搜索（少量） | ⚠ 需要专项 repo；目前只能靠 M 工程严谨 + 自建 |
| **GPU kernel** (CUDA / Triton / MPS) | MA + M（间接） | ⚠ 需要专项 repo；MA 反 anti-pattern 帮纪律，M /diagnose 帮调试 |
| **Web3 / 智能合约** | C 搜索 | ⚠ 需要专项 repo |
| **Cloud IaC** (Terraform / K8s / Pulumi) | AM（通用工程） | ⚠ 缺专项；AM 的 hooks/commands 可装但不够深 |
| **嵌入式 / Rust systems** | M + MA | ⚠ 间接，靠通用工程纪律 |
| **Native mobile** (iOS / Android primary) | NL（部分 SwiftUI） | ⚠ NL 偏 UI 层，不覆盖 native API |
| **Computer Vision / 多模态 ML** | AD + M（通用工程） | ⚠ 无 CV / multimodal 专项 |
| **Data engineering at scale** (Spark / Airflow / dbt) | AD（通用）+ C 搜 | ⚠ 缺专项；AD 工程实践通用 |
| **Database internals** (B-tree / OLAP / 优化) | AD | ⚠ 缺专项 |
| **OS / Compiler / Linker** 工作 | M + MA（通用纪律） | ⚠ 最深的系统工作，cohort 完全不覆盖 |
| **Quant / Trading 算法** | M + AD | ⚠ 缺专项 |
| **Security offensive** (pentest / red team) | AM, AD（防御侧） | ⚠ 缺 offensive 专项 |

> **关键观察**：cohort 强在"agent 开发 + 设计 + web frontend + 营销 + 知识管理"五块；弱在"low-level systems / GPU / game / 多模态 ML / cloud IaC"。这与 community velocity 一致 — 当前 skill 生态主要在 _应用层 agent + 内容侧 + 设计侧_ 发力，深 system 还在自建阶段。

---

## 附录 / Appendix: 13 repo 的功能正交矩阵

> 简化 1-5 评分，每行表示该 repo 在该领域的覆盖强度。✅ ≥4，➕ ≥2，— = 不覆盖。

| 领域 \ Repo | AM | O | NX | A | NL | AD | CH | C | M | OAI | MA | K | V |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 通用工程 | ✅ | ✅ | — | ➕ | — | ✅ | — | ➕ | ✅ | ✅ | ✅ | — | — |
| Web 前端 | ➕ | — | — | — | ➕ | ➕ | ➕ | ➕ | — | — | — | — | **✅** |
| UI/UX 设计 | — | — | **✅** | ➕ | **✅** | — | — | ➕ | — | — | — | — | ➕ |
| Design system / 品牌 | — | — | **✅** | ➕ | ➕ | — | ➕ | — | — | — | — | — | — |
| 方法论 (TDD/debug/plan) | ➕ | **✅** | — | ➕ | — | ➕ | — | ➕ | ➕ | ➕ | ✅ | — | — |
| AI / Agent 建构 | **✅** | ➕ | — | ✅ | — | ➕ | — | ➕ | — | ✅ | ➕ | — | — |
| Skill 元开发 | ➕ | ➕ | — | **✅** | — | ➕ | ➕ | ➕ | — | **✅** | — | — | ➕ |
| 营销 / Growth | — | — | ➕ | — | — | — | **✅** | ➕ | — | — | — | — | ➕ |
| 知识管理 | — | — | — | ➕ | — | — | — | — | — | — | — | **✅** | — |
| 文档输出 | ➕ | — | ➕ | ✅ | — | ➕ | ➕ | ➕ | — | — | — | ➕ | — |
| Performance / Optimization | ➕ | — | — | — | — | ✅ | — | — | ➕ | — | ➕ | — | **✅** |
| Reseach / Eval | ➕ | **✅** | — | ➕ | — | ➕ | — | — | ✅ | — | ➕ | ➕ | — |
| Discovery / Browse | — | — | — | — | — | — | — | **✅** | — | — | — | — | — |

---

_本手册基于 §10 哲学考据 + 各 repo 实际文档抽样。任务列表参考 AI agent 实际使用场景，并尝试覆盖用户提到的 game / 前后端 / AI GPU / 研究 / 实验 / loop / 设计 / 品味探索 + 类似 30+ 类。覆盖缺口部分诚实标注 — 不强行推荐 cohort 不擅长的领域。_
