"""
Rebuild `scoring.ipynb` with pre-baked HTML outputs (GitHub-renderable).

Pattern (mirrors gguf_exp_on_mac/benchmark_visualization.ipynb):
  - Each code cell source is a one-line `# Title` comment.
  - outputs[0].data['text/html'] holds a pre-rendered colored table.
  - GitHub renders the notebook directly — no kernel, no execution needed.

Emits BOTH scoring.ipynb (English) and scoring.cn.ipynb (Chinese) from the
same data — UI strings come from the TXT i18n table; repo data is shared.

Maintenance flow:
  1. Edit EVALUATIONS below (append a new dict; never modify history).
  2. python3 build_scoring_notebook.py   # regenerates scoring.ipynb + scoring.cn.ipynb
  3. git add scoring.ipynb scoring.cn.ipynb build_scoring_notebook.py && git commit && git push

Color interpolation: rgba(220,60,60,0.35) worst → rgba(220,220,60,0.35) mid → rgba(40,200,100,0.35) best.
Per-column min/max normalization; column-best is bolded.
"""
from __future__ import annotations

import datetime as _dt
import subprocess
from pathlib import Path

import nbformat as nbf

REPO_ROOT = Path(__file__).resolve().parent

# ──────────────────────────────────────────────────────────────────────────────
# DATA
# ──────────────────────────────────────────────────────────────────────────────

# 15 dims: (id, label, short description). D1 is user-required.
DIMENSIONS = [
    ('D1',  'Star Velocity ⭐',          'stars/day since creation (user-required)'),
    ('D2',  'Total Stars',               'absolute popularity'),
    ('D3',  'Forks',                     'replication / serious users'),
    ('D4',  'Watchers',                  'deep subscribers'),
    ('D5',  'Commit Recency',            'days-since-last-push (inverted)'),
    ('D6',  'Commit Cadence',            'commits/day since creation'),
    ('D7',  'Contributors',              'author diversity'),
    ('D8',  'Skill Volume',              'count of SKILL.md'),
    ('D9',  'Skill Depth',               'avg SKILL.md bytes'),
    ('D10', 'Supp. Material Density',    'supporting docs per skill'),
    ('D11', 'Doc Quality',               'README + structural docs'),
    ('D12', 'Eng. Hygiene',              'LICENSE/tests/hooks/CI/scripts'),
    ('D13', 'Multi-Agent Portability',   '# agent platforms supported'),
    ('D14', 'Domain Breadth',            'general vs niche'),
    ('D15', 'Originality / Authority',   'first-mover, official vs derivative'),
    ('D16', 'Reddit Heat (30d)',         'posts + comments/10 in last 30 days'),
    ('D17', 'Reddit Sentiment (30d)',    'avg upvote score per post (last 30d)'),
    ('D18', 'HN Heat (30d)',             'stories*10 + comments in last 30 days'),
    ('D19', 'HN Sentiment (30d)',        'avg points per story (last 30d)'),
    ('D20', 'Task Decomposition',        'inverse of avg SKILL.md bytes — smaller skills = better task decomposition (theory: each skill should solve one focused task)'),
    ('D21', 'Lesson-Encoded Quality',    '% of *.md containing failure-lesson markers (anti-pattern, red-flag, when-NOT-to-use, lessons-learned, pitfalls) + version/context signals — proxy for "model-unknown knowledge + env-context + real-failure-lessons"'),
]
DIM_IDS = [d[0] for d in DIMENSIONS]
MAX_TOTAL = len(DIMENSIONS) * 10  # 210

# Chinese dimension labels/descriptions (same IDs/order as DIMENSIONS).
DIMENSIONS_ZH = [
    ('D1',  '星增速 ⭐',            '创建至今每日新增 star（用户强调）'),
    ('D2',  '总 Star 数',           '绝对人气'),
    ('D3',  'Fork 数',              '复制 / 重度用户'),
    ('D4',  'Watcher 数',           '深度订阅者'),
    ('D5',  '提交新近度',           '距上次 push 天数（取反）'),
    ('D6',  '提交频率',             '创建至今每日提交数'),
    ('D7',  '贡献者数',             '作者多样性'),
    ('D8',  '技能数量',             'SKILL.md 文件数'),
    ('D9',  '技能深度',             'SKILL.md 平均字节数'),
    ('D10', '辅料密度',             '每技能的辅助文档数'),
    ('D11', '文档质量',             'README + 结构化文档'),
    ('D12', '工程化程度',           'LICENSE/测试/hooks/CI/脚本'),
    ('D13', '多 Agent 可移植性',    '支持的 agent 平台数'),
    ('D14', '领域广度',             '通用 vs 垂直'),
    ('D15', '原创性 / 权威性',      '首创、官方 vs 衍生'),
    ('D16', 'Reddit 热度 (30天)',   '近 30 天 帖子数 + 评论数/10'),
    ('D17', 'Reddit 口碑 (30天)',   '近 30 天 每帖平均 upvote'),
    ('D18', 'HN 热度 (30天)',       '近 30 天 story×10 + 评论数'),
    ('D19', 'HN 口碑 (30天)',       '近 30 天 每 story 平均 points'),
    ('D20', '任务分解度',           'SKILL.md 平均字节数取反——技能越小分解越好（理论：每个技能应聚焦一个任务）'),
    ('D21', '教训编码质量',         '含失败教训标记（anti-pattern / red-flag / when-NOT-to-use / lessons-learned / pitfalls）+ 版本/上下文信号的 *.md 占比——衡量"模型未知知识 + 环境上下文 + 真实失败教训"'),
]


def dims_for(lang: str):
    return DIMENSIONS_ZH if lang == 'zh' else DIMENSIONS


# UI string table. Keys are stable; values per language. Templates use str.format.
TXT = {
    'legend': {
        'en': ('<p style="color:#666;font-size:0.85em;margin:4px 0">Color gradient: '
               '<span style="background:rgba(220,60,60,0.35);padding:2px 8px;border-radius:3px">worst</span> → '
               '<span style="background:rgba(220,220,60,0.35);padding:2px 8px;border-radius:3px">mid</span> → '
               '<span style="background:rgba(40,200,100,0.35);padding:2px 8px;border-radius:3px">best</span>'
               '&nbsp;·&nbsp;per-column normalized · column-best <b>bolded</b></p>'),
        'zh': ('<p style="color:#666;font-size:0.85em;margin:4px 0">颜色梯度：'
               '<span style="background:rgba(220,60,60,0.35);padding:2px 8px;border-radius:3px">最差</span> → '
               '<span style="background:rgba(220,220,60,0.35);padding:2px 8px;border-radius:3px">中</span> → '
               '<span style="background:rgba(40,200,100,0.35);padding:2px 8px;border-radius:3px">最佳</span>'
               '&nbsp;·&nbsp;按列归一化 · 列最优值<b>加粗</b></p>'),
    },
    'overall_h3': {'en': '🏆 Overall Ranking — {date} (v{ver})', 'zh': '🏆 总排行 — {date}（v{ver}）'},
    'th_num':      {'en': '#', 'zh': '#'},
    'th_repo':     {'en': 'Repo', 'zh': '仓库'},
    'th_tier':     {'en': 'Tier', 'zh': '等级'},
    'th_total210': {'en': 'Total /210 ↑', 'zh': '总分 /210 ↑'},
    'th_d1':       {'en': 'D1 ⭐ /10 ↑', 'zh': 'D1 ⭐ /10 ↑'},
    'th_stars':    {'en': 'Stars ↑', 'zh': 'Stars ↑'},
    'th_starsday': {'en': 'Stars/day ↑', 'zh': 'Stars/天 ↑'},
    'th_forks':    {'en': 'Forks ↑', 'zh': 'Forks ↑'},
    'th_contribs': {'en': 'Contribs ↑', 'zh': '贡献者 ↑'},
    'th_desc':     {'en': 'Description', 'zh': '说明'},
    'matrix_h3':   {'en': '📋 Full Score Matrix · {ndim} Dimensions × {nrepo} Repos — {date}',
                    'zh': '📋 完整评分矩阵 · {ndim} 维 × {nrepo} repos — {date}'},
    'matrix_note': {'en': '<p style="color:#666;font-size:0.85em;margin:4px 0">Each cell colored 1-10 within its dimension column. Column-best <b>bolded</b>. Hover header for definition.</p>',
                    'zh': '<p style="color:#666;font-size:0.85em;margin:4px 0">每格按所在维度列的 1-10 着色，列最优值<b>加粗</b>，鼠标悬停表头查看定义。</p>'},
    'dim_defs':    {'en': '📖 Dimension definitions', 'zh': '📖 维度定义'},
    'th_total':    {'en': 'Total ↑', 'zh': '总分 ↑'},
    'th_id':       {'en': 'ID', 'zh': 'ID'},
    'th_label':    {'en': 'Label', 'zh': '名称'},
    'th_descr':    {'en': 'Description', 'zh': '说明'},
    'raw_h3':      {'en': '📊 Raw Metrics Snapshot — {date}', 'zh': '📊 原始指标快照 — {date}'},
    'raw_note':    {'en': '<p style="color:#666;font-size:0.85em;margin:4px 0">↑ higher is better · ↓ lower is better. Per-column normalized.</p>',
                    'zh': '<p style="color:#666;font-size:0.85em;margin:4px 0">↑ 越高越好 · ↓ 越低越好。按列归一化。</p>'},
    'drift_h3':    {'en': '🔗 Submodule Snapshot & Drift — {date}', 'zh': '🔗 Submodule 快照与漂移 — {date}'},
    'drift_note':  {'en': 'Snapshot SHAs captured at evaluation time ({eval}); current SHAs read at notebook build time ({now}).',
                    'zh': '快照 SHA 采集于评测时刻（{eval}）；当前 SHA 读取于 notebook 构建时刻（{now}）。'},
    'th_submodule':   {'en': 'Submodule', 'zh': 'Submodule'},
    'th_snapshot_sha':{'en': 'Snapshot SHA', 'zh': '快照 SHA'},
    'th_current_sha': {'en': 'Current SHA', 'zh': '当前 SHA'},
    'th_status':      {'en': 'Status', 'zh': '状态'},
    'st_missing':  {'en': '✗ missing', 'zh': '✗ 缺失'},
    'st_same':     {'en': '✓ same', 'zh': '✓ 一致'},
    'st_drifted':  {'en': '⚠ drifted', 'zh': '⚠ 漂移'},
    'domain_h3':   {'en': '🎯 Best Repo by Domain — {date}', 'zh': '🎯 各领域最佳 repo — {date}'},
    'domain_note': {'en': '<p style="color:#666;font-size:0.85em;margin:4px 0">Tier badges from the snapshot above; descriptions are the discriminating signal for that domain.</p>',
                    'zh': '<p style="color:#666;font-size:0.85em;margin:4px 0">等级徽章来自上方快照；说明是该领域的关键区分信号。</p>'},
    'th_domain':   {'en': 'Domain / Use case', 'zh': '领域 / 用例'},
    'th_bestrepo': {'en': 'Best repo', 'zh': '最佳 repo'},
    'th_why':      {'en': 'Why', 'zh': '理由'},
    'diff_h3':     {'en': '🔁 Score Δ — {old} → {new}', 'zh': '🔁 评分变化 Δ — {old} → {new}'},
    'diff_note':   {'en': '<p style="color:#666;font-size:0.85em;margin:4px 0">Per-dimension score change; positive (green) = improved.</p>',
                    'zh': '<p style="color:#666;font-size:0.85em;margin:4px 0">各维度评分变化；正值（绿）= 提升。</p>'},
    'th_dtotal':   {'en': 'ΔTotal', 'zh': 'Δ总分'},
    'new_badge_txt': {'en': 'NEW', 'zh': '新增'},
    # raw-metric column labels (keyed by metric key)
    'rm_stars':      {'en': 'Stars ↑', 'zh': 'Stars ↑'},
    'rm_stars_per_day': {'en': 'Stars/day ↑', 'zh': 'Stars/天 ↑'},
    'rm_forks':      {'en': 'Forks ↑', 'zh': 'Forks ↑'},
    'rm_watchers':   {'en': 'Watchers ↑', 'zh': 'Watchers ↑'},
    'rm_contribs':   {'en': 'Contribs ↑', 'zh': '贡献者 ↑'},
    'rm_days_alive': {'en': 'Days alive', 'zh': '存活天数'},
    'rm_last_push':  {'en': 'Last push (d ago) ↓', 'zh': '距上次 push(天) ↓'},
    'rm_commits_per_day': {'en': 'Commits/day ↑', 'zh': '提交/天 ↑'},
    'rm_skill_md':   {'en': 'SKILL.md count ↑', 'zh': 'SKILL.md 数 ↑'},
    'rm_avg_skill_bytes': {'en': 'Avg SKILL bytes ↑', 'zh': 'SKILL 平均字节 ↑'},
    'rm_platforms':  {'en': 'Agent platforms ↑', 'zh': 'Agent 平台数 ↑'},
}


def t(key: str, lang: str, **kw) -> str:
    s = TXT[key][lang]
    return s.format(**kw) if kw else s

# Repo registry: code → (owner, repo, oneliner)
REPOS = [
    ('AM',  'affaan-m',         'everything-claude-code',   'Agent harness perf framework'),
    ('O',   'obra',             'superpowers',              'Agentic skill methodology'),
    ('NX',  'nexu-io',          'open-design',              'OSS Claude Design alt'),
    ('A',   'anthropics',       'skills',                   'Official Anthropic spec'),
    ('NL',  'nextlevelbuilder', 'ui-ux-pro-max-skill',      'UI/UX design skill'),
    ('AD',  'addyosmani',       'agent-skills',             'Production engineering'),
    ('CH',  'coreyhaines31',    'marketingskills',          'Marketing / CRO / SEO'),
    ('C',   'ComposioHQ',       'awesome-claude-skills',    'Awesome list curation'),
    ('M',   'mattpocock',       'skills',                   'Skills for Real Engineers'),
    ('OAI', 'openai',           'skills',                   'Codex skill catalog'),
    ('MA',  'multica-ai',       'andrej-karpathy-skills',   'Karpathy-derived CLAUDE.md'),
    ('K',   'kepano',           'obsidian-skills',          'Obsidian-native'),
    ('V',   'vercel-labs',      'agent-skills',             'Vercel deploy + React/Next.js skills'),
    ('GS',  'garrytan',         'gstack',                   'Garry Tan exact Claude Code setup (23 role agents)'),
    ('AA',  'msitarzewski',     'agency-agents',            'AI agency — 222 personality-driven agents across 18 domains'),
    ('CV',  'juliusbrussee',    'caveman',                  'Token-efficient prompt engineering — "caveman talk" cuts 65% tokens'),
    ('UA',  'Egonex-AI',        'Understand-Anything',      'Turns a codebase into an interactive knowledge graph'),
    ('OS',  'Fission-AI',       'OpenSpec',                 'Spec-driven development workflow for AI coding agents'),
    ('CO',  'santifer',         'career-ops',               'Job-search / career automation pipeline (CV, ATS, tracking)'),
    ('TS',  'Leonxlnx',         'taste-skill',              'Design "taste" skill — steers agents away from generic output'),
    ('L30', 'mvanhorn',         'last30days-skill',         'Researches last-30-day trends across Reddit/X/YouTube/HN/web'),
]
REPO_BY_CODE = {c: (c, o, r, l) for c, o, r, l in REPOS}

