#!/usr/bin/env python3
"""Check evidence/translation contracts and optionally reproduce the offline build."""
import argparse
from collections import Counter
from decimal import Decimal
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import urlparse
from build_evidence import LANGUAGES, load_locales, load_readers, load_glossary

ROOT = Path(__file__).resolve().parent
FIELDS = (
    "factor", "originalClaim", "finding", "effect", "ci", "comparison",
    "population", "design", "gradeReason", "limitations", "action",
)


class EmbeddedJSON(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.current = None
        self.blocks = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and attrs.get("type") == "application/json":
            self.current = attrs.get("id")
            if self.current:
                self.blocks[self.current] = ""

    def handle_endtag(self, tag):
        if tag == "script":
            self.current = None

    def handle_data(self, text):
        if self.current:
            self.blocks[self.current] += text


def numeric_tokens(value):
    # A singular "per additional serving" states a one-serving increment.
    # Preserve that unit when comparing Chinese's explicit 每额外1份 with English.
    value = value.replace("每增加一份", "每增加1份")
    value = re.sub(r"\bper additional serving\b", "per additional 1 serving", value,
                   flags=re.IGNORECASE)
    # These are equivalent units/dates, not permission to drop quantitative detail.
    value = re.sub(r"(\d+(?:\.\d+)?)万", lambda m: format(Decimal(m[1]) * 10000, "f"), value)
    value = value.replace("千人年", "1000人年")
    # Month names in faithful translated date expressions; compare the same date numbers.
    names = {'février': 2, 'mai': 5, 'Februar': 2, 'Mai': 5, 'febrero': 2, 'mayo': 5,
             'fevereiro': 2, 'maio': 5, 'فبراير': 2, 'مايو': 5}
    for name, number in names.items():
        value = re.sub(r"(?<!\w)" + re.escape(name) + r"(?!\w)", str(number), value, flags=re.IGNORECASE)
    months = dict(zip(("January", "February", "March", "April", "May", "June", "July",
                       "August", "September", "October", "November", "December"), range(1, 13)))
    value = re.sub(r"\b(" + "|".join(months) + r")\b", lambda m: str(months[m[0]]), value)
    value = re.sub(r"(?<=\d),(?=\d{3}(?:\D|$))", "", value)
    return Counter(Decimal(token) for token in re.findall(r"\d+(?:\.\d+)?", value))


def validate(check_build=False):
    data = json.loads((ROOT / "evidence-data.json").read_text(encoding="utf-8"))
    locale = json.loads((ROOT / "evidence-i18n.en.json").read_text(encoding="utf-8"))
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    records = data.get("records", [])
    require(bool(records), "records must not be empty")
    ids = [record.get("id") for record in records]
    require(all(isinstance(key, str) and key for key in ids), "every record needs an ID")
    require(len(set(ids)) == len(ids), "duplicate record ID")
    require(locale.get("language") == "en", "translation language must be en")
    translated = locale.get("records", {})
    require(set(translated) == set(ids), "English IDs must exactly match evidence IDs")
    source_count = 0
    for record in records:
        key = record.get("id", "<missing>")
        require(record.get("grade") in ("A", "B", "C", "D", "U"), f"{key}: invalid grade")
        for field in FIELDS:
            require(isinstance(record.get(field), str) and bool(record[field].strip()),
                    f"{key}: missing evidence field {field}")
        english = translated.get(key, {})
        for field in FIELDS:
            value = english.get(field)
            require(isinstance(value, str) and bool(value.strip()), f"{key}: missing English {field}")
            if field in ("effect", "ci") and isinstance(value, str):
                require(numeric_tokens(record.get(field, "")) == numeric_tokens(value),
                        f"{key}: effect/CI numeric tokens differ in {field}; review both languages")
        sources = record.get("sources", [])
        require(isinstance(sources, list) and bool(sources), f"{key}: no source entries")
        english_sources = english.get("sources", [])
        require(len(english_sources) == len(sources), f"{key}: source translation count differs")
        for index, source in enumerate(sources):
            source_count += 1
            url = urlparse(source.get("url", ""))
            require(url.scheme in ("https", "http") and bool(url.netloc), f"{key}: invalid source URL")
            require(bool(source.get("readLevel")), f"{key}: source reading level missing")
            require(bool(source.get("status")), f"{key}: source status missing")
            require(bool(source.get("title")), f"{key}: source title missing")
            if index < len(english_sources):
                evidence = english_sources[index].get("evidence")
                require(isinstance(evidence, str) and bool(evidence.strip()),
                        f"{key}: English source evidence {index} missing")

    citations = data.get("citations", [])
    urls = [citation.get("url") for citation in citations]
    require(len(set(urls)) == len(urls), "citation ledger contains duplicate URLs")
    for citation in citations:
        url = urlparse(citation.get("url", ""))
        require(url.scheme in ("http", "https") and bool(url.netloc), "invalid citation URL")
        require(bool(citation.get("readLevel")) and bool(citation.get("status")),
                "citation reading level/status missing")
    original = ROOT / "docs/original-readme.zh.md"
    require(original.is_file(), "frozen Chinese README archive missing")
    if original.is_file():
        require(hashlib.sha256(original.read_bytes()).hexdigest() ==
                data.get("metadata", {}).get("sourceReadmeSHA256"), "original README provenance hash differs")

    locale_bundle = {}
    try:
        locale_bundle, _ = load_locales(records)
    except (ValueError, OSError, KeyError) as exc:
        errors.append(str(exc))
    require(set(locale_bundle) == set(LANGUAGES), "all eight complete language bundles required")
    reader_bundle, glossary = {}, {}
    try:
        reader_bundle = load_readers(records)
        glossary = load_glossary()
        by_id = {record['id']: record for record in records}
        for code, payload in reader_bundle.items():
            for key, entry in payload['records'].items():
                available = set(numeric_tokens(json.dumps(by_id[key], ensure_ascii=False)))
                mentioned = set(numeric_tokens(' '.join(entry.values())))
                require(mentioned <= available, f'{code}/{key}: reader copy introduces numeric tokens')
    except (ValueError, OSError, KeyError) as exc:
        errors.append(str(exc))
    language_counts = {"zh": len(records)}
    url_tokens = lambda value: re.findall(r"https?://[^\s)<>]+", value)
    for code, payload in locale_bundle.items():
        if code == "zh":
            continue
        language_counts[code] = len(payload.get("records", {}))
        for raw in records:
            tr = payload.get("records", {}).get(raw["id"], {})
            reference = translated.get(raw["id"], {})
            for field in ("effect", "ci"):
                value = tr.get(field, "")
                require(numeric_tokens(reference.get(field, "")) == numeric_tokens(value),
                        f"{code}/{raw['id']}: numerical mismatch in {field}")
                measures = lambda text: Counter(re.findall(r"(?<![A-Za-z])(?:HR|RR|OR|STR)(?![A-Za-z])", text))
                require(measures(reference.get(field, "")) == measures(value),
                        f"{code}/{raw['id']}: effect type mismatch in {field}")
            require(url_tokens(tr.get("originalClaim", "")) == url_tokens(reference.get("originalClaim", "")),
                    f"{code}/{raw['id']}: original claim URLs changed or reordered")
            if code not in ("en", "zh"):
                for field in ("finding", "limitations", "action"):
                    require(tr.get(field, "").strip() != reference.get(field, "").strip(),
                            f"{code}/{raw['id']}: untranslated English {field}")
                if code in ("ja", "ar"):
                    alphabet = r"[\u3040-\u30ff\u3400-\u9fff]" if code == "ja" else r"[\u0600-\u06ff]"
                    require(bool(re.search(alphabet, tr.get("finding", ""))),
                            f"{code}/{raw['id']}: missing target-language script")

    if check_build and not errors:
        with tempfile.TemporaryDirectory(prefix="htll-check-") as tmp:
            artifact = Path(tmp) / "index.html"
            subprocess.run([sys.executable, str(ROOT / "build_evidence.py"), "--output", str(artifact)],
                           check=True, cwd=ROOT, stdout=subprocess.DEVNULL)
            require(artifact.read_bytes() == (ROOT / "index.html").read_bytes(),
                    "index.html differs from a clean rebuild; run python3 build_evidence.py")
            parser = EmbeddedJSON()
            parser.feed(artifact.read_text(encoding="utf-8"))
            expected = {"dataset": records, "citations": citations, "metadata": data["metadata"],
                        "i18n-data": locale, "locales-data": locale_bundle, "readme-data": original.read_text(encoding="utf-8"),
                        "readers-data": reader_bundle, "glossary-data": glossary}
            for block, value in expected.items():
                try:
                    require(json.loads(parser.blocks[block]) == value, f"embedded {block} differs from source")
                except (KeyError, ValueError) as exc:
                    errors.append(f"embedded {block} missing or invalid: {exc}")

    result = {"ok": not errors, "records": len(records), "sources": source_count,
              "citations": len(citations), "english_records": len(translated), "language_records": language_counts,
              "reader_records": {code: len(bundle["records"]) for code, bundle in reader_bundle.items()},
              "glossary_terms": len(glossary.get("languages", {}).get("en", {})),
              "clean_rebuild_checked": check_build and not errors,
              "scope": "Eight-language structure, provenance, translation coverage, effect/CI types and numeric tokens; not medical interpretation",
              "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-build", action="store_true", help="rebuild in a temporary directory and compare")
    args = parser.parse_args()
    raise SystemExit(validate(args.check_build))
