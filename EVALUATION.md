# Skill Repo 评测报告 / Skill Collection Evaluation

> 🌐 **Language**: **🇨🇳 中文** · [🇬🇧 English](./EVALUATION.en.md)

> 评测日期 / Date: **2026-05-13**  
> 当前 Snapshot / Current: **v1.5** — **21-repo cohort × 21 dims**（v1.0 / v1.1 / v1.2 / v1.3 / v1.4 历史在 `scoring.ipynb`）  
> 评分量表 / Scale: **1–10** (10 = best in cohort)  
> 总分上限 / Max total: **210** (21 dims × 10)  
> ⚠ **阅读须知 / Reading guide（务必先读）**
>
> 1. **当前有效数据 = §14 (v1.5) + [`scoring.ipynb`](./scoring.ipynb)。** 本 markdown 的 **§3 / §4 / §5 表格是 v1.1 历史快照（13 repos、满分 150），仅作上下文、数字已过时** —— 请勿当成当前排名（例：§5 显示 AM=129 是旧标尺；当前 §14 为 AM=154、满分 210）。分节历史：§11→v1.2 (D16-D19 社交信号)、§12→v1.3 (D20-D21 任务质量)、§13→v1.4 (CV)、**§14→v1.5（新增 UA/OS/CO/TS/L30）**。
> 2. **5 个 v1.5 新 repo 的分数为 provisional（暂定）**：主观维度 (D14/D15) 与 1-10 rank 校准为单轮评估；且**评测时 Reddit 不可达 (HTTP 403)，其 D16/D17 未测量、floor 到 1**（`raw_metrics` 记 `-1` sentinel）。因此新 repo 在社交两维上被系统性低估，总分与原有 16 repo **不完全同口径**，名次宜作方向性参考而非精确定论。
> 3. **采集时间混合**：原有 16 repo 的指标采于 **2026-05-13**，5 个新 repo 采于 **2026-06-17**。

## 1. 入选仓库 / Cohort

