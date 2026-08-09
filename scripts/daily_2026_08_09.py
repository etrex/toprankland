#!/usr/bin/env python3
"""Daily update merge helper for 2026-08-09.

Reads a payload JSON: { slug: { "references": [...], "i18n": {...},
                                "adjust": { comp_id: {"rank": n, "score": s,
                                                      "scores": {k: v}} } } }
Rankings are copied forward from the file's latest history entry, then
`adjust` is applied on top. Idempotent: an existing 2026-08-09 entry is
replaced, never duplicated. Always reloads the file at write time.
"""
import json
import sys

DATE = '2026-08-09'
ROOT = '/Users/etrexkuo/toprankland/src/content/rankings'


def merge(slug, payload):
    path = f'{ROOT}/{slug}.json'
    with open(path) as f:
        d = json.load(f)

    prior = [h for h in d['history'] if h['date'] != DATE]
    base = prior[-1] if prior else d['history'][-1]

    rankings = json.loads(json.dumps(base['rankings']))
    for r in rankings:
        adj = payload.get('adjust', {}).get(r['id'])
        if not adj:
            continue
        if 'rank' in adj:
            r['rank'] = adj['rank']
        if 'score' in adj:
            r['score'] = adj['score']
        for k, v in adj.get('scores', {}).items():
            if k in r.get('scores', {}):
                r['scores'][k] = v
    rankings.sort(key=lambda r: r['rank'])

    ranks = [r['rank'] for r in rankings]
    assert sorted(ranks) == list(range(1, len(ranks) + 1)), (slug, ranks)
    assert payload['i18n']['en']['commentary'], slug
    assert payload['i18n']['zh-tw']['commentary'], slug
    for lang in ('en', 'zh-tw'):
        hl = payload['i18n'][lang]['highlights']
        assert 3 <= len(hl) <= 5, (slug, lang, len(hl))
        for h in hl:
            assert set(h) == {'title', 'body'}, (slug, lang, h)
    assert payload['references'], slug

    entry = {
        'date': DATE,
        'rankings': rankings,
        'references': payload['references'],
        'i18n': payload['i18n'],
    }
    d['history'] = prior + [entry]

    with open(path, 'w') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    return f'OK {slug} (history={len(d["history"])}, comps={len(rankings)})'


def main():
    with open(sys.argv[1]) as f:
        payloads = json.load(f)
    for slug, payload in payloads.items():
        print(merge(slug, payload))


if __name__ == '__main__':
    main()
