"""
Sample Reddit + Hacker News public APIs for last-30-day discussion volume
and sentiment about each of the 13 skill-collection repos in this cohort.

Reddit endpoint:
    https://www.reddit.com/search.json?q=<query>&t=month&sort=top&limit=100
    - public, no auth, requires User-Agent header
    - `t=month` restricts to last 30 days
    - rate-limited; we sleep between calls

Hacker News (Algolia) endpoint:
    https://hn.algolia.com/api/v1/search?query=<query>&tags=story
        &numericFilters=created_at_i>UNIX_30D_AGO
    - public, no auth
    - covers stories + comments (we filter to stories first)

Per repo we run 2 queries (owner+repo combo, and the repo's GitHub URL),
union the unique hits by ID, then compute:
    Reddit:  posts_count, comments_sum, avg_score
    HN:      stories_count, comments_sum, avg_points

Output is written to social_sample.json and printed as a summary table.
"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

REPOS = [
    ('AM',  'affaan-m',         'everything-claude-code'),
    ('O',   'obra',             'superpowers'),
    ('NX',  'nexu-io',          'open-design'),
    ('A',   'anthropics',       'skills'),
    ('NL',  'nextlevelbuilder', 'ui-ux-pro-max-skill'),
    ('AD',  'addyosmani',       'agent-skills'),
    ('CH',  'coreyhaines31',    'marketingskills'),
    ('C',   'ComposioHQ',       'awesome-claude-skills'),
    ('M',   'mattpocock',       'skills'),
    ('OAI', 'openai',           'skills'),
    ('MA',  'multica-ai',       'andrej-karpathy-skills'),
    ('K',   'kepano',           'obsidian-skills'),
    ('V',   'vercel-labs',      'agent-skills'),
]

USER_AGENT = 'skill-obs/1.0 (https://github.com/host452b/skill-obs)'
SAMPLED_AT = datetime.now(timezone.utc).isoformat(timespec='seconds')
UNIX_30D_AGO = int((datetime.now(timezone.utc) - timedelta(days=30)).timestamp())


def _http_get_json(url: str, retries: int = 3, sleep: float = 2.0) -> dict | None:
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'application/json'})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status != 200:
                    print(f'  ! HTTP {r.status} on {url[:80]}', file=sys.stderr)
                    return None
                return json.loads(r.read().decode('utf-8'))
        except Exception as e:
            print(f'  ! attempt {attempt+1}/{retries} failed: {e}', file=sys.stderr)
            time.sleep(sleep * (attempt + 1))
    return None


def query_reddit(q: str) -> list[dict]:
    """Return list of post dicts from Reddit search.json, last month."""
    url = (
        'https://www.reddit.com/search.json?'
        + urllib.parse.urlencode({'q': q, 't': 'month', 'sort': 'top', 'limit': 100})
    )
    data = _http_get_json(url)
    if data is None or 'data' not in data:
        return []
    children = data.get('data', {}).get('children', [])
    return [c.get('data', {}) for c in children if c.get('kind') == 't3']


def query_hn(q: str) -> list[dict]:
    """Return list of story hits from HN Algolia search, last 30 days."""
    url = (
        'https://hn.algolia.com/api/v1/search?'
        + urllib.parse.urlencode({
            'query': q,
            'tags': 'story',
            'numericFilters': f'created_at_i>{UNIX_30D_AGO}',
            'hitsPerPage': 100,
        })
    )
    data = _http_get_json(url)
    if data is None:
        return []
    return data.get('hits', [])


def collect_one(owner: str, repo: str) -> dict:
    """Run all queries for one repo, dedupe by ID, compute summary stats."""
    queries = [
        f'{owner} {repo}',           # owner + repo as separate terms
        f'github.com/{owner}/{repo}', # URL form
    ]

    # Reddit
    reddit_seen: dict[str, dict] = {}
    for q in queries:
        for p in query_reddit(q):
            pid = p.get('id') or p.get('name')
            if pid and pid not in reddit_seen:
                reddit_seen[pid] = p
        time.sleep(1.5)  # rate-limit politeness

    reddit_posts = list(reddit_seen.values())
    reddit_post_count = len(reddit_posts)
    reddit_total_comments = sum(int(p.get('num_comments') or 0) for p in reddit_posts)
    reddit_scores = [int(p.get('score') or 0) for p in reddit_posts]
    reddit_total_score = sum(reddit_scores)
    reddit_avg_score = (sum(reddit_scores) / len(reddit_scores)) if reddit_scores else 0.0
    reddit_top_score = max(reddit_scores) if reddit_scores else 0

    # HN
    hn_seen: dict[str, dict] = {}
    for q in queries:
        for h in query_hn(q):
            hid = str(h.get('objectID'))
            if hid and hid not in hn_seen:
                hn_seen[hid] = h
        time.sleep(0.6)

    hn_hits = list(hn_seen.values())
    hn_count = len(hn_hits)
    hn_total_comments = sum(int(h.get('num_comments') or 0) for h in hn_hits)
    hn_points = [int(h.get('points') or 0) for h in hn_hits]
    hn_total_points = sum(hn_points)
    hn_avg_points = (sum(hn_points) / len(hn_points)) if hn_points else 0.0
    hn_top_points = max(hn_points) if hn_points else 0

    return {
        'reddit': {
            'queries':       queries,
            'post_count':    reddit_post_count,
            'total_comments': reddit_total_comments,
            'total_score':   reddit_total_score,
            'avg_score':     round(reddit_avg_score, 1),
            'top_score':     reddit_top_score,
        },
        'hn': {
            'queries':         queries,
            'story_count':     hn_count,
            'total_comments':  hn_total_comments,
            'total_points':    hn_total_points,
            'avg_points':      round(hn_avg_points, 1),
            'top_points':      hn_top_points,
        },
    }


def main():
    print(f'Sampling Reddit + HN public APIs for last 30 days')
    print(f'  sampled_at  = {SAMPLED_AT}')
    print(f'  window_from = {datetime.fromtimestamp(UNIX_30D_AGO, tz=timezone.utc).isoformat(timespec="seconds")}')
    print()
    results = {'sampled_at': SAMPLED_AT, 'window_unix_from': UNIX_30D_AGO, 'per_repo': {}}
    for code, owner, repo in REPOS:
        print(f'[{code:3s}] {owner}/{repo}')
        try:
            data = collect_one(owner, repo)
        except Exception as e:
            print(f'  ✗ error: {e}')
            data = {
                'reddit': {'post_count': 0, 'total_comments': 0, 'total_score': 0, 'avg_score': 0.0, 'top_score': 0, 'queries': []},
                'hn':     {'story_count': 0, 'total_comments': 0, 'total_points': 0, 'avg_points': 0.0, 'top_points': 0, 'queries': []},
                'error':  str(e),
            }
        r, h = data['reddit'], data['hn']
        print(f'  reddit: posts={r["post_count"]:3d} comments={r["total_comments"]:4d} '
              f'avg_score={r["avg_score"]:6.1f} top={r["top_score"]:5d}')
        print(f'      hn: stories={h["story_count"]:3d} comments={h["total_comments"]:4d} '
              f'avg_pts={h["avg_points"]:6.1f} top={h["top_points"]:5d}')
        results['per_repo'][code] = data
        time.sleep(2.0)  # be polite between repos
    out_path = 'social_sample.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f'\nWrote {out_path}')


if __name__ == '__main__':
    main()
