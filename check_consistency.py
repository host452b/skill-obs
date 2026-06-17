#!/usr/bin/env python3
"""
check_consistency.py — cross-document regression guard.

The canonical scores live in build_scoring_notebook.py (EVALUATIONS[-1]). The
README "Top-line Findings" table and EVALUATION "§14.1" leaderboard are
hand-maintained markdown that must agree with them. They drifted once (TS was
mislabeled tier D vs the canonical C); this guard fails loudly when it happens
again.

Scope is deliberately narrow — only the CURRENT v1.5 leaderboard tables. The
frozen historical tables (§4/§5, v1.1, max 150) are intentionally stale and are
NOT checked (they live above the §14 / Top-line markers we anchor on).

Usage:  python3 check_consistency.py        # exit 0 = consistent, 1 = mismatch
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _load_canonical() -> dict[str, tuple[int, str]]:
    spec = importlib.util.spec_from_file_location('bsn', ROOT / 'build_scoring_notebook.py')
    bsn = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bsn)
    v = bsn.EVALUATIONS[-1]
    out = {}
    for code, owner, repo, _ in bsn.REPOS:
        if code in v['scores']:
            total = sum(v['scores'][code].values())
            out[f'{owner}/{repo}'] = (total, bsn.tier_for_total(total))
    return out


# A leaderboard row carries "... | <total> | <tier> | ..." (total may be **bold**).
ROW = re.compile(r'\|\s*\*{0,2}(\d{2,3})\*{0,2}\s*\|\s*\*{0,2}([SABCD]\+?)\*{0,2}\s*\|')


def _section(text: str, start_pat: str, stop_pats: tuple[str, ...]) -> str:
    """Return the slice of `text` from the line matching start_pat up to the
    first subsequent line matching any stop_pat (exclusive)."""
    lines = text.splitlines()
    out, capturing = [], False
    for ln in lines:
        if not capturing:
            if re.search(start_pat, ln):
                capturing = True
            continue
        if any(re.search(p, ln) for p in stop_pats):
            break
        out.append(ln)
    return '\n'.join(out)


def _check_table(canonical, full_to_repo, section_text, where, problems):
    for line in section_text.splitlines():
        repo = next((f for f in canonical if f in line), None)
        if not repo:
            continue
        m = ROW.search(line)
        if not m:
            continue
        got_total, got_tier = int(m.group(1)), m.group(2)
        exp_total, exp_tier = canonical[repo]
        if got_total != exp_total:
            problems.append(f'{where}: {repo} total = {got_total}, canonical = {exp_total}')
        if got_tier != exp_tier:
            problems.append(f'{where}: {repo} tier = {got_tier}, canonical = {exp_tier}')


def main() -> int:
    canonical = _load_canonical()
    full_to_repo = {f: f for f in canonical}
    problems: list[str] = []

    # README top-line tables (zh + en): anchor on the findings header, stop at the
    # changelog blockquote or next H2.
    for fn in ('README.md', 'README.en.md'):
        txt = (ROOT / fn).read_text(encoding='utf-8')
        sec = _section(txt, r'Top-line Findings', (r'^>\s', r'^## '))
        _check_table(canonical, full_to_repo, sec, f'{fn} (Top-line Findings)', problems)

    # EVALUATION §14.1 leaderboard (zh + en): anchor on "14.1", stop at next "###"/"##".
    for fn in ('EVALUATION.md', 'EVALUATION.en.md'):
        txt = (ROOT / fn).read_text(encoding='utf-8')
        sec = _section(txt, r'14\.1', (r'^###\s', r'^##\s'))
        _check_table(canonical, full_to_repo, sec, f'{fn} (§14.1)', problems)

    if problems:
        print(f'✗ {len(problems)} consistency problem(s) between docs and canonical scores:')
        for p in problems:
            print(f'  - {p}')
        return 1
    print(f'✓ docs consistent with canonical v1.5 scores ({len(canonical)} repos checked '
          'across README + README.en + EVALUATION §14.1 + EVALUATION.en §14.1).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
