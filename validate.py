# -*- coding: utf-8 -*-
"""Валидация data/section_*.json: структура, квизы, минимальные объёмы."""
import json, os, sys, re

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, 'data')
LEVELS = {'\U0001F7E2 Junior', '\U0001F7E1 Middle', '\U0001F534 Senior'}

errors = []
for i in range(20):
    p = os.path.join(DATA, f'section_{i}.json')
    tag = f'section_{i}'
    if not os.path.exists(p):
        errors.append(f'{tag}: MISSING'); continue
    try:
        with open(p, encoding='utf-8') as f:
            s = json.load(f)
    except Exception as e:
        errors.append(f'{tag}: JSON parse error: {e}'); continue
    for k in ('phase', 'section', 'topics', 'quiz'):
        if k not in s:
            errors.append(f'{tag}: missing key "{k}"')
    if not re.match(r'^Phase [1-5] — ', s.get('phase', '')):
        errors.append(f'{tag}: bad phase format: {s.get("phase")!r}')
    topics = s.get('topics', [])
    if len(topics) < 10:
        errors.append(f'{tag}: only {len(topics)} topics (need >=10)')
    for ti, t in enumerate(topics):
        for k in ('title', 'level', 'explanation'):
            if not t.get(k):
                errors.append(f'{tag} topic {ti}: empty/missing "{k}"')
        if t.get('level') and t['level'] not in LEVELS:
            errors.append(f'{tag} topic {ti}: bad level {t["level"]!r}')
        if len(t.get('explanation', '')) < 400:
            errors.append(f'{tag} topic {ti}: explanation too short ({len(t.get("explanation",""))} chars)')
        links = t.get('links', [])
        if not isinstance(links, list) or len(links) < 2:
            errors.append(f'{tag} topic {ti}: need >=2 links, got {len(links) if isinstance(links, list) else links!r}')
        else:
            for li, l in enumerate(links):
                if not l.get('title') or not str(l.get('url', '')).startswith('http'):
                    errors.append(f'{tag} topic {ti} link {li}: bad title/url')
    quiz = s.get('quiz', [])
    if len(quiz) < 8:
        errors.append(f'{tag}: only {len(quiz)} quiz questions (need >=8)')
    for qi, q in enumerate(quiz):
        if not q.get('q') or not q.get('explain'):
            errors.append(f'{tag} quiz {qi}: empty q/explain')
        opts = q.get('options', [])
        if len(opts) != 4:
            errors.append(f'{tag} quiz {qi}: {len(opts)} options (need 4)')
        a = q.get('answer')
        if not isinstance(a, int) or not (0 <= a < len(opts or [1])):
            errors.append(f'{tag} quiz {qi}: bad answer index {a!r}')

if errors:
    print('\n'.join(errors))
    print(f'\nFAIL: {len(errors)} problems')
    sys.exit(1)
print('OK: all 20 sections valid')
