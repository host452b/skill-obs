# Skill Repo 评测报告 / Skill Collection Evaluation

> 🌐 **Language**: **🇨🇳 中文** · [🇬🇧 English](./EVALUATION.en.md)

> 评测日期 / Date: **2026-05-13**  
> 评测对象 / Cohort: 12 个 Agent Skills / Claude Skills / 类 Skills 仓库（作为本 repo 的 git submodule）  
> 评分量表 / Scale: **1–10** (10 = best in cohort)  
> 总分上限 / Max total: **150** (15 dims × 10)

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
| OAI| [`openai/skills`](https://github.com/openai/skills) | 18,982 | 1,259 | 2025-11-25 | 2026-05-12 | Codex skills catalog |

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

## 4. 评分总表 / Score Matrix

```
列顺序：AM | O | NX | A | NL | AD | CH | C | M | OAI | MA | K
```

| Dim | Description | AM | O | NX | A | NL | AD | CH | C | M | OAI | MA | K |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| D1  | Star Velocity ⭐ | 9 | 8 | **10** | 6 | 5 | 5 | 3 | 4 | 7 | 1 | 9 | 2 |
| D2  | Total Stars | 9 | **10** | 4 | 9 | 7 | 4 | 2 | 5 | 6 | 1 | 8 | 3 |
| D3  | Forks | **10** | 9 | 3 | 8 | 6 | 4 | 4 | 5 | 5 | 1 | 7 | 2 |
| D4  | Watchers | **10** | 8 | 2 | 9 | 5 | 3 | 4 | 5 | 6 | 1 | 7 | 2 |
| D5  | Commit Recency | **10** | **10** | **10** | 8 | 2 | 8 | 6 | 7 | 9 | 9 | 4 | 7 |
| D6  | Commit Cadence | 9 | 7 | **10** | 1 | 6 | 7 | 8 | 3 | 5 | 4 | 2 | 3 |
| D7  | Contributors | 9 | 7 | **10** | 3 | 6 | 4 | 4 | 5 | 1 | 8 | 2 | 3 |
| D8  | Skill Volume | 9 | 3 | 8 | 3 | 2 | 4 | 6 | **10** | 5 | 7 | 1 | 1 |
| D9  | Skill Depth | 6 | 5 | 3 | 9 | **10** | 8 | 9 | 3 | 2 | 7 | 1 | 4 |
| D10 | Supp. Material Density | 5 | 7 | 4 | 7 | 9 | 3 | 7 | 1 | 2 | **10** | 8 | 2 |
| D11 | Doc Quality | **10** | 8 | **10** | 6 | 9 | 9 | 8 | 8 | 7 | 3 | 7 | 4 |
| D12 | Eng. Hygiene | **10** | 9 | **10** | 6 | 8 | 8 | 9 | 4 | 6 | 3 | 3 | 3 |
| D13 | Multi-Agent Portability | 8 | 7 | **10** | 1 | 9 | 8 | 6 | 8 | 2 | 1 | 2 | 4 |
| D14 | Domain Breadth | **10** | 9 | 8 | 8 | 4 | 8 | 4 | 9 | 6 | 7 | 1 | 3 |
| D15 | Originality / Authority | 5 | 9 | 8 | **10** | 6 | 7 | 6 | 3 | 7 | **10** | 8 | 7 |
| **Σ** | **Total (out of 150)** | **129** | **116** | **110** | **94** | **94** | **90** | **86** | **80** | **76** | **73** | **70** | **50** |

## 5. 总排行 / Overall Ranking

### 5.1 等权 / Equal-weighted (default)

| Rank | Repo | Score | Tier |
|---:|---|---:|---|
| 🥇 1 | `affaan-m/everything-claude-code` | **129** | S |
| 🥈 2 | `obra/superpowers` | 116 | S |
| 🥉 3 | `nexu-io/open-design` | 110 | S |
| 4 | `anthropics/skills` | 94 | A |
| 4 | `nextlevelbuilder/ui-ux-pro-max-skill` | 94 | A |
| 6 | `addyosmani/agent-skills` | 90 | A |
| 7 | `coreyhaines31/marketingskills` | 86 | A |
| 8 | `ComposioHQ/awesome-claude-skills` | 80 | B |
| 9 | `mattpocock/skills` | 76 | B |
| 10 | `openai/skills` | 73 | B |
| 11 | `multica-ai/andrej-karpathy-skills` | 70 | B |
| 12 | `kepano/obsidian-skills` | 50 | C |

### 5.2 D1 加权 ×3 / Velocity-emphasized ranking

如果按用户强调的 D1（star velocity）加权 ×3（其他维度仍 ×1）：

| Rank | Repo | Adj. Score |
|---:|---|---:|
| 🥇 1 | `affaan-m/everything-claude-code` | 147 |
| 🥈 2 | `obra/superpowers` | 132 |
| 🥉 3 | `nexu-io/open-design` | 130 |
| 4 | `anthropics/skills` | 106 |
| 5 | `nextlevelbuilder/ui-ux-pro-max-skill` | 104 |
| 6 | `addyosmani/agent-skills` | 100 |
| 7 | `coreyhaines31/marketingskills` | 92 |
| 8 | `mattpocock/skills` | 90 |
| 9 | `ComposioHQ/awesome-claude-skills` | 88 |
| 9 | `multica-ai/andrej-karpathy-skills` | 88 |
| 11 | `openai/skills` | 75 |
| 12 | `kepano/obsidian-skills` | 54 |

> 加权后 Top-3 不变，中段排序有所交换；说明 velocity 维度对结论稳健。

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
| **openai/skills** (B) | 官方 Codex skill catalog | ✅ 辅料密度最高（D10=10）+ 原创权威；⚠ 仅 Codex、社区小 |
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
| 营销 / 增长 | `coreyhaines31/marketingskills` |
| 研究 / 知识工作者 | `kepano/obsidian-skills` + `anthropics/skills`（doc-coauthoring 等官方 skill） |
| AI 工具 / Skill 构建者 | `anthropics/skills`（规范）+ `affaan-m/everything-claude-code`（参考实现） |
| 试水（5 分钟内引入） | `multica-ai/andrej-karpathy-skills`（单文件 drop-in） |

---

_所有原始查询通过 `gh repo view --json` + 本地 `find` 完成；submodules 已 shallow 克隆至 `skills/<owner>__<repo>/`。复现脚本：见本仓库根目录 `.gitmodules` + 评分采用 rank-based 等权方法（见 §7）。_
