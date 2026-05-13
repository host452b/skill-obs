"""
Regenerates `scoring.ipynb` from source.

This script is the canonical structure of the scoring notebook. The notebook
itself supports day-to-day maintenance by appending new snapshots to its
`EVALUATIONS` list (no need to re-run this script for that). Re-run this only
if you want to restructure cells, add dimensions, or refresh the static layout.

Usage:
    python3 build_scoring_notebook.py
    jupyter nbconvert --to notebook --execute --inplace scoring.ipynb   # optional
"""
from __future__ import annotations

import nbformat as nbf


def md(text: str):
    return nbf.v4.new_markdown_cell(text.strip("\n"))


def code(src: str):
    return nbf.v4.new_code_cell(src.strip("\n"))


cells = []

# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(r"""
# Skill Repo 评测 / Scoring Notebook

**Cohort**：12 个 Agent Skills / Claude Skills / 类 Skills 仓库（明细见 `EVALUATION.md`，均作为本 repo 的 `submodule`）。

**Notebook 的作用**
- 用 **绿→黄→红分阶染色**（HTML 内置样式，不依赖外部 css）展示每个仓库在 15 个维度的得分。
- **快照式记录**：每次 re-score 都把当时的 *submodule SHA*、*评估时间戳*、*raw 指标*、*1-10 评分*一起写入 `EVALUATIONS` 列表（append-only）。
- **漂移检测**：对比 snapshot 中记录的 submodule SHA 与当前 HEAD，方便判断"评分基准是否已经过时"。
- **未来扩展**：方法论变了？— 在新 snapshot 里写新的 `scores`；维度变了？— 改一次 `DIMENSIONS` 然后重新评。

**Run**:
```bash
jupyter nbconvert --to html --execute scoring.ipynb       # 静态 HTML
jupyter notebook scoring.ipynb                            # 交互
```

**长期维护**：每次重新评估，往下方 `EVALUATIONS` 列表追加一份 dict 即可，不用动其他 cell。
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 2 — Imports, repo-root detection, current submodule SHA fetch
import datetime as _dt
import subprocess
from pathlib import Path

import pandas as pd

NB_DIR = Path.cwd()


def fetch_current_submodule_shas(repo_root: Path = NB_DIR) -> dict:
    '''Return {submodule_path: sha} via `git submodule status`. Empty dict on failure.'''
    try:
        out = subprocess.check_output(
            ['git', 'submodule', 'status'], cwd=str(repo_root), text=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}
    result = {}
    for line in out.strip().splitlines():
        parts = line.strip().split()
        if len(parts) >= 2:
            # Status prefix: '-' uninit / '+' drift / 'U' merge conflict
            sha = parts[0].lstrip('-+U')
            path = parts[1]
            result[path] = sha
    return result


CURRENT_SHAS = fetch_current_submodule_shas()
print(f'Detected {len(CURRENT_SHAS)} submodules at current HEAD.')
print(f'Notebook loaded at  {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")}')
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 3 — 15 dimensions + repo registry (stable identifiers)

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
]
DIM_IDS = [d[0] for d in DIMENSIONS]

# Code → (owner, repo, oneliner)
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
]
print(f'{len(DIMENSIONS)} dims × {len(REPOS)} repos = {len(DIMENSIONS) * len(REPOS)} cells.')
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 4 — EVALUATIONS history (append-only).
#
# Schema per entry:
#   eval_date:      ISO-8601 UTC string (when scoring was done)
#   version:        human-readable version tag
#   note:           free-form description
#   submodule_shas: {path -> 40-char SHA}    submodule HEAD at scoring time
#   raw_metrics:    {code -> {metric -> val}} preserved for re-scoring later
#   scores:         {code -> {dim_id -> 1..10 int}}
#
# To add a new snapshot: append a new dict (do NOT mutate old ones).