# Append-only snapshot history.
EVALUATIONS = [
    {
        'eval_date': '2026-05-13T08:00:00Z',
        'version': '1.0',
        'note': 'Initial baseline — 12-repo cohort, rank-based 1-10 scoring within cohort.',
        'submodule_shas': {
            'skills/affaan-m__everything-claude-code':      'd4728a0d801f1ebbc2384547009df17cbf16bfd1',
            'skills/obra__superpowers':                     'f2cbfbefebbfef77321e4c9abc9e949826bea9d7',
            'skills/nexu-io__open-design':                  '6341b2677aa7075b8027e3647310d61060b63e1b',
            'skills/anthropics__skills':                    'f458cee31a7577a47ba0c9a101976fa599385174',
            'skills/nextlevelbuilder__ui-ux-pro-max-skill': 'b7e3af80f6e331f6fb456667b82b12cade7c9d35',
            'skills/addyosmani__agent-skills':              '3ff4b518b3cd3077ca27cf883aa21d21faf53802',
            'skills/coreyhaines31__marketingskills':        '906c2fb28e471c5b1d149d4159ec5ddb40b7c364',
            'skills/ComposioHQ__awesome-claude-skills':     'f2b5e29bc315f04c8e09591ba275f4c4f7d4b8fe',
            'skills/mattpocock__skills':                    'f304057d61d3df3c9fd992ac2b6e3833cb9325fb',
            'skills/openai__skills':                        'c25113bf4c64c8dba6bfe61acf06051d79aa43f6',
            'skills/multica-ai__andrej-karpathy-skills':    '2c606141936f1eeef17fa3043a72095b4765b9c2',
            'skills/kepano__obsidian-skills':               'ac9398734fe719565809f7a6048b05c36b1ca38f',
        },
        'raw_metrics': {
            'AM':  {'stars': 180838, 'forks': 27876, 'watchers': 899, 'contribs': 183, 'skill_md': 572, 'avg_skill_bytes': 8847,  'days_alive': 115, 'stars_per_day': 1572.5, 'commits_per_day': 14.82, 'platforms': 7, 'last_push_days_ago': 0},
            'O':   {'stars': 188498, 'forks': 16759, 'watchers': 753, 'contribs': 33,  'skill_md': 14,  'avg_skill_bytes': 8168,  'days_alive': 216, 'stars_per_day': 872.7,  'commits_per_day': 2.04,  'platforms': 6, 'last_push_days_ago': 0},
            'NX':  {'stars': 38735,  'forks': 4403,  'watchers': 142, 'contribs': 186, 'skill_md': 218, 'avg_skill_bytes': 3438,  'days_alive': 15,  'stars_per_day': 2582.3, 'commits_per_day': 42.5,  'platforms': 9, 'last_push_days_ago': 0},
            'A':   {'stars': 133251, 'forks': 15715, 'watchers': 865, 'contribs': 13,  'skill_md': 18,  'avg_skill_bytes': 10995, 'days_alive': 233, 'stars_per_day': 571.9,  'commits_per_day': 0.15,  'platforms': 1, 'last_push_days_ago': 4},
            'NL':  {'stars': 77723,  'forks': 7977,  'watchers': 381, 'contribs': 31,  'skill_md': 7,   'avg_skill_bytes': 12272, 'days_alive': 164, 'stars_per_day': 474.0,  'commits_per_day': 0.82,  'platforms': 8, 'last_push_days_ago': 40},
            'AD':  {'stars': 40580,  'forks': 4472,  'watchers': 255, 'contribs': 23,  'skill_md': 22,  'avg_skill_bytes': 10703, 'days_alive': 87,  'stars_per_day': 466.4,  'commits_per_day': 2.0,   'platforms': 7, 'last_push_days_ago': 3},
            'CH':  {'stars': 28215,  'forks': 4550,  'watchers': 288, 'contribs': 16,  'skill_md': 41,  'avg_skill_bytes': 11443, 'days_alive': 118, 'stars_per_day': 239.1,  'commits_per_day': 2.21,  'platforms': 5, 'last_push_days_ago': 7},
            'C':   {'stars': 59518,  'forks': 6462,  'watchers': 399, 'contribs': 26,  'skill_md': 864, 'avg_skill_bytes': 3444,  'days_alive': 208, 'stars_per_day': 286.1,  'commits_per_day': 0.34,  'platforms': 7, 'last_push_days_ago': 6},
            'M':   {'stars': 77173,  'forks': 6656,  'watchers': 532, 'contribs': 2,   'skill_md': 28,  'avg_skill_bytes': 3321,  'days_alive': 99,  'stars_per_day': 779.5,  'commits_per_day': 0.78,  'platforms': 2, 'last_push_days_ago': 1},
            'OAI': {'stars': 18982,  'forks': 1259,  'watchers': 110, 'contribs': 34,  'skill_md': 43,  'avg_skill_bytes': 9435,  'days_alive': 169, 'stars_per_day': 112.3,  'commits_per_day': 0.64,  'platforms': 1, 'last_push_days_ago': 1},
            'MA':  {'stars': 127547, 'forks': 12958, 'watchers': 671, 'contribs': 7,   'skill_md': 1,   'avg_skill_bytes': 2518,  'days_alive': 106, 'stars_per_day': 1203.3, 'commits_per_day': 0.26,  'platforms': 2, 'last_push_days_ago': 23},
            'K':   {'stars': 30825,  'forks': 2100,  'watchers': 185, 'contribs': 13,  'skill_md': 5,   'avg_skill_bytes': 6040,  'days_alive': 131, 'stars_per_day': 235.3,  'commits_per_day': 0.30,  'platforms': 3, 'last_push_days_ago': 6},
        },
        'scores': {
            'AM':  {'D1': 9, 'D2': 9, 'D3':10, 'D4':10, 'D5':10, 'D6': 9, 'D7': 9, 'D8': 9, 'D9': 6, 'D10': 5, 'D11':10, 'D12':10, 'D13': 8, 'D14':10, 'D15': 5},
            'O':   {'D1': 8, 'D2':10, 'D3': 9, 'D4': 8, 'D5':10, 'D6': 7, 'D7': 7, 'D8': 3, 'D9': 5, 'D10': 7, 'D11': 8, 'D12': 9, 'D13': 7, 'D14': 9, 'D15': 9},
            'NX':  {'D1':10, 'D2': 4, 'D3': 3, 'D4': 2, 'D5':10, 'D6':10, 'D7':10, 'D8': 8, 'D9': 3, 'D10': 4, 'D11':10, 'D12':10, 'D13':10, 'D14': 8, 'D15': 8},
            'A':   {'D1': 6, 'D2': 9, 'D3': 8, 'D4': 9, 'D5': 8, 'D6': 1, 'D7': 3, 'D8': 3, 'D9': 9, 'D10': 7, 'D11': 6, 'D12': 6, 'D13': 1, 'D14': 8, 'D15':10},
            'NL':  {'D1': 5, 'D2': 7, 'D3': 6, 'D4': 5, 'D5': 2, 'D6': 6, 'D7': 6, 'D8': 2, 'D9':10, 'D10': 9, 'D11': 9, 'D12': 8, 'D13': 9, 'D14': 4, 'D15': 6},
            'AD':  {'D1': 5, 'D2': 4, 'D3': 4, 'D4': 3, 'D5': 8, 'D6': 7, 'D7': 4, 'D8': 4, 'D9': 8, 'D10': 3, 'D11': 9, 'D12': 8, 'D13': 8, 'D14': 8, 'D15': 7},
            'CH':  {'D1': 3, 'D2': 2, 'D3': 4, 'D4': 4, 'D5': 6, 'D6': 8, 'D7': 4, 'D8': 6, 'D9': 9, 'D10': 7, 'D11': 8, 'D12': 9, 'D13': 6, 'D14': 4, 'D15': 6},
            'C':   {'D1': 4, 'D2': 5, 'D3': 5, 'D4': 5, 'D5': 7, 'D6': 3, 'D7': 5, 'D8':10, 'D9': 3, 'D10': 1, 'D11': 8, 'D12': 4, 'D13': 8, 'D14': 9, 'D15': 3},
            'M':   {'D1': 7, 'D2': 6, 'D3': 5, 'D4': 6, 'D5': 9, 'D6': 5, 'D7': 1, 'D8': 5, 'D9': 2, 'D10': 2, 'D11': 7, 'D12': 6, 'D13': 2, 'D14': 6, 'D15': 7},
            'OAI': {'D1': 1, 'D2': 1, 'D3': 1, 'D4': 1, 'D5': 9, 'D6': 4, 'D7': 8, 'D8': 7, 'D9': 7, 'D10':10, 'D11': 3, 'D12': 3, 'D13': 1, 'D14': 7, 'D15':10},
            'MA':  {'D1': 9, 'D2': 8, 'D3': 7, 'D4': 7, 'D5': 4, 'D6': 2, 'D7': 2, 'D8': 1, 'D9': 1, 'D10': 8, 'D11': 7, 'D12': 3, 'D13': 2, 'D14': 1, 'D15': 8},
            'K':   {'D1': 2, 'D2': 3, 'D3': 2, 'D4': 2, 'D5': 7, 'D6': 3, 'D7': 3, 'D8': 1, 'D9': 4, 'D10': 2, 'D11': 4, 'D12': 3, 'D13': 4, 'D14': 3, 'D15': 7},
        },
    },
    {
        'eval_date': '2026-05-13T16:30:00Z',
        'version': '1.1',
        'note': 'Added vercel-labs/agent-skills to cohort (13 repos). V displaces OAI on D10 (supp. material density 19.3 vs 11.33); 6 incumbents lose 1 point on D10 from cohort re-rank. Other dims stable.',
        'submodule_shas': {
            'skills/affaan-m__everything-claude-code':      'd4728a0d801f1ebbc2384547009df17cbf16bfd1',
            'skills/obra__superpowers':                     'f2cbfbefebbfef77321e4c9abc9e949826bea9d7',
            'skills/nexu-io__open-design':                  '6341b2677aa7075b8027e3647310d61060b63e1b',
            'skills/anthropics__skills':                    'f458cee31a7577a47ba0c9a101976fa599385174',
            'skills/nextlevelbuilder__ui-ux-pro-max-skill': 'b7e3af80f6e331f6fb456667b82b12cade7c9d35',
            'skills/addyosmani__agent-skills':              '3ff4b518b3cd3077ca27cf883aa21d21faf53802',
            'skills/coreyhaines31__marketingskills':        '906c2fb28e471c5b1d149d4159ec5ddb40b7c364',
            'skills/ComposioHQ__awesome-claude-skills':     'f2b5e29bc315f04c8e09591ba275f4c4f7d4b8fe',
            'skills/mattpocock__skills':                    'f304057d61d3df3c9fd992ac2b6e3833cb9325fb',
            'skills/openai__skills':                        'c25113bf4c64c8dba6bfe61acf06051d79aa43f6',
            'skills/multica-ai__andrej-karpathy-skills':    '2c606141936f1eeef17fa3043a72095b4765b9c2',
            'skills/kepano__obsidian-skills':               'ac9398734fe719565809f7a6048b05c36b1ca38f',
            'skills/vercel-labs__agent-skills':             'b9c8ee0643d87d3c5a953d1e22382ff2ead39229',
        },
        'raw_metrics': {
            'AM':  {'stars': 180838, 'forks': 27876, 'watchers': 899, 'contribs': 183, 'skill_md': 572, 'avg_skill_bytes': 8847,  'days_alive': 115, 'stars_per_day': 1572.5, 'commits_per_day': 14.82, 'platforms': 7, 'last_push_days_ago': 0},
            'O':   {'stars': 188498, 'forks': 16759, 'watchers': 753, 'contribs': 33,  'skill_md': 14,  'avg_skill_bytes': 8168,  'days_alive': 216, 'stars_per_day': 872.7,  'commits_per_day': 2.04,  'platforms': 6, 'last_push_days_ago': 0},
            'NX':  {'stars': 38735,  'forks': 4403,  'watchers': 142, 'contribs': 186, 'skill_md': 218, 'avg_skill_bytes': 3438,  'days_alive': 15,  'stars_per_day': 2582.3, 'commits_per_day': 42.5,  'platforms': 9, 'last_push_days_ago': 0},
            'A':   {'stars': 133251, 'forks': 15715, 'watchers': 865, 'contribs': 13,  'skill_md': 18,  'avg_skill_bytes': 10995, 'days_alive': 233, 'stars_per_day': 571.9,  'commits_per_day': 0.15,  'platforms': 1, 'last_push_days_ago': 4},
            'NL':  {'stars': 77723,  'forks': 7977,  'watchers': 381, 'contribs': 31,  'skill_md': 7,   'avg_skill_bytes': 12272, 'days_alive': 164, 'stars_per_day': 474.0,  'commits_per_day': 0.82,  'platforms': 8, 'last_push_days_ago': 40},
            'AD':  {'stars': 40580,  'forks': 4472,  'watchers': 255, 'contribs': 23,  'skill_md': 22,  'avg_skill_bytes': 10703, 'days_alive': 87,  'stars_per_day': 466.4,  'commits_per_day': 2.0,   'platforms': 7, 'last_push_days_ago': 3},
            'CH':  {'stars': 28215,  'forks': 4550,  'watchers': 288, 'contribs': 16,  'skill_md': 41,  'avg_skill_bytes': 11443, 'days_alive': 118, 'stars_per_day': 239.1,  'commits_per_day': 2.21,  'platforms': 5, 'last_push_days_ago': 7},
            'C':   {'stars': 59518,  'forks': 6462,  'watchers': 399, 'contribs': 26,  'skill_md': 864, 'avg_skill_bytes': 3444,  'days_alive': 208, 'stars_per_day': 286.1,  'commits_per_day': 0.34,  'platforms': 7, 'last_push_days_ago': 6},
            'M':   {'stars': 77173,  'forks': 6656,  'watchers': 532, 'contribs': 2,   'skill_md': 28,  'avg_skill_bytes': 3321,  'days_alive': 99,  'stars_per_day': 779.5,  'commits_per_day': 0.78,  'platforms': 2, 'last_push_days_ago': 1},
            'OAI': {'stars': 18982,  'forks': 1259,  'watchers': 110, 'contribs': 34,  'skill_md': 43,  'avg_skill_bytes': 9435,  'days_alive': 169, 'stars_per_day': 112.3,  'commits_per_day': 0.64,  'platforms': 1, 'last_push_days_ago': 1},
            'MA':  {'stars': 127547, 'forks': 12958, 'watchers': 671, 'contribs': 7,   'skill_md': 1,   'avg_skill_bytes': 2518,  'days_alive': 106, 'stars_per_day': 1203.3, 'commits_per_day': 0.26,  'platforms': 2, 'last_push_days_ago': 23},
            'K':   {'stars': 30825,  'forks': 2100,  'watchers': 185, 'contribs': 13,  'skill_md': 5,   'avg_skill_bytes': 6040,  'days_alive': 131, 'stars_per_day': 235.3,  'commits_per_day': 0.30,  'platforms': 3, 'last_push_days_ago': 6},
            'V':   {'stars': 26494,  'forks': 2416,  'watchers': 114, 'contribs': 21,  'skill_md': 7,   'avg_skill_bytes': 7224,  'days_alive': 156, 'stars_per_day': 169.8,  'commits_per_day': 1.27,  'platforms': 4, 'last_push_days_ago': 6},
        },
        'scores': {
            # Unchanged from v1.0 except where V displaces in D10.
            'AM':  {'D1': 9, 'D2': 9, 'D3':10, 'D4':10, 'D5':10, 'D6': 9, 'D7': 9, 'D8': 9, 'D9': 6, 'D10': 5, 'D11':10, 'D12':10, 'D13': 8, 'D14':10, 'D15': 5},
            'O':   {'D1': 8, 'D2':10, 'D3': 9, 'D4': 8, 'D5':10, 'D6': 7, 'D7': 7, 'D8': 3, 'D9': 5, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 7, 'D14': 9, 'D15': 9},  # D10 7→6
            'NX':  {'D1':10, 'D2': 4, 'D3': 3, 'D4': 2, 'D5':10, 'D6':10, 'D7':10, 'D8': 8, 'D9': 3, 'D10': 4, 'D11':10, 'D12':10, 'D13':10, 'D14': 8, 'D15': 8},
            'A':   {'D1': 6, 'D2': 9, 'D3': 8, 'D4': 9, 'D5': 8, 'D6': 1, 'D7': 3, 'D8': 3, 'D9': 9, 'D10': 6, 'D11': 6, 'D12': 6, 'D13': 1, 'D14': 8, 'D15':10},  # D10 7→6
            'NL':  {'D1': 5, 'D2': 7, 'D3': 6, 'D4': 5, 'D5': 2, 'D6': 6, 'D7': 6, 'D8': 2, 'D9':10, 'D10': 8, 'D11': 9, 'D12': 8, 'D13': 9, 'D14': 4, 'D15': 6},  # D10 9→8
            'AD':  {'D1': 5, 'D2': 4, 'D3': 4, 'D4': 3, 'D5': 8, 'D6': 7, 'D7': 4, 'D8': 4, 'D9': 8, 'D10': 3, 'D11': 9, 'D12': 8, 'D13': 8, 'D14': 8, 'D15': 7},
            'CH':  {'D1': 3, 'D2': 2, 'D3': 4, 'D4': 4, 'D5': 6, 'D6': 8, 'D7': 4, 'D8': 6, 'D9': 9, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 6, 'D14': 4, 'D15': 6},  # D10 7→6
            'C':   {'D1': 4, 'D2': 5, 'D3': 5, 'D4': 5, 'D5': 7, 'D6': 3, 'D7': 5, 'D8':10, 'D9': 3, 'D10': 1, 'D11': 8, 'D12': 4, 'D13': 8, 'D14': 9, 'D15': 3},
            'M':   {'D1': 7, 'D2': 6, 'D3': 5, 'D4': 6, 'D5': 9, 'D6': 5, 'D7': 1, 'D8': 5, 'D9': 2, 'D10': 2, 'D11': 7, 'D12': 6, 'D13': 2, 'D14': 6, 'D15': 7},
            'OAI': {'D1': 1, 'D2': 1, 'D3': 1, 'D4': 1, 'D5': 9, 'D6': 4, 'D7': 8, 'D8': 7, 'D9': 7, 'D10': 9, 'D11': 3, 'D12': 3, 'D13': 1, 'D14': 7, 'D15':10},  # D10 10→9
            'MA':  {'D1': 9, 'D2': 8, 'D3': 7, 'D4': 7, 'D5': 4, 'D6': 2, 'D7': 2, 'D8': 1, 'D9': 1, 'D10': 7, 'D11': 7, 'D12': 3, 'D13': 2, 'D14': 1, 'D15': 8},  # D10 8→7
            'K':   {'D1': 2, 'D2': 3, 'D3': 2, 'D4': 2, 'D5': 7, 'D6': 3, 'D7': 3, 'D8': 1, 'D9': 4, 'D10': 2, 'D11': 4, 'D12': 3, 'D13': 4, 'D14': 3, 'D15': 7},
            'V':   {'D1': 2, 'D2': 2, 'D3': 3, 'D4': 2, 'D5': 7, 'D6': 6, 'D7': 4, 'D8': 2, 'D9': 5, 'D10':10, 'D11': 8, 'D12': 6, 'D13': 5, 'D14': 4, 'D15': 9},  # NEW (total = 75 → B)
        },
    },
    {
        'eval_date': '2026-05-13T17:30:00Z',
        'version': '1.2',
        'note': 'Added garrytan/gstack + msitarzewski/agency-agents (15-repo cohort); added 4 new dimensions D16-D19 (Reddit Heat/Sentiment + HN Heat/Sentiment, sampled via public APIs last 30 days). Max total now 190 (19 dims × 10). GS displaces NL on D9 (avg SKILL.md 52,730B = cohort top); AA fills the game-dev coverage gap with 20 game-development agents. GS/AA both top Reddit signals (avg scores 2,769 / 2,897) on launch wave. NOTE: AA uses `.md` per role rather than SKILL.md — treated as the same volume metric.',
        'submodule_shas': {
            'skills/affaan-m__everything-claude-code':      'd4728a0d801f1ebbc2384547009df17cbf16bfd1',
            'skills/obra__superpowers':                     'f2cbfbefebbfef77321e4c9abc9e949826bea9d7',
            'skills/nexu-io__open-design':                  '6341b2677aa7075b8027e3647310d61060b63e1b',
            'skills/anthropics__skills':                    'f458cee31a7577a47ba0c9a101976fa599385174',
            'skills/nextlevelbuilder__ui-ux-pro-max-skill': 'b7e3af80f6e331f6fb456667b82b12cade7c9d35',
            'skills/addyosmani__agent-skills':              '3ff4b518b3cd3077ca27cf883aa21d21faf53802',
            'skills/coreyhaines31__marketingskills':        '906c2fb28e471c5b1d149d4159ec5ddb40b7c364',
            'skills/ComposioHQ__awesome-claude-skills':     'f2b5e29bc315f04c8e09591ba275f4c4f7d4b8fe',
            'skills/mattpocock__skills':                    'f304057d61d3df3c9fd992ac2b6e3833cb9325fb',
            'skills/openai__skills':                        'c25113bf4c64c8dba6bfe61acf06051d79aa43f6',
            'skills/multica-ai__andrej-karpathy-skills':    '2c606141936f1eeef17fa3043a72095b4765b9c2',
            'skills/kepano__obsidian-skills':               'ac9398734fe719565809f7a6048b05c36b1ca38f',
            'skills/vercel-labs__agent-skills':             'b9c8ee0643d87d3c5a953d1e22382ff2ead39229',
            'skills/garrytan__gstack':                      'dc6252d1df7f1f650ea6e9b2bba7d08fab5de902',
            'skills/msitarzewski__agency-agents':           '783f6a72bfd7f3135700ac273c619d92821b419a',
        },
        'raw_metrics': {
            'AM':  {'stars': 180838, 'forks': 27876, 'watchers': 899, 'contribs': 183, 'skill_md': 572, 'avg_skill_bytes': 8847,  'days_alive': 115, 'stars_per_day': 1572.5, 'commits_per_day': 14.82, 'platforms': 7, 'last_push_days_ago': 0, 'reddit_posts': 8,   'reddit_comments': 96,    'reddit_avg_score': 126.5,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0},
            'O':   {'stars': 188498, 'forks': 16759, 'watchers': 753, 'contribs': 33,  'skill_md': 14,  'avg_skill_bytes': 8168,  'days_alive': 216, 'stars_per_day': 872.7,  'commits_per_day': 2.04,  'platforms': 6, 'last_push_days_ago': 0, 'reddit_posts': 40,  'reddit_comments': 243,   'reddit_avg_score':  31.4,  'hn_stories': 1, 'hn_comments': 0,   'hn_avg_points': 3.0},
            'NX':  {'stars': 38735,  'forks': 4403,  'watchers': 142, 'contribs': 186, 'skill_md': 218, 'avg_skill_bytes': 3438,  'days_alive': 15,  'stars_per_day': 2582.3, 'commits_per_day': 42.5,  'platforms': 9, 'last_push_days_ago': 0, 'reddit_posts': 8,   'reddit_comments': 103,   'reddit_avg_score':  63.2,  'hn_stories': 1, 'hn_comments': 92,  'hn_avg_points': 230.0},
            'A':   {'stars': 133251, 'forks': 15715, 'watchers': 865, 'contribs': 13,  'skill_md': 18,  'avg_skill_bytes': 10995, 'days_alive': 233, 'stars_per_day': 571.9,  'commits_per_day': 0.15,  'platforms': 1, 'last_push_days_ago': 4, 'reddit_posts': 169, 'reddit_comments': 6451,  'reddit_avg_score': 151.7,  'hn_stories': 8, 'hn_comments': 9,   'hn_avg_points': 5.0},
            'NL':  {'stars': 77723,  'forks': 7977,  'watchers': 381, 'contribs': 31,  'skill_md': 7,   'avg_skill_bytes': 12272, 'days_alive': 164, 'stars_per_day': 474.0,  'commits_per_day': 0.82,  'platforms': 8, 'last_push_days_ago': 40,'reddit_posts': 2,   'reddit_comments': 1,     'reddit_avg_score':   1.5,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0},
            'AD':  {'stars': 40580,  'forks': 4472,  'watchers': 255, 'contribs': 23,  'skill_md': 22,  'avg_skill_bytes': 10703, 'days_alive': 87,  'stars_per_day': 466.4,  'commits_per_day': 2.0,   'platforms': 7, 'last_push_days_ago': 3, 'reddit_posts': 6,   'reddit_comments': 54,    'reddit_avg_score':  22.2,  'hn_stories': 1, 'hn_comments': 212, 'hn_avg_points': 375.0},
            'CH':  {'stars': 28215,  'forks': 4550,  'watchers': 288, 'contribs': 16,  'skill_md': 41,  'avg_skill_bytes': 11443, 'days_alive': 118, 'stars_per_day': 239.1,  'commits_per_day': 2.21,  'platforms': 5, 'last_push_days_ago': 7, 'reddit_posts': 5,   'reddit_comments': 97,    'reddit_avg_score':  38.2,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0},
            'C':   {'stars': 59518,  'forks': 6462,  'watchers': 399, 'contribs': 26,  'skill_md': 864, 'avg_skill_bytes': 3444,  'days_alive': 208, 'stars_per_day': 286.1,  'commits_per_day': 0.34,  'platforms': 7, 'last_push_days_ago': 6, 'reddit_posts': 5,   'reddit_comments': 98,    'reddit_avg_score':  87.8,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0},
            'M':   {'stars': 77173,  'forks': 6656,  'watchers': 532, 'contribs': 2,   'skill_md': 28,  'avg_skill_bytes': 3321,  'days_alive': 99,  'stars_per_day': 779.5,  'commits_per_day': 0.78,  'platforms': 2, 'last_push_days_ago': 1, 'reddit_posts': 14,  'reddit_comments': 303,   'reddit_avg_score':  92.9,  'hn_stories': 1, 'hn_comments': 0,   'hn_avg_points': 5.0},
            'OAI': {'stars': 18982,  'forks': 1259,  'watchers': 110, 'contribs': 34,  'skill_md': 43,  'avg_skill_bytes': 9435,  'days_alive': 169, 'stars_per_day': 112.3,  'commits_per_day': 0.64,  'platforms': 1, 'last_push_days_ago': 1, 'reddit_posts': 171, 'reddit_comments': 3358,  'reddit_avg_score':  54.9,  'hn_stories': 7, 'hn_comments': 16,  'hn_avg_points': 8.7},
            'MA':  {'stars': 127547, 'forks': 12958, 'watchers': 671, 'contribs': 7,   'skill_md': 1,   'avg_skill_bytes': 2518,  'days_alive': 106, 'stars_per_day': 1203.3, 'commits_per_day': 0.26,  'platforms': 2, 'last_push_days_ago': 23,'reddit_posts': 0,   'reddit_comments': 0,     'reddit_avg_score':   0.0,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0},
            'K':   {'stars': 30825,  'forks': 2100,  'watchers': 185, 'contribs': 13,  'skill_md': 5,   'avg_skill_bytes': 6040,  'days_alive': 131, 'stars_per_day': 235.3,  'commits_per_day': 0.30,  'platforms': 3, 'last_push_days_ago': 6, 'reddit_posts': 2,   'reddit_comments': 19,    'reddit_avg_score':  65.0,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0},
            'V':   {'stars': 26494,  'forks': 2416,  'watchers': 114, 'contribs': 21,  'skill_md': 7,   'avg_skill_bytes': 7224,  'days_alive': 156, 'stars_per_day': 169.8,  'commits_per_day': 1.27,  'platforms': 4, 'last_push_days_ago': 6, 'reddit_posts': 25,  'reddit_comments': 425,   'reddit_avg_score':  63.8,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0},
            'GS':  {'stars': 95212,  'forks': 14113, 'watchers': 575, 'contribs': 10,  'skill_md': 51,  'avg_skill_bytes': 52730, 'days_alive': 63,  'stars_per_day': 1511.3, 'commits_per_day': 4.33,  'platforms': 8, 'last_push_days_ago': 1, 'reddit_posts': 111, 'reddit_comments': 32442, 'reddit_avg_score': 2769.0, 'hn_stories': 4, 'hn_comments': 0,   'hn_avg_points': 2.2},
            'AA':  {'stars': 96620,  'forks': 16028, 'watchers': 771, 'contribs': 72,  'skill_md': 222, 'avg_skill_bytes': 12293, 'days_alive': 212, 'stars_per_day': 455.8,  'commits_per_day': 1.37,  'platforms': 9, 'last_push_days_ago': 31,'reddit_posts': 104, 'reddit_comments': 29053, 'reddit_avg_score': 2897.4, 'hn_stories': 2, 'hn_comments': 3,   'hn_avg_points': 1.5},
        },
        'scores': {
            #     D1   D2   D3   D4   D5   D6   D7   D8   D9   D10  D11  D12  D13  D14  D15  D16  D17  D18  D19  Total
            'AM':  {'D1': 9, 'D2': 9, 'D3':10, 'D4':10, 'D5':10, 'D6': 9, 'D7': 9, 'D8': 9, 'D9': 6, 'D10': 5, 'D11':10, 'D12':10, 'D13': 8, 'D14':10, 'D15': 5, 'D16': 5, 'D17': 9, 'D18': 1, 'D19': 1},  # 145
            'O':   {'D1': 8, 'D2':10, 'D3': 9, 'D4': 8, 'D5':10, 'D6': 7, 'D7': 7, 'D8': 3, 'D9': 5, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 7, 'D14': 9, 'D15': 9, 'D16': 7, 'D17': 3, 'D18': 6, 'D19': 6},  # 137
            'NX':  {'D1':10, 'D2': 4, 'D3': 3, 'D4': 2, 'D5':10, 'D6':10, 'D7':10, 'D8': 8, 'D9': 3, 'D10': 4, 'D11':10, 'D12':10, 'D13':10, 'D14': 8, 'D15': 8, 'D16': 6, 'D17': 5, 'D18': 9, 'D19': 9},  # 139
            'A':   {'D1': 6, 'D2': 9, 'D3': 8, 'D4': 9, 'D5': 8, 'D6': 1, 'D7': 3, 'D8': 3, 'D9': 9, 'D10': 6, 'D11': 6, 'D12': 6, 'D13': 1, 'D14': 8, 'D15':10, 'D16': 9, 'D17': 9, 'D18': 9, 'D19': 7},  # 127
            'NL':  {'D1': 5, 'D2': 7, 'D3': 6, 'D4': 5, 'D5': 2, 'D6': 6, 'D7': 6, 'D8': 2, 'D9': 9, 'D10': 8, 'D11': 9, 'D12': 8, 'D13': 9, 'D14': 4, 'D15': 6, 'D16': 2, 'D17': 2, 'D18': 1, 'D19': 1},  # 98 (D9 10→9 due to GS)
            'AD':  {'D1': 5, 'D2': 4, 'D3': 4, 'D4': 3, 'D5': 8, 'D6': 7, 'D7': 4, 'D8': 4, 'D9': 8, 'D10': 3, 'D11': 9, 'D12': 8, 'D13': 8, 'D14': 8, 'D15': 7, 'D16': 3, 'D17': 2, 'D18':10, 'D19':10},  # 115
            'CH':  {'D1': 3, 'D2': 2, 'D3': 4, 'D4': 4, 'D5': 6, 'D6': 8, 'D7': 4, 'D8': 6, 'D9': 9, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 6, 'D14': 4, 'D15': 6, 'D16': 4, 'D17': 4, 'D18': 1, 'D19': 1},  # 95
            'C':   {'D1': 4, 'D2': 5, 'D3': 5, 'D4': 5, 'D5': 7, 'D6': 3, 'D7': 5, 'D8':10, 'D9': 3, 'D10': 1, 'D11': 8, 'D12': 4, 'D13': 8, 'D14': 9, 'D15': 3, 'D16': 4, 'D17': 7, 'D18': 1, 'D19': 1},  # 93
            'M':   {'D1': 7, 'D2': 6, 'D3': 5, 'D4': 6, 'D5': 9, 'D6': 5, 'D7': 1, 'D8': 5, 'D9': 2, 'D10': 2, 'D11': 7, 'D12': 6, 'D13': 2, 'D14': 6, 'D15': 7, 'D16': 7, 'D17': 8, 'D18': 6, 'D19': 7},  # 104
            'OAI': {'D1': 1, 'D2': 1, 'D3': 1, 'D4': 1, 'D5': 9, 'D6': 4, 'D7': 8, 'D8': 7, 'D9': 7, 'D10': 9, 'D11': 3, 'D12': 3, 'D13': 1, 'D14': 7, 'D15':10, 'D16': 9, 'D17': 4, 'D18': 8, 'D19': 8},  # 101
            'MA':  {'D1': 9, 'D2': 8, 'D3': 7, 'D4': 7, 'D5': 4, 'D6': 2, 'D7': 2, 'D8': 1, 'D9': 1, 'D10': 7, 'D11': 7, 'D12': 3, 'D13': 2, 'D14': 1, 'D15': 8, 'D16': 1, 'D17': 1, 'D18': 1, 'D19': 1},  # 73
            'K':   {'D1': 2, 'D2': 3, 'D3': 2, 'D4': 2, 'D5': 7, 'D6': 3, 'D7': 3, 'D8': 1, 'D9': 4, 'D10': 2, 'D11': 4, 'D12': 3, 'D13': 4, 'D14': 3, 'D15': 7, 'D16': 3, 'D17': 7, 'D18': 1, 'D19': 1},  # 62
            'V':   {'D1': 2, 'D2': 2, 'D3': 3, 'D4': 2, 'D5': 7, 'D6': 6, 'D7': 4, 'D8': 2, 'D9': 5, 'D10':10, 'D11': 8, 'D12': 6, 'D13': 5, 'D14': 4, 'D15': 9, 'D16': 8, 'D17': 6, 'D18': 1, 'D19': 1},  # 91
            'GS':  {'D1': 9, 'D2': 7, 'D3': 8, 'D4': 7, 'D5': 9, 'D6': 8, 'D7': 3, 'D8': 7, 'D9':10, 'D10': 3, 'D11': 9, 'D12': 9, 'D13': 9, 'D14': 9, 'D15': 8, 'D16':10, 'D17':10, 'D18': 7, 'D19': 5},  # 147 (new #1)
            'AA':  {'D1': 5, 'D2': 7, 'D3': 8, 'D4': 8, 'D5': 3, 'D6': 6, 'D7': 8, 'D8': 8, 'D9': 9, 'D10': 1, 'D11':10, 'D12': 9, 'D13':10, 'D14':10, 'D15': 7, 'D16':10, 'D17':10, 'D18': 6, 'D19': 4},  # 139 (tied #3 with NX)
        },
    },
    {
        'eval_date': '2026-05-13T18:00:00Z',
        'version': '1.3',
        'note': 'Added 2 new dimensions: D20 Task Decomposition (inverse of avg SKILL.md bytes — smaller = better decomposition per "one skill = one focused task" theory); D21 Lesson-Encoded Quality (composite proxy for valuable-skills criteria: (1) model-unknown knowledge, (2) env-specific context, (3) lessons from real failures — measured via marker scan in all .md files). Max total: 190 → 210 (21 dims × 10). Tier thresholds rescaled. Cohort unchanged (15 repos). GS retains #1 (depth + Reddit) despite D20=1 (penalty for fat SKILL.md). MA gains big from D20=10 (smallest avg) + D21=9 (anti-pattern-dense).',
        'submodule_shas': {
            'skills/affaan-m__everything-claude-code':      'd4728a0d801f1ebbc2384547009df17cbf16bfd1',
            'skills/obra__superpowers':                     'f2cbfbefebbfef77321e4c9abc9e949826bea9d7',
            'skills/nexu-io__open-design':                  '6341b2677aa7075b8027e3647310d61060b63e1b',
            'skills/anthropics__skills':                    'f458cee31a7577a47ba0c9a101976fa599385174',
            'skills/nextlevelbuilder__ui-ux-pro-max-skill': 'b7e3af80f6e331f6fb456667b82b12cade7c9d35',
            'skills/addyosmani__agent-skills':              '3ff4b518b3cd3077ca27cf883aa21d21faf53802',
            'skills/coreyhaines31__marketingskills':        '906c2fb28e471c5b1d149d4159ec5ddb40b7c364',
            'skills/ComposioHQ__awesome-claude-skills':     'f2b5e29bc315f04c8e09591ba275f4c4f7d4b8fe',
            'skills/mattpocock__skills':                    'f304057d61d3df3c9fd992ac2b6e3833cb9325fb',
            'skills/openai__skills':                        'c25113bf4c64c8dba6bfe61acf06051d79aa43f6',
            'skills/multica-ai__andrej-karpathy-skills':    '2c606141936f1eeef17fa3043a72095b4765b9c2',
            'skills/kepano__obsidian-skills':               'ac9398734fe719565809f7a6048b05c36b1ca38f',
            'skills/vercel-labs__agent-skills':             'b9c8ee0643d87d3c5a953d1e22382ff2ead39229',
            'skills/garrytan__gstack':                      'dc6252d1df7f1f650ea6e9b2bba7d08fab5de902',
            'skills/msitarzewski__agency-agents':           '783f6a72bfd7f3135700ac273c619d92821b419a',
        },
        'raw_metrics': {
            # Same metrics as v1.2 with new fields: lesson_pct, value_density_pct
            'AM':  {'stars': 180838, 'forks': 27876, 'watchers': 899, 'contribs': 183, 'skill_md': 572, 'avg_skill_bytes': 8847,  'days_alive': 115, 'stars_per_day': 1572.5, 'commits_per_day': 14.82, 'platforms': 7, 'last_push_days_ago': 0, 'reddit_posts': 8,   'reddit_comments': 96,    'reddit_avg_score': 126.5,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 10.5, 'value_density_pct': 11.3},
            'O':   {'stars': 188498, 'forks': 16759, 'watchers': 753, 'contribs': 33,  'skill_md': 14,  'avg_skill_bytes': 8168,  'days_alive': 216, 'stars_per_day': 872.7,  'commits_per_day': 2.04,  'platforms': 6, 'last_push_days_ago': 0, 'reddit_posts': 40,  'reddit_comments': 243,   'reddit_avg_score':  31.4,  'hn_stories': 1, 'hn_comments': 0,   'hn_avg_points': 3.0,   'lesson_pct': 37.1, 'value_density_pct': 25.0},
            'NX':  {'stars': 38735,  'forks': 4403,  'watchers': 142, 'contribs': 186, 'skill_md': 218, 'avg_skill_bytes': 3438,  'days_alive': 15,  'stars_per_day': 2582.3, 'commits_per_day': 42.5,  'platforms': 9, 'last_push_days_ago': 0, 'reddit_posts': 8,   'reddit_comments': 103,   'reddit_avg_score':  63.2,  'hn_stories': 1, 'hn_comments': 92,  'hn_avg_points': 230.0, 'lesson_pct': 18.5, 'value_density_pct': 13.3},
            'A':   {'stars': 133251, 'forks': 15715, 'watchers': 865, 'contribs': 13,  'skill_md': 18,  'avg_skill_bytes': 10995, 'days_alive': 233, 'stars_per_day': 571.9,  'commits_per_day': 0.15,  'platforms': 1, 'last_push_days_ago': 4, 'reddit_posts': 169, 'reddit_comments': 6451,  'reddit_avg_score': 151.7,  'hn_stories': 8, 'hn_comments': 9,   'hn_avg_points': 5.0,   'lesson_pct': 31.5, 'value_density_pct': 22.4},
            'NL':  {'stars': 77723,  'forks': 7977,  'watchers': 381, 'contribs': 31,  'skill_md': 7,   'avg_skill_bytes': 12272, 'days_alive': 164, 'stars_per_day': 474.0,  'commits_per_day': 0.82,  'platforms': 8, 'last_push_days_ago': 40,'reddit_posts': 2,   'reddit_comments': 1,     'reddit_avg_score':   1.5,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct':  4.6, 'value_density_pct':  7.4},
            'AD':  {'stars': 40580,  'forks': 4472,  'watchers': 255, 'contribs': 23,  'skill_md': 22,  'avg_skill_bytes': 10703, 'days_alive': 87,  'stars_per_day': 466.4,  'commits_per_day': 2.0,   'platforms': 7, 'last_push_days_ago': 3, 'reddit_posts': 6,   'reddit_comments': 54,    'reddit_avg_score':  22.2,  'hn_stories': 1, 'hn_comments': 212, 'hn_avg_points': 375.0, 'lesson_pct': 59.3, 'value_density_pct': 39.4},
            'CH':  {'stars': 28215,  'forks': 4550,  'watchers': 288, 'contribs': 16,  'skill_md': 41,  'avg_skill_bytes': 11443, 'days_alive': 118, 'stars_per_day': 239.1,  'commits_per_day': 2.21,  'platforms': 5, 'last_push_days_ago': 7, 'reddit_posts': 5,   'reddit_comments': 97,    'reddit_avg_score':  38.2,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 18.4, 'value_density_pct': 13.5},
            'C':   {'stars': 59518,  'forks': 6462,  'watchers': 399, 'contribs': 26,  'skill_md': 864, 'avg_skill_bytes': 3444,  'days_alive': 208, 'stars_per_day': 286.1,  'commits_per_day': 0.34,  'platforms': 7, 'last_push_days_ago': 6, 'reddit_posts': 5,   'reddit_comments': 98,    'reddit_avg_score':  87.8,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 94.7, 'value_density_pct': 57.3},
            'M':   {'stars': 77173,  'forks': 6656,  'watchers': 532, 'contribs': 2,   'skill_md': 28,  'avg_skill_bytes': 3321,  'days_alive': 99,  'stars_per_day': 779.5,  'commits_per_day': 0.78,  'platforms': 2, 'last_push_days_ago': 1, 'reddit_posts': 14,  'reddit_comments': 303,   'reddit_avg_score':  92.9,  'hn_stories': 1, 'hn_comments': 0,   'hn_avg_points': 5.0,   'lesson_pct':  6.7, 'value_density_pct':  4.5},
            'OAI': {'stars': 18982,  'forks': 1259,  'watchers': 110, 'contribs': 34,  'skill_md': 43,  'avg_skill_bytes': 9435,  'days_alive': 169, 'stars_per_day': 112.3,  'commits_per_day': 0.64,  'platforms': 1, 'last_push_days_ago': 1, 'reddit_posts': 171, 'reddit_comments': 3358,  'reddit_avg_score':  54.9,  'hn_stories': 7, 'hn_comments': 16,  'hn_avg_points': 8.7,   'lesson_pct': 41.9, 'value_density_pct': 31.6},
            'MA':  {'stars': 127547, 'forks': 12958, 'watchers': 671, 'contribs': 7,   'skill_md': 1,   'avg_skill_bytes': 2518,  'days_alive': 106, 'stars_per_day': 1203.3, 'commits_per_day': 0.26,  'platforms': 2, 'last_push_days_ago': 23,'reddit_posts': 0,   'reddit_comments': 0,     'reddit_avg_score':   0.0,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 66.7, 'value_density_pct': 42.5},
            'K':   {'stars': 30825,  'forks': 2100,  'watchers': 185, 'contribs': 13,  'skill_md': 5,   'avg_skill_bytes': 6040,  'days_alive': 131, 'stars_per_day': 235.3,  'commits_per_day': 0.30,  'platforms': 3, 'last_push_days_ago': 6, 'reddit_posts': 2,   'reddit_comments': 19,    'reddit_avg_score':  65.0,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 18.2, 'value_density_pct': 10.9},
            'V':   {'stars': 26494,  'forks': 2416,  'watchers': 114, 'contribs': 21,  'skill_md': 7,   'avg_skill_bytes': 7224,  'days_alive': 156, 'stars_per_day': 169.8,  'commits_per_day': 1.27,  'platforms': 4, 'last_push_days_ago': 6, 'reddit_posts': 25,  'reddit_comments': 425,   'reddit_avg_score':  63.8,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 10.6, 'value_density_pct':  8.8},
            'GS':  {'stars': 95212,  'forks': 14113, 'watchers': 575, 'contribs': 10,  'skill_md': 51,  'avg_skill_bytes': 52730, 'days_alive': 63,  'stars_per_day': 1511.3, 'commits_per_day': 4.33,  'platforms': 8, 'last_push_days_ago': 1, 'reddit_posts': 111, 'reddit_comments': 32442, 'reddit_avg_score': 2769.0, 'hn_stories': 4, 'hn_comments': 0,   'hn_avg_points': 2.2,   'lesson_pct': 56.0, 'value_density_pct': 39.3},
            'AA':  {'stars': 96620,  'forks': 16028, 'watchers': 771, 'contribs': 72,  'skill_md': 222, 'avg_skill_bytes': 12293, 'days_alive': 212, 'stars_per_day': 455.8,  'commits_per_day': 1.37,  'platforms': 9, 'last_push_days_ago': 31,'reddit_posts': 104, 'reddit_comments': 29053, 'reddit_avg_score': 2897.4, 'hn_stories': 2, 'hn_comments': 3,   'hn_avg_points': 1.5,   'lesson_pct': 25.2, 'value_density_pct': 18.3},
        },
        'scores': {
            #     D1   D2   D3   D4   D5   D6   D7   D8   D9   D10  D11  D12  D13  D14  D15  D16  D17  D18  D19  D20  D21  Total
            'AM':  {'D1': 9, 'D2': 9, 'D3':10, 'D4':10, 'D5':10, 'D6': 9, 'D7': 9, 'D8': 9, 'D9': 6, 'D10': 5, 'D11':10, 'D12':10, 'D13': 8, 'D14':10, 'D15': 5, 'D16': 5, 'D17': 9, 'D18': 1, 'D19': 1, 'D20': 5, 'D21': 4},  # 154
            'O':   {'D1': 8, 'D2':10, 'D3': 9, 'D4': 8, 'D5':10, 'D6': 7, 'D7': 7, 'D8': 3, 'D9': 5, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 7, 'D14': 9, 'D15': 9, 'D16': 7, 'D17': 3, 'D18': 6, 'D19': 6, 'D20': 6, 'D21': 7},  # 150
            'NX':  {'D1':10, 'D2': 4, 'D3': 3, 'D4': 2, 'D5':10, 'D6':10, 'D7':10, 'D8': 8, 'D9': 3, 'D10': 4, 'D11':10, 'D12':10, 'D13':10, 'D14': 8, 'D15': 8, 'D16': 6, 'D17': 5, 'D18': 9, 'D19': 9, 'D20': 9, 'D21': 4},  # 152
            'A':   {'D1': 6, 'D2': 9, 'D3': 8, 'D4': 9, 'D5': 8, 'D6': 1, 'D7': 3, 'D8': 3, 'D9': 9, 'D10': 6, 'D11': 6, 'D12': 6, 'D13': 1, 'D14': 8, 'D15':10, 'D16': 9, 'D17': 9, 'D18': 9, 'D19': 7, 'D20': 3, 'D21': 6},  # 136
            'NL':  {'D1': 5, 'D2': 7, 'D3': 6, 'D4': 5, 'D5': 2, 'D6': 6, 'D7': 6, 'D8': 2, 'D9': 9, 'D10': 8, 'D11': 9, 'D12': 8, 'D13': 9, 'D14': 4, 'D15': 6, 'D16': 2, 'D17': 2, 'D18': 1, 'D19': 1, 'D20': 2, 'D21': 2},  # 102
            'AD':  {'D1': 5, 'D2': 4, 'D3': 4, 'D4': 3, 'D5': 8, 'D6': 7, 'D7': 4, 'D8': 4, 'D9': 8, 'D10': 3, 'D11': 9, 'D12': 8, 'D13': 8, 'D14': 8, 'D15': 7, 'D16': 3, 'D17': 2, 'D18':10, 'D19':10, 'D20': 4, 'D21': 9},  # 128
            'CH':  {'D1': 3, 'D2': 2, 'D3': 4, 'D4': 4, 'D5': 6, 'D6': 8, 'D7': 4, 'D8': 6, 'D9': 9, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 6, 'D14': 4, 'D15': 6, 'D16': 4, 'D17': 4, 'D18': 1, 'D19': 1, 'D20': 3, 'D21': 5},  # 103
            'C':   {'D1': 4, 'D2': 5, 'D3': 5, 'D4': 5, 'D5': 7, 'D6': 3, 'D7': 5, 'D8':10, 'D9': 3, 'D10': 1, 'D11': 8, 'D12': 4, 'D13': 8, 'D14': 9, 'D15': 3, 'D16': 4, 'D17': 7, 'D18': 1, 'D19': 1, 'D20': 8, 'D21':10},  # 111
            'M':   {'D1': 7, 'D2': 6, 'D3': 5, 'D4': 6, 'D5': 9, 'D6': 5, 'D7': 1, 'D8': 5, 'D9': 2, 'D10': 2, 'D11': 7, 'D12': 6, 'D13': 2, 'D14': 6, 'D15': 7, 'D16': 7, 'D17': 8, 'D18': 6, 'D19': 7, 'D20': 9, 'D21': 1},  # 114
            'OAI': {'D1': 1, 'D2': 1, 'D3': 1, 'D4': 1, 'D5': 9, 'D6': 4, 'D7': 8, 'D8': 7, 'D9': 7, 'D10': 9, 'D11': 3, 'D12': 3, 'D13': 1, 'D14': 7, 'D15':10, 'D16': 9, 'D17': 4, 'D18': 8, 'D19': 8, 'D20': 4, 'D21': 8},  # 113
            'MA':  {'D1': 9, 'D2': 8, 'D3': 7, 'D4': 7, 'D5': 4, 'D6': 2, 'D7': 2, 'D8': 1, 'D9': 1, 'D10': 7, 'D11': 7, 'D12': 3, 'D13': 2, 'D14': 1, 'D15': 8, 'D16': 1, 'D17': 1, 'D18': 1, 'D19': 1, 'D20':10, 'D21': 9},  # 92
            'K':   {'D1': 2, 'D2': 3, 'D3': 2, 'D4': 2, 'D5': 7, 'D6': 3, 'D7': 3, 'D8': 1, 'D9': 4, 'D10': 2, 'D11': 4, 'D12': 3, 'D13': 4, 'D14': 3, 'D15': 7, 'D16': 3, 'D17': 7, 'D18': 1, 'D19': 1, 'D20': 7, 'D21': 3},  # 72
            'V':   {'D1': 2, 'D2': 2, 'D3': 3, 'D4': 2, 'D5': 7, 'D6': 6, 'D7': 4, 'D8': 2, 'D9': 5, 'D10':10, 'D11': 8, 'D12': 6, 'D13': 5, 'D14': 4, 'D15': 9, 'D16': 8, 'D17': 6, 'D18': 1, 'D19': 1, 'D20': 7, 'D21': 3},  # 101
            'GS':  {'D1': 9, 'D2': 7, 'D3': 8, 'D4': 7, 'D5': 9, 'D6': 8, 'D7': 3, 'D8': 7, 'D9':10, 'D10': 3, 'D11': 9, 'D12': 9, 'D13': 9, 'D14': 9, 'D15': 8, 'D16':10, 'D17':10, 'D18': 7, 'D19': 5, 'D20': 1, 'D21': 8},  # 156 (still #1)
            'AA':  {'D1': 5, 'D2': 7, 'D3': 8, 'D4': 8, 'D5': 3, 'D6': 6, 'D7': 8, 'D8': 8, 'D9': 9, 'D10': 1, 'D11':10, 'D12': 9, 'D13':10, 'D14':10, 'D15': 7, 'D16':10, 'D17':10, 'D18': 6, 'D19': 4, 'D20': 2, 'D21': 5},  # 146
        },
    },
    {
        'eval_date': '2026-05-13T19:00:00Z',
        'version': '1.4',
        'note': 'Added juliusbrussee/caveman (16-repo cohort) — viral "caveman talk" token-efficient prompt engineering, 60k stars in 39 days. Fills "token optimization / prompt engineering" vertical. 9 platforms incl. first antigravity mention in cohort. Cohort: 16 repos × 21 dims (max still 210). CV scores 137 (#6, between A=136 and AA=146).',
        'submodule_shas': {
            'skills/affaan-m__everything-claude-code':      'd4728a0d801f1ebbc2384547009df17cbf16bfd1',
            'skills/obra__superpowers':                     'f2cbfbefebbfef77321e4c9abc9e949826bea9d7',
            'skills/nexu-io__open-design':                  '6341b2677aa7075b8027e3647310d61060b63e1b',
            'skills/anthropics__skills':                    'f458cee31a7577a47ba0c9a101976fa599385174',
            'skills/nextlevelbuilder__ui-ux-pro-max-skill': 'b7e3af80f6e331f6fb456667b82b12cade7c9d35',
            'skills/addyosmani__agent-skills':              '3ff4b518b3cd3077ca27cf883aa21d21faf53802',
            'skills/coreyhaines31__marketingskills':        '906c2fb28e471c5b1d149d4159ec5ddb40b7c364',
            'skills/ComposioHQ__awesome-claude-skills':     'f2b5e29bc315f04c8e09591ba275f4c4f7d4b8fe',
            'skills/mattpocock__skills':                    'f304057d61d3df3c9fd992ac2b6e3833cb9325fb',
            'skills/openai__skills':                        'c25113bf4c64c8dba6bfe61acf06051d79aa43f6',
            'skills/multica-ai__andrej-karpathy-skills':    '2c606141936f1eeef17fa3043a72095b4765b9c2',
            'skills/kepano__obsidian-skills':               'ac9398734fe719565809f7a6048b05c36b1ca38f',
            'skills/vercel-labs__agent-skills':             'b9c8ee0643d87d3c5a953d1e22382ff2ead39229',
            'skills/garrytan__gstack':                      'dc6252d1df7f1f650ea6e9b2bba7d08fab5de902',
            'skills/msitarzewski__agency-agents':           '783f6a72bfd7f3135700ac273c619d92821b419a',
            'skills/juliusbrussee__caveman':                '63a91ecadbf4c4719a4602a5abb00883f9966034',
        },
        'raw_metrics': {
            'AM':  {'stars': 180838, 'forks': 27876, 'watchers': 899, 'contribs': 183, 'skill_md': 572, 'avg_skill_bytes': 8847,  'days_alive': 115, 'stars_per_day': 1572.5, 'commits_per_day': 14.82, 'platforms': 7, 'last_push_days_ago': 0, 'reddit_posts': 8,   'reddit_comments': 96,    'reddit_avg_score': 126.5,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 10.5, 'value_density_pct': 11.3},
            'O':   {'stars': 188498, 'forks': 16759, 'watchers': 753, 'contribs': 33,  'skill_md': 14,  'avg_skill_bytes': 8168,  'days_alive': 216, 'stars_per_day': 872.7,  'commits_per_day': 2.04,  'platforms': 6, 'last_push_days_ago': 0, 'reddit_posts': 40,  'reddit_comments': 243,   'reddit_avg_score':  31.4,  'hn_stories': 1, 'hn_comments': 0,   'hn_avg_points': 3.0,   'lesson_pct': 37.1, 'value_density_pct': 25.0},
            'NX':  {'stars': 38735,  'forks': 4403,  'watchers': 142, 'contribs': 186, 'skill_md': 218, 'avg_skill_bytes': 3438,  'days_alive': 15,  'stars_per_day': 2582.3, 'commits_per_day': 42.5,  'platforms': 9, 'last_push_days_ago': 0, 'reddit_posts': 8,   'reddit_comments': 103,   'reddit_avg_score':  63.2,  'hn_stories': 1, 'hn_comments': 92,  'hn_avg_points': 230.0, 'lesson_pct': 18.5, 'value_density_pct': 13.3},
            'A':   {'stars': 133251, 'forks': 15715, 'watchers': 865, 'contribs': 13,  'skill_md': 18,  'avg_skill_bytes': 10995, 'days_alive': 233, 'stars_per_day': 571.9,  'commits_per_day': 0.15,  'platforms': 1, 'last_push_days_ago': 4, 'reddit_posts': 169, 'reddit_comments': 6451,  'reddit_avg_score': 151.7,  'hn_stories': 8, 'hn_comments': 9,   'hn_avg_points': 5.0,   'lesson_pct': 31.5, 'value_density_pct': 22.4},
            'NL':  {'stars': 77723,  'forks': 7977,  'watchers': 381, 'contribs': 31,  'skill_md': 7,   'avg_skill_bytes': 12272, 'days_alive': 164, 'stars_per_day': 474.0,  'commits_per_day': 0.82,  'platforms': 8, 'last_push_days_ago': 40,'reddit_posts': 2,   'reddit_comments': 1,     'reddit_avg_score':   1.5,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct':  4.6, 'value_density_pct':  7.4},
            'AD':  {'stars': 40580,  'forks': 4472,  'watchers': 255, 'contribs': 23,  'skill_md': 22,  'avg_skill_bytes': 10703, 'days_alive': 87,  'stars_per_day': 466.4,  'commits_per_day': 2.0,   'platforms': 7, 'last_push_days_ago': 3, 'reddit_posts': 6,   'reddit_comments': 54,    'reddit_avg_score':  22.2,  'hn_stories': 1, 'hn_comments': 212, 'hn_avg_points': 375.0, 'lesson_pct': 59.3, 'value_density_pct': 39.4},
            'CH':  {'stars': 28215,  'forks': 4550,  'watchers': 288, 'contribs': 16,  'skill_md': 41,  'avg_skill_bytes': 11443, 'days_alive': 118, 'stars_per_day': 239.1,  'commits_per_day': 2.21,  'platforms': 5, 'last_push_days_ago': 7, 'reddit_posts': 5,   'reddit_comments': 97,    'reddit_avg_score':  38.2,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 18.4, 'value_density_pct': 13.5},
            'C':   {'stars': 59518,  'forks': 6462,  'watchers': 399, 'contribs': 26,  'skill_md': 864, 'avg_skill_bytes': 3444,  'days_alive': 208, 'stars_per_day': 286.1,  'commits_per_day': 0.34,  'platforms': 7, 'last_push_days_ago': 6, 'reddit_posts': 5,   'reddit_comments': 98,    'reddit_avg_score':  87.8,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 94.7, 'value_density_pct': 57.3},
            'M':   {'stars': 77173,  'forks': 6656,  'watchers': 532, 'contribs': 2,   'skill_md': 28,  'avg_skill_bytes': 3321,  'days_alive': 99,  'stars_per_day': 779.5,  'commits_per_day': 0.78,  'platforms': 2, 'last_push_days_ago': 1, 'reddit_posts': 14,  'reddit_comments': 303,   'reddit_avg_score':  92.9,  'hn_stories': 1, 'hn_comments': 0,   'hn_avg_points': 5.0,   'lesson_pct':  6.7, 'value_density_pct':  4.5},
            'OAI': {'stars': 18982,  'forks': 1259,  'watchers': 110, 'contribs': 34,  'skill_md': 43,  'avg_skill_bytes': 9435,  'days_alive': 169, 'stars_per_day': 112.3,  'commits_per_day': 0.64,  'platforms': 1, 'last_push_days_ago': 1, 'reddit_posts': 171, 'reddit_comments': 3358,  'reddit_avg_score':  54.9,  'hn_stories': 7, 'hn_comments': 16,  'hn_avg_points': 8.7,   'lesson_pct': 41.9, 'value_density_pct': 31.6},
            'MA':  {'stars': 127547, 'forks': 12958, 'watchers': 671, 'contribs': 7,   'skill_md': 1,   'avg_skill_bytes': 2518,  'days_alive': 106, 'stars_per_day': 1203.3, 'commits_per_day': 0.26,  'platforms': 2, 'last_push_days_ago': 23,'reddit_posts': 0,   'reddit_comments': 0,     'reddit_avg_score':   0.0,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 66.7, 'value_density_pct': 42.5},
            'K':   {'stars': 30825,  'forks': 2100,  'watchers': 185, 'contribs': 13,  'skill_md': 5,   'avg_skill_bytes': 6040,  'days_alive': 131, 'stars_per_day': 235.3,  'commits_per_day': 0.30,  'platforms': 3, 'last_push_days_ago': 6, 'reddit_posts': 2,   'reddit_comments': 19,    'reddit_avg_score':  65.0,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 18.2, 'value_density_pct': 10.9},
            'V':   {'stars': 26494,  'forks': 2416,  'watchers': 114, 'contribs': 21,  'skill_md': 7,   'avg_skill_bytes': 7224,  'days_alive': 156, 'stars_per_day': 169.8,  'commits_per_day': 1.27,  'platforms': 4, 'last_push_days_ago': 6, 'reddit_posts': 25,  'reddit_comments': 425,   'reddit_avg_score':  63.8,  'hn_stories': 0, 'hn_comments': 0,   'hn_avg_points': 0.0,   'lesson_pct': 10.6, 'value_density_pct':  8.8},
            'GS':  {'stars': 95212,  'forks': 14113, 'watchers': 575, 'contribs': 10,  'skill_md': 51,  'avg_skill_bytes': 52730, 'days_alive': 63,  'stars_per_day': 1511.3, 'commits_per_day': 4.33,  'platforms': 8, 'last_push_days_ago': 1, 'reddit_posts': 111, 'reddit_comments': 32442, 'reddit_avg_score': 2769.0, 'hn_stories': 4, 'hn_comments': 0,   'hn_avg_points': 2.2,   'lesson_pct': 56.0, 'value_density_pct': 39.3},
            'AA':  {'stars': 96620,  'forks': 16028, 'watchers': 771, 'contribs': 72,  'skill_md': 222, 'avg_skill_bytes': 12293, 'days_alive': 212, 'stars_per_day': 455.8,  'commits_per_day': 1.37,  'platforms': 9, 'last_push_days_ago': 31,'reddit_posts': 104, 'reddit_comments': 29053, 'reddit_avg_score': 2897.4, 'hn_stories': 2, 'hn_comments': 3,   'hn_avg_points': 1.5,   'lesson_pct': 25.2, 'value_density_pct': 18.3},
            'CV':  {'stars': 60365,  'forks': 3346,  'watchers': 141, 'contribs': 29,  'skill_md': 15,  'avg_skill_bytes': 3266,  'days_alive': 39,  'stars_per_day': 1547.8, 'commits_per_day': 4.67,  'platforms': 9, 'last_push_days_ago': 1, 'reddit_posts': 105, 'reddit_comments': 15705, 'reddit_avg_score': 788.8,  'hn_stories': 3, 'hn_comments': 1,   'hn_avg_points': 3.0,   'lesson_pct': 22.0, 'value_density_pct': 14.2},
        },
        'scores': {
            # Same scores as v1.3 for existing 15 repos; CV slotted in based on its position in each dim.
            'AM':  {'D1': 9, 'D2': 9, 'D3':10, 'D4':10, 'D5':10, 'D6': 9, 'D7': 9, 'D8': 9, 'D9': 6, 'D10': 5, 'D11':10, 'D12':10, 'D13': 8, 'D14':10, 'D15': 5, 'D16': 5, 'D17': 9, 'D18': 1, 'D19': 1, 'D20': 5, 'D21': 4},  # 154
            'O':   {'D1': 8, 'D2':10, 'D3': 9, 'D4': 8, 'D5':10, 'D6': 7, 'D7': 7, 'D8': 3, 'D9': 5, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 7, 'D14': 9, 'D15': 9, 'D16': 7, 'D17': 3, 'D18': 6, 'D19': 6, 'D20': 6, 'D21': 7},  # 150
            'NX':  {'D1':10, 'D2': 4, 'D3': 3, 'D4': 2, 'D5':10, 'D6':10, 'D7':10, 'D8': 8, 'D9': 3, 'D10': 4, 'D11':10, 'D12':10, 'D13':10, 'D14': 8, 'D15': 8, 'D16': 6, 'D17': 5, 'D18': 9, 'D19': 9, 'D20': 9, 'D21': 4},  # 152
            'A':   {'D1': 6, 'D2': 9, 'D3': 8, 'D4': 9, 'D5': 8, 'D6': 1, 'D7': 3, 'D8': 3, 'D9': 9, 'D10': 6, 'D11': 6, 'D12': 6, 'D13': 1, 'D14': 8, 'D15':10, 'D16': 9, 'D17': 9, 'D18': 9, 'D19': 7, 'D20': 3, 'D21': 6},  # 136
            'NL':  {'D1': 5, 'D2': 7, 'D3': 6, 'D4': 5, 'D5': 2, 'D6': 6, 'D7': 6, 'D8': 2, 'D9': 9, 'D10': 8, 'D11': 9, 'D12': 8, 'D13': 9, 'D14': 4, 'D15': 6, 'D16': 2, 'D17': 2, 'D18': 1, 'D19': 1, 'D20': 2, 'D21': 2},  # 102
            'AD':  {'D1': 5, 'D2': 4, 'D3': 4, 'D4': 3, 'D5': 8, 'D6': 7, 'D7': 4, 'D8': 4, 'D9': 8, 'D10': 3, 'D11': 9, 'D12': 8, 'D13': 8, 'D14': 8, 'D15': 7, 'D16': 3, 'D17': 2, 'D18':10, 'D19':10, 'D20': 4, 'D21': 9},  # 128
            'CH':  {'D1': 3, 'D2': 2, 'D3': 4, 'D4': 4, 'D5': 6, 'D6': 8, 'D7': 4, 'D8': 6, 'D9': 9, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 6, 'D14': 4, 'D15': 6, 'D16': 4, 'D17': 4, 'D18': 1, 'D19': 1, 'D20': 3, 'D21': 5},  # 103
            'C':   {'D1': 4, 'D2': 5, 'D3': 5, 'D4': 5, 'D5': 7, 'D6': 3, 'D7': 5, 'D8':10, 'D9': 3, 'D10': 1, 'D11': 8, 'D12': 4, 'D13': 8, 'D14': 9, 'D15': 3, 'D16': 4, 'D17': 7, 'D18': 1, 'D19': 1, 'D20': 8, 'D21':10},  # 111
            'M':   {'D1': 7, 'D2': 6, 'D3': 5, 'D4': 6, 'D5': 9, 'D6': 5, 'D7': 1, 'D8': 5, 'D9': 2, 'D10': 2, 'D11': 7, 'D12': 6, 'D13': 2, 'D14': 6, 'D15': 7, 'D16': 7, 'D17': 8, 'D18': 6, 'D19': 7, 'D20': 9, 'D21': 1},  # 114
            'OAI': {'D1': 1, 'D2': 1, 'D3': 1, 'D4': 1, 'D5': 9, 'D6': 4, 'D7': 8, 'D8': 7, 'D9': 7, 'D10': 9, 'D11': 3, 'D12': 3, 'D13': 1, 'D14': 7, 'D15':10, 'D16': 9, 'D17': 4, 'D18': 8, 'D19': 8, 'D20': 4, 'D21': 8},  # 113
            'MA':  {'D1': 9, 'D2': 8, 'D3': 7, 'D4': 7, 'D5': 4, 'D6': 2, 'D7': 2, 'D8': 1, 'D9': 1, 'D10': 7, 'D11': 7, 'D12': 3, 'D13': 2, 'D14': 1, 'D15': 8, 'D16': 1, 'D17': 1, 'D18': 1, 'D19': 1, 'D20':10, 'D21': 9},  # 92
            'K':   {'D1': 2, 'D2': 3, 'D3': 2, 'D4': 2, 'D5': 7, 'D6': 3, 'D7': 3, 'D8': 1, 'D9': 4, 'D10': 2, 'D11': 4, 'D12': 3, 'D13': 4, 'D14': 3, 'D15': 7, 'D16': 3, 'D17': 7, 'D18': 1, 'D19': 1, 'D20': 7, 'D21': 3},  # 72
            'V':   {'D1': 2, 'D2': 2, 'D3': 3, 'D4': 2, 'D5': 7, 'D6': 6, 'D7': 4, 'D8': 2, 'D9': 5, 'D10':10, 'D11': 8, 'D12': 6, 'D13': 5, 'D14': 4, 'D15': 9, 'D16': 8, 'D17': 6, 'D18': 1, 'D19': 1, 'D20': 7, 'D21': 3},  # 101
            'GS':  {'D1': 9, 'D2': 7, 'D3': 8, 'D4': 7, 'D5': 9, 'D6': 8, 'D7': 3, 'D8': 7, 'D9':10, 'D10': 3, 'D11': 9, 'D12': 9, 'D13': 9, 'D14': 9, 'D15': 8, 'D16':10, 'D17':10, 'D18': 7, 'D19': 5, 'D20': 1, 'D21': 8},  # 156
            'AA':  {'D1': 5, 'D2': 7, 'D3': 8, 'D4': 8, 'D5': 3, 'D6': 6, 'D7': 8, 'D8': 8, 'D9': 9, 'D10': 1, 'D11':10, 'D12': 9, 'D13':10, 'D14':10, 'D15': 7, 'D16':10, 'D17':10, 'D18': 6, 'D19': 4, 'D20': 2, 'D21': 5},  # 146
            'CV':  {'D1': 9, 'D2': 6, 'D3': 3, 'D4': 2, 'D5': 9, 'D6': 9, 'D7': 6, 'D8': 3, 'D9': 2, 'D10': 5, 'D11': 8, 'D12': 9, 'D13':10, 'D14': 4, 'D15': 8, 'D16': 9, 'D17':10, 'D18': 6, 'D19': 6, 'D20': 9, 'D21': 4},  # 137 (NEW; #6)
        },
    },
    # ── Append new snapshots here ─────────────────────────────────────────────
    {
        'eval_date': '2026-06-17T08:00:00Z',
        'version': '1.5',
        'note': 'Added 5 repos (21-repo cohort): Egonex-AI/Understand-Anything (UA), Fission-AI/OpenSpec (OS), santifer/career-ops (CO), Leonxlnx/taste-skill (TS), mvanhorn/last30days-skill (L30). Real metrics collected 2026-06-17 via gh API + local scan_lessons.py + HN Algolia. Reddit unreachable (HTTP 403) at eval time, so D16/D17 are unmeasured and floored to 1 for the 5 new repos. UA=117 (#9, B), CO=113 (#12, B), L30=98 (#17, C), OS=97 (#18, C), TS=84 (#20, C). TS leads newcomers on D9 depth (23KB avg) and D21 lessons (41.4%); L30 has the single deepest SKILL.md (140KB), D9=10 but D20=1.',
        'submodule_shas': {
            'skills/affaan-m__everything-claude-code': 'd4728a0d801f1ebbc2384547009df17cbf16bfd1',
            'skills/obra__superpowers': 'f2cbfbefebbfef77321e4c9abc9e949826bea9d7',
            'skills/nexu-io__open-design': '6341b2677aa7075b8027e3647310d61060b63e1b',
            'skills/anthropics__skills': 'f458cee31a7577a47ba0c9a101976fa599385174',
            'skills/nextlevelbuilder__ui-ux-pro-max-skill': 'b7e3af80f6e331f6fb456667b82b12cade7c9d35',
            'skills/addyosmani__agent-skills': '3ff4b518b3cd3077ca27cf883aa21d21faf53802',
            'skills/coreyhaines31__marketingskills': '906c2fb28e471c5b1d149d4159ec5ddb40b7c364',
            'skills/ComposioHQ__awesome-claude-skills': 'f2b5e29bc315f04c8e09591ba275f4c4f7d4b8fe',
            'skills/mattpocock__skills': 'f304057d61d3df3c9fd992ac2b6e3833cb9325fb',
            'skills/openai__skills': 'c25113bf4c64c8dba6bfe61acf06051d79aa43f6',
            'skills/multica-ai__andrej-karpathy-skills': '2c606141936f1eeef17fa3043a72095b4765b9c2',
            'skills/kepano__obsidian-skills': 'ac9398734fe719565809f7a6048b05c36b1ca38f',
            'skills/vercel-labs__agent-skills': 'b9c8ee0643d87d3c5a953d1e22382ff2ead39229',
            'skills/garrytan__gstack': 'dc6252d1df7f1f650ea6e9b2bba7d08fab5de902',
            'skills/msitarzewski__agency-agents': '783f6a72bfd7f3135700ac273c619d92821b419a',
            'skills/juliusbrussee__caveman': '63a91ecadbf4c4719a4602a5abb00883f9966034',
            'skills/Egonex-AI__Understand-Anything': 'ba9ba1f73ce4f2ce35aeaaa55b01c9f8d4279bfe',
            'skills/Fission-AI__OpenSpec': '1b06fddd59d8e592d5b5794a1970b22867e85b1f',
            'skills/santifer__career-ops': '4e05cfda98b5dccfd2c664c12335ee20812b451b',
            'skills/Leonxlnx__taste-skill': '01d850496846d21f1f8f89fc8e08c58f76e4ae3e',
            'skills/mvanhorn__last30days-skill': '2cc88ecaf1f2445eae0276709cd60d9166e32c8d',
        },
        'raw_metrics': {
            'AM': {'stars': 180838, 'forks': 27876, 'watchers': 899, 'contribs': 183, 'skill_md': 572, 'avg_skill_bytes': 8847, 'days_alive': 115, 'stars_per_day': 1572.5, 'commits_per_day': 14.82, 'platforms': 7, 'last_push_days_ago': 0, 'reddit_posts': 8, 'reddit_comments': 96, 'reddit_avg_score': 126.5, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 10.5, 'value_density_pct': 11.3},
            'O': {'stars': 188498, 'forks': 16759, 'watchers': 753, 'contribs': 33, 'skill_md': 14, 'avg_skill_bytes': 8168, 'days_alive': 216, 'stars_per_day': 872.7, 'commits_per_day': 2.04, 'platforms': 6, 'last_push_days_ago': 0, 'reddit_posts': 40, 'reddit_comments': 243, 'reddit_avg_score': 31.4, 'hn_stories': 1, 'hn_comments': 0, 'hn_avg_points': 3.0, 'lesson_pct': 37.1, 'value_density_pct': 25.0},
            'NX': {'stars': 38735, 'forks': 4403, 'watchers': 142, 'contribs': 186, 'skill_md': 218, 'avg_skill_bytes': 3438, 'days_alive': 15, 'stars_per_day': 2582.3, 'commits_per_day': 42.5, 'platforms': 9, 'last_push_days_ago': 0, 'reddit_posts': 8, 'reddit_comments': 103, 'reddit_avg_score': 63.2, 'hn_stories': 1, 'hn_comments': 92, 'hn_avg_points': 230.0, 'lesson_pct': 18.5, 'value_density_pct': 13.3},
            'A': {'stars': 133251, 'forks': 15715, 'watchers': 865, 'contribs': 13, 'skill_md': 18, 'avg_skill_bytes': 10995, 'days_alive': 233, 'stars_per_day': 571.9, 'commits_per_day': 0.15, 'platforms': 1, 'last_push_days_ago': 4, 'reddit_posts': 169, 'reddit_comments': 6451, 'reddit_avg_score': 151.7, 'hn_stories': 8, 'hn_comments': 9, 'hn_avg_points': 5.0, 'lesson_pct': 31.5, 'value_density_pct': 22.4},
            'NL': {'stars': 77723, 'forks': 7977, 'watchers': 381, 'contribs': 31, 'skill_md': 7, 'avg_skill_bytes': 12272, 'days_alive': 164, 'stars_per_day': 474.0, 'commits_per_day': 0.82, 'platforms': 8, 'last_push_days_ago': 40, 'reddit_posts': 2, 'reddit_comments': 1, 'reddit_avg_score': 1.5, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 4.6, 'value_density_pct': 7.4},
            'AD': {'stars': 40580, 'forks': 4472, 'watchers': 255, 'contribs': 23, 'skill_md': 22, 'avg_skill_bytes': 10703, 'days_alive': 87, 'stars_per_day': 466.4, 'commits_per_day': 2.0, 'platforms': 7, 'last_push_days_ago': 3, 'reddit_posts': 6, 'reddit_comments': 54, 'reddit_avg_score': 22.2, 'hn_stories': 1, 'hn_comments': 212, 'hn_avg_points': 375.0, 'lesson_pct': 59.3, 'value_density_pct': 39.4},
            'CH': {'stars': 28215, 'forks': 4550, 'watchers': 288, 'contribs': 16, 'skill_md': 41, 'avg_skill_bytes': 11443, 'days_alive': 118, 'stars_per_day': 239.1, 'commits_per_day': 2.21, 'platforms': 5, 'last_push_days_ago': 7, 'reddit_posts': 5, 'reddit_comments': 97, 'reddit_avg_score': 38.2, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 18.4, 'value_density_pct': 13.5},
            'C': {'stars': 59518, 'forks': 6462, 'watchers': 399, 'contribs': 26, 'skill_md': 864, 'avg_skill_bytes': 3444, 'days_alive': 208, 'stars_per_day': 286.1, 'commits_per_day': 0.34, 'platforms': 7, 'last_push_days_ago': 6, 'reddit_posts': 5, 'reddit_comments': 98, 'reddit_avg_score': 87.8, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 94.7, 'value_density_pct': 57.3},
            'M': {'stars': 77173, 'forks': 6656, 'watchers': 532, 'contribs': 2, 'skill_md': 28, 'avg_skill_bytes': 3321, 'days_alive': 99, 'stars_per_day': 779.5, 'commits_per_day': 0.78, 'platforms': 2, 'last_push_days_ago': 1, 'reddit_posts': 14, 'reddit_comments': 303, 'reddit_avg_score': 92.9, 'hn_stories': 1, 'hn_comments': 0, 'hn_avg_points': 5.0, 'lesson_pct': 6.7, 'value_density_pct': 4.5},
            'OAI': {'stars': 18982, 'forks': 1259, 'watchers': 110, 'contribs': 34, 'skill_md': 43, 'avg_skill_bytes': 9435, 'days_alive': 169, 'stars_per_day': 112.3, 'commits_per_day': 0.64, 'platforms': 1, 'last_push_days_ago': 1, 'reddit_posts': 171, 'reddit_comments': 3358, 'reddit_avg_score': 54.9, 'hn_stories': 7, 'hn_comments': 16, 'hn_avg_points': 8.7, 'lesson_pct': 41.9, 'value_density_pct': 31.6},
            'MA': {'stars': 127547, 'forks': 12958, 'watchers': 671, 'contribs': 7, 'skill_md': 1, 'avg_skill_bytes': 2518, 'days_alive': 106, 'stars_per_day': 1203.3, 'commits_per_day': 0.26, 'platforms': 2, 'last_push_days_ago': 23, 'reddit_posts': 0, 'reddit_comments': 0, 'reddit_avg_score': 0.0, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 66.7, 'value_density_pct': 42.5},
            'K': {'stars': 30825, 'forks': 2100, 'watchers': 185, 'contribs': 13, 'skill_md': 5, 'avg_skill_bytes': 6040, 'days_alive': 131, 'stars_per_day': 235.3, 'commits_per_day': 0.3, 'platforms': 3, 'last_push_days_ago': 6, 'reddit_posts': 2, 'reddit_comments': 19, 'reddit_avg_score': 65.0, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 18.2, 'value_density_pct': 10.9},
            'V': {'stars': 26494, 'forks': 2416, 'watchers': 114, 'contribs': 21, 'skill_md': 7, 'avg_skill_bytes': 7224, 'days_alive': 156, 'stars_per_day': 169.8, 'commits_per_day': 1.27, 'platforms': 4, 'last_push_days_ago': 6, 'reddit_posts': 25, 'reddit_comments': 425, 'reddit_avg_score': 63.8, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 10.6, 'value_density_pct': 8.8},
            'GS': {'stars': 95212, 'forks': 14113, 'watchers': 575, 'contribs': 10, 'skill_md': 51, 'avg_skill_bytes': 52730, 'days_alive': 63, 'stars_per_day': 1511.3, 'commits_per_day': 4.33, 'platforms': 8, 'last_push_days_ago': 1, 'reddit_posts': 111, 'reddit_comments': 32442, 'reddit_avg_score': 2769.0, 'hn_stories': 4, 'hn_comments': 0, 'hn_avg_points': 2.2, 'lesson_pct': 56.0, 'value_density_pct': 39.3},
            'AA': {'stars': 96620, 'forks': 16028, 'watchers': 771, 'contribs': 72, 'skill_md': 222, 'avg_skill_bytes': 12293, 'days_alive': 212, 'stars_per_day': 455.8, 'commits_per_day': 1.37, 'platforms': 9, 'last_push_days_ago': 31, 'reddit_posts': 104, 'reddit_comments': 29053, 'reddit_avg_score': 2897.4, 'hn_stories': 2, 'hn_comments': 3, 'hn_avg_points': 1.5, 'lesson_pct': 25.2, 'value_density_pct': 18.3},
            'CV': {'stars': 60365, 'forks': 3346, 'watchers': 141, 'contribs': 29, 'skill_md': 15, 'avg_skill_bytes': 3266, 'days_alive': 39, 'stars_per_day': 1547.8, 'commits_per_day': 4.67, 'platforms': 9, 'last_push_days_ago': 1, 'reddit_posts': 105, 'reddit_comments': 15705, 'reddit_avg_score': 788.8, 'hn_stories': 3, 'hn_comments': 1, 'hn_avg_points': 3.0, 'lesson_pct': 22.0, 'value_density_pct': 14.2},
            'UA': {'stars': 62155, 'forks': 5129, 'watchers': 200, 'contribs': 43, 'skill_md': 8, 'avg_skill_bytes': 9974, 'days_alive': 94, 'stars_per_day': 661.2, 'commits_per_day': 6.05, 'platforms': 6, 'last_push_days_ago': 1, 'reddit_posts': -1, 'reddit_comments': -1, 'reddit_avg_score': -1.0, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 14.2, 'value_density_pct': 16.1},
            'OS': {'stars': 55241, 'forks': 3866, 'watchers': 245, 'contribs': 60, 'skill_md': 0, 'avg_skill_bytes': 0, 'days_alive': 316, 'stars_per_day': 174.8, 'commits_per_day': 1.91, 'platforms': 3, 'last_push_days_ago': 4, 'reddit_posts': -1, 'reddit_comments': -1, 'reddit_avg_score': -1.0, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 5.8, 'value_density_pct': 4.7},
            'CO': {'stars': 54306, 'forks': 10774, 'watchers': 207, 'contribs': 93, 'skill_md': 4, 'avg_skill_bytes': 4086, 'days_alive': 74, 'stars_per_day': 733.9, 'commits_per_day': 4.41, 'platforms': 4, 'last_push_days_ago': 1, 'reddit_posts': -1, 'reddit_comments': -1, 'reddit_avg_score': -1.0, 'hn_stories': 0, 'hn_comments': 0, 'hn_avg_points': 0.0, 'lesson_pct': 12.3, 'value_density_pct': 8.4},
            'TS': {'stars': 45534, 'forks': 3169, 'watchers': 132, 'contribs': 6, 'skill_md': 13, 'avg_skill_bytes': 23256, 'days_alive': 118, 'stars_per_day': 385.9, 'commits_per_day': 0.9, 'platforms': 1, 'last_push_days_ago': 5, 'reddit_posts': -1, 'reddit_comments': -1, 'reddit_avg_score': -1.0, 'hn_stories': 1, 'hn_comments': 0, 'hn_avg_points': 3.0, 'lesson_pct': 41.4, 'value_density_pct': 27.2},
            'L30': {'stars': 43681, 'forks': 3592, 'watchers': 153, 'contribs': 48, 'skill_md': 1, 'avg_skill_bytes': 140801, 'days_alive': 145, 'stars_per_day': 301.2, 'commits_per_day': 4.37, 'platforms': 3, 'last_push_days_ago': 0, 'reddit_posts': -1, 'reddit_comments': -1, 'reddit_avg_score': -1.0, 'hn_stories': 1, 'hn_comments': 0, 'hn_avg_points': 2.0, 'lesson_pct': 14.3, 'value_density_pct': 16.0},
        },
        'scores': {
            'AM': {'D1': 9, 'D2': 9, 'D3': 10, 'D4': 10, 'D5': 10, 'D6': 9, 'D7': 9, 'D8': 9, 'D9': 6, 'D10': 5, 'D11': 10, 'D12': 10, 'D13': 8, 'D14': 10, 'D15': 5, 'D16': 5, 'D17': 9, 'D18': 1, 'D19': 1, 'D20': 5, 'D21': 4},  # 154
            'O': {'D1': 8, 'D2': 10, 'D3': 9, 'D4': 8, 'D5': 10, 'D6': 7, 'D7': 7, 'D8': 3, 'D9': 5, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 7, 'D14': 9, 'D15': 9, 'D16': 7, 'D17': 3, 'D18': 6, 'D19': 6, 'D20': 6, 'D21': 7},  # 150
            'NX': {'D1': 10, 'D2': 4, 'D3': 3, 'D4': 2, 'D5': 10, 'D6': 10, 'D7': 10, 'D8': 8, 'D9': 3, 'D10': 4, 'D11': 10, 'D12': 10, 'D13': 10, 'D14': 8, 'D15': 8, 'D16': 6, 'D17': 5, 'D18': 9, 'D19': 9, 'D20': 9, 'D21': 4},  # 152
            'A': {'D1': 6, 'D2': 9, 'D3': 8, 'D4': 9, 'D5': 8, 'D6': 1, 'D7': 3, 'D8': 3, 'D9': 9, 'D10': 6, 'D11': 6, 'D12': 6, 'D13': 1, 'D14': 8, 'D15': 10, 'D16': 9, 'D17': 9, 'D18': 9, 'D19': 7, 'D20': 3, 'D21': 6},  # 136
            'NL': {'D1': 5, 'D2': 7, 'D3': 6, 'D4': 5, 'D5': 2, 'D6': 6, 'D7': 6, 'D8': 2, 'D9': 9, 'D10': 8, 'D11': 9, 'D12': 8, 'D13': 9, 'D14': 4, 'D15': 6, 'D16': 2, 'D17': 2, 'D18': 1, 'D19': 1, 'D20': 2, 'D21': 2},  # 102
            'AD': {'D1': 5, 'D2': 4, 'D3': 4, 'D4': 3, 'D5': 8, 'D6': 7, 'D7': 4, 'D8': 4, 'D9': 8, 'D10': 3, 'D11': 9, 'D12': 8, 'D13': 8, 'D14': 8, 'D15': 7, 'D16': 3, 'D17': 2, 'D18': 10, 'D19': 10, 'D20': 4, 'D21': 9},  # 128
            'CH': {'D1': 3, 'D2': 2, 'D3': 4, 'D4': 4, 'D5': 6, 'D6': 8, 'D7': 4, 'D8': 6, 'D9': 9, 'D10': 6, 'D11': 8, 'D12': 9, 'D13': 6, 'D14': 4, 'D15': 6, 'D16': 4, 'D17': 4, 'D18': 1, 'D19': 1, 'D20': 3, 'D21': 5},  # 103
            'C': {'D1': 4, 'D2': 5, 'D3': 5, 'D4': 5, 'D5': 7, 'D6': 3, 'D7': 5, 'D8': 10, 'D9': 3, 'D10': 1, 'D11': 8, 'D12': 4, 'D13': 8, 'D14': 9, 'D15': 3, 'D16': 4, 'D17': 7, 'D18': 1, 'D19': 1, 'D20': 8, 'D21': 10},  # 111
            'M': {'D1': 7, 'D2': 6, 'D3': 5, 'D4': 6, 'D5': 9, 'D6': 5, 'D7': 1, 'D8': 5, 'D9': 2, 'D10': 2, 'D11': 7, 'D12': 6, 'D13': 2, 'D14': 6, 'D15': 7, 'D16': 7, 'D17': 8, 'D18': 6, 'D19': 7, 'D20': 9, 'D21': 1},  # 114
            'OAI': {'D1': 1, 'D2': 1, 'D3': 1, 'D4': 1, 'D5': 9, 'D6': 4, 'D7': 8, 'D8': 7, 'D9': 7, 'D10': 9, 'D11': 3, 'D12': 3, 'D13': 1, 'D14': 7, 'D15': 10, 'D16': 9, 'D17': 4, 'D18': 8, 'D19': 8, 'D20': 4, 'D21': 8},  # 113
            'MA': {'D1': 9, 'D2': 8, 'D3': 7, 'D4': 7, 'D5': 4, 'D6': 2, 'D7': 2, 'D8': 1, 'D9': 1, 'D10': 7, 'D11': 7, 'D12': 3, 'D13': 2, 'D14': 1, 'D15': 8, 'D16': 1, 'D17': 1, 'D18': 1, 'D19': 1, 'D20': 10, 'D21': 9},  # 92
            'K': {'D1': 2, 'D2': 3, 'D3': 2, 'D4': 2, 'D5': 7, 'D6': 3, 'D7': 3, 'D8': 1, 'D9': 4, 'D10': 2, 'D11': 4, 'D12': 3, 'D13': 4, 'D14': 3, 'D15': 7, 'D16': 3, 'D17': 7, 'D18': 1, 'D19': 1, 'D20': 7, 'D21': 3},  # 72
            'V': {'D1': 2, 'D2': 2, 'D3': 3, 'D4': 2, 'D5': 7, 'D6': 6, 'D7': 4, 'D8': 2, 'D9': 5, 'D10': 10, 'D11': 8, 'D12': 6, 'D13': 5, 'D14': 4, 'D15': 9, 'D16': 8, 'D17': 6, 'D18': 1, 'D19': 1, 'D20': 7, 'D21': 3},  # 101
            'GS': {'D1': 9, 'D2': 7, 'D3': 8, 'D4': 7, 'D5': 9, 'D6': 8, 'D7': 3, 'D8': 7, 'D9': 10, 'D10': 3, 'D11': 9, 'D12': 9, 'D13': 9, 'D14': 9, 'D15': 8, 'D16': 10, 'D17': 10, 'D18': 7, 'D19': 5, 'D20': 1, 'D21': 8},  # 156
            'AA': {'D1': 5, 'D2': 7, 'D3': 8, 'D4': 8, 'D5': 3, 'D6': 6, 'D7': 8, 'D8': 8, 'D9': 9, 'D10': 1, 'D11': 10, 'D12': 9, 'D13': 10, 'D14': 10, 'D15': 7, 'D16': 10, 'D17': 10, 'D18': 6, 'D19': 4, 'D20': 2, 'D21': 5},  # 146
            'CV': {'D1': 9, 'D2': 6, 'D3': 3, 'D4': 2, 'D5': 9, 'D6': 9, 'D7': 6, 'D8': 3, 'D9': 2, 'D10': 5, 'D11': 8, 'D12': 9, 'D13': 10, 'D14': 4, 'D15': 8, 'D16': 9, 'D17': 10, 'D18': 6, 'D19': 6, 'D20': 9, 'D21': 4},  # 137
            'UA': {'D1': 7, 'D2': 6, 'D3': 4, 'D4': 3, 'D5': 10, 'D6': 9, 'D7': 7, 'D8': 2, 'D9': 7, 'D10': 8, 'D11': 8, 'D12': 9, 'D13': 8, 'D14': 7, 'D15': 8, 'D16': 1, 'D17': 1, 'D18': 1, 'D19': 1, 'D20': 5, 'D21': 5},  # 117
            'OS': {'D1': 2, 'D2': 5, 'D3': 4, 'D4': 3, 'D5': 8, 'D6': 7, 'D7': 8, 'D8': 1, 'D9': 1, 'D10': 8, 'D11': 8, 'D12': 9, 'D13': 5, 'D14': 7, 'D15': 8, 'D16': 1, 'D17': 1, 'D18': 1, 'D19': 1, 'D20': 6, 'D21': 3},  # 97
            'CO': {'D1': 7, 'D2': 5, 'D3': 7, 'D4': 3, 'D5': 10, 'D6': 8, 'D7': 8, 'D8': 2, 'D9': 3, 'D10': 8, 'D11': 9, 'D12': 10, 'D13': 6, 'D14': 3, 'D15': 7, 'D16': 1, 'D17': 1, 'D18': 1, 'D19': 1, 'D20': 8, 'D21': 5},  # 113
            'TS': {'D1': 4, 'D2': 4, 'D3': 3, 'D4': 2, 'D5': 7, 'D6': 6, 'D7': 2, 'D8': 3, 'D9': 9, 'D10': 3, 'D11': 6, 'D12': 5, 'D13': 1, 'D14': 4, 'D15': 7, 'D16': 1, 'D17': 1, 'D18': 2, 'D19': 2, 'D20': 3, 'D21': 9},  # 84
            'L30': {'D1': 4, 'D2': 4, 'D3': 3, 'D4': 2, 'D5': 10, 'D6': 8, 'D7': 7, 'D8': 1, 'D9': 10, 'D10': 6, 'D11': 7, 'D12': 8, 'D13': 5, 'D14': 4, 'D15': 7, 'D16': 1, 'D17': 1, 'D18': 2, 'D19': 2, 'D20': 1, 'D21': 5},  # 98
        },
    },
]

# Domain → recommended skill (used in §"By Domain" cell)
DOMAIN_RECS = [
    ('学 SKILL.md 官方规范 / Learn SKILL.md spec',           'A',   'Official Anthropic authority; D15=10 — frontmatter standard'),
    ('OpenAI Codex 用户 / Codex users',                       'OAI', 'Official Codex companion; D10=10 — richest supplementary docs'),
    ('大而全 agent 工程框架 / Comprehensive agent framework',  'AM',  'Overall #1 (129); commands + hooks + plugins + install scripts'),
    ('方法论 / 元技能 / Engineering methodology',             'O',   'Original "superpowers" framework; D15=9 — deepest methodology'),
    ('生产级软件工程 / Production engineering (general)',     'AD',  'Author authority + clean structure; D14=8'),
    ('TypeScript / Real engineering',                         'M',   'Matt Pocock TS-first lens; opinionated curation'),
    ('UI / UX 组件级 / Component-level UI/UX',                 'NL',  'D9=10 — most detailed color/font/component recipes'),
    ('设计系统 + 多平台输出 / Design systems + multi-platform','NX',  '19 skills + 71 design systems; D13=10 (9 agent platforms)'),
    ('营销 / Marketing / CRO / SEO',                          'CH',  'Only marketing-specialized repo; ships validate-skills.sh'),
    ('Obsidian / 知识管理 / Knowledge management',             'K',   'kepano (Obsidian creator) maintains; only repo covering Canvas/Bases'),
    ('零负担 CLAUDE.md / Drop-in single-file',                'MA',  'Single CLAUDE.md drop-in; Karpathy LLM-coding anti-patterns'),
    ('浏览 / 发现 skill / Discovery / browse',                'C',   '864 SKILL.md index; biggest awesome-list'),
    ('Vercel / Next.js / React 生产工程 / Vercel-native web',  'V',   'Official Vercel; 40+ React perf rules from Vercel engineering; D10=10 supplementary density'),
    ('YC / 创业公司角色分工 setup / Opinionated startup workflow', 'GS',  'Garry Tan exact Claude Code setup; 23 role-specialized agents (CEO/Designer/Eng-Mgr/Release/Doc/QA); deepest avg SKILL.md (52KB); top Reddit social signal'),
    ('Game 开发 / Game development',                              'AA',  '20 game-development agents — fills cohort game gap (the only repo with substantial game coverage)'),
    ('个性化 multi-role 创意 agency / Personality-driven agency',  'AA',  '222 agents across 18 domains (engineering/marketing/design/finance/spatial-computing/...); each agent has personality + emoji + vibe; ties NX on D13 (9 platforms)'),
    ('Token 优化 / Prompt engineering 节省 token',                'CV',  'caveman ("why use many token when few token do trick") — claims 65% token reduction via prompt-style minification; 9 platforms incl. antigravity; viral (60k stars in 39 days)'),
    ('理解既有代码库 / Understand existing codebase',             'UA',  'Egonex-AI/Understand-Anything — turns a codebase into an interactive knowledge graph; only repo specialized in reading existing code (🆕 v1.5)'),
    ('Spec-driven 开发 / Spec-driven development',                'OS',  'Fission-AI/OpenSpec — spec→tasks→implementation workflow; a spec tool (0 SKILL.md) with 517 docs (🆕 v1.5)'),
    ('求职 / 简历自动化 / Job-search & resume automation',        'CO',  'santifer/career-ops — CV/ATS/application tracking; strongest engineering hygiene in cohort (D12=10), 13-language READMEs (🆕 v1.5)'),
    ('设计品味 / 审美判断 / Design taste & aesthetic judgment',   'TS',  'Leonxlnx/taste-skill — steers agents away from generic output; highest lesson density among newcomers (41.4%) (🆕 v1.5)'),
    ('近期趋势研究 / Recent-trend research',                      'L30', 'mvanhorn/last30days-skill — last-30-day trends across Reddit/X/YouTube/HN/web; single 140KB SKILL.md (deepest in cohort) (🆕 v1.5)'),
]

# Chinese domain recommendations (parallel to DOMAIN_RECS, same order/codes).
DOMAIN_RECS_ZH = [
    ('学 SKILL.md 官方规范',              'A',   '官方 Anthropic 权威；D15=10 — frontmatter 标准制定者'),
    ('OpenAI Codex 用户',                 'OAI', '官方 Codex 配套；D10=10 — 辅助文档最丰富'),
    ('大而全 agent 工程框架',             'AM',  '综合 #1；commands + hooks + plugins + 安装脚本一站式'),
    ('方法论 / 元技能',                   'O',   '原创 "superpowers" 框架；D15=9 — 方法论最深'),
    ('生产级软件工程（通用）',            'AD',  '作者权威 + 结构清晰；D14=8'),
    ('TypeScript / 真实工程',             'M',   'Matt Pocock 的 TS 优先视角；强观点策展'),
    ('UI / UX 组件级',                    'NL',  'D9=10 — 最详尽的配色/字体/组件配方'),
    ('设计系统 + 多平台输出',             'NX',  '19 skills + 71 design systems；D13=10（9 个 agent 平台）'),
    ('营销 / CRO / SEO',                  'CH',  '唯一营销专项 repo；自带 validate-skills.sh'),
    ('Obsidian / 知识管理',               'K',   'kepano（Obsidian 作者）维护；唯一覆盖 Canvas/Bases'),
    ('零负担 CLAUDE.md（单文件 drop-in）','MA',  '单 CLAUDE.md drop-in；Karpathy LLM 编码反 anti-pattern'),
    ('浏览 / 发现 skill',                 'C',   '864 个 SKILL.md 索引；最大 awesome-list'),
    ('Vercel / Next.js / React 生产工程', 'V',   '官方 Vercel；40+ React 性能规则；D10=10 辅料密度'),
    ('YC / 创业公司角色分工 setup',       'GS',  'Garry Tan 实战 Claude Code setup；23 个角色 agent（CEO/Designer/Eng-Mgr/Release/Doc/QA）；avg SKILL.md 最深（52KB）；Reddit 社交信号最强'),
    ('Game 开发',                         'AA',  '20 个 game-development agents — 填补 cohort game 缺口（唯一有实质 game 覆盖的 repo）'),
    ('个性化 multi-role 创意 agency',     'AA',  '222 个 agent 跨 18 领域（工程/营销/设计/金融/空间计算…）；每个 agent 有 personality + emoji + vibe；D13 与 NX 并列（9 平台）'),
    ('Token 优化 / Prompt engineering 省 token', 'CV', 'caveman（"why use many token when few token do trick"）——号称 prompt 极简化省 65% token；9 平台含 antigravity；爆红（39 天 60k stars）'),
    ('理解既有代码库',                    'UA',  'Egonex-AI/Understand-Anything — 把代码库转成交互式知识图谱；cohort 唯一专做"读懂既有代码"（🆕 v1.5）'),
    ('Spec-driven 开发',                  'OS',  'Fission-AI/OpenSpec — spec→tasks→实现 工作流；spec 工具（0 个 SKILL.md）+ 517 docs（🆕 v1.5）'),
    ('求职 / 简历自动化',                 'CO',  'santifer/career-ops — CV/ATS/求职追踪；cohort 最强工程化（D12=10）+ 13 语言 README（🆕 v1.5）'),
    ('设计品味 / 审美判断',               'TS',  'Leonxlnx/taste-skill — 引导 agent 避免通用/平庸输出；新晋最高 lesson 密度（41.4%）（🆕 v1.5）'),
    ('近期趋势研究',                      'L30', 'mvanhorn/last30days-skill — 跨 Reddit/X/YouTube/HN/web 的近 30 天趋势；单个 140KB SKILL.md（全 cohort 最深）（🆕 v1.5）'),
]


def domain_recs_for(lang: str):
    return DOMAIN_RECS_ZH if lang == 'zh' else DOMAIN_RECS


# ──────────────────────────────────────────────────────────────────────────────
# COLOR
# ──────────────────────────────────────────────────────────────────────────────

def _interp(t: float) -> tuple[int, int, int]:
    """Map t∈[0,1] to (r,g,b) along worst→mid→best."""
    t = max(0.0, min(1.0, t))
    if t < 0.5:
        u = t / 0.5
        return 220, int(60 + 160 * u), 60
    u = (t - 0.5) / 0.5
    return int(220 - 180 * u), int(220 - 20 * u), int(60 + 40 * u)


def rgba(value, lo, hi, alpha: float = 0.35, inverted: bool = False) -> str:
    """Color a value within [lo, hi]. Higher=better unless inverted."""
    if value is None or hi == lo:
        return ''
    t = (value - lo) / (hi - lo)
    if inverted:
        t = 1.0 - t
    r, g, b = _interp(t)
    return f'rgba({r},{g},{b},{alpha})'


def bg(value, lo, hi, inverted: bool = False) -> str:
    c = rgba(value, lo, hi, inverted=inverted)
    return f'background-color:{c};' if c else ''


# Tier badge colors — thresholds rescaled for v1.3 max=210 (21 dims × 10).
def tier_for_total(v: int) -> str:
    if v >= 165: return 'S+'
    if v >= 145: return 'S'
    if v >= 125: return 'A'
    if v >= 100: return 'B'
    if v >= 80:  return 'C'
    return 'D'


_TIER_COLOR = {
    'S+': 'rgba(40,200,100,0.55)',
    'S':  'rgba(120,210,80,0.45)',
    'A':  'rgba(180,215,70,0.40)',
    'B':  'rgba(220,220,60,0.40)',
    'C':  'rgba(220,140,60,0.40)',
    'D':  'rgba(220,60,60,0.40)',
}


def tier_badge(tier: str) -> str:
    color = _TIER_COLOR.get(tier, 'rgba(200,200,200,0.4)')
    return (f'<span style="background:{color};padding:2px 8px;border-radius:3px;'
            f'font-weight:600;font-size:0.92em">{tier}</span>')


# ──────────────────────────────────────────────────────────────────────────────
# HTML BUILDING BLOCKS
# ──────────────────────────────────────────────────────────────────────────────

TD = 'padding:4px 10px'
TH = 'padding:4px 10px;background:#f0f0f0'

# (Color legend is rendered per-language via TXT['legend'] — see t().)


def iter_snapshot_repos(snapshot: dict):
    """Yield (code, owner, repo, label) for repos present in a snapshot, in REPOS order."""
    for code, owner, repo, label in REPOS:
        if code in snapshot.get('scores', {}):
            yield code, owner, repo, label


def _fetch_current_shas() -> dict:
    try:
        out = subprocess.check_output(
            ['git', 'submodule', 'status'], cwd=str(REPO_ROOT), text=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}
    result = {}
    for line in out.strip().splitlines():
        parts = line.strip().split()
        if len(parts) >= 2:
            sha = parts[0].lstrip('-+U')
            path = parts[1]
            result[path] = sha
    return result


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 1 · Overall Ranking
# ──────────────────────────────────────────────────────────────────────────────

def build_overall(snapshot: dict, lang: str = 'en') -> str:
    rows = []
    for code, owner, repo, label in iter_snapshot_repos(snapshot):
        sc = snapshot['scores'][code]
        m = snapshot['raw_metrics'][code]
        total = sum(sc.values())
        rows.append({
            'code': code,
            'repo': f'{owner}/{repo}',
            'total': total,
            'tier': tier_for_total(total),
            'd1': sc['D1'],
            'stars': m['stars'],
            'stars_per_day': m['stars_per_day'],
            'forks': m['forks'],
            'contribs': m['contribs'],
            'label': label,
        })
    rows.sort(key=lambda r: r['total'], reverse=True)

    def _range(key):
        vals = [r[key] for r in rows]
        return min(vals), max(vals)

    tot_lo, tot_hi = _range('total')
    star_lo, star_hi = _range('stars')
    spd_lo, spd_hi = _range('stars_per_day')
    fork_lo, fork_hi = _range('forks')
    con_lo, con_hi = _range('contribs')
    best = {
        'total': max(r['total'] for r in rows),
        'd1':    max(r['d1'] for r in rows),
        'stars': max(r['stars'] for r in rows),
        'stars_per_day': max(r['stars_per_day'] for r in rows),
        'forks': max(r['forks'] for r in rows),
        'contribs': max(r['contribs'] for r in rows),
    }

    parts = [
        f'<h3>{t("overall_h3", lang, date=snapshot["eval_date"][:10], ver=snapshot["version"])}</h3>',
        f'<p style="color:#888;font-size:0.85em;margin:4px 0 8px 0">{snapshot["note"]}</p>',
        t('legend', lang),
        '<table style="border-collapse:collapse;font-size:0.92em">',
        '<tr>'
        f'<th style="{TH};text-align:right">{t("th_num", lang)}</th>'
        f'<th style="{TH};text-align:left">{t("th_repo", lang)}</th>'
        f'<th style="{TH};text-align:center">{t("th_tier", lang)}</th>'
        f'<th style="{TH};text-align:right">{t("th_total210", lang)}</th>'
        f'<th style="{TH};text-align:right">{t("th_d1", lang)}</th>'
        f'<th style="{TH};text-align:right">{t("th_stars", lang)}</th>'
        f'<th style="{TH};text-align:right">{t("th_starsday", lang)}</th>'
        f'<th style="{TH};text-align:right">{t("th_forks", lang)}</th>'
        f'<th style="{TH};text-align:right">{t("th_contribs", lang)}</th>'
        f'<th style="{TH};text-align:left">{t("th_desc", lang)}</th>'
        '</tr>',
    ]

    def fmt_b(v, is_best, fmt='{:,}'):
        s = fmt.format(v)
        return f'<b>{s}</b>' if is_best else s

    for i, r in enumerate(rows, 1):
        parts.append(
            f'<tr>'
            f'<td style="{TD};text-align:right">{i}</td>'
            f'<td style="{TD};text-align:left"><b>{r["repo"]}</b></td>'
            f'<td style="{TD};text-align:center">{tier_badge(r["tier"])}</td>'
            f'<td style="{bg(r["total"], tot_lo, tot_hi)}{TD};text-align:right">'
            f'{fmt_b(r["total"], r["total"] == best["total"], "{}")}</td>'
            f'<td style="{bg(r["d1"], 1, 10)}{TD};text-align:right">'
            f'{fmt_b(r["d1"], r["d1"] == best["d1"], "{}")}</td>'
            f'<td style="{bg(r["stars"], star_lo, star_hi)}{TD};text-align:right">'
            f'{fmt_b(r["stars"], r["stars"] == best["stars"], "{:,}")}</td>'
            f'<td style="{bg(r["stars_per_day"], spd_lo, spd_hi)}{TD};text-align:right">'
            f'{fmt_b(r["stars_per_day"], r["stars_per_day"] == best["stars_per_day"], "{:,.0f}")}</td>'
            f'<td style="{bg(r["forks"], fork_lo, fork_hi)}{TD};text-align:right">'
            f'{fmt_b(r["forks"], r["forks"] == best["forks"], "{:,}")}</td>'
            f'<td style="{bg(r["contribs"], con_lo, con_hi)}{TD};text-align:right">'
            f'{fmt_b(r["contribs"], r["contribs"] == best["contribs"], "{:,}")}</td>'
            f'<td style="{TD};text-align:left;color:#666;font-size:0.88em">{r["label"]}</td>'
            f'</tr>'
        )
    parts.append('</table>')
    return ''.join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 2 · Full Score Matrix
# ──────────────────────────────────────────────────────────────────────────────

def build_score_matrix(snapshot: dict, lang: str = 'en') -> str:
    DIMS = dims_for(lang)
    rows = []
    for code, owner, repo, label in iter_snapshot_repos(snapshot):
        sc = snapshot['scores'][code]
        total = sum(sc.values())
        rows.append({'code': code, 'repo': f'{owner}/{repo}', 'total': total,
                     'tier': tier_for_total(total), 'scores': sc})
    rows.sort(key=lambda r: r['total'], reverse=True)
    best_per_dim = {did: max(r['scores'][did] for r in rows) for did in DIM_IDS}
    best_total = max(r['total'] for r in rows)
    tot_lo = min(r['total'] for r in rows)
    tot_hi = best_total

    th_cells = ['<th style="{}text-align:right">{}</th>'.format(TH + ';', t('th_num', lang)),
                '<th style="{}text-align:left">{}</th>'.format(TH + ';', t('th_repo', lang)),
                '<th style="{}text-align:center">{}</th>'.format(TH + ';', t('th_tier', lang))]
    for did, label, descr in DIMS:
        th_cells.append(
            f'<th style="{TH};text-align:right" title="{descr}">{did}</th>'
        )
    th_cells.append(f'<th style="{TH};text-align:right">{t("th_total", lang)}</th>')

    parts = [
        f'<h3>{t("matrix_h3", lang, ndim=len(DIMS), nrepo=len(rows), date=snapshot["eval_date"][:10])}</h3>',
        t('matrix_note', lang),
        t('legend', lang),
        '<table style="border-collapse:collapse;font-size:0.88em">',
        '<tr>' + ''.join(th_cells) + '</tr>',
    ]
    for i, r in enumerate(rows, 1):
        line = [
            f'<td style="{TD};text-align:right">{i}</td>',
            f'<td style="{TD};text-align:left;white-space:nowrap"><b>{r["repo"]}</b></td>',
            f'<td style="{TD};text-align:center">{tier_badge(r["tier"])}</td>',
        ]
        for did in DIM_IDS:
            v = r['scores'][did]
            cell = f'<b>{v}</b>' if v == best_per_dim[did] else str(v)
            line.append(f'<td style="{bg(v, 1, 10)}{TD};text-align:right">{cell}</td>')
        line.append(
            f'<td style="{bg(r["total"], tot_lo, tot_hi)}{TD};text-align:right">'
            f'{"<b>" + str(r["total"]) + "</b>" if r["total"] == best_total else r["total"]}'
            f'</td>'
        )
        parts.append('<tr>' + ''.join(line) + '</tr>')
    parts.append('</table>')

    # Dimension legend below
    parts.append(f'<details style="margin-top:12px"><summary style="cursor:pointer;color:#666;font-size:0.88em">{t("dim_defs", lang)}</summary>')
    parts.append('<table style="border-collapse:collapse;font-size:0.85em;margin-top:6px">')
    parts.append(f'<tr><th style="{TH};text-align:left">{t("th_id", lang)}</th><th style="{TH};text-align:left">{t("th_label", lang)}</th><th style="{TH};text-align:left">{t("th_descr", lang)}</th></tr>')
    for did, label, descr in DIMS:
        parts.append(f'<tr><td style="{TD};text-align:left"><b>{did}</b></td><td style="{TD};text-align:left">{label}</td><td style="{TD};text-align:left;color:#666">{descr}</td></tr>')
    parts.append('</table></details>')

    return ''.join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 3 · Raw Metrics
# ──────────────────────────────────────────────────────────────────────────────

def build_raw_metrics(snapshot: dict, lang: str = 'en') -> str:
    rows = []
    for code, owner, repo, _ in iter_snapshot_repos(snapshot):
        m = snapshot['raw_metrics'][code]
        rows.append({'code': code, 'repo': f'{owner}/{repo}', **m})
    # Sort by stars desc
    rows.sort(key=lambda r: r['stars'], reverse=True)

    cols = [
        # (key, txt_key, fmt, inverted)
        ('stars',           'rm_stars',           '{:,}',    False),
        ('stars_per_day',   'rm_stars_per_day',   '{:,.0f}', False),
        ('forks',           'rm_forks',           '{:,}',    False),
        ('watchers',        'rm_watchers',        '{:,}',    False),
        ('contribs',        'rm_contribs',        '{:,}',    False),
        ('days_alive',      'rm_days_alive',      '{}',      False),
        ('last_push_days_ago', 'rm_last_push',    '{}',      True),
        ('commits_per_day', 'rm_commits_per_day', '{:,.2f}', False),
        ('skill_md',        'rm_skill_md',        '{:,}',    False),
        ('avg_skill_bytes', 'rm_avg_skill_bytes', '{:,}',    False),
        ('platforms',       'rm_platforms',       '{}',      False),
    ]

    col_ranges = {}
    col_best = {}
    for k, _, _, inv in cols:
        vals = [r[k] for r in rows]
        col_ranges[k] = (min(vals), max(vals))
        col_best[k] = min(vals) if inv else max(vals)

    parts = [
        f'<h3>{t("raw_h3", lang, date=snapshot["eval_date"][:10])}</h3>',
        t('raw_note', lang),
        t('legend', lang),
        '<table style="border-collapse:collapse;font-size:0.88em">',
        '<tr><th style="{}text-align:right">{}</th><th style="{}text-align:left">{}</th>'.format(TH + ';', t('th_num', lang), TH + ';', t('th_repo', lang))
        + ''.join(f'<th style="{TH};text-align:right">{t(lbl_key, lang)}</th>' for _, lbl_key, _, _ in cols)
        + '</tr>',
    ]
    for i, r in enumerate(rows, 1):
        line = [
            f'<td style="{TD};text-align:right">{i}</td>',
            f'<td style="{TD};text-align:left;white-space:nowrap"><b>{r["repo"]}</b></td>',
        ]
        for k, _, fmt, inv in cols:
            v = r[k]
            lo, hi = col_ranges[k]
            cell = fmt.format(v)
            if v == col_best[k]:
                cell = f'<b>{cell}</b>'
            line.append(f'<td style="{bg(v, lo, hi, inverted=inv)}{TD};text-align:right">{cell}</td>')
        parts.append('<tr>' + ''.join(line) + '</tr>')
    parts.append('</table>')
    return ''.join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 4 · Submodule Snapshot & Drift
# ──────────────────────────────────────────────────────────────────────────────

def build_drift_table(snapshot: dict, current_shas: dict, lang: str = 'en') -> str:
    rows = []
    for path, recorded in snapshot['submodule_shas'].items():
        cur = current_shas.get(path)
        if cur is None:
            status, status_color = t('st_missing', lang), 'rgba(220,60,60,0.40)'
        elif cur == recorded:
            status, status_color = t('st_same', lang),    'rgba(40,200,100,0.35)'
        else:
            status, status_color = t('st_drifted', lang), 'rgba(220,220,60,0.40)'
        rows.append({
            'path':     path.replace('skills/', ''),
            'recorded': recorded,
            'current':  cur or '—',
            'status':   status,
            'color':    status_color,
        })
    parts = [
        f'<h3>{t("drift_h3", lang, date=snapshot["eval_date"][:10])}</h3>',
        f'<p style="color:#888;font-size:0.85em;margin:4px 0">'
        + t('drift_note', lang, eval=snapshot["eval_date"],
            now=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"))
        + '</p>',
        '<table style="border-collapse:collapse;font-size:0.92em">',
        f'<tr>'
        f'<th style="{TH};text-align:left">{t("th_submodule", lang)}</th>'
        f'<th style="{TH};text-align:left">{t("th_snapshot_sha", lang)}</th>'
        f'<th style="{TH};text-align:left">{t("th_current_sha", lang)}</th>'
        f'<th style="{TH};text-align:center">{t("th_status", lang)}</th>'
        f'</tr>',
    ]
    for r in rows:
        same = r['status'].startswith('✓')
        rec_display = f'<code style="font-size:0.85em">{r["recorded"][:10]}</code>'
        cur_display = f'<code style="font-size:0.85em">{r["current"][:10] if r["current"] != "—" else "—"}</code>'
        if not same and r['current'] != '—':
            cur_display = f'<b>{cur_display}</b>'
        parts.append(
            f'<tr>'
            f'<td style="{TD};text-align:left">{r["path"]}</td>'
            f'<td style="{TD};text-align:left">{rec_display}</td>'
            f'<td style="{TD};text-align:left">{cur_display}</td>'
            f'<td style="background:{r["color"]};{TD};text-align:center;font-weight:600">{r["status"]}</td>'
            f'</tr>'
        )
    parts.append('</table>')
    return ''.join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 5 · By Domain
# ──────────────────────────────────────────────────────────────────────────────

def build_domain_recs(snapshot: dict, lang: str = 'en') -> str:
    total_lbl = '总分' if lang == 'zh' else 'Total'
    parts = [
        f'<h3>{t("domain_h3", lang, date=snapshot["eval_date"][:10])}</h3>',
        t('domain_note', lang),
        '<table style="border-collapse:collapse;font-size:0.92em">',
        f'<tr>'
        f'<th style="{TH};text-align:right">{t("th_num", lang)}</th>'
        f'<th style="{TH};text-align:left">{t("th_domain", lang)}</th>'
        f'<th style="{TH};text-align:left">{t("th_bestrepo", lang)}</th>'
        f'<th style="{TH};text-align:center">{t("th_tier", lang)}</th>'
        f'<th style="{TH};text-align:right">{total_lbl}</th>'
        f'<th style="{TH};text-align:left">{t("th_why", lang)}</th>'
        f'</tr>',
    ]
    for i, (domain, code, reason) in enumerate(domain_recs_for(lang), 1):
        if code not in snapshot['scores']:
            continue  # repo not present in this snapshot; skip domain entry
        _, owner, repo, _ = REPO_BY_CODE[code]
        total = sum(snapshot['scores'][code].values())
        tier = tier_for_total(total)
        parts.append(
            f'<tr>'
            f'<td style="{TD};text-align:right">{i}</td>'
            f'<td style="{TD};text-align:left">{domain}</td>'
            f'<td style="{TD};text-align:left;white-space:nowrap"><b>{owner}/{repo}</b></td>'
            f'<td style="{TD};text-align:center">{tier_badge(tier)}</td>'
            f'<td style="{TD};text-align:right;color:#666">{total}</td>'
            f'<td style="{TD};text-align:left;color:#555;font-size:0.92em">{reason}</td>'
            f'</tr>'
        )
    parts.append('</table>')
    return ''.join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 6 · Δ-diff (if ≥2 snapshots)
# ──────────────────────────────────────────────────────────────────────────────

def build_diff(snap_new: dict, snap_old: dict, lang: str = 'en') -> str:
    parts = [
        f'<h3>{t("diff_h3", lang, old=snap_old["eval_date"][:10], new=snap_new["eval_date"][:10])}</h3>',
        t('diff_note', lang),
        '<table style="border-collapse:collapse;font-size:0.88em">',
        '<tr>'
        f'<th style="{TH};text-align:left">{t("th_repo", lang)}</th>'
        + ''.join(f'<th style="{TH};text-align:right">{did}</th>' for did in DIM_IDS)
        + f'<th style="{TH};text-align:right">{t("th_dtotal", lang)}</th>'
        '</tr>',
    ]
    NEW_BADGE = f'<span style="background:rgba(40,200,100,0.45);padding:1px 6px;border-radius:3px;font-size:0.78em;font-weight:600;margin-left:6px">{t("new_badge_txt", lang)}</span>'
    for code, owner, repo, _ in REPOS:
        new = snap_new['scores'].get(code)
        old = snap_old['scores'].get(code)
        if new is None:
            continue  # not in new snapshot; nothing to diff
        if old is None:
            # NEW entry — display raw scores with NEW badge, neutral background
            dtot = sum(new.values())
            line = [f'<td style="{TD};text-align:left;white-space:nowrap"><b>{owner}/{repo}</b>{NEW_BADGE}</td>']
            for did in DIM_IDS:
                v = new[did]
                line.append(f'<td style="background-color:rgba(120,160,220,0.20);{TD};text-align:right">{v}*</td>')
            line.append(f'<td style="background-color:rgba(120,160,220,0.30);{TD};text-align:right;font-weight:600">{dtot}*</td>')
            parts.append('<tr>' + ''.join(line) + '</tr>')
            continue
        deltas = {did: new.get(did, 0) - old.get(did, 0) for did in DIM_IDS}
        dtot = sum(deltas.values())
        line = [f'<td style="{TD};text-align:left;white-space:nowrap"><b>{owner}/{repo}</b></td>']
        for did in DIM_IDS:
            d = deltas[did]
            color = rgba(d, -5, 5)
            sign = '+' if d > 0 else ''
            line.append(f'<td style="background-color:{color};{TD};text-align:right">{sign}{d}</td>' if color else f'<td style="{TD};text-align:right">·</td>')
        c = rgba(dtot, -30, 30)
        line.append(f'<td style="background-color:{c};{TD};text-align:right;font-weight:600">{("+" if dtot > 0 else "") + str(dtot)}</td>' if c else f'<td style="{TD};text-align:right;font-weight:600">·</td>')
        parts.append('<tr>' + ''.join(line) + '</tr>')
    parts.append('</table>')
    return ''.join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# ASSEMBLY
# ──────────────────────────────────────────────────────────────────────────────

def make_code_cell_with_html(title: str, html: str, exec_count: int) -> nbf.NotebookNode:
    cell = nbf.v4.new_code_cell(source=f'# {title}')
    cell.execution_count = exec_count
    cell.outputs = [
        nbf.v4.new_output(
            output_type='execute_result',
            execution_count=exec_count,
            data={'text/html': html},
            metadata={},
        )
    ]
    return cell


# Markdown cells + code-cell titles, per language.
INTRO = {
    'en': (
        '<!-- Pre-rendered HTML tables baked into outputs[].data["text/html"]. '
        'GitHub renders directly; no kernel needed. To update, edit EVALUATIONS '
        'in build_scoring_notebook.py and re-run that script. -->\n\n'
        '# Skill Repo Scoring\n\n'
        '> 🌐 **Language**: **🇬🇧 English** · [🇨🇳 中文](./scoring.cn.ipynb)\n\n'
        '**Latest snapshot**: `{date}` · `v{ver}` — _{note}_\n\n'
        '**Cohort**: {nrepo} skill-collection repos as submodules. **Dimensions**: {ndim} '
        '(see [`EVALUATION.en.md`](./EVALUATION.en.md)).\n\n'
        '**Maintenance**: edit `EVALUATIONS` list in `build_scoring_notebook.py`, '
        'append a new dict (never modify history), then `python3 build_scoring_notebook.py` '
        '(regenerates both `scoring.ipynb` and `scoring.cn.ipynb`).'
    ),
    'zh': (
        '<!-- 预渲染的 HTML 表格已嵌入 outputs[].data["text/html"]，GitHub 直接渲染、无需 kernel。'
        '更新方式：编辑 build_scoring_notebook.py 中的 EVALUATIONS 后重跑该脚本。 -->\n\n'
        '# Skill Repo 评分\n\n'
        '> 🌐 **语言**: [🇬🇧 English](./scoring.ipynb) · **🇨🇳 中文**\n\n'
        '**最新快照**：`{date}` · `v{ver}` — _{note}_\n\n'
        '**Cohort**：{nrepo} 个 skill-collection repo（以 submodule 形式）。**维度**：{ndim} 个'
        '（详见 [`EVALUATION.md`](./EVALUATION.md)）。\n\n'
        '**维护**：编辑 `build_scoring_notebook.py` 的 `EVALUATIONS` 列表，追加一个新 dict（切勿修改历史），'
        '再 `python3 build_scoring_notebook.py`（会同时重新生成 `scoring.ipynb` 与 `scoring.cn.ipynb`）。'
    ),
}

CLOSING = {
    'en': (
        '## 📝 Long-term maintenance / 长期维护\n\n'
        'Each re-scoring run **appends** a new dict to `EVALUATIONS` in `build_scoring_notebook.py`. '
        'A snapshot dict contains:\n\n'
        '- `eval_date` — ISO-8601 UTC timestamp\n'
        '- `version` — human-readable tag\n'
        '- `submodule_shas` — `{path → SHA}` at scoring time (copy from `git submodule status`)\n'
        '- `raw_metrics` — `{code → {metric → value}}` (gh API + local `find`)\n'
        '- `scores` — `{code → {dim_id → 1-10 int}}` (rank-based)\n\n'
        '**Never modify history.** Stale snapshots stay as audit trail. When ≥2 snapshots exist, '
        'the Δ-diff section auto-renders.\n\n'
        '**To add a new cohort member**: register it in `REPOS` list, add scores for it in every '
        'snapshot (use `null` if not evaluated in older snapshots), then re-run the build script.'
    ),
    'zh': (
        '## 📝 长期维护 / Long-term maintenance\n\n'
        '每次重新评分都会向 `build_scoring_notebook.py` 的 `EVALUATIONS` **追加**一个新 dict。'
        '一个快照 dict 包含：\n\n'
        '- `eval_date` — ISO-8601 UTC 时间戳\n'
        '- `version` — 人类可读标签\n'
        '- `submodule_shas` — 评分时刻的 `{路径 → SHA}`（从 `git submodule status` 复制）\n'
        '- `raw_metrics` — `{code → {指标 → 值}}`（gh API + 本地 `find`）\n'
        '- `scores` — `{code → {维度id → 1-10 整数}}`（基于排名）\n\n'
        '**切勿修改历史。** 旧快照作为审计轨迹留存。当存在 ≥2 个快照时，Δ-diff 部分会自动渲染。\n\n'
        '**新增 cohort 成员**：在 `REPOS` 列表注册，并在每个快照里为它补分（旧快照未评测则用 `null`），'
        '再重跑构建脚本。'
    ),
}

CELL_TITLES = {
    'en': {'overall': 'Overall Ranking', 'matrix': 'Full Score Matrix', 'raw': 'Raw Metrics Snapshot',
           'drift': 'Submodule Snapshot & Drift', 'domain': 'Best Repo by Domain', 'diff': 'Snapshot Δ-diff'},
    'zh': {'overall': '总排行', 'matrix': '完整评分矩阵', 'raw': '原始指标快照',
           'drift': 'Submodule 快照与漂移', 'domain': '各领域最佳 repo', 'diff': '快照 Δ-diff'},
}


def build_cells(lang: str, snapshot: dict, current_shas: dict) -> list:
    ndim = len(DIMENSIONS)
    nrepo = len(snapshot['scores'])
    ct = CELL_TITLES[lang]
    cells = [
        nbf.v4.new_markdown_cell(INTRO[lang].format(
            date=snapshot['eval_date'], ver=snapshot['version'],
            note=snapshot['note'], nrepo=nrepo, ndim=ndim)),
        make_code_cell_with_html(ct['overall'], build_overall(snapshot, lang), 1),
        make_code_cell_with_html(f"{ct['matrix']} ({ndim} dims)", build_score_matrix(snapshot, lang), 2),
        make_code_cell_with_html(ct['raw'], build_raw_metrics(snapshot, lang), 3),
        make_code_cell_with_html(ct['drift'], build_drift_table(snapshot, current_shas, lang), 4),
        make_code_cell_with_html(ct['domain'], build_domain_recs(snapshot, lang), 5),
    ]
    if len(EVALUATIONS) >= 2:
        cells.append(make_code_cell_with_html(
            ct['diff'], build_diff(EVALUATIONS[-1], EVALUATIONS[-2], lang), 6))
    cells.append(nbf.v4.new_markdown_cell(CLOSING[lang]))
    return cells


def main():
    snapshot = EVALUATIONS[-1]
    current_shas = _fetch_current_shas()

    # (lang, output filename) — repo convention: no-suffix = primary, .cn = Chinese.
    for lang, fname in [('en', 'scoring.ipynb'), ('zh', 'scoring.cn.ipynb')]:
        cells = build_cells(lang, snapshot, current_shas)
        nb = nbf.v4.new_notebook()
        nb.cells = cells
        nb.metadata = {
            'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
            'language_info': {'name': 'python', 'version': '3.12'},
        }
        out_path = REPO_ROOT / fname
        with open(out_path, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)

        total_html = sum(
            len(''.join(o['data']['text/html']) if isinstance(o['data']['text/html'], list) else o['data']['text/html'])
            for c in cells if c.cell_type == 'code'
            for o in c.get('outputs', []) if 'data' in o and 'text/html' in o['data']
        )
        print(f'Wrote {out_path.name} — {len(cells)} cells, {total_html:,} bytes of pre-baked HTML')


if __name__ == '__main__':
    main()
