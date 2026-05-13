"""
Rebuild `scoring.ipynb` with pre-baked HTML outputs (GitHub-renderable).

Pattern (mirrors gguf_exp_on_mac/benchmark_visualization.ipynb):
  - Each code cell source is a one-line `# Title` comment.
  - outputs[0].data['text/html'] holds a pre-rendered colored table.
  - GitHub renders the notebook directly — no kernel, no execution needed.

Maintenance flow:
  1. Edit EVALUATIONS below (append a new dict; never modify history).
  2. python3 build_scoring_notebook.py
  3. git add scoring.ipynb build_scoring_notebook.py && git commit && git push

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
]
DIM_IDS = [d[0] for d in DIMENSIONS]

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
    # ── Append new snapshots here ─────────────────────────────────────────────
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
]


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


# Tier badge colors
def tier_for_total(v: int) -> str:
    if v >= 120: return 'S+'
    if v >= 105: return 'S'
    if v >= 90:  return 'A'
    if v >= 75:  return 'B'
    if v >= 60:  return 'C'
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

LEGEND = (
    '<p style="color:#666;font-size:0.85em;margin:4px 0">'
    'Color gradient: '
    '<span style="background:rgba(220,60,60,0.35);padding:2px 8px;border-radius:3px">worst</span> → '
    '<span style="background:rgba(220,220,60,0.35);padding:2px 8px;border-radius:3px">mid</span> → '
    '<span style="background:rgba(40,200,100,0.35);padding:2px 8px;border-radius:3px">best</span>'
    '&nbsp;·&nbsp;per-column normalized · column-best <b>bolded</b>'
    '</p>'
)


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

def build_overall(snapshot: dict) -> str:
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
        f'<h3>🏆 Overall Ranking — {snapshot["eval_date"][:10]} (v{snapshot["version"]})</h3>',
        f'<p style="color:#888;font-size:0.85em;margin:4px 0 8px 0">{snapshot["note"]}</p>',
        LEGEND,
        '<table style="border-collapse:collapse;font-size:0.92em">',
        '<tr>'
        f'<th style="{TH};text-align:right">#</th>'
        f'<th style="{TH};text-align:left">Repo</th>'
        f'<th style="{TH};text-align:center">Tier</th>'
        f'<th style="{TH};text-align:right">Total /150 ↑</th>'
        f'<th style="{TH};text-align:right">D1 ⭐ /10 ↑</th>'
        f'<th style="{TH};text-align:right">Stars ↑</th>'
        f'<th style="{TH};text-align:right">Stars/day ↑</th>'
        f'<th style="{TH};text-align:right">Forks ↑</th>'
        f'<th style="{TH};text-align:right">Contribs ↑</th>'
        f'<th style="{TH};text-align:left">Description</th>'
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

def build_score_matrix(snapshot: dict) -> str:
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

    th_cells = ['<th style="{}text-align:right">#</th>'.format(TH + ';'),
                '<th style="{}text-align:left">Repo</th>'.format(TH + ';'),
                '<th style="{}text-align:center">Tier</th>'.format(TH + ';')]
    for did, label, descr in DIMENSIONS:
        th_cells.append(
            f'<th style="{TH};text-align:right" title="{descr}">{did}</th>'
        )
    th_cells.append(f'<th style="{TH};text-align:right">Total ↑</th>')

    parts = [
        f'<h3>📋 Full Score Matrix · 15 Dimensions × 12 Repos — {snapshot["eval_date"][:10]}</h3>',
        '<p style="color:#666;font-size:0.85em;margin:4px 0">Each cell colored 1-10 within its dimension column. Column-best <b>bolded</b>. Hover header for definition.</p>',
        LEGEND,
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
    parts.append('<details style="margin-top:12px"><summary style="cursor:pointer;color:#666;font-size:0.88em">📖 Dimension definitions</summary>')
    parts.append('<table style="border-collapse:collapse;font-size:0.85em;margin-top:6px">')
    parts.append(f'<tr><th style="{TH};text-align:left">ID</th><th style="{TH};text-align:left">Label</th><th style="{TH};text-align:left">Description</th></tr>')
    for did, label, descr in DIMENSIONS:
        parts.append(f'<tr><td style="{TD};text-align:left"><b>{did}</b></td><td style="{TD};text-align:left">{label}</td><td style="{TD};text-align:left;color:#666">{descr}</td></tr>')
    parts.append('</table></details>')

    return ''.join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 3 · Raw Metrics
# ──────────────────────────────────────────────────────────────────────────────

def build_raw_metrics(snapshot: dict) -> str:
    rows = []
    for code, owner, repo, _ in iter_snapshot_repos(snapshot):
        m = snapshot['raw_metrics'][code]
        rows.append({'code': code, 'repo': f'{owner}/{repo}', **m})
    # Sort by stars desc
    rows.sort(key=lambda r: r['stars'], reverse=True)

    cols = [
        # (key, label, fmt, inverted)
        ('stars',           'Stars ↑',           '{:,}',    False),
        ('stars_per_day',   'Stars/day ↑',       '{:,.0f}', False),
        ('forks',           'Forks ↑',           '{:,}',    False),
        ('watchers',        'Watchers ↑',        '{:,}',    False),
        ('contribs',        'Contribs ↑',        '{:,}',    False),
        ('days_alive',      'Days alive',        '{}',      False),
        ('last_push_days_ago', 'Last push (d ago) ↓', '{}', True),
        ('commits_per_day', 'Commits/day ↑',     '{:,.2f}', False),
        ('skill_md',        'SKILL.md count ↑',  '{:,}',    False),
        ('avg_skill_bytes', 'Avg SKILL bytes ↑', '{:,}',    False),
        ('platforms',       'Agent platforms ↑', '{}',      False),
    ]

    col_ranges = {}
    col_best = {}
    for k, _, _, inv in cols:
        vals = [r[k] for r in rows]
        col_ranges[k] = (min(vals), max(vals))
        col_best[k] = min(vals) if inv else max(vals)

    parts = [
        f'<h3>📊 Raw Metrics Snapshot — {snapshot["eval_date"][:10]}</h3>',
        '<p style="color:#666;font-size:0.85em;margin:4px 0">↑ higher is better · ↓ lower is better. Per-column normalized.</p>',
        LEGEND,
        '<table style="border-collapse:collapse;font-size:0.88em">',
        '<tr><th style="{}text-align:right">#</th><th style="{}text-align:left">Repo</th>'.format(TH + ';', TH + ';')
        + ''.join(f'<th style="{TH};text-align:right">{lbl}</th>' for _, lbl, _, _ in cols)
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

def build_drift_table(snapshot: dict, current_shas: dict) -> str:
    rows = []
    for path, recorded in snapshot['submodule_shas'].items():
        cur = current_shas.get(path)
        if cur is None:
            status, status_color = '✗ missing', 'rgba(220,60,60,0.40)'
        elif cur == recorded:
            status, status_color = '✓ same',    'rgba(40,200,100,0.35)'
        else:
            status, status_color = '⚠ drifted', 'rgba(220,220,60,0.40)'
        rows.append({
            'path':     path.replace('skills/', ''),
            'recorded': recorded,
            'current':  cur or '—',
            'status':   status,
            'color':    status_color,
        })
    parts = [
        f'<h3>🔗 Submodule Snapshot & Drift — {snapshot["eval_date"][:10]}</h3>',
        f'<p style="color:#888;font-size:0.85em;margin:4px 0">'
        f'Snapshot SHAs captured at evaluation time ({snapshot["eval_date"]}); '
        f'current SHAs read at notebook build time ({_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")}).'
        f'</p>',
        '<table style="border-collapse:collapse;font-size:0.92em">',
        f'<tr>'
        f'<th style="{TH};text-align:left">Submodule</th>'
        f'<th style="{TH};text-align:left">Snapshot SHA</th>'
        f'<th style="{TH};text-align:left">Current SHA</th>'
        f'<th style="{TH};text-align:center">Status</th>'
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

def build_domain_recs(snapshot: dict) -> str:
    parts = [
        f'<h3>🎯 Best Repo by Domain — {snapshot["eval_date"][:10]}</h3>',
        '<p style="color:#666;font-size:0.85em;margin:4px 0">Tier badges from the snapshot above; descriptions are the discriminating signal for that domain.</p>',
        '<table style="border-collapse:collapse;font-size:0.92em">',
        f'<tr>'
        f'<th style="{TH};text-align:right">#</th>'
        f'<th style="{TH};text-align:left">Domain / Use case</th>'
        f'<th style="{TH};text-align:left">Best repo</th>'
        f'<th style="{TH};text-align:center">Tier</th>'
        f'<th style="{TH};text-align:right">Total</th>'
        f'<th style="{TH};text-align:left">Why</th>'
        f'</tr>',
    ]
    for i, (domain, code, reason) in enumerate(DOMAIN_RECS, 1):
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

def build_diff(snap_new: dict, snap_old: dict) -> str:
    parts = [
        f'<h3>🔁 Score Δ — {snap_old["eval_date"][:10]} → {snap_new["eval_date"][:10]}</h3>',
        '<p style="color:#666;font-size:0.85em;margin:4px 0">Per-dimension score change; positive (green) = improved.</p>',
        '<table style="border-collapse:collapse;font-size:0.88em">',
        '<tr>'
        f'<th style="{TH};text-align:left">Repo</th>'
        + ''.join(f'<th style="{TH};text-align:right">{did}</th>' for did in DIM_IDS)
        + f'<th style="{TH};text-align:right">ΔTotal</th>'
        '</tr>',
    ]
    NEW_BADGE = '<span style="background:rgba(40,200,100,0.45);padding:1px 6px;border-radius:3px;font-size:0.78em;font-weight:600;margin-left:6px">NEW</span>'
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
        deltas = {did: new[did] - old[did] for did in DIM_IDS}
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


def main():
    snapshot = EVALUATIONS[-1]
    current_shas = _fetch_current_shas()

    cells = []

    # Cell 0 — intro markdown
    cells.append(nbf.v4.new_markdown_cell(
        '<!-- Pre-rendered HTML tables baked into outputs[].data["text/html"]. '
        'GitHub renders directly; no kernel needed. To update, edit EVALUATIONS '
        'in build_scoring_notebook.py and re-run that script. -->\n\n'
        '# Skill Repo Scoring\n\n'
        f'**Latest snapshot**: `{snapshot["eval_date"]}` · `v{snapshot["version"]}` — _{snapshot["note"]}_\n\n'
        f'**Cohort**: 12 skill-collection repos as submodules. **Dimensions**: 15 (see §[`EVALUATION.md`](./EVALUATION.md)).\n\n'
        '**Maintenance**: edit `EVALUATIONS` list in `build_scoring_notebook.py`, '
        'append a new dict (never modify history), then `python3 build_scoring_notebook.py`.'
    ))

    # Cell 1 — Overall ranking
    cells.append(make_code_cell_with_html('Overall Ranking', build_overall(snapshot), 1))

    # Cell 2 — Full score matrix
    cells.append(make_code_cell_with_html('Full Score Matrix (15 dims)', build_score_matrix(snapshot), 2))

    # Cell 3 — Raw metrics
    cells.append(make_code_cell_with_html('Raw Metrics Snapshot', build_raw_metrics(snapshot), 3))

    # Cell 4 — Submodule drift
    cells.append(make_code_cell_with_html('Submodule Snapshot & Drift', build_drift_table(snapshot, current_shas), 4))

    # Cell 5 — Best by domain
    cells.append(make_code_cell_with_html('Best Repo by Domain', build_domain_recs(snapshot), 5))

    # Cell 6 — Diff (only if ≥2 snapshots)
    if len(EVALUATIONS) >= 2:
        cells.append(make_code_cell_with_html(
            'Snapshot Δ-diff',
            build_diff(EVALUATIONS[-1], EVALUATIONS[-2]),
            6,
        ))

    # Cell N — closing markdown
    cells.append(nbf.v4.new_markdown_cell(
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
    ))

    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata = {
        'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
        'language_info': {'name': 'python', 'version': '3.12'},
    }

    out_path = REPO_ROOT / 'scoring.ipynb'
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