EVALUATIONS = [
    {
        'eval_date': '2026-05-13T08:00:00Z',
        'version': '1.0',
        'note': 'Initial baseline — 12-repo cohort, rank-based 1-10 scoring within cohort.',
        'submodule_shas': {
            'skills/affaan-m__everything-claude-code':     'd4728a0d801f1ebbc2384547009df17cbf16bfd1',
            'skills/obra__superpowers':                    'f2cbfbefebbfef77321e4c9abc9e949826bea9d7',
            'skills/nexu-io__open-design':                 '6341b2677aa7075b8027e3647310d61060b63e1b',
            'skills/anthropics__skills':                   'f458cee31a7577a47ba0c9a101976fa599385174',
            'skills/nextlevelbuilder__ui-ux-pro-max-skill':'b7e3af80f6e331f6fb456667b82b12cade7c9d35',
            'skills/addyosmani__agent-skills':             '3ff4b518b3cd3077ca27cf883aa21d21faf53802',
            'skills/coreyhaines31__marketingskills':       '906c2fb28e471c5b1d149d4159ec5ddb40b7c364',
            'skills/ComposioHQ__awesome-claude-skills':    'f2b5e29bc315f04c8e09591ba275f4c4f7d4b8fe',
            'skills/mattpocock__skills':                   'f304057d61d3df3c9fd992ac2b6e3833cb9325fb',
            'skills/openai__skills':                       'c25113bf4c64c8dba6bfe61acf06051d79aa43f6',
            'skills/multica-ai__andrej-karpathy-skills':   '2c606141936f1eeef17fa3043a72095b4765b9c2',
            'skills/kepano__obsidian-skills':              'ac9398734fe719565809f7a6048b05c36b1ca38f',
        },
        'raw_metrics': {
            'AM':  {'stars': 180838, 'forks': 27876, 'watchers': 899, 'contribs': 183, 'skill_md': 572, 'avg_skill_bytes': 8847,  'days_alive': 115, 'stars_per_day': 1572.5, 'commits_per_day': 14.82, 'platforms': 7},
            'O':   {'stars': 188498, 'forks': 16759, 'watchers': 753, 'contribs': 33,  'skill_md': 14,  'avg_skill_bytes': 8168,  'days_alive': 216, 'stars_per_day': 872.7,  'commits_per_day': 2.04,  'platforms': 6},
            'NX':  {'stars': 38735,  'forks': 4403,  'watchers': 142, 'contribs': 186, 'skill_md': 218, 'avg_skill_bytes': 3438,  'days_alive': 15,  'stars_per_day': 2582.3, 'commits_per_day': 42.5,  'platforms': 9},
            'A':   {'stars': 133251, 'forks': 15715, 'watchers': 865, 'contribs': 13,  'skill_md': 18,  'avg_skill_bytes': 10995, 'days_alive': 233, 'stars_per_day': 571.9,  'commits_per_day': 0.15,  'platforms': 1},
            'NL':  {'stars': 77723,  'forks': 7977,  'watchers': 381, 'contribs': 31,  'skill_md': 7,   'avg_skill_bytes': 12272, 'days_alive': 164, 'stars_per_day': 474.0,  'commits_per_day': 0.82,  'platforms': 8},
            'AD':  {'stars': 40580,  'forks': 4472,  'watchers': 255, 'contribs': 23,  'skill_md': 22,  'avg_skill_bytes': 10703, 'days_alive': 87,  'stars_per_day': 466.4,  'commits_per_day': 2.0,   'platforms': 7},
            'CH':  {'stars': 28215,  'forks': 4550,  'watchers': 288, 'contribs': 16,  'skill_md': 41,  'avg_skill_bytes': 11443, 'days_alive': 118, 'stars_per_day': 239.1,  'commits_per_day': 2.21,  'platforms': 5},
            'C':   {'stars': 59518,  'forks': 6462,  'watchers': 399, 'contribs': 26,  'skill_md': 864, 'avg_skill_bytes': 3444,  'days_alive': 208, 'stars_per_day': 286.1,  'commits_per_day': 0.34,  'platforms': 7},
            'M':   {'stars': 77173,  'forks': 6656,  'watchers': 532, 'contribs': 2,   'skill_md': 28,  'avg_skill_bytes': 3321,  'days_alive': 99,  'stars_per_day': 779.5,  'commits_per_day': 0.78,  'platforms': 2},
            'OAI': {'stars': 18982,  'forks': 1259,  'watchers': 110, 'contribs': 34,  'skill_md': 43,  'avg_skill_bytes': 9435,  'days_alive': 169, 'stars_per_day': 112.3,  'commits_per_day': 0.64,  'platforms': 1},
            'MA':  {'stars': 127547, 'forks': 12958, 'watchers': 671, 'contribs': 7,   'skill_md': 1,   'avg_skill_bytes': 2518,  'days_alive': 106, 'stars_per_day': 1203.3, 'commits_per_day': 0.26,  'platforms': 2},
            'K':   {'stars': 30825,  'forks': 2100,  'watchers': 185, 'contribs': 13,  'skill_md': 5,   'avg_skill_bytes': 6040,  'days_alive': 131, 'stars_per_day': 235.3,  'commits_per_day': 0.30,  'platforms': 3},
        },
        'scores': {
            #     D1   D2   D3   D4   D5   D6   D7   D8   D9   D10  D11  D12  D13  D14  D15
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
    # ── Append new snapshots here as the cohort evolves ───────────────────────
]

print(f'Loaded {len(EVALUATIONS)} evaluation snapshot(s):')
for ev in EVALUATIONS:
    print(f"  {ev['eval_date']}  v{ev['version']:<5}  {ev['note']}")
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 5 — Staged green→red coloring (inline HTML CSS, no matplotlib needed).

def stage_color(v):
    '''9-stage gradient for 1..10 scores.'''
    try:
        v = float(v)
    except (TypeError, ValueError):
        return ''
    if v >= 9:  return 'background-color:#006837;color:#fff;font-weight:600;'
    if v >= 8:  return 'background-color:#1a9850;color:#fff;'
    if v >= 7:  return 'background-color:#66bd63;'
    if v >= 6:  return 'background-color:#a6d96a;'
    if v >= 5:  return 'background-color:#fee08b;'
    if v >= 4:  return 'background-color:#fdae61;'
    if v >= 3:  return 'background-color:#f46d43;color:#fff;'
    if v >= 2:  return 'background-color:#d73027;color:#fff;'
    return 'background-color:#a50026;color:#fff;font-weight:600;'


def total_color(v):
    '''7-stage gradient for the 15..150 Total column.'''
    try:
        v = float(v)
    except (TypeError, ValueError):
        return ''
    if v >= 120: return 'background-color:#006837;color:#fff;font-weight:700;'
    if v >= 105: return 'background-color:#1a9850;color:#fff;font-weight:600;'
    if v >= 90:  return 'background-color:#66bd63;font-weight:600;'
    if v >= 75:  return 'background-color:#fee08b;font-weight:600;'
    if v >= 60:  return 'background-color:#fdae61;font-weight:600;'
    if v >= 45:  return 'background-color:#f46d43;color:#fff;font-weight:600;'
    return 'background-color:#d73027;color:#fff;font-weight:600;'


def tier_for_total(v):
    if v >= 120: return 'S+'
    if v >= 105: return 'S'
    if v >= 90:  return 'A'
    if v >= 75:  return 'B'
    if v >= 60:  return 'C'
    return 'D'


def column_color(col_values):
    '''Closure: rank a column's values into the same 9-stage gradient.'''
    col_min = min(v for v in col_values if v is not None)
    col_max = max(v for v in col_values if v is not None)
    span = col_max - col_min if col_max != col_min else 1

    def _color(v):
        try:
            v = float(v)
        except (TypeError, ValueError):
            return ''
        pct = (v - col_min) / span  # 0..1, higher is better
        if pct >= 0.88: return 'background-color:#006837;color:#fff;font-weight:600;'
        if pct >= 0.75: return 'background-color:#1a9850;color:#fff;'
        if pct >= 0.62: return 'background-color:#66bd63;'
        if pct >= 0.50: return 'background-color:#a6d96a;'
        if pct >= 0.37: return 'background-color:#fee08b;'
        if pct >= 0.25: return 'background-color:#fdae61;'
        if pct >= 0.12: return 'background-color:#f46d43;color:#fff;'
        return 'background-color:#d73027;color:#fff;'

    return _color


print('Color functions ready (stage_color, total_color, column_color, tier_for_total).')
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 6 — Build the score matrix and render with staged coloring.

def build_score_df(snapshot):
    rows = []
    for code_id, owner, repo, label in REPOS:
        scores = snapshot['scores'][code_id]
        row = {'Repo': f'{owner}/{repo}', 'Code': code_id}
        for did in DIM_IDS:
            row[did] = scores.get(did)
        row['Total'] = sum(scores.values())
        row['Tier'] = tier_for_total(row['Total'])
        rows.append(row)
    return (pd.DataFrame(rows)
              .set_index('Repo')
              .sort_values('Total', ascending=False))


def render_styled(df, caption=''):
    return (df.style
              .map(stage_color, subset=DIM_IDS)
              .map(total_color, subset=['Total'])
              .set_caption(caption)
              .set_table_styles([
                  {'selector': 'caption',
                   'props': [('caption-side', 'top'), ('font-weight', '600'),
                             ('font-size', '14px'), ('padding', '6px 0'),
                             ('text-align', 'left')]},
                  {'selector': 'th',
                   'props': [('text-align', 'center'), ('padding', '4px 8px'),
                             ('background-color', '#f5f5f5')]},
                  {'selector': 'td',
                   'props': [('text-align', 'center'), ('padding', '4px 8px'),
                             ('font-variant-numeric', 'tabular-nums')]},
              ])
              .format(precision=0))


latest = EVALUATIONS[-1]
df_scores = build_score_df(latest)
caption = f"Score Matrix · {latest['eval_date']} · v{latest['version']} — {latest['note']}"
render_styled(df_scores, caption=caption)
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 7 — Top-line ranking with badge.

def build_ranking_df(snapshot):
    rows = []
    for code_id, owner, repo, label in REPOS:
        scores = snapshot['scores'][code_id]
        total = sum(scores.values())
        rows.append({
            'Repo':         f'{owner}/{repo}',
            'Code':         code_id,
            'Total':        total,
            'Tier':         tier_for_total(total),
            'D1 ⭐ (vel)':   scores['D1'],
            'One-liner':    label,
        })
    df = (pd.DataFrame(rows)
            .sort_values('Total', ascending=False)
            .reset_index(drop=True))
    df.index = df.index + 1
    df.index.name = 'Rank'
    return df


ranking = build_ranking_df(latest)
(ranking.style
       .map(total_color, subset=['Total'])
       .map(stage_color, subset=['D1 ⭐ (vel)'])
       .set_caption(f"Overall Ranking · {latest['eval_date']}")
       .set_table_styles([
           {'selector': 'caption', 'props': [('caption-side', 'top'), ('font-weight', '600'),
                                              ('font-size', '14px'), ('padding', '6px 0')]},
           {'selector': 'th', 'props': [('padding', '4px 8px'), ('background-color', '#f5f5f5')]},
           {'selector': 'td', 'props': [('padding', '4px 8px'), ('font-variant-numeric', 'tabular-nums')]},
       ])
       .format({'Total': '{:.0f}', 'D1 ⭐ (vel)': '{:.0f}'}))
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 8 — Drift detection: snapshot SHAs vs current submodule HEAD.

def drift_report(snapshot, current_shas=None):
    if current_shas is None:
        current_shas = CURRENT_SHAS
    rows = []
    for path, recorded_sha in snapshot['submodule_shas'].items():
        cur = current_shas.get(path)
        if cur is None:
            status = '✗ missing'
        elif cur == recorded_sha:
            status = '✓ same'
        else:
            status = '⚠ drifted'
        rows.append({
            'Submodule':    path.replace('skills/', ''),
            'Snapshot SHA': recorded_sha[:10],
            'Current SHA':  (cur or '—')[:10],
            'Status':       status,
        })
    return pd.DataFrame(rows)


def style_drift(df):
    def _row_bg(r):
        if r['Status'].startswith('✓'): bg = '#d4edda'
        elif r['Status'].startswith('⚠'): bg = '#fff3cd'
        else: bg = '#f8d7da'
        return [f'background-color:{bg};'] * len(r)

    return (df.style
              .apply(_row_bg, axis=1)
              .set_caption(f"Submodule SHA drift vs. snapshot {latest['eval_date']}")
              .set_table_styles([
                  {'selector': 'caption', 'props': [('caption-side', 'top'), ('font-weight', '600'),
                                                     ('font-size', '14px'), ('padding', '6px 0')]},
                  {'selector': 'th', 'props': [('padding', '4px 8px'), ('background-color', '#f5f5f5')]},
                  {'selector': 'td', 'props': [('padding', '4px 8px'), ('font-family', 'monospace')]},
              ]))


style_drift(drift_report(latest))
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 9 — Raw metrics with per-column staged coloring (preserves audit trail).

def build_raw_df(snapshot):
    rows = []
    for code_id, owner, repo, _ in REPOS:
        m = snapshot.get('raw_metrics', {}).get(code_id, {})
        rows.append({'Repo': f'{owner}/{repo}', **m})
    return pd.DataFrame(rows).set_index('Repo')


def style_raw(df):
    styler = df.style
    color_cols = ['stars', 'forks', 'watchers', 'contribs', 'skill_md',
                  'avg_skill_bytes', 'stars_per_day', 'commits_per_day', 'platforms']
    for col in color_cols:
        if col in df.columns:
            styler = styler.map(column_color(df[col].dropna().tolist()), subset=[col])
    return (styler
            .set_caption(f"Raw Metrics · snapshot {latest['eval_date']} (higher = greener)")
            .set_table_styles([
                {'selector': 'caption', 'props': [('caption-side', 'top'), ('font-weight', '600'),
                                                    ('font-size', '14px'), ('padding', '6px 0')]},
                {'selector': 'th', 'props': [('padding', '4px 8px'), ('background-color', '#f5f5f5')]},
                {'selector': 'td', 'props': [('padding', '4px 8px'), ('font-variant-numeric', 'tabular-nums'),
                                              ('text-align', 'right')]},
            ])
            .format(precision=1))


style_raw(build_raw_df(latest))
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(code(r"""
# Cell 10 — Diff between the two latest snapshots (only renders if ≥2 exist).
from IPython.display import display, HTML

def diff_styled(d_new, d_old, caption=''):
    delta = d_new[DIM_IDS + ['Total']] - d_old[DIM_IDS + ['Total']]
    def _delta_color(v):
        try: v = float(v)
        except (TypeError, ValueError): return ''
        if v >= 3:  return 'background-color:#1a9850;color:#fff;'
        if v >= 1:  return 'background-color:#a6d96a;'
        if v == 0:  return ''
        if v >= -2: return 'background-color:#fdae61;'
        return 'background-color:#d73027;color:#fff;'
    return (delta.style
                 .map(_delta_color)
                 .format('{:+.0f}')
                 .set_caption(caption)
                 .set_table_styles([
                     {'selector': 'caption', 'props': [('caption-side', 'top'),
                                                        ('font-weight', '600'),
                                                        ('padding', '6px 0')]},
                 ]))


if len(EVALUATIONS) >= 2:
    df_new = build_score_df(EVALUATIONS[-1])
    df_old = build_score_df(EVALUATIONS[-2])
    caption = (f"Δ Scores · {EVALUATIONS[-2]['eval_date']} → {EVALUATIONS[-1]['eval_date']} "
               f"(positive = improved)")
    display(diff_styled(df_new, df_old, caption=caption))
else:
    display(HTML('<p style=\"color:#888;font-style:italic;\">'
                 'Only one snapshot loaded — diff view unlocks at ≥2.</p>'))
"""))

# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(r"""
## 📝 长期维护操作 / Adding a new snapshot

每次需要重新评估时，往 `EVALUATIONS` 列表（cell 4）**追加**（不要修改）一条新 dict：

```python
EVALUATIONS.append({
    'eval_date': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
    'version':   '1.1',
    'note':      '<本次评估的变更说明，例如：更新到最新 submodule HEAD>',
    'submodule_shas': {  # ← 从 `git submodule status` 复制
        # ...
    },
    'raw_metrics': {  # ← 从 `gh repo view` + 本地 `find` 重新采集
        # ...
    },
    'scores': {  # ← 用 rank-based 1-10 重新打分
        # ...
    },
})
```

### 步骤

1. **同步最新代码**：`git submodule update --remote`（如需引入最新 HEAD），或保持当前 SHA 不变。
2. **采集原始指标**（每个 repo）：
   ```bash
   gh repo view <owner>/<repo> --json stargazerCount,forkCount,watchers,createdAt,pushedAt,description \
     --jq '{stars: .stargazerCount, forks: .forkCount, watchers: .watchers.totalCount, created: .createdAt}'
   ```
   - 本地：`find skills/<dir> -name SKILL.md -not -path '*/.git/*' | wc -l`
3. **重新打分**（rank-based 1-10）：方法论见 `EVALUATION.md` §7。
4. **追加 snapshot** 并 re-run all cells；最新 snapshot 自动用于可视化。
5. **Cell 10 自动渲染 Δ-diff**：新旧两份 snapshot 间每个维度的得分变化。

### 注意

- **不要修改历史 snapshot**（破坏审计追溯）；若发现错评，写新 snapshot + 在 `note` 里说明 supersedes 即可。
- **submodule SHA 与 raw_metrics 必须同时记录**：方法论变了，靠 raw_metrics 重打分；submodule 更新了，靠 SHA 知道基准变了。
- **染色阈值**（cell 5）可以全局调整；改完后历史 snapshot 的视觉表现也会变（不修改数据）。
"""))

# ─────────────────────────────────────────────────────────────────────────────
nb = nbf.v4.new_notebook()
nb.cells = cells
nb.metadata = {
    'kernelspec': {
        'display_name': 'Python 3',
        'language': 'python',
        'name': 'python3',
    },
    'language_info': {
        'name': 'python',
        'version': '3.12',
    },
}

OUT = 'scoring.ipynb'
with open(OUT, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f'Wrote {OUT} — {len(cells)} cells')
