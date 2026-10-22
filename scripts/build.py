#!/usr/bin/env python3
"""Build a self-contained, eight-language evidence atlas with the Python standard library."""
import argparse
import base64
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRANSLATED_FIELDS = ('factor', 'originalClaim', 'finding', 'effect', 'ci', 'comparison',
                     'population', 'design', 'gradeReason', 'limitations', 'action')
LANGUAGES = {'zh': ('简体中文', 'ltr'), 'en': ('English', 'ltr'),
             'es': ('Español', 'ltr'), 'fr': ('Français', 'ltr'),
             'de': ('Deutsch', 'ltr'), 'pt': ('Português', 'ltr'),
             'ja': ('日本語', 'ltr'), 'ar': ('العربية', 'rtl')}


def encode(value):
    return json.dumps(value, ensure_ascii=False).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')


def load_locales(records, english=None, allow_incomplete=False):
    interface = json.loads((ROOT / 'locales/interface.json').read_text(encoding='utf-8'))
    english = english if english is not None else json.loads((ROOT / 'locales/en.json').read_text(encoding='utf-8'))
    locales, problems = {}, []
    for code, (name, direction) in LANGUAGES.items():
        if code == 'zh':
            payload = {'language': code, 'name': name, 'dir': direction, **interface[code], 'records': {}}
        elif code == 'en':
            payload = {**english, 'name': name, 'dir': direction, **interface[code]}
        else:
            path = ROOT / 'locales' / (code + '.json')
            if not path.exists():
                problems.append(f'{code}: translation file missing')
                continue
            payload = json.loads(path.read_text(encoding='utf-8'))
        if payload.get('language') != code or payload.get('dir') != direction:
            problems.append(f'{code}: invalid language or direction')
        for section, expected in [('ui', interface['en']['ui']), ('terms', interface['en']['terms'] if code != 'zh' else {})]:
            actual = payload.get(section, {})
            if set(actual) != set(expected) or any(not isinstance(v, str) or not v.strip() for v in actual.values()):
                problems.append(f'{code}: incomplete {section} contract')
        if code != 'zh':
            translated = payload.get('records', {})
            if set(translated) != {r['id'] for r in records}:
                problems.append(f'{code}: record IDs must exactly match')
            for raw in records:
                tr = translated.get(raw['id'], {})
                absent = [key for key in TRANSLATED_FIELDS if not isinstance(tr.get(key), str) or not tr[key].strip()]
                sources = tr.get('sources', [])
                if len(sources) != len(raw['sources']) or any(not isinstance(s.get('evidence'), str) or not s['evidence'].strip() for s in sources):
                    absent.append('source evidence')
                if absent:
                    problems.append(f"{code}/{raw['id']}: missing {', '.join(absent)}")
        locales[code] = payload
    if problems and not allow_incomplete:
        raise ValueError('Incomplete language contracts:\n' + '\n'.join(problems))
    return locales, problems


def load_readers(records):
    readers = {}
    ids = {record['id'] for record in records}
    for code in LANGUAGES:
        payload = json.loads((ROOT / 'locales/readers' / (code + '.json')).read_text(encoding='utf-8'))
        if payload.get('language') != code or set(payload.get('records', {})) != ids:
            raise ValueError(f'{code}: reader record IDs must exactly match')
        for key, entry in payload['records'].items():
            if not {'summary', 'takeaway'} <= set(entry) or not set(entry) <= {'summary', 'takeaway', 'title'} or any(
                    not isinstance(value, str) or not value.strip() for value in entry.values()):
                raise ValueError(f'{code}/{key}: incomplete reader copy')
        readers[code] = payload
    return readers


def load_glossary():
    glossary = json.loads((ROOT / 'data/glossary.json').read_text(encoding='utf-8'))
    required = {'HR', 'RR', 'OR', 'CI', 'ACM', 'RCT', 'CVD', 'DOI', 'MET', 'SD',
                'LDL-C', 'PM2.5', 'BMI', 'CKD'}
    if set(glossary.get('languages', {})) != set(LANGUAGES):
        raise ValueError('Glossary needs all eight languages')
    for code, entries in glossary['languages'].items():
        if not required <= set(entries) or set(entries) != set(glossary['languages']['en']) or any(
                not isinstance(entry.get(field), str) or not entry[field].strip()
                for entry in entries.values() for field in ('name', 'description')):
            raise ValueError(f'{code}: incomplete glossary')
    return glossary


def build():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / 'data/evidence.json')
    parser.add_argument('--i18n', type=Path, default=ROOT / 'locales/en.json')
    parser.add_argument('--readme', type=Path, help='Frozen original Chinese README')
    parser.add_argument('--output', type=Path, default=ROOT / 'index.html')
    parser.add_argument('--allow-incomplete-i18n', action='store_true', help='Development only; missing translations remain explicitly incomplete')
    args = parser.parse_args()
    data = json.loads(args.data.read_text(encoding='utf-8'))
    records = data['records']
    if len({r['id'] for r in records}) != len(records):
        raise ValueError('Duplicate record IDs')
    for record in records:
        if record.get('grade') not in ('A', 'B', 'C', 'D', 'U'):
            raise ValueError(f"Invalid grade: {record.get('id')}")
        for source in record['sources']:
            if not source.get('url', '').startswith(('https://', 'http://')):
                raise ValueError(f"Invalid source URL: {record['id']}")
    english = json.loads(args.i18n.read_text(encoding='utf-8'))
    locales, problems = load_locales(records, english, args.allow_incomplete_i18n)
    readme = args.readme or (ROOT / 'docs/original-readme.zh.md')
    cover = ROOT / 'assets/life-evidence-cover-v3.jpg'
    cover_uri = 'data:image/jpeg;base64,' + base64.b64encode(cover.read_bytes()).decode('ascii')
    logo_uri = 'data:image/svg+xml;base64,' + base64.b64encode((ROOT / 'assets/logo.svg').read_bytes()).decode('ascii')
    values = {'__DATA__': records, '__CITATIONS__': data['citations'], '__META__': data['metadata'],
              '__README__': readme.read_text(encoding='utf-8'), '__I18N__': english, '__LOCALES__': locales,
              '__READERS__': load_readers(records), '__GLOSSARY__': load_glossary()}
    html = (ROOT / 'src/index.template.html').read_text(encoding='utf-8')
    html = re.sub(r'__(?:DATA|CITATIONS|META|README|I18N|LOCALES|READERS|GLOSSARY|COVER_URI|LOGO_URI|ORIGIN_OPTIONS)__',
                  lambda m: '' if m[0] == '__ORIGIN_OPTIONS__' else cover_uri if m[0] == '__COVER_URI__'
                  else logo_uri if m[0] == '__LOGO_URI__' else encode(values[m[0]]), html)
    args.output.write_bytes(html.encode('utf-8'))
    print(json.dumps({'records': len(records), 'citations': len(data['citations']),
                      'languages': list(locales), 'translationComplete': not problems, 'incomplete': problems,
                      'readme': str(readme), 'sourceReadmeSHA256': hashlib.sha256(readme.read_bytes()).hexdigest(),
                      'output': str(args.output), 'bytes': args.output.stat().st_size,
                      'sha256': hashlib.sha256(args.output.read_bytes()).hexdigest()}, ensure_ascii=False))


if __name__ == '__main__':
    build()
