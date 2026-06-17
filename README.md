# skill-obs

> 🌐 **Language**: **🇨🇳 中文** · [🇬🇧 English](./README.en.md)

> **Skill Observatory** — 一个对当下 Agent Skills / Claude Skills 生态做横向评测的元仓库。
> 12 个主流 skill collection repo 作为 git submodule，配 15 维度评分 + 可视化 notebook + append-only 评估历史。

[![Eval baseline](https://img.shields.io/badge/eval-2026--06--17-blue)](./EVALUATION.md)
[![Notebook](https://img.shields.io/badge/notebook-scoring.ipynb-orange)](./scoring.ipynb)
[![Notebook 中文](https://img.shields.io/badge/notebook-scoring.cn.ipynb-orange)](./scoring.cn.ipynb)
[![Task Guide](https://img.shields.io/badge/任务→repo-TASK__GUIDE-red)](./TASK_GUIDE.md)
[![5-Model Summary](https://img.shields.io/badge/5_AI_模型对比-agent__summary-blueviolet)](./agent_summary.md)
[![Cohort size](https://img.shields.io/badge/repos-21-green)](./.gitmodules)
[![Dimensions](https://img.shields.io/badge/dimensions-21-purple)](./EVALUATION.md#2-15-个评测维度--15-evaluation-dimensions)
[![Snapshots](https://img.shields.io/badge/snapshots-v1.0_→_v1.5-yellow)](./scoring.ipynb)
[![Social signals](https://img.shields.io/badge/Reddit_+_HN-30d_sampled-orange)](./scoring.ipynb)
[![Quality signals](https://img.shields.io/badge/D20_Decomp_+_D21_Lessons-v1.3-pink)](./EVALUATION.md)

---

## 🎯 这是什么 / What is this

社区里"Skill"类 repo 已经有几十个，但它们的 **覆盖深度、原创度、工程化程度、可移植性** 差异巨大。本仓库的目的：

1. **集中观察**：把当下 stars 最多、最有代表性的 skill collection 仓库以 **git submodule** 的形式聚到一起，方便本地浏览和比对。
2. **统一评测**：用 15 个维度（含用户强调的 ⭐ star velocity）对所有 repo 打分，结论可追溯、可重打。
3. **持续追踪**：每次评估都记录 **submodule SHA + 时间戳 + raw metrics + 1-10 分数**，做成 append-only 快照历史，方便长期对比。

它不是 awesome-list（那种纯链接索引由 `ComposioHQ/awesome-claude-skills` 已经做得很好）；它是 **打分 + 可观测 + 可复现** 的评估底座。

## 🚀 Quick Start

```bash
# 1. Clone with submodules（必须带 --recurse-submodules）
git clone --recurse-submodules https://github.com/host452b/skill-obs.git
cd skill-obs

# 2. 如果已经 clone 但忘了 submodule
git submodule update --init --depth 1

# 3. 浏览评分（静态 markdown）
$EDITOR EVALUATION.md

# 4. 交互可视化（推荐）
jupyter notebook scoring.ipynb
#   或者只生成静态 HTML：
jupyter nbconvert --to html --execute scoring.ipynb && open scoring.html
```

> ⚠️ shallow clone：每个 submodule 用 `--depth 1`，整套约 **225 MB**（最大 `nexu-io/open-design` 137 MB）。

## 📂 Repo Layout

```
skill-obs/
├── README.md                          ← 你正在看
├── EVALUATION.md                      ← 完整评测报告：15 维度 × 12 repos
├── scoring.ipynb                      ← 可视化 notebook（英文，绿→红分阶染色）
├── scoring.cn.ipynb                   ← 可视化 notebook（中文版，同源生成）
├── build_scoring_notebook.py          ← 从源码重新生成两个 notebook 的脚本（中英双语）
├── .gitmodules                        ← 16 个 submodule 注册
└── skills/                            ← 各 submodule（shallow clone）
    ├── affaan-m__everything-claude-code/
    ├── anthropics__skills/
    ├── ComposioHQ__awesome-claude-skills/
    ├── coreyhaines31__marketingskills/
    ├── garrytan__gstack/                       ← 🆕 v1.2
    ├── juliusbrussee__caveman/                 ← 🆕 v1.4 (token-efficient)
    ├── kepano__obsidian-skills/
    ├── mattpocock__skills/
    ├── msitarzewski__agency-agents/            ← 🆕 v1.2
    ├── multica-ai__andrej-karpathy-skills/
    ├── nextlevelbuilder__ui-ux-pro-max-skill/
    ├── nexu-io__open-design/
    ├── obra__superpowers/
    ├── openai__skills/
    ├── addyosmani__agent-skills/
    ├── vercel-labs__agent-skills/
    ├── Egonex-AI__Understand-Anything/          ← 🆕 v1.5 (codebase→knowledge graph)
    ├── Fission-AI__OpenSpec/                     ← 🆕 v1.5 (spec-driven dev)
    ├── santifer__career-ops/                     ← 🆕 v1.5 (job-search automation)
    ├── Leonxlnx__taste-skill/                    ← 🆕 v1.5 (design taste)
    └── mvanhorn__last30days-skill/               ← 🆕 v1.5 (trend research)
```

## 🏆 Top-line Findings (latest snapshot **v1.5** · 2026-06-17 · max **210**)

| Rank | Repo | Score / 210 | Tier | 标签 |
|---:|---|---:|:---:|---|
| 🥇 1 | [`garrytan/gstack`](https://github.com/garrytan/gstack) | **156** | S | Garry Tan 实战 setup — D9=10 (52KB 最深) + D21=8 |
| 🥈 2 | [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) | 154 | S | 大而全 — 事实标准 |
| 🥉 3 | [`nexu-io/open-design`](https://github.com/nexu-io/open-design) | 152 | S | 设计赛道 + D20=9 |
| 4 | [`obra/superpowers`](https://github.com/obra/superpowers) | 150 | S | 原创方法论 — D21=7 |
| 5 | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) | 146 | S | "AI agency" — 222 个 agent 跨 18 领域 |
| 6 | [`juliusbrussee/caveman`](https://github.com/juliusbrussee/caveman) | 137 | A | "talk caveman, save 65% tokens" — token-efficient prompt engineering |
| 7 | `anthropics/skills` | 136 | A | 官方规范 |
| 8 | `addyosmani/agent-skills` | 128 | A | 生产级 — D21=9 |
| **9** | **[`Egonex-AI/Understand-Anything`](https://github.com/Egonex-AI/Understand-Anything)** | **117** | B | 🆕 v1.5 · 代码库→交互式知识图谱；D5=10/D6=9/D12=9/D13=8（多平台），661 stars/day |
| 10 | `mattpocock/skills` | 114 | B | TS 视角 — D20=9 |
| 11 | `openai/skills` | 113 | B | Codex 配套 — D21=8 |
| **12** | **[`santifer/career-ops`](https://github.com/santifer/career-ops)** | **113** | B | 🆕 v1.5 · 求职/简历自动化；D12=10（最强工程化）+ D3=7（10.7k forks）+ 13 语言 README，734 stars/day |
| 13 | `ComposioHQ/awesome-claude-skills` | 111 | B | D21=10 (含 awesome-list noise caveat) |
| 14 | `coreyhaines31/marketingskills` | 103 | B | 营销垂直 |
| 15 | `nextlevelbuilder/ui-ux-pro-max-skill` | 102 | B | UI/UX 产品化 |
| 16 | `vercel-labs/agent-skills` | 101 | B | Vercel 官方 |
| **17** | **[`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill)** | **98** | C | 🆕 v1.5 · 近30天趋势研究；D9=10（单文件 140KB 最深 SKILL.md）但 D20=1（巨型单技能） |
| **18** | **[`Fission-AI/OpenSpec`](https://github.com/Fission-AI/OpenSpec)** | **97** | C | 🆕 v1.5 · spec-driven 开发；0 个 SKILL.md（spec 工具）但 D12=9 + 517 docs |
| 19 | `multica-ai/andrej-karpathy-skills` | 92 | C | D20=10 + D21=9 但其他维度低 |
| **20** | **[`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill)** | **84** | C | 🆕 v1.5 · 设计"品味"技能；D21=9（41.4% lesson 密度最高）+ D9=9（13 技能均 23KB）但社区/contrib 低 |
| 21 | `kepano/obsidian-skills` | 72 | D | Obsidian 垂直 |

> **v1.4 → v1.5 变更**：
> 1. Cohort **16 → 21 repos**：新增 `Egonex-AI/Understand-Anything` (UA)、`Fission-AI/OpenSpec` (OS)、`santifer/career-ops` (CO)、`Leonxlnx/taste-skill` (TS)、`mvanhorn/last30days-skill` (L30)。总维度数 21 不变；max 210 不变。
> 2. **真实数据**（2026-06-17 采集）：D1-D7 via `gh` API；D8/D9/D13/D20 本地结构扫描；D21 via `scan_lessons.py`；D18/D19 via HN Algolia。
> 3. ⚠️ **Reddit 不可达**（HTTP 403）：5 个新 repo 的 D16/D17 未测量，floored 到 1（`raw_metrics` 中记为 `-1` sentinel）。既有 16 repo 的 v1.4 reddit 数据保留。
> 4. 最佳新晋：**UA #9 (B)** — 工程化 + 多平台 + 高 velocity；**CO #12 (B)** — 最强 D12 工程化 + 13 语言 i18n。
> 5. 极值：**L30** 单个 SKILL.md 达 **140KB**（全 cohort 最深 → D9=10，但 D20=1）；**TS** lesson 密度 **41.4%**（全新晋最高 → D21=9）。
> 6. 完整 v1.4 → v1.5 Δ-diff 见 `scoring.ipynb` 第 7 cell。

完整评分矩阵、按领域/角色推荐、方法论与 caveat 见 **[`EVALUATION.md`](./EVALUATION.md)**。

按 **具体任务 → 该装哪个 repo** 的功能正交决策手册见 **[`TASK_GUIDE.md`](./TASK_GUIDE.md)**（含 AM × O × NX overlap/正交/互补深度对比 + ~50 个任务 lookup + 推荐 stacks + 覆盖缺口）。

**5 个 AI 模型（Claude / ChatGPT / Gemini / Grok / Perplexity）独立评估的横向总结** 见 **[`agent_summary.md`](./agent_summary.md)** — 含强共识层（4 个必装 / 3 个避坑）、主要分歧、最小可用组合，以及与本仓库 v1.3 评分的对比。

## 📐 21 个评测维度 / 21 Dimensions

简表（详见 [`EVALUATION.md §2`](./EVALUATION.md#2-15-个评测维度--15-evaluation-dimensions) + [`§11`](./EVALUATION.md#11-v12-snapshot--新增-d16-d19social-signals--gs--aa) + [`§12`](./EVALUATION.md#12-v13-snapshot--新增-d20-d21--task-decomposition--lesson-encoded-quality)）：

| 类别 | Dimensions |
|---|---|
| 用户强调 ⭐ | **D1 Star Velocity** (stars/day since creation) |
| 社区热度 | D1, D2 Total Stars, D4 Watchers |
| 工程信号 | D3 Forks, D5 Commit Recency, D6 Commit Cadence, D7 Contributors |
| 内容侧 | D8 Skill Volume, D9 Skill Depth, D10 Supp. Material Density |
| 工程化 | D11 Doc Quality, D12 Eng. Hygiene |
| 生态可移植 | D13 Multi-Agent Portability |
| 战略价值 | D14 Domain Breadth, D15 Originality / Authority |
| 社交信号 (v1.2) | **D16 Reddit Heat** (30d posts + comments) · **D17 Reddit Sentiment** (30d avg upvote) · **D18 HN Heat** (30d stories + comments) · **D19 HN Sentiment** (30d avg points) |
| **🆕 任务质量信号 (v1.3)** | **D20 Task Decomposition** (反转 avg SKILL.md 字节，越小越好 — 每个 skill 应聚焦一个任务) · **D21 Lesson-Encoded Quality** (含 anti-pattern / red-flag / lessons-learned / version / context 标记的 .md 占比 — "有价值的 skill 应包含 模型未知知识 + 环境上下文 + 真实失败教训") |

## 🧪 Skill 验证 / 测试 / 防回归 横向研究（v1.5 附录 · 未计分）

> 现有 21 个维度里 **没有**任何一维直接衡量「这个 repo 是否验证 skill 的**行为 / 效果**、是否防行为回归」——`D12 Engineering Hygiene` 只把 tests/CI/validators 笼统当工程信号。本节是对 21 个 repo 的专项遍历结论，提议作为 **D22 Skill-Behavior Validation Rigor**（暂不计分，遵循「不把判断写进单文件」原则）。
>
> **核心区分**：绝大多数 repo「测的是支撑脚本 / lint frontmatter」，而**真正运行 skill、对它的输出或效果打分**的极少。

### 用到的测试框架与实现方式

社区**没有**统一的「skill 测试框架」。实测栈分四类：

| 类别 | 工具 | 谁在用 · 怎么实现 |
|---|---|---|
| 通用代码 test runner | **Vitest** / **Pytest** / 自研 Node runner | UA·OS·NX·GS 用 vitest；L30·AM 用 pytest（`uv run pytest`）；CO 用自研 `test-all.mjs`（无框架，自己数 pass/fail）；AM 用 `node tests/run-all.js`。**只测脚本，不碰 prose** |
| LLM-as-judge 行为评测（**全是自研，无共享库**） | `claude -p` / Anthropic SDK / Gemini REST + 打分 | **GS** `test/helpers/llm-judge.ts`+`benchmark-judge.ts` 跑 `claude -p` 比 `eval-baselines.json`；**anthropics** `skill-creator` 用 `run_eval.py`+`grader.md`/`comparator.md` 子 agent 判官；**L30** `evaluate_search_quality.py` 调 Gemini 判官出 Precision@5/nDCG；**caveman** `llm_run.py` 三臂 + tiktoken 数 token |
| 结构 / frontmatter validator（测形不测效） | `agentskills/skills-ref` · `Flash-Brew-Digital/validate-skill` · `claude plugin validate` · 自研 sh | **CH** 双 validator（自研 + 官方 skills-ref）；**AD** 用 `claude plugin validate`+真实安装；**AA** `lint-agents.sh`；**OAI** `quick_validate.py` |
| AI review bot / 视觉回归 | CodeRabbit · `claude-code-action` · Playwright | **CO·OS** 挂 `.coderabbit.yaml`；**NL** 挂 `/code-review` bot；**NX** 用 Playwright `toHaveScreenshot` 截图基线（针对 app UI，非 skill 产出） |

> **最接近「可复用 skill 测试框架」的**：`affaan-m/everything-claude-code` 出货了 `eval-harness`（eval-driven-development 框架）、`agent-eval`（pass@k + YAML task 定义）、`skill-comply`（测「prompt 中立时 agent 是否仍遵守 SKILL.md」）——但这是**卖给用户**的工具，没接到它自己的 CI 门。

### L0–L5 验证层级阶梯

| 层 | 含义 |
|---|---|
| **L0** | 无验证（纯人工策展 prose） |
| **L1** | 仅 CHANGELOG / 版本纪律 |
| **L2** | 支撑**代码**测试（脚本单元/集成，**不碰 skill prose**） |
| **L3** | **skill 行为**评测（eval / LLM-judge / golden transcript / 对 skill I/O 的契约测试） |
| **L4** | **CI 回归门**（PR/push 上阻断式跑） |
| **L5** | **元技能**：明文规定「如何写 / 测 / 验证一个 skill」 |

### 主表（21 repo）

| Repo | 命中层级 | 真测 skill 行为? | 回归防护核心 |
|---|---|---|---|
| **GS** gstack | L1·L2·L3·L4·L5 | ✅ 唯一全闭环 | `eval-baselines.json`+回归判官+version/docs 门 |
| **L30** last30days | L1·L2·L3·L4 | ✅ 最完整两层 | 阻断契约套件 + 跨 git-ref LLM-judge A/B |
| **caveman** | L1·L2·L3 | ✅ 测 token 效果 | 提交 `snapshots/results.json`+`skill_md_sha256` 钉版本 |
| **A** anthropics | L3·L5 | ✅ 统计化（不入库） | 新旧快照 head-to-head + train/test split |
| **O** superpowers | L1·L2·L3·L5 | ✅ 对抗式行为 TDD | verify-before-done + 可重跑行为测试 + 94% PR 拒绝 |
| **OAI** openai | L2·L3\*·L5 | ◑ golden（不 gate） | eval JSON + QA rubric（手动重跑） |
| **CH** marketingskills | L1·L2·L3\*·L4 | ◑ 设计了不 gate | per-skill SemVer + frontmatter CI（197 evals 未入门） |
| **AM** affaan-m | L1·L2·L4·L5 | ✖ eval 工具卖给用户 | 矩阵 CI 仅守代码+元数据 |
| **UA** Understand-Anything | L2·L3·L4 | ◑ 脚本 golden | 字节级**确定性**断言 + 阻断 CI |
| **OS** OpenSpec | L1·L2·L3·L4 | ◑ 测**交付/安装** | **migration + drift** 测试 |
| **CO** career-ops | L1·L2·L3\*·L4 | ◑ grep prose 契约 | 阻断 CI + 分支保护 + CodeRabbit |
| **NX** open-design | L1·L2·L3·L4·L5\* | ✖ 测引擎/UI | 240 测试 + Playwright 截图基线 |
| **AD** addyosmani | L2·L4·L5 | ✖ 守打包/可装 | `claude plugin validate` + 真实安装 |
| **V** vercel-labs | L2·L4·L5 | ✖ 守 rules 构建 | path-filtered 单 skill 门 |
| **AA** agency-agents | L2·L4 | ✖ frontmatter lint | `lint-agents.sh` 阻断 PR |
| **NL** ui-ux-pro-max | L1·L2 | ✖ conda CI 近空跑 | `skill.json` 版本 + LLM-reviewer bot |
| **C** ComposioHQ | L4 | ✖ 守 list 卫生 | diff 感知 PR 门（限定 README 区域） |
| **M** mattpocock | L1·L5 | ✖ | `write-a-skill` 清单 + `deprecated/` 目录生命周期 |
| **TS** taste-skill | L1 | ✖ 人工观察 | 失败→具名禁令 + 起飞前 checklist |
| **MA** karpathy | L0 | ✖ | 无（仅 README 主观「怎么判断在生效」） |
| **K** obsidian | L0 | ✖ | 无 |

> `*` = L3\* 评测套件已设计但未入 CI；L5\* 为非正式（review-lane / red-spec 文档而非元技能）。◑ = 有但不阻断 / 只测代码或契约层。✖ = 该层缺失或只守打包。

### 真正测「skill 行为」的少数派（按严格度）

1. **GS gstack** — 唯一全闭环且阻断在 CI：`skill-e2e-*.test.ts` 用 `claude -p`/Agent SDK 真跑 skill 打 golden，`llm-judge.ts` 给 1–5 分 + 算**埋雷检出率**，`evals.yml` 12 套件矩阵在 Docker 里跑、贴 PR「通过/失败+成本」评论（diff 选择压到 ~$4/run）。
2. **L30 last30days** — 确定性契约入阻断 CI + **离线** Gemini-judge A/B（跨 git-ref，Precision@5/nDCG@5），并用一份 ADR 明文论证 judge eval 为何**不进**阻断门（成本/判官不确定→会变 flaky）。
3. **caveman** — 唯一测「效果」：三臂 `baseline`/`terse`/`skill`，诚实指标取 **skill−terse**（剔除「泛泛简洁」的功劳）；提交结果快照 + `skill_md_sha256` 钉到具体 SKILL.md。
4. **anthropics `skill-creator`** — 同轮 spawn 装/不装（或新/旧快照）双 subagent + 判官子 agent + mean±stddev + 60/40 train/test split 防过拟合（作者期工具，不入库不 gate）。
5. **obra/superpowers** — 对抗式 TDD-for-skills：让没装 skill 的 fresh subagent 在压力场景失败 → 逐字记录狡辩 → 写最小 skill 堵 → 重跑；真行为测试埋 SQL 注入断言 skill 被触发且 bug 被拦（无 CI，靠 94% PR 拒绝治理）。
6. **OAI / CH** — golden-transcript eval JSON（query+expected_behavior+success_criteria / assertion 清单），**设计好但未接进 CI**。

### 回归防护工具箱

| 机制 | 谁在用 | 一句话 |
|---|---|---|
| **基线对比 eval** | GS·A·L30·caveman | 量化「这版是不是变差了」——最硬核 |
| **CI 阻断门** | GS·L30·OS·UA·CO·AM·NX·AD·V·AA·C | 但多数只 gate 代码/打包/frontmatter，仅 GS·L30 gate 到**行为** |
| **确定性 / golden 钉死** | UA（字节级）·caveman（snapshot+sha）·L30（mock-JSON） | 同输入必同输出，改逻辑立刻现 diff |
| **migration + drift 测试** | OS（最佳） | 专测「升级后落到磁盘的 skill 文件是否仍正确」 |
| **prose 契约断言** | CO（grep 门短语）·GS（命令存在性）·AD（hook JSON） | 防 SKILL.md 承重指令被悄悄删改 |
| **版本 / CHANGELOG 纪律** | GS·OS（changesets）·CO（Release-Please）·CH | 每条修复都能追到锁它的那个测试 |
| **治理门（人工）** | O（94% PR 拒绝 + 必交 eval evidence）·anthropics | 改 Red-Flags 表必须附前后 eval 证据 |
| **累积反模式清单** | TS | 纯 prose repo 的防护：每次踩坑变永久具名禁令 |

### 可借鉴（尤其想给自己的 skill 做回归测试时）

- 抄 **GS**：代表性 prompt → golden fixture → `claude -p` 跑 → LLM-judge 打分 → 存 baseline → 新版比基线，diff 选择 + 成本上限进 CI。
- 抄 **caveman 的 control-arm**：测「装 skill vs 等价的精简指令」的**边际**差异，别把模型本来就会的功劳算给 skill。
- 抄 **L30 的 ADR 纪律**：确定性契约入阻断门；贵且不确定的 LLM-judge eval 留 `workflow_dispatch` 手动。
- 抄 **OpenSpec 的 migration + drift 测试**：把「升级后落到用户磁盘的 skill 文件」当一个被测的契约。

## 🎨 Notebook 渲染示意 / Notebook preview

`scoring.ipynb` 的 11 个 cells：

| Cell | 用途 |
|:---:|---|
| 1 | 概览 + 维护说明 |
| 2 | 实时从 `git submodule status` 读取 HEAD SHA |
| 3 | `DIMENSIONS` + `REPOS` 注册表 |
| 4 | **`EVALUATIONS` 快照历史**（你只需要 append） |
| 5 | 颜色函数（9 段绿→红，无 matplotlib 依赖） |
| 6 | **分数矩阵 + 染色** |
| 7 | Ranking + Tier 徽章 |
| 8 | **SHA Drift 检测**（snapshot vs 当前 HEAD） |
| 9 | Raw metrics（每列 percentile 染色） |
| 10 | **Δ-diff**（≥2 个 snapshot 时自动渲染维度变化） |
| 11 | "如何追加新 snapshot" 手册 |

## 🔄 长期维护 / Long-term maintenance

每隔一段时间想 refresh 评分？只需要做一件事：**往 `scoring.ipynb` 的 `EVALUATIONS` 列表里 append 一份新 dict**，包含：

```python
{
    'eval_date':      '2026-MM-DDTHH:MM:SSZ',
    'version':        '1.1',
    'note':           '...',
    'submodule_shas': {...},   # 从 `git submodule status` 复制
    'raw_metrics':    {...},   # 从 `gh repo view --json` 重新采集
    'scores':         {...},   # rank-based 1-10 重新打分
}
```

Re-run all cells，Cell 10 会自动渲染新旧 snapshot 的 Δ-diff。

**重要原则**：
- ✅ append-only — 永远不修改历史 snapshot
- ✅ submodule SHA + raw_metrics 必须同时记录（前者锚定基准，后者支持方法论变更后的回填）
- ❌ 不要把"什么是 skill 好"的判断写进任何单个文件 — 写进 `EVALUATIONS`，让历史说话

## 🤔 Caveats（务必知道）

1. **velocity 维度对新仓库利好**：`nexu-io/open-design` 只有 15 天活跃就在 D1 拿满分；早期峰值不可外推到 6 个月之后。需要与 D2（绝对存量）一起看。
2. **"SKILL.md 数量"是双刃剑**：`ComposioHQ` 用 awesome-list 风格堆量到 864，但每个 SKILL 平均 3.4 KB，辅料密度仅 0.03 — D9/D10 一并消除该 bias。
3. **半客观维度（D11/D12/D14/D15）依赖人工抽样判断**：可能有误差，欢迎在 PR 里挑战具体打分。
4. **forrestchang/andrej-karpathy-skills 已被 GitHub 重定向到 `multica-ai/andrej-karpathy-skills`**（owner 重命名），合并为一项。

## 🔗 当前 Cohort / Submodules

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

数据快照时间：**2026-05-13**。最新数据见各仓库 GitHub 页或 `scoring.ipynb` 内 `raw_metrics`。

## 📜 想要加入 / Adding a new repo to the cohort

```bash
# 1. 增加 submodule
git submodule add --depth 1 https://github.com/<owner>/<repo>.git skills/<owner>__<repo>

# 2. 采集 raw metrics（参见 EVALUATION.md §3）
gh repo view <owner>/<repo> --json stargazerCount,forkCount,createdAt,pushedAt,description

# 3. 在 scoring.ipynb 的 REPOS 列表里注册新 code
# 4. 在新 snapshot 里给它 15 个分数
# 5. Re-run notebook，commit + push
```

## 📝 License

本仓库的"评测代码 + 文档"基于 **MIT**（如未来添加 LICENSE 文件）。每个 submodule 各自的 license 见其 LICENSE 文件（详见 §9.1）。

数据来源：GitHub API（`gh repo view`）+ 各仓库公开内容。所有评分本质上是 **截止 2026-05-13 的快照判断**，不构成对任何项目质量的最终评价。

---

_这个项目欢迎挑战。在 issue 里指出具体维度评分有误，或建议新维度，远比口头讨论更有帮助。_