| Code | Repo | Stars | Forks | Created | Last push | 主题 |
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
| **UA** 🆕 | **[`Egonex-AI/Understand-Anything`](https://github.com/Egonex-AI/Understand-Anything)** | **62,155** | **5,129** | **2026-03-15** | **2026-06-16** | **代码库→交互式知识图谱 (🆕 v1.5)** |
| **OS** 🆕 | **[`Fission-AI/OpenSpec`](https://github.com/Fission-AI/OpenSpec)** | **55,241** | **3,866** | **2025-08-05** | **2026-06-13** | **spec-driven 开发工作流 (🆕 v1.5)** |
| **CO** 🆕 | **[`santifer/career-ops`](https://github.com/santifer/career-ops)** | **54,306** | **10,774** | **2026-04-04** | **2026-06-16** | **求职/简历自动化 CV/ATS/tracking (🆕 v1.5)** |
| **TS** 🆕 | **[`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill)** | **45,534** | **3,169** | **2026-02-19** | **2026-06-12** | **设计"品味"技能，避免通用输出 (🆕 v1.5)** |
| **L30** 🆕 | **[`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill)** | **43,681** | **3,592** | **2026-01-23** | **2026-06-17** | **近 30 天趋势研究 Reddit/X/YouTube/HN/web (🆕 v1.5)** |

> 注 / Note: `forrestchang/andrej-karpathy-skills` 已被 GitHub 重定向到 `multica-ai/andrej-karpathy-skills`（仓库迁移/重命名），合并为同一项。

## 2. 15 个评测维度 / 15 Evaluation Dimensions

15 个维度借鉴 CHAOSS OSS 健康度模型 + awesome-list 质量评测 + Claude Skills 规范要素综合提炼。**D1 是用户明确要求的维度**（star/天 = stars 总数 ÷ 创建至今的天数）。

| #   | 维度 Dimension | 类型 | 测量方式 |
|----:|---|---|---|
| **D1**  | **Star Velocity** ⭐ (stars/day since creation) | 客观 | `stargazerCount / days_since_created` — 用户强调维度 |
| D2  | Total Stars | 客观 | 绝对热度 / mindshare |
| D3  | Fork Volume | 客观 | 真实使用 / 复制深度 |
| D4  | Watcher Count | 客观 | 深度订阅用户 |
| D5  | Commit Recency | 客观 | `days_since_pushed`（反向，越小越好） |
| D6  | Commit Cadence | 客观 | `total_commits / days_since_created` — 持续开发力 |
| D7  | Contributor Diversity | 客观 | 不同贡献者数（含匿名） |
| D8  | Skill Volume | 客观 | `SKILL.md` 文件数 |
| D9  | Skill Depth | 客观 | 平均 `SKILL.md` 字节数 |
| D10 | Supplementary Material Density | 客观 | (`*.md` − `SKILL.md`) / `SKILL.md` — 每个 skill 的辅助文档量 |
| D11 | Documentation Quality | 半客观 | README 行数 + 顶层文档完整度（CHANGELOG, CONTRIBUTING, AGENTS, CLAUDE 等） |
| D12 | Engineering Hygiene | 半客观 | LICENSE、tests、hooks、validators、CI、install 脚本、CoC、changelog 等 |
| D13 | Multi-Agent Portability | 客观 | README 内提及的 agent 平台数（Claude / Codex / Cursor / Gemini / Copilot / OpenCode / Qwen / Windsurf / Kimi …） |
| D14 | Domain Coverage Breadth | 半客观 | 涉及领域宽度（通用 vs 单一领域） |
| D15 | Originality / Authority | 半客观 | 首创/官方权威 vs 二次聚合 vs 同质化 |

**为什么这 15 个 / Why these 15:**

| 维度选择原则 | 体现哪些 dims |
|---|---|
| 用户显式要求 | D1 |
| 社区热度（短期 vs 长期 vs 深度） | D1, D2, D4 |
| 工程信号（真实使用 vs 看戏） | D3, D5, D6, D7 |
| 内容侧（量 vs 质 vs 辅料） | D8, D9, D10 |
| 工程化成熟度（可消费性） | D11, D12 |
| 生态可移植性（避免厂商锁定） | D13 |
| 战略价值（覆盖面 + 差异化） | D14, D15 |

## 3. 关键原始指标 / Raw Metrics

> 截止 2026-05-13。所有计算可通过 `gh repo view <owner>/<repo> --json …` 复现。

| Repo | Days alive | Stars/day (D1) | Stars | Forks | Watchers | Last push (d ago) | Commits/day | Contribs | SKILL.md | Avg SKILL bytes | Supp.docs/skill | Multi-agent count |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AM | 115 | **1,572.5** | 180,838 | 27,876 | 899 | 0  | **14.82** | 183 | 572 | 8,847 | 2.0  | 7 |
| O  | 216 | 872.7 | 188,498 | 16,759 | 753 | 0  | 2.04  | 33  | 14  | 8,168 | 4.0  | 6 |
| A  | 233 | 571.9 | 133,251 | 15,715 | 865 | 4  | 0.15  | 13  | 18  | 10,995 | 3.94 | 1 |
| MA | 106 | 1,203.3 | 127,547 | 12,958 | 671 | 23 | 0.26  | 7   | 1   | 2,518 | 5.0  | 2 |
| NL | 164 | 474.0 | 77,723 | 7,977 | 381 | 40 | 0.82  | 31  | 7   | 12,272 | 8.29 | 8 |
| M  | 99 | 779.5 | 77,173 | 6,656 | 532 | 1  | 0.78  | 2   | 28  | 3,321 | 1.14 | 2 |
| C  | 208 | 286.1 | 59,518 | 6,462 | 399 | 6  | 0.34  | 26  | **864** | 3,444 | 0.03 | 7 |
| AD | 87 | 466.4 | 40,580 | 4,472 | 255 | 3  | 2.0  | 23  | 22  | 10,703 | 1.45 | 7 |
| NX | 15 | **2,582.3** | 38,735 | 4,403 | 142 | 0  | **42.5** | **186** | 218 | 3,438 | 1.86 | **9** |
| K  | 131 | 235.3 | 30,825 | 2,100 | 185 | 6  | 0.30  | 13  | 5   | 6,040 | 1.2  | 3 |
| CH | 118 | 239.1 | 28,215 | 4,550 | 288 | 7  | 2.21 | 16  | 41  | 11,443 | 4.02 | 5 |
| OAI| 169 | 112.3 | 18,982 | 1,259 | 110 | 1  | 0.64 | 34  | 43  | 9,435 | **11.33** | 1 |

> **D1 注意**：NX (`nexu-io/open-design`) 只有 15 天，velocity 2,582 stars/day 含早期峰值偏置；不可直接外推。

## 4. 评分总表 / Score Matrix (Snapshot **v1.1** · 13 repos)

```
列顺序：AM | O | NX | A | NL | AD | CH | C | M | V | OAI | MA | K
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

> **v1.0 → v1.1 Δ**：新增 V (vercel-labs)。V 在 D10（辅料密度 19.3）取代 OAI 登顶，连带 OAI/O/A/NL/CH/MA 在 D10 各掉 1 分，6 个 repo 总分各降 1。v1.0 baseline 完整保留在 `scoring.ipynb`。

## 5. 总排行 / Overall Ranking

### 5.1 等权 / Equal-weighted (default)

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

### 5.2 D1 加权 ×3 / Velocity-emphasized ranking

如果按用户强调的 D1（star velocity）加权 ×3（其他维度仍 ×1） — 即 total + 2×D1：

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

> 加权后 Top-3 不变（顺序甚至完全相同），V 仍在 #11 — velocity 维度对结论稳健。

## 6. 各仓库一句话定位 / One-liner per repo

| Repo | 一句话 | 看点 / 风险 |
|---|---|---|
| **affaan-m/everything-claude-code** (S) | 最像"事实标准"的 agent harness 优化套件——大而全 | ✅ 工程完备度顶级；⚠ 多为对其他社区资产的整合，原创性中等 |
| **obra/superpowers** (S) | 原创"超能力"方法论——TDD / debugging / planning 等元技能 | ✅ 思想性最强；⚠ skill 文件数偏少（14），靠深度而非数量 |
| **nexu-io/open-design** (S) | 15 天上线就吃下设计赛道的 OSS Claude Design 替代品 | ✅ 工程化 + 多语言 + 多平台兼容最广（9 个 agent）；⚠ velocity 含早期偏置 |
| **anthropics/skills** (A) | 官方规范 — 定义了 SKILL.md 的"标准" | ✅ 权威 + 质量基线；⚠ 单平台、节奏慢、量少 |
| **nextlevelbuilder/ui-ux-pro-max-skill** (A) | 商业化最像产品的 UI/UX 套件 | ✅ 平均 skill 12KB、文档丰富；⚠ 近 40 天未更新 |
| **addyosmani/agent-skills** (A) | "Production-grade" 通用工程技能集 | ✅ 结构清晰，作者背书；⚠ 体量中等 |
| **coreyhaines31/marketingskills** (A) | 营销 / CRO / SEO 垂直 skills | ✅ 工程化好、有 validator；⚠ 领域窄 |
| **ComposioHQ/awesome-claude-skills** (B) | 大型 awesome-list / 索引（864 个 SKILL.md） | ✅ 数量碾压；⚠ 几乎无辅助文档（D10=1），高度同质化 |
| **mattpocock/skills** (B) | TypeScript 大神的"工程师真正用的 skills" | ✅ 个人风格鲜明；⚠ 仅 2 贡献者、平台覆盖窄 |
| **vercel-labs/agent-skills** (B · 🆕 v1.1) | Vercel 官方 — Vercel 部署 + React/Next.js 实战 | ✅ D10 辅料密度全 cohort 第一（19.3）+ 官方权威；⚠ 体量 7 skills、仅 Web 单一领域、无 LICENSE |
| **openai/skills** (B) | 官方 Codex skill catalog | ✅ 辅料密度次高（D10=9）+ 原创权威；⚠ 仅 Codex、社区小 |
| **multica-ai/andrej-karpathy-skills** (B) | 一份基于 Karpathy 观察的 CLAUDE.md | ✅ velocity 极高；⚠ 1 个文件、单点价值 |
| **kepano/obsidian-skills** (C) | Obsidian / Markdown / Canvas 垂直 | ✅ 创作者权威；⚠ 体量最小、覆盖窄 |

## 7. 评测方法论与局限 / Methodology & Caveats

**评分映射**：每个维度内对 12 个仓库 rank-based 1–10 评分（rank 1 → 10，rank 12 → 1，均匀分布；并列取平均）。客观维度直接用数值排序；半客观维度（D11、D12、D14、D15）由对 README、目录结构、CONTRIBUTING、validators 的人工抽样判断。

**主要 caveat**：

1. **Velocity 维度对新仓库利好**：NX (15 天 alive) 在 D1/D6 拿满分；早期峰值不可外推到 6 个月之后。建议结合 D2（绝对存量）一起看。
2. **"SKILL.md 数量"是双刃剑**：ComposioHQ 用 awesome-list 风格堆量到 864，但每个 SKILL 平均仅 3.4KB 且辅料密度仅 0.03；这是数量陷阱。D9（深度）+ D10（辅料）一并消除该 bias。
3. **frontmatter 合规率 ≈ 100%**：早期检测脚本因 `xargs` 解析 bug 误报全员 0%；修正后所有仓库 SKILL.md 都符合 `name:` + `description:` 基本 frontmatter（这是社区已收敛的事实标准），因此该维度不再具有区分度，被替换为 D10（辅料密度）。
4. **多平台支持靠 README 提及关键词检测**：可能误判（README 提到但未真支持）；建议人工复核 D13。
5. **AM 与 NX 工程化分都给到 10**：他们的工程化方向不同（AM 侧重 hooks/scripts/install/lint，NX 侧重 multi-lang docs + e2e + Nix）；都是 cohort 顶端，并列。
6. **MA = multica-ai 是 forrestchang 重定向**：GitHub 端做了 owner 重命名/迁移，所以两者数据等价；这里以 multica-ai 为规范名。

## 8. 一句话推荐 / TL;DR

- **追"事实标准 / 总分最高"**：`affaan-m/everything-claude-code`
- **追"原创方法论 / 思想深度"**：`obra/superpowers`  
- **追"官方规范 / 学 SKILL.md 怎么写"**：`anthropics/skills`
- **追"设计赛道 / 多平台兼容最广"**：`nexu-io/open-design`
- **追"垂直领域参考"**：`coreyhaines31/marketingskills` (营销) · `nextlevelbuilder/ui-ux-pro-max-skill` (UI/UX) · `kepano/obsidian-skills` (Obsidian)
- **追"广撒网 / 一站式索引"**：`ComposioHQ/awesome-claude-skills`
- **追"官方 Codex 配套"**：`openai/skills`

## 9. 按领域 / 按角色 推荐 / By Domain & By Persona

### 9.1 按领域 · 用例 / Use case

| # | 领域 / 使用场景 | 最合适 repo | 关键理由（引用维度） |
|---:|---|---|---|
| 1 | **学 SKILL.md 官方规范**（自建 skill） | [`anthropics/skills`](https://github.com/anthropics/skills) | 唯一官方权威；frontmatter 标准定义者；D15(原创性)=10 |
| 2 | **OpenAI Codex 用户** | [`openai/skills`](https://github.com/openai/skills) | 官方 Codex 配套；D10(辅料密度)=10 — 每个 skill 11+ 份支撑文档 |
| 3 | **大而全的 agent 工程框架** | [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) | 总分 #1 (129)；commands + hooks + plugins + install 脚本一站齐 |
| 4 | **方法论 / 元技能**（TDD、debugging、planning、brainstorming） | [`obra/superpowers`](https://github.com/obra/superpowers) | 原创"超能力"框架；D15=9；思想深度最强 |
| 5 | **生产级软件工程**（通用） | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 作者背书 + 结构清晰；D14(领域宽度)=8 |
| 6 | **TypeScript / 个人工程师效率** | [`mattpocock/skills`](https://github.com/mattpocock/skills) | Matt Pocock 的 TS-first 视角；"Skills for Real Engineers" 自带筛选 |
| 7 | **UI / UX 组件级设计** | [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | D9(skill 深度)=10；色板/字体/产品类型最详细 |
| 8 | **设计系统 + 多平台创意输出**（slides/HTML/PDF/视频） | [`nexu-io/open-design`](https://github.com/nexu-io/open-design) | 19 skills + 71 design systems；D13(多平台兼容)=10（9 个 agent） |
| 9 | **营销 / CRO / SEO / Growth** | [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) | 唯一专攻营销；附 `validate-skills.sh`，工程化最严谨 |
| 10 | **Obsidian / Markdown 知识管理** | [`kepano/obsidian-skills`](https://github.com/kepano/obsidian-skills) | Obsidian creator (kepano) 亲自维护；唯一覆盖 Canvas / Bases / JSON Canvas |
| 11 | **零负担 CLAUDE.md 快速接入** | [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | 单文件 drop-in；Karpathy 提炼的 LLM coding 反模式 |
| 12 | **浏览 / 发现 skill 生态** | [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | 864 个 SKILL.md 索引；最大 awesome-list |
| **13** | **Vercel / Next.js / React 生产工程** | [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | Vercel 官方；React 40+ 性能规则；D10(辅料)=10 全 cohort 第一 |

### 9.2 横切需求 / Cross-cutting

| 需求 | 推荐 |
|---|---|
| 最广 agent 平台兼容（9 个：Claude/Codex/Cursor/Gemini/Copilot/OpenCode/Qwen/Windsurf/Kimi） | `nexu-io/open-design` |
| 规范 + 实战范例配套 | `anthropics/skills`（规范）+ `obra/superpowers`（范例） |
| 中文 / 多语 i18n 友好 | `nexu-io/open-design`（中/日/葡/德/法 CONTRIBUTING）+ `multica-ai`（含 README.zh） |
| 个人 + 团队两端通吃 | `affaan-m/everything-claude-code`（含 hooks + commitlint + ESLint，团队可直接接） |

### 9.3 按角色 / By persona

| 角色 / Role | 推荐组合 |
|---|---|
| 后端 / DevOps 工程师 | `obra/superpowers`（方法论）+ `addyosmani/agent-skills`（工程实践） |
| 前端 / 设计师 | `nextlevelbuilder/ui-ux-pro-max-skill`（组件级）+ `nexu-io/open-design`（设计系统） |
| **Vercel / Next.js / React 工程师** | **`vercel-labs/agent-skills`（官方部署 + 40+ React 性能规则）** |
| 营销 / 增长 | `coreyhaines31/marketingskills` |
| 研究 / 知识工作者 | `kepano/obsidian-skills` + `anthropics/skills`（doc-coauthoring 等官方 skill） |
| AI 工具 / Skill 构建者 | `anthropics/skills`（规范）+ `affaan-m/everything-claude-code`（参考实现） |
| 试水（5 分钟内引入） | `multica-ai/andrej-karpathy-skills`（单文件 drop-in） |

## 10. 底层哲学 · 有效性策略 · 长期迭代 / Philosophy, Validity, Iteration

> **用户问题**：每个 repo 的作者哲学是什么？他们怎么保证 skills 有效？参考 [Anthropic 提出的双轴](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)：
> 1. **Output quality** — 当 skill 激活时，它能给出好答案吗？
> 2. **Trigger precision** — Claude 在该激活的时候才激活，且**只**在该时候激活吗？
>
> 以及：长期迭代怎么决定 *add vs remove*？

本节基于对 13 个 repo 的 README / AGENTS.md / CLAUDE.md / CONTRIBUTING / 抽样 SKILL.md 的代码考古。

### 10.1 "什么是 skill"——五种范式 / Five paradigms of "what a skill IS"

| 范式 / Paradigm | 代表 repo | 关键信条 |
|---|---|---|
| **强制工作流 / Mandatory workflow** | `obra/superpowers` (O), `addyosmani/agent-skills` (AD) | "If a task matches a skill, you MUST invoke it" — 硬门 (hard-gates) 阻止 agent 跳步；O 的 TDD skill 直接说 _"NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"_ |
| **可选 reference / Optional reference** | `anthropics/skills` (A), `openai/skills` (OAI), `affaan-m/everything-claude-code` (AM), `mattpocock/skills` (M), `kepano/obsidian-skills` (K) | "Skills are tools Claude can **choose** to use when they're relevant" — 提供能力，不强制激活；OAI 三层 `.system / .curated / .experimental` 让用户自选 |
| **可组合 artifact / Composable artifact** | `nexu-io/open-design` (NX) | Skills + Design Systems + Craft 模块构成"分层能力栈"；每个 skill 答"产出什么"，design system 答"长什么样" |
| **领域专家工作流 / Domain expert workflow** | `coreyhaines31/marketingskills` (CH), `vercel-labs/agent-skills` (V), `nextlevelbuilder/ui-ux-pro-max-skill` (NL) | Skill = 装好的领域决策树（CH：marketing CRO/SEO 框架；V：React 40+ 规则按 Impact 排序；NL：CSV-backed BM25 推理引擎） |
| **行为指令 / Behavioral directive** | `multica-ai/andrej-karpathy-skills` (MA) | 不存在"激活时机"——4 条 Karpathy 原则永远在场（Don't assume / Simplicity first / Surgical changes / Goal-driven） |
| **聚合索引 / Aggregated index** | `ComposioHQ/awesome-claude-skills` (C) | Awesome-list-style 治理；PR 审核员判断"真实使用 / 测过 / 有归属"，准入即生效 |

### 10.2 Output Quality 策略 / How they ensure good answers when skill is active

| Repo | 主策略 | 引用 / 来源 |
|---|---|---|
| **O** | **PR 需提供 eval evidence**：必须提交"在 'Let's make a react todo list' 输入下，brainstorming skill 自动触发"的 transcript；~94% PR 拒绝率 | `CONTRIBUTING.md`：reject "compliance changes without eval evidence" |
| **AD** | **Skill 体内强制结构**：Verification 段 + 退出标准 + Red Flags 表 + Common Rationalizations 段；CONTRIBUTING 强制四原则（Specific / Verifiable / Battle-tested / Minimal） | `docs/skill-anatomy.md`；`CONTRIBUTING.md` "Don't add skills that are vague advice" |
| **AM** | **结构 + 周边资源**：每个 SKILL.md 必含 "When to Activate" + 代码示例 + 反模式段 + 跨平台映射；scripts/ 与 references/ 实现 progressive context loading | `CONTRIBUTING.md` "Skill Development Guide"；500 行上限 |
| **NX** | **每个 skill 独立 checklist**：P0/P1/P2 gates 写进 `references/checklist.md`；"诚实规则"如 release-notes skill 要求写 "None" 而不是编造；live-artifact 预览验证后才输出 | 各 skill 的 references/ 目录 |
| **NL** | **CSV 驱动推理**：BM25 排序 + 161 条 industry-specific 决策规则 + 20+ 项 pre-delivery checklist（对比度 ≥4.5:1、cursor-pointer、hover 150–300ms 等） | `src/ui-ux-pro-max/data/*.csv`；README §"Pre-delivery checklist" |
| **CH** | **`validate-skills.sh` 自动化**：检查 frontmatter、500 行硬限、trigger phrase 存在性、related-skill 引用；CONTRIBUTING 含 "Skill Quality Checklist" | `validate-skills.sh`；`CONTRIBUTING.md` |
| **V** | **优先级矩阵 + 单条规则文件**：rules/ 下每条规则独立 `Explanation / Incorrect Example / Correct Example / Context`；`web-design-guidelines` 用 `WebFetch` 取最新规则避免 vendored 过期 | `skills/react-best-practices/rules/`；`skills/web-design-guidelines/SKILL.md` |
| **A** | **官方 spec + 模板**：`template/SKILL.md` 演示最小 frontmatter；progressive disclosure（metadata always / SKILL.md body when triggered / bundled resources unlimited） | `template/`；agentskills.io spec |
| **OAI** | **Degrees of Freedom 设计**：高自由度文字 / 中自由度伪代码 / 低自由度具体脚本；"Context window is a public good"——大型 reference 必须含 TOC + grep pattern | `.system/skill-creator/SKILL.md` |
| **M** | **反失败模式**：每个 skill 对应一种 agent 失败（/grill-me 修对齐、/diagnose 修反馈循环、/tdd 修测试）；CONTEXT.md + ADR 让 skill 接地项目术语 | README "Why These Skills Exist" |
| **K** | **specification completeness**：每个 skill 含 `references/*.md` 完整覆盖一个 Obsidian 格式（properties / embeds / callouts），让 agent 按需 load | `skills/obsidian-markdown/references/` |
| **MA** | **四条负向原则**：Don't assume / Simplicity first / Surgical changes / Goal-driven；README "How to Know It's Working" 给元判据（diff 变小、rewrites 变少） | `CLAUDE.md`；README |
| **C** | **PR 真实性证明**：必须 "based on a real use case, not hypothetical"；must "be tested across Claude.ai, Claude Code, and API"；归属可考 | `CONTRIBUTING.md` |

### 10.3 Trigger Precision 策略 / How they ensure correct activation

| Repo | 主策略 | 典型做法 |
|---|---|---|
| **CH** | **穷举枚举**：单个 skill description 内列 15+ trigger phrase 变体（"CRO" / "conversion rate optimization" / "this page isn't converting" / "bounce rate is too high" ...） | `page-cro` skill description |
| **NL** | **超大 description**：200+ phrase / project / element / topic 词集中在一个 description 里（actions × projects × elements × topics） | `SKILL.md` frontmatter `description` 字段 |
| **NX** | **frontmatter `triggers:` 数组**：4-6 个变体；额外用 `od:mode / od:scenario` 扩展字段区分意图（prototype vs workflow） | `od:` frontmatter |
| **AD** | **正 + 负边界**：每个 skill 含 "Use when" 段 + 显式 "When NOT to use"（如 "Single-line fixes, typo corrections" 排除假阳性）；AGENTS.md 写"intent → skill"映射 | `skill-anatomy.md` §Frontmatter |
| **O** | **prescriptive 命令式**：description 直接写 _"You MUST use this before any creative work"_、_"Use when implementing any feature or bugfix, before writing implementation code"_ | brainstorming / TDD skills |
| **V** | **"Use when:" 段 + 任务条件**：description 含触发短语（"Deploy my app"）+ 任务类型（"when asked to review UI code for Web Interface Guidelines compliance"） | 各 skill SKILL.md |
| **K** | **明确格式术语**：description 内嵌特定 Obsidian 术语（"wikilinks" / "callouts" / "properties"），让 agent 按词触发 | `obsidian-markdown` description |
| **M** | **多面 description**：触发场景 × 用户口头表达组合（如 /tdd："Use when user wants to build features or fix bugs using TDD, mentions 'red-green-refactor', wants integration tests, or asks for test-first development"） | 各 skill description |
| **AM** | **"When to Activate" 段**：每个 skill 必含此段；description 同时说明"做什么" + "什么时候用"；related skills 链接引导上下文级联激活 | `docs/SKILL-DEVELOPMENT-GUIDE.md` |
| **A / OAI** | **极简精准**："Default assumption: Codex is already very smart"——description 只写 name + 关键场景，相信模型能根据用户意图判断 | `template/SKILL.md` |
| **C** | **问题陈述式**：1-2 句聚焦"解决什么问题"而非穷举词；分类目录引导发现（Business & Marketing / Communication & Writing 等） | README §Categorization |
| **MA** | **隐式 / 全局触发**：CLAUDE.md 安装后对所有 coding 工作生效，无 fine-grained 触发 | 单文件 design |

### 10.4 长期迭代 / Add vs Remove

| Repo | 加入门槛 | 退出 / 弃用机制 |
|---|---|---|
| **O** | ⛔ 最严：~94% PR 拒绝；要求 eval evidence + 单一问题单 PR + 真实人类 review 完整 diff | 未明文，但 CONTRIBUTING 拒绝 "compliance changes" |
| **AD** | CONTRIBUTING 四原则；vague advice 直接拒；新 skill 必须 reference 已有 skill 避免重复 | 未明文，加入后视为永久 |
| **AM** | "Skill Adaptation Policy"：copy 思想不 copy 产品标识；新 skill 单一领域、含示例、含反模式、可测 | 未明文 |
| **NX** | PR 对照 "Common rejection patterns"；design system 必过 5 点门槛（9 段齐全 / hex 来源可考 / 无 marketing 废话 / ASCII slug / 等） | CHANGELOG 累加（v0.6.0 = 136 PR），无 removal pattern |
| **NL** | npm CLI（`uipro-cli`）+ semver；变更走 CSV row addition；source-of-truth 是 `src/ui-ux-pro-max/`，symlinks 自动 sync | "持续数据增强"，无 skill 增删，只有 CSV 行变更 |
| **CH** | `validate-skills.sh` 自动 PR 验证；CONTRIBUTING 强制 PR 模板（new-skill.md / skill-update.md） + Skill Quality Checklist；version metadata | 未明文 deprecation，靠 fork / 选择性 install |
| **V** | AGENTS.md 强制：kebab-case 目录 / SKILL.md 必有 / scripts/ 必有 / .zip 打包 / **500 行上限** | 未明文，但 "End-User Installation" 文档区分稳定 vs 实验 |
| **A** | 无 CONTRIBUTING；strict 选 curated 例子；THIRD_PARTY_NOTICES.md 严格 license 审 | 无 retirement policy，"demonstration purposes only" |
| **OAI** | 12 行 CONTRIBUTING.md（"Be kind and inclusive"）；技术门槛低；skill-creator 含 eval scripts (`generate_review.py`, `eval-viewer`) | 三层 `.system / .curated / .experimental` ≈ stable / mature / preview 区分 |
| **M** | 无正式 CONTRIBUTING；通过 **目录隔离**：`engineering/ productivity/ misc/` 必须挂 README + plugin.json；`in-progress/ personal/ deprecated/` 不挂 | **目录 deprecated/ 保留历史但不推荐** — 优雅退役 |
| **K** | 无 CONTRIBUTING；指向 agentskills.io spec | 静态 reference，仅 Obsidian 出新语法时更新 |
| **MA** | 单文件，read-only | "These guidelines are designed to be merged"——不收外部 skill |
| **C** | PR 必须 "based on a real use case, not hypothetical" + 测过 Claude.ai/Claude Code/API + 归属可考 | 无 removal，靠归类（Business / Communication / ...） |

### 10.5 横切观察 / Cross-cutting insights

**三种哲学极**：

| 极点 | Repo | 立场 |
|---|---|---|
| 强制 (Enforce) | O, AD | "如果匹配，你 **必须** 用" |
| 可选 (Offer) | A, OAI, AM, M, K, V | "我提供能力，你自己选" |
| 行为指令 (Always-on) | MA | "这就是你写代码的方式" |

**两种 QA 模式**：

| 模式 | Repo | 工具 |
|---|---|---|
| 机械 / 自动化 | CH, O, V, NX, NL | shell script / eval transcript / 500 行硬限 / P0-P2 checklist / 20-test pre-delivery |
| 判断 / 人工审 | C, A, MA | PR reviewer 判断真实性 / 官方 curated / 永久原则 |

**触发策略光谱**：

```
高 recall ←——————————————————————————→ 高 precision
穷举枚举          正+负边界          精简 description
(CH / NL)         (AD)               (A / OAI)
```

CH/NL 的 200+ phrase enumeration 最大化 recall（不漏激活），但容易过度触发。A/OAI 的 minimal 描述则相信模型有判断力，对模型质量更敏感。AD 的 "Use when X / When NOT to use Y" 同时给正负边界，是当前最 balanced 的做法。

**迭代治理光谱**：

```
重门槛 ←————————————————————→ 轻治理
O / AD     CH / V     NX / NL      C       MA / K / OAI
eval req   validator  CHANGELOG    PR attest  ~no gate
```

**针对用户两个问题的最佳实践提炼**：

1. **Output Quality**：最严格的做法是 **"skill 体内塞结构"** + **"PR 时验证"** 双重保险。AD 的 Verification + Red Flags + Use When 段结构 + O 的 eval transcript 要求是组合拳。
2. **Trigger Precision**：**正+负边界**优于**纯穷举**。AD 的 "When NOT to use" 比 CH 的 15-phrase enumeration 更能压制假阳性。但 CH 的方法在 trigger 多变的领域（marketing 用户用各种口语描述需求）依然有效。

**长期 add/remove 的可参考决策**：

| 信号 | 暗示 | 行动 |
|---|---|---|
| 某 skill 没有 eval evidence | "可能从来不在该激活时激活" | **拒绝 / 移除** |
| 某 skill 描述触发词与现有 skill 重叠 | 假阳性 / 误触发 | **合并 or 加 "see X" boundary 句** |
| 某 skill body > 500 行 | 上下文成本高，可能稀释指令权重 | **拆分 / 移到 references/** |
| 某 skill 内容易过期（如 SDK 版本） | vendored 内容会腐烂 | **改 WebFetch 实时拉取**（V 的做法） |
| 某 skill 不能跨平台 | 仅 Claude 工作 | **降级到 `experimental/`**（OAI 三层模型） |
| 某 skill 长时间未触发 | 用户实际不需要 | **移到 `deprecated/`**（M 的目录隔离） |

> **结论**：13 个 repo 的对比揭示一个反直觉事实——**社区 stars 与 skill 治理严密度并不正相关**。最严格的 O（94% 拒绝率）和最宽松的 MA（单文件 read-only）都在 cohort 顶部；规模最大的 C（864 skills）的 D10 辅料密度反而最低（0.03）。"严"和"松"都可以做好，但 **不能"严-松混搭"** —— 装严格门槛但实际不审，是最差的状态。

---

_所有原始查询通过 `gh repo view --json` + 本地 `find` 完成；submodules 已 shallow 克隆至 `skills/<owner>__<repo>/`。复现脚本：见本仓库根目录 `.gitmodules` + 评分采用 rank-based 等权方法（见 §7）。§10 哲学考据基于 13 个 repo 的实际文档抽样。_

## 11. v1.2 Snapshot — 新增 D16-D19（social signals）+ GS + AA

### 11.1 新增维度

| Dim | 名字 | 测量 | 数据源 |
|---|---|---|---|
| **D16** | **Reddit Heat (30d)** | `posts + comments/10` 最近 30 天 | Reddit 公共 search.json API（`t=month`）|
| **D17** | **Reddit Sentiment (30d)** | 每帖平均 upvote score（最近 30 天）| 同上 |
| **D18** | **HN Heat (30d)** | `stories*10 + comments` 最近 30 天 | HN Algolia Search API（`numericFilters=created_at_i>UNIX_30D_AGO`）|
| **D19** | **HN Sentiment (30d)** | 每 story 平均 points | 同上 |

### 11.2 采样方法学 / Sampling methodology

- **查询策略**：每个 repo 用 2 个 query：`"<owner> <repo>"` 和 `"github.com/<owner>/<repo>"`，按 ID 去重后合并。
- **窗口**：自采样时刻 (2026-05-13T09:08 UTC) 向前 30 天。
- **采样工具**：`sample_social.py`（提交在 repo 根目录），用 stdlib `urllib.request`，无外部依赖；rate-limit politeness：Reddit 1.5s 间隔，HN 0.6s 间隔，每 repo 间 2s。
- **User-Agent**：`skill-obs/1.0`。

### 11.3 v1.2 完整排行（max 190）

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

### 11.4 关键 caveat / Caveats

1. **查询字符串污染**：query "anthropics skills" 会同时匹配该 repo 和 Anthropic 关于 "Skills" 功能的广义讨论。**D16/D17 的 A/OAI 数值含官方功能讨论的 spill-over，并非纯 repo 讨论**。
2. **GS / AA top Reddit avg_score 2769 / 2897 含发布期峰值**：launch wave 带来高 upvote，类似 NX D1 的早期峰值偏置。半年后真实热度可能稳态低很多。
3. **HN signal 稀疏**：14 个 repo 在 30 天内有 ≥1 HN story，其余 7 个为 0。AD 的 1 story 拿了 212 评论（一个 viral story）— HN D18/D19 容易被单次 viral 主导。
4. **bot / 重复内容**：Reddit 没有去 bot/cross-post 处理，"garry tan claude code" 这种 query 会匹配 user "garrytan" 的 self-promo 帖子。统计意义上代表"传播量"，不严格区分"自发讨论 vs 营销"。
5. **D16-D19 评分采用 rank-based 1-10**：与 D1-D15 相同方法，新增 4 维度但保持 cohort 内相对排名一致。

### 11.5 GS + AA 加入引发的连锁

- **GS** (avg SKILL.md 52,730 bytes) 显著超过 v1.1 D9 头部 NL (12,272 bytes)，把 NL 从 10 顶到 9。
- **AA** 的 222 agents (`.md` 而非 `SKILL.md`)（**注**：方法学上以 *.md 数量作为 skill volume 度量）+ 9 platforms (与 NX 并列顶部) + 18 个领域目录（含 game-dev）。
- 两个新 repo 都是 **D16/D17 顶部**（Reddit avg score 2769 / 2897 vs 第三名 A 的 151.7）— 显著拉开 social 维度的 spread。

> 想看完整 19-dim × 15-repo 染色矩阵：打开 `scoring.ipynb`（GitHub 直接渲染，无需执行）。

## 12. v1.3 Snapshot — 新增 D20-D21 (Task Decomposition + Lesson-Encoded Quality)

> **用户提出的两条理论**：
> 1. *"每个 repo 可能会拆分不同任务到每个具体的 skill，那么从理论上来讲每个具体任务的 skill 长度或者文字字数越小越好"* → **D20 Task Decomposition**
> 2. *"有价值的技能应包含——(1) 模型不知道的知识，(2) 特定环境的上下文信息，(3) 从真实失败中总结的教训"* → **D21 Lesson-Encoded Quality**

### 12.1 新增维度定义

| Dim | 名字 | 测量 | 假设 / 理论依据 |
|---|---|---|---|
| **D20** | **Task Decomposition** | rank-based 反转 `avg_skill_bytes` — 越小越好 | "每个 skill 应聚焦一个具体任务"；fat skills (>10KB) 意味着把多个任务捏成一个，触发精度差、上下文成本高 |
| **D21** | **Lesson-Encoded Quality** | rank-based `value_density_pct` — 越大越好；composite = 60% × lesson markers + 25% × version markers + 15% × context markers | 有价值的 skill 应承载 (1)+(2)+(3)；通过 keyword scan 估算 — lesson markers 主要捕捉 (3)，version 捕捉 (1)，context 捕捉 (2) |

### 12.2 D21 marker scan 方法学

`scan_lessons.py`（提交在 repo 根目录）扫描每个 submodule 的所有 `*.md`：

**Lesson markers (criterion #3 — 真实失败教训)**：
`anti-pattern`, `red flag`, `common mistake`, `common pitfall`, `common rationalization`, `when not to use`, `do not use`, `failure mode`, `pitfall`, `lessons learned`, `avoid this/the/using/over`, `don't do/use`, `wrong way`, `common failure/error`, `gotchas`, `caveats`, `hard-gate`, `why not`, `mistake`

**Version markers (criterion #1 — 模型未知知识 / 时间敏感信息)**：
`as of YYYY`, `since vN.N`, `api version`, `deprecated since`, version comparisons

**Context markers (criterion #2 — 环境特定上下文)**：
`export`, `process.env`, `${VAR}`, `~/.config`, `.env`, `localhost`, `127.0.0.1`, `/usr/local`, `/etc/`, `/opt/`

每个 repo 的输出：`lesson_pct`, `version_pct`, `context_pct`, `value_density_pct` (composite)。

### 12.3 D20 + D21 原始数据 + 评分

| Repo | avg_skill_bytes | D20 (反转) | lesson_pct | version_pct | context_pct | value_density_pct | D21 |
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

### 12.4 v1.3 完整排行（max 210）

| Rank | Repo | Score | Tier | Δ vs v1.2 |
|---:|---|---:|:---:|---:|
| 🥇 1 | **`garrytan/gstack`** | **156** | S | +9 (D9+D21 强 / D20 是代价) |
| 🥈 2 | `affaan-m/everything-claude-code` | 154 | S | +9 |
| 🥉 3 | `nexu-io/open-design` | 152 | S | +13 (D20=9 加分) |
| 4 | `obra/superpowers` | 150 | S | +13 |
| 5 | `msitarzewski/agency-agents` | 146 | S | +7 |
| 6 | `anthropics/skills` | 136 | A | +9 |
| 7 | `addyosmani/agent-skills` | 128 | A | +13 (D21=9 加大分) |
| 8 | `mattpocock/skills` | 114 | B | +10 (D20=9 / D21=1) |
| 9 | `openai/skills` | 113 | B | +12 |
| 10 | `ComposioHQ/awesome-claude-skills` | 111 | B | **+18** (D21=10 ⚠ 含 caveat) |
| 11 | `coreyhaines31/marketingskills` | 103 | B | +8 |
| 12 | `nextlevelbuilder/ui-ux-pro-max-skill` | 102 | B | +4 |
| 13 | `vercel-labs/agent-skills` | 101 | B | +10 |
| 14 | `multica-ai/andrej-karpathy-skills` | 92 | C | **+19** (D20+D21 双高) |
| 15 | `kepano/obsidian-skills` | 72 | D | +10 |

> 注：Tier 阈值随 max=210 重新校准：S+ ≥165, S ≥145, A ≥125, B ≥100, C ≥80, D <80。

### 12.5 关键 caveat / Caveats

1. **C 的 D21=10 (94.7%)**：值得高度警惕——ComposioHQ 是 864 SKILL.md 的 awesome-list，平均每个 SKILL.md 只有 3.4KB（多为短 stub）。94.7% 的 lesson-marker 命中可能是：(a) 短 description 里含 "common ..." / "avoid ..." 等关键词的零碎匹配，(b) 真实有意义的 lessons-learned。我**无法**单纯从 regex 判断；建议人工抽样 30 个 ComposioHQ SKILL.md 判断是真知识还是噪声。
2. **D21 的三个 sub-criterion 权重 (60/25/15)**：基于"lesson markers 比 version/context 更明确表示 'real-world value'"假设；可争议。如果给三者等权，C/OAI 的 ranking 会不同。
3. **D20 与 D9 (Skill Depth) 是负相关 / 直接冲突**：D9 假设"深 = substantive"，D20 假设"小 = 聚焦"。两个维度都给 GS 极端分数（D9=10, D20=1），所以 GS 总分 net 不变；但对于中段 repo (NL 12KB) 这是 -1 / -2 的差。**两者同时存在的意义**：评估视角的平衡——单看 D9 偏 "大而全"，单看 D20 偏 "小而精"。
4. **value_density_pct 跨 repo 不绝对可比**：repo A 有 5 个 SKILL.md，1 个含 anti-pattern → 20%；repo B 有 500 个 SKILL.md，100 个含 → 也是 20%。但 repo B 的 100 个反 anti-pattern 含量是 100 倍。**绝对量 vs 比例**没有单一最佳指标；这里用比例避免大 repo 自动赢。
5. **理论 vs 实测**：D20 的"小 = 好"是用户的*理论假设*。GS 的 52KB SKILL.md 实际是角色定义（CEO/Designer/QA 等），不是单任务实现。所以 GS D20=1 的"惩罚"反映的是**"角色式 fat skill 在分解层面的代价"**，但不否定 GS 内容质量本身（D21=8）。
6. **运行 caveat**：v1.2 D16-D19 caveats（query 污染 / launch wave / HN 稀疏）继续适用。

### 12.6 D20+D21 引发的 ranking 大变

**大幅上升**：
- **MA** +19：单文件 2.5KB（D20=10 满）+ Karpathy 4 条原则全是 anti-pattern 警示（D21=9）
- **C** +18：D21=10 但含强 caveat（可能是 awesome-list 噪声）
- **AD** +13：原本"Verifiable/Battle-tested"段就大量 Red Flags 内容
- **O** +13：原创方法论本来含 anti-pattern 教育
- **NX** +13：3.4KB 平均 + 13.3% value-density

**小幅 / 不变**：
- **NL** +4：D20=2 + D21=2 双低；UI/UX 文档侧重组件，少 lessons-learned 语料
- **NL** 仍排 12（虽 D9=9 在 v1.2/v1.3 都高）
- **M** +10 但 D21=1：mattpocock 用 /diagnose / /tdd 等名字而非"anti-pattern"等关键词，scan miss

**对 v1.3 排行的总体启示**：
- v1.0-v1.2 偏向 popularity + 工程化测量
- v1.3 引入 D20+D21 后，**"信号质量 / 教训密度"**成为新的差异化轴 — MA 凭 4 条 anti-pattern 原则就比 V (Vercel 官方) 拉到 92 vs 101（接近！）
- **GS 的 #1 不再纯靠 popularity**，而是 popularity + D9（最深）+ D21（rich lessons）的组合— 多维度 robust win

> 想看完整 21-dim × 15-repo 染色矩阵 + Δ v1.2→v1.3：打开 `scoring.ipynb`（GitHub 直接渲染，无需执行）。

## 13. v1.4 Snapshot — 新增 `juliusbrussee/caveman` (CV)

### 13.1 加入理由

CV 是个**单点 viral repo**：
- 概念：**"talk caveman, save tokens"** — 让 Claude 用 caveman 风格说话（短句、无虚词）减少 token 消耗 65%
- 数据：60,365 stars / 39 天 alive = **1,548 stars/day**（接近 NX 的 launch 峰值）
- 工程：很完整（bin/dist/commands/agents/plugins/evals/benchmarks/tests + 多 OS installer + Gemini extension）
- **填补"token efficiency / prompt minification"垂直** — 之前 cohort 没有这个角度

### 13.2 CV 21 维度评分

| Dim | Score | 备注 |
|---|---:|---|
| D1 Star Velocity | 9 | 1,548 stars/day（含 launch 峰值 caveat）|
| D2 Total Stars | 6 | 60k（M 之下 C 之上）|
| D3 Forks | 3 | 3,346（NX 之下 V 之上）|
| D4 Watchers | 2 | 141（最低段）|
| D5 Recency | 9 | 1 天前 push |
| D6 Cadence | 9 | 4.67 commits/day（仅次于 NX 42.5 和 AM 14.82）|
| D7 Contributors | 6 | 29 |
| D8 Skill Volume | 3 | 15 SKILL.md（小）|
| D9 Skill Depth | 2 | avg 3.3KB（小）|
| D10 Supp Material | 5 | 2.93 supp/skill |
| D11 Doc Quality | 8 | 224 README + AGENTS+CLAUDE+GEMINI+INSTALL+CONTRIBUTING+docs/ |
| D12 Eng Hygiene | 9 | benchmark/evals/tests + 多 OS installer + gemini-ext |
| **D13 Multi-Agent** | **10** | **9 平台（首个含 antigravity）** — 与 NX/AA 并列顶 |
| D14 Domain Breadth | 4 | 仅 prompt engineering 单一垂直 |
| D15 Originality | 8 | 独特的 caveman 概念 + 病毒式传播 |
| D16 Reddit Heat | 9 | 105 posts + 15705 comments |
| **D17 Reddit Sentiment** | **10** | **avg 788.8**（与 GS 2769 / AA 2897 同 top tier）|
| D18 HN Heat | 6 | 3 stories + 1 comment |
| D19 HN Sentiment | 6 | avg 3.0 |
| D20 Task Decomposition | 9 | avg 3.3KB（属于"小而精"档）|
| D21 Lesson-Encoded | 4 | 22% lesson + 0% version + 6.8% context = 14.2 density |
| **Σ Total** | **137** | **A 级，排 #6** |

### 13.3 v1.4 完整排行（max 210）

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

### 13.4 关键 caveat

1. **CV launch-wave 偏置**：1,548 stars/day 含发布期病毒峰值。**meme 类 repo** 衰减通常比"工具类" repo 更快；6 个月后稳态 velocity 估计降到 200-400 stars/day 量级，对应 D1 会跌到 4-5 分。
2. **CV 的 D14=4 是真实窄定位**：15 个 skill 全部围绕 "caveman talk" 这一个 prompt-style 优化 — 严格意义上是**单点 trick repo**，不是 framework。它的 #6 排位主要靠 D6/D13/D16/D17 拉动（active + 多平台 + 社交热度高）。
3. **CV 占用的细分 niche 独特**：cohort 中没有其他 prompt-engineering / token-efficiency 专项。这对实际用户的价值不一定按总分线性看 — 如果你 specifically 担心 token 成本，CV 是**唯一选项**。
4. **9 个平台首含 antigravity**：CV 是 cohort 中首个明确支持 antigravity 的 repo。如果用户走 antigravity 工作流，这是**独有 fit**。

### 13.5 与五模型评测（[附录 B](#agent-summary)）的对比

CV 太新（创建于 2026-04-04），**§1-§6 的 5 模型评测都在 v1.2 之前进行**，**没有涵盖 CV**。如果未来想做 v1.4 完整 LLM 复评，需要重新 prompt 5 个模型评 CV 的实战价值。当前 v1.4 #6 是**本仓库自评分**，不代表 5 模型共识。

> 想看完整 21-dim × 16-repo 染色矩阵 + Δ v1.3→v1.4：打开 `scoring.ipynb`（GitHub 直接渲染，无需执行）。

## 14. v1.5 Snapshot — 新增 5 repo (cohort 16 → 21)

v1.5 把 cohort 从 16 扩到 **21**，新增 5 个 repo：**UA** (`Egonex-AI/Understand-Anything`)、**OS** (`Fission-AI/OpenSpec`)、**CO** (`santifer/career-ops`)、**TS** (`Leonxlnx/taste-skill`)、**L30** (`mvanhorn/last30days-skill`)。本轮数据为真实采集，时间戳 **2026-06-17**（D1-D7 走 `gh` API，D8/D9/D13/D20 本地扫描，D21 `scan_lessons.py`，D18/D19 HN Algolia）。

> ⚠ **Reddit-403 caveat**：采集时 Reddit 公共 API 不可达（HTTP 403），**5 个新 repo 的 D16/D17 未测量，floored 到 1**（`raw_metrics` 记 `-1` sentinel）。既有 16 个 repo 保留 v1.4 的 Reddit 数据。因此新 repo 的总分在 social 两维上被低估，下面排名以"已采集维度"为准。

### 14.1 v1.5 完整排行（21 repos · max 210）

| Rank | Repo | Score | Tier |
|---:|---|---:|:---:|
| 🥇 1 | `garrytan/gstack` | 156 | S |
| 🥈 2 | `affaan-m/everything-claude-code` | 154 | S |
| 🥉 3 | `nexu-io/open-design` | 152 | S |
| 4 | `obra/superpowers` | 150 | S |
| 5 | `msitarzewski/agency-agents` | 146 | S |
| 6 | `juliusbrussee/caveman` | 137 | A |
| 7 | `anthropics/skills` | 136 | A |
| 8 | `addyosmani/agent-skills` | 128 | A |
| **9** | **`Egonex-AI/Understand-Anything`** 🆕 | **117** | B |
| 10 | `mattpocock/skills` | 114 | B |
| 11 | `openai/skills` | 113 | B |
| **12** | **`santifer/career-ops`** 🆕 | **113** | B |
| 13 | `ComposioHQ/awesome-claude-skills` | 111 | B |
| 14 | `coreyhaines31/marketingskills` | 103 | B |
| 15 | `nextlevelbuilder/ui-ux-pro-max-skill` | 102 | B |
| 16 | `vercel-labs/agent-skills` | 101 | B |
| **17** | **`mvanhorn/last30days-skill`** 🆕 | **98** | C |
| **18** | **`Fission-AI/OpenSpec`** 🆕 | **97** | C |
| 19 | `multica-ai/andrej-karpathy-skills` | 92 | C |
| **20** | **`Leonxlnx/taste-skill`** 🆕 | **84** | C |
| 21 | `kepano/obsidian-skills` | 72 | D |

> 5 个新 repo 直接插进中段（#9 / #12 / #17 / #18 / #20）；top-8 与 v1.4 完全一致，扩 cohort 没有动摇头部结论。Tier 阈值沿用 §12.4 校准（S ≥145, A ≥125, B ≥100, C ≥80, D <80）。

### 14.2 新晋 5 repo 画像 / Profiles of the 5 newcomers

**UA — `Egonex-AI/Understand-Anything`（#9, B, 117）**：一句话 = **把代码库变成交互式知识图谱**。62,155 stars / 5,129 forks / 200 watchers / 43 contribs，2026-03-15 创建、2026-06-16 push，94 天 alive，**661 stars/day**、6.05 commits/day。8 个 SKILL.md、平均 ~10KB、lesson 14.2%。强项：D5=10（最近 push）+ D6=9（活跃）+ D12=9（工程化）+ D13=8（多平台）+ D15=8（原创代码理解工具）；弱项 D8=2（skill 量少）。领域偏代码理解 / 开发工具，相对通用。社区热度（stars/day 661 + 高活跃）是它进 B 级前段的主要拉力。

**CO — `santifer/career-ops`（#12, B, 113）**：一句话 = **求职 / 简历自动化（CV / ATS / tracking）**。54,306 stars / **10,774 forks**（新晋最高 fork）/ 207 watchers / 93 contribs，2026-04-04 创建、2026-06-16 push，74 天 alive，**734 stars/day**（5 个新 repo 最高 velocity）、4.41 commits/day。4 个 SKILL.md、平均 ~4KB、110 份 docs（含 13 语言 README）、lesson 12.3%。强项：**D12=10（cohort 最强工程化）** + D5=10 + D11=9（13 语言 i18n）+ D7=8 + D3=7（10.7k forks 体现真实复制）；弱项 D14=3（垂直）+ D8=2。领域是求职 / 职业，属 niche，但工程化 + i18n 把它顶进 B 级。

**L30 — `mvanhorn/last30days-skill`（#17, C, 98）**：一句话 = **近 30 天趋势研究（Reddit / X / YouTube / HN / web）**。43,681 stars / 3,592 forks / 153 watchers / 48 contribs，2026-01-23 创建、2026-06-17 push，145 天 alive，**301 stars/day**、4.37 commits/day。只有 1 个 SKILL.md 但 **140KB（全 cohort 单文件最深）**、lesson 14.3%。强项：**D9=10（最深 skill）** + D5=10 + D6=8 + D7=7；弱项 D8=1（单 skill）+ **D20=1（巨型单技能 = 任务分解最差）**。领域是趋势研究 niche。它是 D9（深度）与 D20（分解）冲突的又一个极端案例——单个 140KB skill 把"研究全流程"塞进一个文件。

**OS — `Fission-AI/OpenSpec`（#18, C, 97）**：一句话 = **spec-driven 开发工作流**。55,241 stars / 3,866 forks / 245 watchers / 60 contribs，2025-08-05 创建（5 个新 repo 中最老）、2026-06-13 push，316 天 alive，**175 stars/day**、1.91 commits/day。**0 个 SKILL.md**（它是 spec 工具而非 skill 集）、517 份 docs、lesson 5.8%。强项：D7=8 + D10=8（辅料密度）+ D12=9（工程化）+ D15=8（原创方法论）；弱项 D8=1（无 SKILL.md）+ D9=1（无 skill 深度可测）+ D21=3。领域是 spec 驱动开发方法论，较通用。它是 cohort 里少见的"非 SKILL.md 形态"项目，D8/D9 天然吃亏，但凭 docs 密度 + 方法论原创性站住 C 级。

**TS — `Leonxlnx/taste-skill`（#20, C, 84）**：一句话 = **设计"品味"技能，避免通用输出**。45,534 stars / 3,169 forks / 132 watchers / **仅 6 contribs**，2026-02-19 创建、2026-06-12 push，118 天 alive，386 stars/day、**0.90 commits/day**（新晋最低）。13 个 SKILL.md、平均 23KB（深）、**lesson 41.4%（新晋最高 value-density）**。强项：**D21=9（教训密度新晋最高）** + D9=9（深）+ D15=7；弱项 **D7=2（仅 6 贡献者）** + D13=1（单平台）。领域是设计品味 / 美学，niche 但跨领域可用。它靠 D21/D9 的内容质量撑分，但贡献者极少 + 平台不可移植把总分压到 C 级底部（84，仅高于 D 线 4 分）——是"内容好但工程/生态薄"的典型。

### 14.3 数据来源与局限 / Data sources & caveats

- **数据源**：D1-D7 走 `gh` repo API（stars/forks/watchers/contribs/created/pushed 等）；D8/D9/D13/D20 本地扫描 submodule（SKILL.md 计数 + 平均字节 + 平台关键词 + 反转字节）；D21 `scan_lessons.py`（lesson/version/context marker → value-density）；D18/D19 HN Algolia Search API。
- **⚠ Reddit-403**：采集时 Reddit 公共 API 返回 HTTP 403，**5 个新 repo 的 D16/D17 未能测量，floored 到 1**，`raw_metrics` 用 `-1` sentinel 标记。既有 16 个 repo 仍沿用 v1.4 的 Reddit 数据，未重采。因此新 repo 与既有 repo 在 social 两维上**口径不完全一致**，新 repo 的总分对 D16/D17 是保守低估。
- **沿用既往 caveat**：v1.2 的 query 污染 / launch-wave / HN 稀疏，以及 v1.3 的 D20-vs-D9 冲突、value_density 跨 repo 不绝对可比，均继续适用。L30 (D9=10/D20=1) 与 TS (D9=9 + D21=9 但 D7=2) 是本轮最能体现这些 trade-off 的样本。

> 想看完整 21-dim × 21-repo 染色矩阵 + Δ v1.4→v1.5：打开 `scoring.ipynb`（GitHub 直接渲染，无需执行）。


---

<a id="task-guide"></a>

## 附录 A — Task → Repo 决策手册 / Task → Repo Decision Guide

> 🔄 **v1.2 同步 (2026-05-13)**：cohort 已扩到 **15 repos**，新增 `garrytan/gstack` (GS) 和 `msitarzewski/agency-agents` (AA)。详见 §1 末尾、§3.7、§5 推荐 stacks、§6 缺口更新。**AA 已填补 game-dev 缺口**（20 game-dev agents）。
>
> 🔄 **v1.5 同步 (2026-06-17)**：cohort 扩到 **21 repos**，新增 `Egonex-AI/Understand-Anything` (UA)、`Fission-AI/OpenSpec` (OS)、`santifer/career-ops` (CO)、`Leonxlnx/taste-skill` (TS)、`mvanhorn/last30days-skill` (L30)。**UA 填补"理解既有代码库"缺口，CO 填补"求职"缺口，OS 填补"spec-driven 开发"缺口。** 详见 §1 表末与 §6。

从 21 个 skill repo 的**功能正交**角度，给定具体 AI agent 任务，应该装哪个 repo（或哪个组合）？本手册覆盖：

- §1 — 13 个 repo 在功能版图上的位置
- §2 — **AM × O × NX 三大代表 repo 的 overlap / 正交 / 互补**（用户重点关注）
- §3 — 其他重要 overlap pair
- §4 — 任务 → 推荐 repo lookup（~50 个任务，覆盖 dev / AI / 设计 / 研究 / 内容 / 知识管理 / 数据等）
- §5 — 推荐 stacks（个人 / 团队 / 角色组合）
- §6 — 覆盖缺口（game / GPU kernel / Web3 / embedded 等 cohort 未覆盖领域）

---

### 1. 21 个 repo 的功能正交位置 / Functional positioning

| Code | Repo | 正交位置（独占价值轴）|
|---|---|---|
| **GS** 🆕 | `garrytan/gstack` | **Opinionated 角色 setup** — Garry Tan 实战 23 个角色 agent (CEO/Designer/Eng-Mgr/Release/Doc/QA)；avg SKILL.md 52KB 是 cohort 最深 |
| **AM** | `affaan-m/everything-claude-code` | **通用 agent harness** — 60 agents + 228 skills + commands + hooks + install 一站；breadth 之王 |
| **O**  | `obra/superpowers` | **工程方法论** — TDD / debug / brainstorm / plan / review 等元技能；depth 之王 |
| **NX** | `nexu-io/open-design` | **设计输出** — 19 skills + 71 design systems；多平台 (web/desktop/mobile/slides/PDF) creative production |
| **AA** 🆕 | `msitarzewski/agency-agents` | **个性化 multi-role agency** — 222 agents 跨 **18 个领域**（含 game-dev / spatial / academic / finance）；每个 agent 有 personality + emoji + vibe |
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
| **UA** 🆕 | `Egonex-AI/Understand-Anything` | **代码库理解 / 知识图谱** — 把既有 codebase 转成交互式知识图谱（节点/边/分层/导览）；填补"读懂 / onboard 既有大型代码库"缺口（cohort 此前各 repo 都偏"生产新代码"）；多平台 (claude/copilot/codex/opencode 等) |
| **OS** 🆕 | `Fission-AI/OpenSpec` | **Spec-driven 开发** — spec→tasks→实现 的规格驱动工作流（0 个 SKILL.md，是 spec 工具而非技能集；517 docs）；与 O 的 process 方法论互补但更偏"先写规格再实现" |
| **CO** 🆕 | `santifer/career-ops` | **求职 / 职业自动化** — 简历 / CV / ATS / 求职追踪垂直；cohort 全新领域；工程化极强 (D12=10)，13 语言 README |
| **TS** 🆕 | `Leonxlnx/taste-skill` | **设计品味 / 审美判断** — 引导 agent 避免"通用/平庸"输出；与 NX（设计系统**产出**）正交（NX 管产出什么，TS 管审美判断/品味）；lesson 密度 41.4% |
| **L30** 🆕 | `mvanhorn/last30days-skill` | **近期趋势研究** — 跨 Reddit/X/YouTube/HN/web 的近30天趋势；研究类新增；单个 140KB SKILL.md |

---

### 2. 三大代表 repo 横切对比 / AM × O × NX deep-dive

> 这是问得最多的对比 — 这三个都是 cohort 顶端（总分 129 / 115 / 110），但各占不同轴。

#### 2.1 核心定位

| | **AM** (everything-claude-code) | **O** (superpowers) | **NX** (open-design) |
|---|---|---|---|
| 核心定位 | 通用 agent harness（capability surface）| 工程方法论（process layer）| 设计输出（output layer）|
| 价值轴 | **广度** breadth | **深度** depth | **垂直** vertical |
| 回答的问题 | "我们都装什么 agents / skills / commands？" | "怎么工作才不出错？" | "怎么产出好看且一致的视觉？" |
| 内容主体 | 228 skills + 60 agents + commands + hooks | 14 高度精打磨的 skills（TDD / debug / plan / brainstorm 等）| 19 skills + 71 design systems |
| 装机时机 | 团队 base setup | 任意时刻（要求纪律时）| 需要产出 UI / 视觉时 |
| 强制度 | optional reference | **mandatory workflow**（hard gates）| optional reference |

#### 2.2 Overlaps（内容碰撞点）

| Pair | 碰撞区 | 具体内容 |
|---|---|---|
| AM ↔ O | **engineering methodology** | AM 含 reviewer/planner/python-reviewer 等 agents；O 含 TDD/debugging/planning skills。AM 是"装在 agent 里的"工程实践（commitlint/ESLint/CoC），O 是"写在 skill 里强制的"方法论 gates（HARD-GATE / eval evidence）|
| AM ↔ NX | **前端 / UI 边界** | AM 有些 frontend-design / UI 相关 skills；NX 是全局 design system。AM 偏 "实现"，NX 偏 "规范" |
| O ↔ NX | **几乎完全正交** | process layer 与 output layer 的关系；不太碰撞 |

#### 2.3 Orthogonality（正交，独立可叠加）

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

#### 2.4 Complementarity（推荐叠加用法）

| Stack | 适用场景 | 协同方式 |
|---|---|---|
| **AM + O** | 团队最佳基线 | AM 装满 capability 池；O 加 discipline gates。Agent 既有能力也有纪律。**最常见组合** |
| **AM + NX** | 全栈交付（工程 + 设计） | AM 处理 engineering 实现；NX 处理视觉/UI 产出 |
| **O + NX** | 设计师 + 想要 process 纪律 | O 的 brainstorming + writing-plans 指导设计决策；NX 产出 |
| **AM + O + NX** | 一站式 power user | 工程 + 方法 + 设计全配。⚠ 代价：上下文成本最高，agent 选择困难，需要 careful 配置 |

#### 2.5 何时只装其一

| 装哪个 | 场景 |
|---|---|
| **只装 AM** | 你想要 "一键全配"，不想自己挑组件。已有 harness 想升级 |
| **只装 O** | 你已有 setup 不想换，但想加 TDD/debug/plan **强制纪律层** |
| **只装 NX** | 你是设计师 / 营销人员，不需要 AM 的 60 agents 但想用 design systems |

---

### 3. 其他重要 overlap / Other notable overlap pairs

#### 3.1 A vs OAI — 两个官方 spec / Two official catalogs

| 共性 | 差异 |
|---|---|
| 都是平台官方 (Anthropic vs OpenAI) | A 服务 Claude，OAI 服务 Codex；A 含 PDF/theme/doc-coauthoring 等通用 reference skills，OAI 含 skill-creator + eval 工具 |

→ **互补**：用哪个看你的 host 平台。如果两个 agent 平台都用，一并装；spec 互相参考但实现独立。

#### 3.2 AM vs AD — 两个广义 engineering / Two broad-eng repos

| 共性 | 差异 |
|---|---|
| 都覆盖通用软件工程（API / 测试 / 性能 / 安全 / 重构 / 文档）| AM 是 **breadth + harness**（agents + commands + hooks）；AD 是 **depth + quality**（每个 skill 有 Verification + Red Flags 段，强制 4 原则 Specific/Verifiable/Battle-tested/Minimal）|

→ **互补 with overlap**：AM 用作团队基础，AD 用作 review/critique 时的 "质量门"。或选其一即可（重复度~50%）。

#### 3.3 NL vs NX — 两个 design / Two design repos

| 共性 | 差异 |
|---|---|
| 都做设计 | NL 是 **component-level UI/UX**（按钮 / 表单 / 调色板 / 字体 / 推理引擎）；NX 是 **system-level + multi-platform output**（71 design systems + slides/PDF/video/mobile） |

→ **互补**：
- 单平台 UI 组件级 → **NL**
- 跨平台创意产出 / 品牌系统 → **NX**
- 同时做组件 + 品牌 → 一起装

#### 3.4 M vs MA — 两个个人视角 / Two individual lenses

| 共性 | 差异 |
|---|---|
| 都是个人作者 | M 是 **lightweight composable techniques**（/diagnose / /tdd / /grill-me）反失败模式；MA 是 **always-on 4 条 Karpathy 原则** 单文件 |

→ **互补**：MA 装上是 base discipline；M 的 skills 按需触发。组合起来 = 个人开发者最轻量基线。

#### 3.5 C vs everyone — Awesome-list 与所有人的 overlap

C 是 awesome-list，**它和谁都 overlap**（因为它聚合所有人的 skills）。差别：
- C 的 SKILL.md 平均只有 3.4KB（vs O 的 8.2KB，AD 的 10.7KB）—— **broad but shallow**
- C 含 864 个 SKILL.md，是 cohort 中最大的"目录"但 D10 辅料密度仅 0.03（最低）

→ **何时用 C**：discovery / 浏览市场上有哪些 skill 形态。**不当主装**，可以挖到具体方向后转向对应的 specialist repo。

#### 3.7 AM vs GS — 两个 "全能型" 但哲学相反（v1.2 新增）

| 共性 | 差异 |
|---|---|
| 都是"团队 production 级"通用 harness | **AM = breadth + neutral**（228 skills + 60 agents，"装满 capability 池"）；**GS = depth + opinion**（51 skills，但平均 52KB，"Garry Tan 个人验证过的实战流程"）|

→ **选择决策**：
- 你的团队是 startup / 接受 strong opinion → **GS**（直接照搬 YC 大佬 setup）
- 你的团队是 enterprise / 需要 capability 多样性 → **AM**（自己组合 / 替换组件）
- 你想要 "AM 的广度 + GS 的深度" → 两者叠加，**AM 给 capability pool + GS 给 high-quality reference**

#### 3.8 AM vs AA — 两个 "大全包" 但维度不同（v1.2 新增）

| 共性 | 差异 |
|---|---|
| 都是大体量（AM 228 skills，AA 222 agents） | **AM = skill-centric**（每个 skill 解决一个能力）；**AA = role-centric + personality**（每个 agent 有 personality + emoji + vibe，按 *角色* 而非 *任务* 组织，18 个领域 vs AM 的工程领域为主）|

→ **选择决策**：
- 你要 "engineering capability 池" → **AM**
- 你要 "多角色 / 跨领域 agency" → **AA**（含 finance/academic/spatial-computing/game-dev 等 AM 不覆盖的领域）
- 同时用？— 可以，但 trigger 可能冲突，建议设置好优先级 / namespace

#### 3.6 V vs A vs OAI — 三个官方 / Three official authorities

| | A | OAI | V |
|---|---|---|---|
| 官方什么 | Claude Skills 规范 | Codex skill catalog | Vercel 部署 + React/Next.js |
| 范围 | 横向（任何领域） | 横向（任何领域） | 纵向（web frontend / Vercel-native） |
| 强项 | spec authority | 三层 .system/.curated/.experimental 治理模型 | live WebFetch 取最新 web 规则 |

→ **正交**：三者覆盖完全不同的官方域。V 与 A/OAI 没有 overlap，是 platform-specific authority。

---

#### 3.9 UA vs O vs OS — 三条"过程 / 理解"轴（v1.5 新增）

| | **UA** (Understand-Anything) | **O** (superpowers) | **OS** (OpenSpec) |
|---|---|---|---|
| 轴 | **理解既有代码**（读 / 映射 / onboard） | **怎么做**（TDD / debug / plan 方法论） | **规格优先地做**（spec → tasks → 实现） |
| 方向 | 向内：理解已有的东西 | 过程：实现时的纪律 | 向内→向外：先定义意图，再实现 |
| 产物 | 交互式知识图谱（节点/边/分层/导览） | 元技能（强制 gates） | 规格文档 + 任务拆解 |

→ **互补**：UA 在你动手前把陌生代码库映射清楚；OS 把"想做的改动"变成规格；O 在实现时强制纪律。UA 与 NX/CO 正交（处于生命周期不同阶段）。

---

### 4. 任务 → 推荐 repo lookup

> ✅ = primary（首选）· ➕ = secondary（次选 / 互补）· ⚠ = cohort 覆盖弱

#### 4.1 Web / 移动 / 系统开发 / Web · Mobile · Systems

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
| 9 | **Game 开发** (Web / Engine) | **AA ✅** (v1.2) | C 搜 | 🆕 **AA 有 20 个 game-development agents**（之前 cohort 完全无 game 专项，AA 加入后填补）|
| 10 | Web3 / Smart Contracts | ⚠ no specialist | C 搜 | ⚠ 同上 |
| 11 | 嵌入式 / Rust systems | M ✅ | MA ➕ | M 的 first-principles + MA 反 anti-pattern |

#### 4.2 AI / ML / Agent 建构 / AI · ML · Agent building

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

#### 4.3 工程方法论 / Engineering methodology

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
| 31a 🆕 | **理解 / onboard 既有代码库** | **UA ✅** | O ➕ | UA 把 codebase 转成交互式知识图谱（节点/边/分层/导览）；cohort 唯一专做"读懂既有代码" |
| 31b 🆕 | **Spec-driven 开发** (spec→实现) | **OS ✅** | O ➕ | OS 规格驱动工作流（spec→tasks→实现）；O 加方法论纪律 |

#### 4.4 研究 / 实验 / 评测 / Research · Experimentation

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
| 39a 🆕 | **近期趋势研究** (Reddit/X/YT/HN/web) | **L30 ✅** | C ➕ | L30 专做近 30 天跨平台趋势采集；C 搜索补充 |

#### 4.5 设计 / 创意 / Design · Creative

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
| 50a 🆕 | **审美判断 / 品味把关** | **TS ✅** | NX ➕ | TS 引导 agent 避免"通用/平庸"输出（NX 管产出什么，TS 管审美判断） |

#### 4.6 内容 / 营销 / Content · Marketing

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 51 | Copywriting | **CH ✅** | — | CH 唯一专项 |
| 52 | SEO | **CH ✅** | — | CH 唯一专项 |
| 53 | **CRO / Landing page** | CH ✅ | V ➕ | CH page-cro + V web-design-guidelines（设计 + 转化） |
| 54 | Email 营销 | CH ✅ | C ➕ | CH 专项 |
| 55 | 社交媒体 | CH ✅ | C ➕ | CH + C 含 slack/twitter |
| 56 | 内容研究 | C ✅ | CH ➕ | C 的 content-research-writer |
| 57 | Growth analytics | CH ✅ | — | CH 含 analytics skills |

#### 4.7 知识管理 / 笔记 / Knowledge management

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 58 | **Markdown / Obsidian** | **K ✅** | — | K 是 Obsidian creator 维护 |
| 59 | Knowledge graphs / JSON Canvas | K ✅ | — | K 含 Canvas skill |
| 60 | 个人笔记 | K ✅ | A ➕ | K Obsidian + A doc-coauthoring |
| 61 | Meeting notes | C ✅ | K ➕ | C meeting-insights-analyzer |
| 62 | Research synthesis | K ✅ | A ➕ | K 笔记 + A 输出 doc |

#### 4.8 生产力 / 沟通 / Productivity · Communication

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 63 | Email | C ✅ | — | C internal-comms |
| 64 | Slack / chat | C ✅ | — | C slack-gif-creator 等 |
| 65 | 项目管理 | **O ✅** | AM ➕ | O plan management + AM commands |
| 66 | Onboarding 文档 | A ✅ | AM ➕ | A doc-coauthoring（UA ➕ 可生成既有代码库的知识图谱辅助 onboarding） |
| 66a 🆕 | **求职 / 简历 / ATS / 求职追踪** | **CO ✅** | — | CO 求职自动化垂直（CV / ATS / tracking）；cohort 唯一专项 |

#### 4.9 数据 / 集成 / Data · Integration

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 67 | API 集成 (OAuth / REST / GraphQL) | C ✅ | AM ➕ | C 的 connect / connect-apps 系列 |
| 68 | 浏览器自动化 | C ✅ | — | C 含相关 skills |
| 69 | Web scraping | C ✅ | — | C 含相关 skills |
| 70 | 数据 ETL | AD ✅ | C ➕ | AD 通用工程；C 有零星 |

#### 4.10 元 / 通用 / Meta · General

| # | 任务 | 主推 | 次推 | 备注 |
|---:|---|---|---|---|
| 71 | **5 分钟快速 CLAUDE.md drop-in** | **MA ✅** | — | 单文件零负担 |
| 72 | 浏览 / 发现 skill 生态 | C ✅ | — | 864 SKILL.md 索引 |
| 73 | 学 SKILL.md 规范 | A ✅ | OAI ➕ | A 是官方权威 |
| 74 | 多 agent 平台兼容 | NX ✅ | NL ➕ V ➕ | NX 9 个平台覆盖最广 |
| 75 | 个人独立工程师 | M ✅ | MA ➕ | M lightweight + MA 反 anti-pattern |
| 76 | 团队 / 公司采用（通用 enterprise） | AM ✅ | AD ➕ O ➕ | AM 含 hooks/commitlint/CoC；AD 严质量门；O 强制方法论 |
| 77 | 🆕 **YC / 创业公司 opinionated setup** | **GS ✅** | AM ➕ | 🆕 v1.2 · Garry Tan 实战角色 setup — 直接照搬，不用挑组件 |
| 78 | 🆕 多角色 / 多领域 agency-as-agents | **AA ✅** | GS ➕ AM ➕ | 🆕 v1.2 · 222 agents 跨 18 领域（finance / academic / spatial-computing / game-dev 等小众） |
| 79 | 🆕 单 SKILL 深度模板（学怎么写"厚" SKILL.md）| **GS ✅** | NL ➕ | 🆕 v1.2 · GS 平均 SKILL.md 52KB 是 cohort 最深；NL 12KB 第二 |

---

### 5. 推荐 Stacks / Recommended combinations

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
| 🆕 **YC / Startup 创始团队 (照搬式)** | **GS** + 可选 O | GS 一键拿 Garry Tan 实战 setup；O 加方法论纪律 |
| 🆕 **跨领域工作室 / 多角色 agency** | **AA** + AM | AA 给 18 个领域的角色化 agent；AM 补 engineering harness |
| 🆕 **游戏开发** | **AA** + M | AA 含 20 game-dev agents（v1.2 唯一覆盖）；M 加工程严谨度 |
| 🆕 **想拿"最佳实例" SKILL.md 模板** | **GS** + A | GS 平均 52KB 是 cohort 最深 reference；A 是规范 |
| 🆕 **接手 / onboard 遗留代码库** | **UA** + O | 🆕 v1.5 · UA 把既有代码映射成知识图谱；O 在你改动前加纪律 |
| 🆕 **规格优先的产品团队** | **OS** + O + AM | 🆕 v1.5 · OS 定义 spec→tasks；O 加 gates；AM 提供实现所需的能力池 |
| 🆕 **求职者 / 职业自动化** | **CO** + A | 🆕 v1.5 · CO 处理简历 / ATS / 求职追踪；A 出精修文档 |

---

### 6. 覆盖缺口 / Coverage gaps（cohort 未覆盖领域）

21 个 repo **没有专项覆盖**的领域 — 这是未来 cohort 扩张的方向：

> ✅ **v1.2 已填补**：~~Game 开发~~ — **AA 含 20 个 game-development agents**
>
> ✅ **v1.5 已填补**：~~理解 / onboard 既有代码库~~ (**UA**)、~~Spec-driven 开发~~ (**OS**)、~~求职 / 职业自动化~~ (**CO**) — 此前 cohort 均无专项

| 缺口 / Gap | 当前最佳替代 | 建议 |
|---|---|---|
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

> **关键观察 (v1.5 更新)**：cohort 强在"agent 开发 + 设计 + web frontend + 营销 + 知识管理 + 多角色 agency (v1.2 AA) + game-dev (v1.2 AA) + **代码库理解 (v1.5 UA) + spec-driven 开发 (v1.5 OS) + 求职自动化 (v1.5 CO)**"；弱在"low-level systems / GPU / 多模态 ML / cloud IaC / 智能合约"。深 system / GPU / Web3 仍处自建阶段。

---

### 附录 / Appendix: 13 repo 的功能正交矩阵

> 简化 1-5 评分，每行表示该 repo 在该领域的覆盖强度。✅ ≥4，➕ ≥2，— = 不覆盖。

| 领域 \ Repo | AM | O | NX | A | NL | AD | CH | C | M | OAI | MA | K | V | **GS** 🆕 | **AA** 🆕 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 通用工程 | ✅ | ✅ | — | ➕ | — | ✅ | — | ➕ | ✅ | ✅ | ✅ | — | — | **✅** | ➕ |
| Web 前端 | ➕ | — | — | — | ➕ | ➕ | ➕ | ➕ | — | — | — | — | **✅** | ➕ | ➕ |
| UI/UX 设计 | — | — | **✅** | ➕ | **✅** | — | — | ➕ | — | — | — | — | ➕ | ➕ | ➕ |
| Design system / 品牌 | — | — | **✅** | ➕ | ➕ | — | ➕ | — | — | — | — | — | — | ➕ | ➕ |
| 方法论 (TDD/debug/plan) | ➕ | **✅** | — | ➕ | — | ➕ | — | ➕ | ➕ | ➕ | ✅ | — | — | ➕ | — |
| AI / Agent 建构 | **✅** | ➕ | — | ✅ | — | ➕ | — | ➕ | — | ✅ | ➕ | — | — | **✅** | **✅** |
| Skill 元开发 | ➕ | ➕ | — | **✅** | — | ➕ | ➕ | ➕ | — | **✅** | — | — | ➕ | ➕ | ➕ |
| 营销 / Growth | — | — | ➕ | — | — | — | **✅** | ➕ | — | — | — | — | ➕ | — | ➕ |
| 知识管理 | — | — | — | ➕ | — | — | — | — | — | — | — | **✅** | — | ➕ | ➕ |
| 文档输出 | ➕ | — | ➕ | ✅ | — | ➕ | ➕ | ➕ | — | — | — | ➕ | — | ✅ | ➕ |
| Performance / Optimization | ➕ | — | — | — | — | ✅ | — | — | ➕ | — | ➕ | — | **✅** | ➕ | — |
| Research / Eval | ➕ | **✅** | — | ➕ | — | ➕ | — | — | ✅ | — | ➕ | ➕ | — | ➕ | ➕ |
| Discovery / Browse | — | — | — | — | — | — | — | **✅** | — | — | — | — | — | — | ➕ |
| **Game 开发** 🆕 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **✅** |
| **多角色 agency (CEO/Designer/QA/etc)** 🆕 | ➕ | — | — | — | — | — | — | — | — | — | — | — | — | **✅** | **✅** |
| **跨领域 (academic/finance/spatial)** 🆕 | ➕ | — | — | — | — | — | — | ➕ | — | — | — | — | — | — | **✅** |

---

_本手册基于 §10 哲学考据 + 各 repo 实际文档抽样。任务列表参考 AI agent 实际使用场景，并尝试覆盖用户提到的 game / 前后端 / AI GPU / 研究 / 实验 / loop / 设计 / 品味探索 + 类似 30+ 类。覆盖缺口部分诚实标注 — 不强行推荐 cohort 不擅长的领域。_


---

<a id="agent-summary"></a>

## 附录 B — 五模型评测总结 / Five-Model Cross-Comparison

本文档收录了 5 个不同 AI 模型（Claude / ChatGPT / Gemini / Grok / Perplexity）独立评估本仓库 15 个 skill repos 后的对比总结。**这不是我自己产出的评分**（评分见 `EVALUATION.md`），而是把不同模型在面对同一份 cohort 数据时给出的判断做了横向汇总。

> ⏱️ **快照说明（v1.5 更新）**：本五模型对比基于 **15-repo cohort**（v1.3 时期）采集,**早于 v1.5 的 21-repo 扩容**（新增 UA/OS/CO/TS/L30）。这 5 个新 repo 未纳入本次跨模型评测;它们的本仓库自评分见 `EVALUATION.md §14`。重跑五模型对比是后续工作。

相关文档：
- 评分细节 → `EVALUATION.md` · [`scoring.ipynb`](./scoring.ipynb)
- 按任务选 repo → 附录 A

---

### TL;DR

**收敛后的最小可用组合**（5 模型交集）：

1. `anthropics/skills`（底座）
2. `obra/superpowers`（方法论）
3. `gstack` 或 `everything-claude-code`（实战，二选一）
4. 按需加 `nexu-io/open-design`（设计）、`vercel-labs/agent-skills`（Next.js）

要不要加 `karpathy-skills` / `addyosmani` / `mattpocock` 取决于具体技术栈，**不存在"必须加"的共识**。

---

### 1. 强共识（所有模型都认）

四个底层选择基本无争议：

| Repo | 角色 | 5 模型共识 |
|---|---|---|
| `anthropics/skills` | 规范/底座层 | 所有人都装 |
| `obra/superpowers` | 方法论层（TDD、subagent-driven） | 所有人都装 |
| `gstack` **OR** `everything-claude-code` | 实战层（二选一） | solo 选前者，团队/多 harness 选后者 |
| `nexu-io/open-design` | 设计扩展 | 在设计是瓶颈时加上 |

### 2. 强共识（所有模型都避）

| Repo | 原因 |
|---|---|
| `msitarzewski/agency-agents` | 222 个 personality agent 被一致定性为"**灵感库不是基础设施**"。ChatGPT 原话"不要把这类大而全的库当核心"；Claude 直接跳过；Gemini 警告 token 成本和延迟 |
| `openai/skills`（D1=1） | 垫底，全员共识跳过 |
| `kepano/obsidian-skills` | 只有 Obsidian 工作流才有意义 |

### 3. 主要分歧

#### 3.1 `multica-ai/andrej-karpathy-skills`

- **Claude / Gemini**：看到 D1=9 觉得是高价值叠加
- **ChatGPT**：当成"个人配置不适合主库"放 C 层
- **判断**：这个分歧来自定位差异 — 它是 **overlay，不是 standalone**

#### 3.2 `addyosmani/agent-skills`

- **ChatGPT**：列为 A 级必用
- **Grok / Claude**：没特别强调
- **差异点**：你是否做生产后端

#### 3.3 `ComposioHQ/awesome-claude-skills`

- **Grok**：推荐用作 **发现层**
- **其他人**：觉得 meta-list 深度不够，不属于工作流

#### 3.4 `mattpocock/skills`

- **全员同意**：只在 TypeScript 场景下用
- **ChatGPT**：评为 B 级"日常贴近"
- **Claude**：视作 **垂直工具**

#### 3.5 推荐方法本身（meta-level disagreement）

| 模型 | 推荐风格 |
|---|---|
| ChatGPT / Claude | 给完整 stack |
| Grok | 主张"最多 2-3 个测试" |
| Gemini | 不给推荐，反问你的场景 |

### 4. 独特视角 / 各家独门洞察

| 模型 | 独有视角 |
|---|---|
| **Claude** | 唯一做了 **`contribs < 20 = bus factor` 分析**（押人 vs 押社区），并警告整个生态不到一年**没经过真实生产检验** |
| **ChatGPT** | 唯一给出**严格的五层架构**：规范 → 方法论 → 实战 → 工程 → 垂直 |
| **Gemini** | 警告 **S 层锁定单一社区方法论**的风险 |
| **Grok** | 实操原则 **"fit > score"** |

### 5. 收敛后的最小可用组合（重述）

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

### 6. 注意

**Perplexity 这次没产出实际内容**（只输出了搜索过程）—— 这是它在 **长 prompt + 表格输入** 下经常出现的失败模式，**不是数据问题**。

---

### 与本仓库自评分的对比 / Comparison with our internal v1.3 scoring

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

_本总结收录自外部 5 个 LLM 的横向对比；具体评分方法学见 `EVALUATION.md` §2-§12。_

---

### 7. 补充：以"实战价值"视角的深度评测（单模型详细版）

> 不同于 §1-§6 的"5 模型横向交集"，本节是**另一个独立 LLM**从"实战价值"出发的详细分类 + 排名。
> 提供：分类学（系统型 / 官方标准型 / 垂直增强型 / 清单型）+ 5 步评价法 + 详细分档表 + 最终排名。
> 注：原文含若干外链 citation 经判断为 AI 生成的伪引用（target 与论点无对应），**已移除**以避免误导。

按**实战价值**而不是单纯星数看，这 15 个 skills set 里，真正有长期复用价值的主要分成 **4 类**：系统型、官方标准型、垂直增强型、清单型。

> **本视角核心结论**：S 档里最强的是 `gstack` 和 `open-design`，A 档里最稳的是 `anthropics/skills`，B 档里最值得按场景选的是 `openai/skills`、`vercel-labs/agent-skills`、`mattpocock/skills`。

#### 7.1 评价 5 步法

1. 先看"**这是不是一个系统**"，不是看星数；能不能覆盖从规划、实现、评审、测试到交付，决定上限。
2. 再看"**是不是官方或接近标准**"；官方仓库通常更适合作为底座，社区仓库更适合做加速层。
3. 再看"**是不是垂直专精**"；设计、前端、营销、开发体验这类 repo，往往单点强，但不适合拿来当总框架。
4. 最后才看本仓库的指标；`Total` 决定综合质量，`D1` 决定第一印象，`Stars/day` 看热度，`Forks/Contribs` 看生态深度。
5. 所以最重要的问题不是"谁最火"，而是"**你要拿它做操作系统、模板库，还是灵感库**"。

#### 7.2 分档判断

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

#### 7.3 重点评价

1. **`gstack`**：如果你要的是"AI 软件工厂"，它最像完整产品而不是 skill 样例；仓库把自己定义成 23 个 specialist 加 8 个 power tools，并把流程组织成从思考、规划、构建、评审、测试到交付的完整链路。
2. `gstack` 的问题也正因为它太完整：强依赖作者的方法论、命令体系和工作节奏，小团队上手会快，大团队统一采用会有治理成本。
3. **`anthropics/skills`**：这是最适合拿来当"官方基线"的仓库；它明确是 Claude skills 的公开实现和示例库，包含 spec、template、不同类别的示例技能，还特别说明很多内容主要用于演示和教育。
4. `anthropics/skills` 的缺点是：它更像"标准参考 + 样例仓库"，不是帮你直接跑完整研发流程的操作系统。
5. **`openai/skills`**：价值在于官方抽象清晰，定位是 Codex 的 skills catalog，并把 skills 定义成可发现、可组合的自包含文件夹。
6. `openai/skills` 的缺点是生态信号和 Claude 兼容心智都不如 Anthropic 这边强，所以更适合借鉴结构，不适合直接拿来当 Claude 主框架。

#### 7.4 推荐选择

1. 如果你要一个"**主工作流**"，选 `gstack`；它最像可直接投入实战的系统。
2. 如果你要一个"**标准底座**"，选 `anthropics/skills`；它最像官方规范、示例和模板库。
3. 如果你是**设计驱动产品**，额外叠加 `open-design` 或 `ui-ux-pro-max-skill`。
4. 如果你是 **Next.js / Vercel 团队**，叠加 `vercel-labs/agent-skills`。
5. 如果你是**多模型团队**，保留 `openai/skills` 作为兼容层思路，而不是唯一来源。

#### 7.5 最终排名（按"长期可用性"）

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

#### 7.6 §7 与 §1-§6 的对比

| 视角 | §1-§6 (5-LLM 横向交集) | §7 (单 LLM 实战价值视角) |
|---|---|---|
| 推荐 #1 实战层 | `gstack` 或 `everything-claude-code` | **`gstack` 一票**（ECC 跌到 #9）|
| 推荐 #1 底座 | `anthropics/skills` | 一致 |
| `obra/superpowers` 定位 | 必装方法论层 | **降至 #8 "增强层"** |
| `everything-claude-code` 定位 | 实战层备选 | **#9 "资源中枢，不一定系统"** |
| `addyosmani` | 分歧 | **#4 工程增强包**（明确推荐工程团队）|
| **最大分歧点** | obra & ECC 是否核心层 | §7 认为只有 gstack 是核心系统，其他都是辅助 |

**判读**：§7 的"系统主义"视角比 §1-§6 的"合议式"视角更**自信地把 gstack 定为唯一主工作流**；§1-§6 倾向"obra 必装"作为方法论强制层，§7 把 obra 降级。这本身就是一个有意思的元数据 —— 不同 LLM 对"什么算 production-ready 框架"的标准本身有分歧。
