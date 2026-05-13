# skill-obs

> 🌐 **Language**: **🇨🇳 中文** · [🇬🇧 English](./README.en.md)

> **Skill Observatory** — 一个对当下 Agent Skills / Claude Skills 生态做横向评测的元仓库。
> 12 个主流 skill collection repo 作为 git submodule，配 15 维度评分 + 可视化 notebook + append-only 评估历史。

[![Eval baseline](https://img.shields.io/badge/eval-2026--05--13-blue)](./EVALUATION.md)
[![Notebook](https://img.shields.io/badge/notebook-scoring.ipynb-orange)](./scoring.ipynb)
[![Task Guide](https://img.shields.io/badge/任务→repo-TASK__GUIDE-red)](./TASK_GUIDE.md)
[![Cohort size](https://img.shields.io/badge/repos-13-green)](./.gitmodules)
[![Dimensions](https://img.shields.io/badge/dimensions-15-purple)](./EVALUATION.md#2-15-个评测维度--15-evaluation-dimensions)
[![Snapshots](https://img.shields.io/badge/snapshots-v1.0_·_v1.1-yellow)](./scoring.ipynb)

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
├── scoring.ipynb                      ← 可视化 notebook（绿→红分阶染色）
├── build_scoring_notebook.py          ← 从源码重新生成 notebook 的脚本
├── .gitmodules                        ← 13 个 submodule 注册
└── skills/                            ← 各 submodule（shallow clone）
    ├── affaan-m__everything-claude-code/
    ├── anthropics__skills/
    ├── ComposioHQ__awesome-claude-skills/
    ├── coreyhaines31__marketingskills/
    ├── kepano__obsidian-skills/
    ├── mattpocock__skills/
    ├── multica-ai__andrej-karpathy-skills/
    ├── nextlevelbuilder__ui-ux-pro-max-skill/
    ├── nexu-io__open-design/
    ├── obra__superpowers/
    ├── openai__skills/
    ├── addyosmani__agent-skills/
    └── vercel-labs__agent-skills/
```

## 🏆 Top-line Findings (latest snapshot **v1.1** · 2026-05-13)

| Rank | Repo | Score / 150 | Tier | Δ vs v1.0 | 标签 |
|---:|---|---:|:---:|---:|---|
| 🥇 1 | [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) | **129** | S | 0 | 大而全 — 事实标准 |
| 🥈 2 | [`obra/superpowers`](https://github.com/obra/superpowers) | 115 | S | −1 | 原创方法论 — 思想最深 |
| 🥉 3 | [`nexu-io/open-design`](https://github.com/nexu-io/open-design) | 110 | S | 0 | 15 天上线就吃下设计赛道 |
| 4= | `anthropics/skills` | 93 | A | −1 | 官方规范 |
| 4= | `nextlevelbuilder/ui-ux-pro-max-skill` | 93 | A | −1 | UI/UX 产品化 |
| 6 | `addyosmani/agent-skills` | 90 | A | 0 | 生产级通用 |
| 7 | `coreyhaines31/marketingskills` | 85 | A | −1 | 营销垂直 |
| 8 | `ComposioHQ/awesome-claude-skills` | 80 | B | 0 | 数量碾压（864 SKILL.md） |
| 9 | `mattpocock/skills` | 76 | B | 0 | TS 工程师视角 |
| **10** | **[`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills)** | **75** | **B** | 🆕 | **Vercel 官方 — D10 辅料密度 第一** |
| 11 | `openai/skills` | 72 | B | −1 | Codex 配套 |
| 12 | `multica-ai/andrej-karpathy-skills` | 69 | B | −1 | 单文件 drop-in |
| 13 | `kepano/obsidian-skills` | 50 | C | 0 | Obsidian 垂直 |

> **v1.0 → v1.1 变更**：新增 `vercel-labs/agent-skills`（13 repos cohort）；V 在 D10（supplementary material density）排第一（19.3 辅料/skill），把 OAI 从 10 → 9 顶下来，连带 5 个排名靠前的 repo 在 D10 维度各掉 1 分，6 个 repo 总分降 1。完整 Δ-diff 见 `scoring.ipynb` 第 7 cell。

完整评分矩阵、按领域/角色推荐、方法论与 caveat 见 **[`EVALUATION.md`](./EVALUATION.md)**。

按 **具体任务 → 该装哪个 repo** 的功能正交决策手册见 **[`TASK_GUIDE.md`](./TASK_GUIDE.md)**（含 AM × O × NX overlap/正交/互补深度对比 + ~50 个任务 lookup + 推荐 stacks + 覆盖缺口）。

## 📐 15 个评测维度 / 15 Dimensions

简表（详见 [`EVALUATION.md §2`](./EVALUATION.md#2-15-个评测维度--15-evaluation-dimensions)）：

| 类别 | Dimensions |
|---|---|
| 用户强调 ⭐ | **D1 Star Velocity** (stars/day since creation) |
| 社区热度 | D1, D2 Total Stars, D4 Watchers |
| 工程信号 | D3 Forks, D5 Commit Recency, D6 Commit Cadence, D7 Contributors |
| 内容侧 | D8 Skill Volume, D9 Skill Depth, D10 Supp. Material Density |
| 工程化 | D11 Doc Quality, D12 Eng. Hygiene |
| 生态可移植 | D13 Multi-Agent Portability |
| 战略价值 | D14 Domain Breadth, D15 Originality / Authority |

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
