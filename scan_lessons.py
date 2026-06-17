"""
Scan each submodule for "lesson-encoded" markers in *.md content.

Rationale: Valuable skills should encode (per user spec):
  1. Knowledge the model doesn't know
  2. Context-specific information
  3. Lessons learned from real failures

The most reliably-detectable signal is (3) — explicit failure-mode language.
We also count a couple of weak signals for (1)/(2) but acknowledge they are noisy.

Output:
  lessons_sample.json — per-repo counts, percentages
  Console summary table
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPOS = [
    ('AM',  'affaan-m__everything-claude-code'),
    ('O',   'obra__superpowers'),
    ('NX',  'nexu-io__open-design'),
    ('A',   'anthropics__skills'),
    ('NL',  'nextlevelbuilder__ui-ux-pro-max-skill'),
    ('AD',  'addyosmani__agent-skills'),
    ('CH',  'coreyhaines31__marketingskills'),
    ('C',   'ComposioHQ__awesome-claude-skills'),
    ('M',   'mattpocock__skills'),
    ('OAI', 'openai__skills'),
    ('MA',  'multica-ai__andrej-karpathy-skills'),
    ('K',   'kepano__obsidian-skills'),
    ('V',   'vercel-labs__agent-skills'),
    ('GS',  'garrytan__gstack'),
    ('AA',  'msitarzewski__agency-agents'),
    ('CV',  'juliusbrussee__caveman'),
    ('UA',  'Egonex-AI__Understand-Anything'),
    ('OS',  'Fission-AI__OpenSpec'),
    ('CO',  'santifer__career-ops'),
    ('TS',  'Leonxlnx__taste-skill'),
    ('L30', 'mvanhorn__last30days-skill'),
]

# Failure-lesson markers (the user's criterion #3)
LESSON_MARKERS = [
    r'\banti[-\s]?pattern\b',
    r'\bred[-\s]?flag\b',
    r'\bcommon (mistake|pitfall|rationalization)s?\b',
    r'\bwhen not to use\b',
    r'\bdo not use\b',
    r'\bfailure mode\b',
    r'\bpitfalls?\b',
    r'\blessons? learned\b',
    r'\bavoid (this|the|using|over)\b',
    r"\bdon'?t (do|use)\b",
    r'\bwrong way\b',
    r'\bcommon (failure|error)s?\b',
    r'\b(?:gotchas?|caveats?)\b',
    r'\bhard[-\s]?gate\b',
    r'\bwhy not\b',
    r'\bmistake[s]?\b',
]
LESSON_PAT = re.compile('|'.join(LESSON_MARKERS), re.IGNORECASE)

# Weak signals for criterion #1 (model-unknown knowledge)
VERSION_PAT = re.compile(
    r'\b(?:as of \d{4}|since (?:v?\d|version)|api version|[<>=]+\s*\d+\.\d+|'
    r'updated? \d{4}|deprecated since)\b',
    re.IGNORECASE,
)

# Weak signals for criterion #2 (context-specific information)
CONTEXT_PAT = re.compile(
    r'(?:\b(?:export|process\.env|\$\{[A-Z_]+\}|'
    r'~/\.[a-z]|\.env\b|localhost|127\.0\.0\.1)|'
    r'/usr/local|/etc/|/opt/)',
)


def scan_repo(code: str, path: Path) -> dict:
    md_files = []
    for f in path.rglob('*.md'):
        if '.git' in f.parts:
            continue
        md_files.append(f)

    total = len(md_files)
    files_with_lesson = 0
    files_with_version = 0
    files_with_context = 0
    marker_hits = {m.pattern: 0 for m in [re.compile(m, re.IGNORECASE) for m in LESSON_MARKERS]}

    for f in md_files:
        try:
            txt = f.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        if LESSON_PAT.search(txt):
            files_with_lesson += 1
        if VERSION_PAT.search(txt):
            files_with_version += 1
        if CONTEXT_PAT.search(txt):
            files_with_context += 1
        # Per-marker tally (best-effort)
        for raw in LESSON_MARKERS:
            if re.search(raw, txt, re.IGNORECASE):
                marker_hits[raw] += 1

    return {
        'md_total':                 total,
        'files_with_lesson':        files_with_lesson,
        'files_with_version':       files_with_version,
        'files_with_context':       files_with_context,
        'lesson_pct':               round(100.0 * files_with_lesson / total, 1) if total else 0.0,
        'version_pct':              round(100.0 * files_with_version / total, 1) if total else 0.0,
        'context_pct':              round(100.0 * files_with_context / total, 1) if total else 0.0,
        # Composite "value-density" — weighted average; tune as you like.
        'value_density_pct':        round(
            (60.0 * files_with_lesson + 25.0 * files_with_version + 15.0 * files_with_context) / total, 1
        ) if total else 0.0,
        'per_marker':               {k: v for k, v in marker_hits.items() if v > 0},
    }


def main():
    root = Path(__file__).resolve().parent
    print(f'Scanning {len(REPOS)} repos for lesson/value markers')
    print(f'  sampled_at = {datetime.now(timezone.utc).isoformat(timespec="seconds")}\n')

    results = {'sampled_at': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'per_repo': {}}
    for code, slug in REPOS:
        path = root / 'skills' / slug
        if not path.exists():
            print(f'[{code:3s}] SKIP — path does not exist: {path}')
            continue
        data = scan_repo(code, path)
        results['per_repo'][code] = data
        print(
            f'[{code:3s}] md={data["md_total"]:4d}  '
            f'lesson={data["files_with_lesson"]:4d}({data["lesson_pct"]:5.1f}%)  '
            f'version={data["files_with_version"]:3d}({data["version_pct"]:4.1f}%)  '
            f'context={data["files_with_context"]:3d}({data["context_pct"]:4.1f}%)  '
            f'value-density={data["value_density_pct"]:5.1f}'
        )

    out = root / 'lessons_sample.json'
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f'\nWrote {out}')


if __name__ == '__main__':
    main()
