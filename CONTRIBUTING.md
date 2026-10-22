# Contributing / 贡献指南

[English](README.md) · [简体中文](docs/readme/zh-CN.md)

## Evidence changes / 证据变更

Start with a stable record ID in `data/evidence.json`. Provide the original paper URL/DOI, study design, population, comparison, outcome, estimate and interval, and what you actually read: relevant full-text sections, abstract, metadata, or unread. State the date and limits of the check. For inaccessible sources, record the failure rather than claiming verification.

修改现有记录时沿用 ID；保留 `originalClaim` 与 `originalClaimRaw` 的历史身份。核验结论写入 `finding`，不能通过改写原话消除错误。新增记录先检查是否已由其他因素覆盖；不要把同一研究拆成多个可相加的“延寿收益”。

- Grade the displayed all-cause mortality conclusion, not the journal's reputation. A null randomized result may be stronger evidence than a large observational association.
- Keep population and indication limits. Do not turn disease-treatment evidence into a recommendation for healthy people.
- Preserve HR/RR/OR, comparison direction, follow-up and confidence levels. If an interval or absolute risk is unavailable, say so; do not invent it.
- Link primary research. Do not import a paper's full text or third-party figures into the repository without checking its terms.
- Distinguish association, causal intervention, indirect endpoints and insufficient evidence. Project grades are not a full GRADE review.

## Translation / 翻译

English records live in `locales/en.json`; Spanish, French, German, Portuguese, Japanese and Arabic live in `locales/{es,fr,de,pt,ja,ar}.json`. Every finished language covers the same 61 stable IDs, all 11 core fields and the source notes in their original order. UI and term keys must match `locales/interface.json`; missing languages or fields fail a strict build, and copying English text does not complete another translation.

A medical change must update Chinese, English and all six additional locales together. Preserve effect type, estimates, confidence levels, comparison direction, population, negation and limitations. Keep the historical `originalClaim` separate from the current finding. Original paper titles and explicitly labeled Chinese archives may retain their original language.

医学修订同步八语言及生成HTML；译文必须补齐句子中的对象和比较关系，不用润色升级推荐强度。原始中文档案、出处备注与核验批次原文保留原语时，界面须明确标注。结构和数字校验不能替代语义审读，翻译也不等于独立重读论文；评审写明实际阅读范围，不称母语医学专家认证。

Keep reviewed translations under version control. After validation, inspect every language on desktop and mobile, long details and exports; Arabic also needs RTL, numeric-range, DOI and PNG checks. Keep research qualifications visible and do not add unsupported data to diagrams.

## Reader copy and terminology

The public cards use `locales/readers/{zh,en,es,fr,de,pt,ja,ar}.json`. Each study needs a concise `summary` and a practical `takeaway`; an optional `title` can replace an editorial or audit-style source title. Write for the reader, preserve the comparison, population and uncertainty, and keep the detailed source record intact. Update all eight languages together. Original claim archives are not shown in the reader interface.

`data/glossary.json` explains technical abbreviations in all eight languages. Keep HR, RR, OR and survival-time ratios distinct. Verify desktop hover, keyboard focus and mobile touch, including Escape dismissal, modal layering and viewport fit. The original vector mark is `assets/logo.svg`.

## Build and check / 构建与检查

Use Python 3.10+. Clone the repository, then build, validate and preview:

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 scripts/build.py
python3 scripts/validate.py --check-build
python3 -m http.server 8000
```

Visit <http://localhost:8000>. After editing the template or data, rebuild and commit the generated `index.html`.

The validator checks schema, IDs, source fields, all eight languages, effect/CI types and numeric tokens, archived provenance and reproducible output. It cannot establish clinical validity, translation nuance, URL availability or visual quality. Investigate every failure rather than weakening a check to make validation pass.

Open the actual generated `index.html`, then check all eight languages at desktop and mobile widths: search, category and evidence-level filters, table/tree consistency, detail and keyboard close, state restoration, CSV/JSON downloads, summary copy and PNG card. A real download should parse or open; a dispatched click alone is not evidence of success. Keep research qualifications visible in shared summaries/cards.

## Review and handoff / 评审与交接

A change description should identify the fixed input version, files changed, actual checks with accessible evidence, and what remains unverified. Link a specific record, file line or output, not only “see my chat”. For evidence changes, reviewers should independently inspect the cited research and affected languages; implementation self-checks are not final acceptance.

原始基线中英 README 位于 `docs/original-readme.*.md`，保持字节不变，不参与自动翻译或新的医学结论改写。更新中文医学记录时同步处理全部译文与生成 HTML；核验日期只覆盖本次实际读取的范围。

The repository retains its existing [Unlicense](LICENSE). Preserve author and source attribution. Linked papers and third-party material have their own terms. Do not include credentials, private medical data, local account state, dependencies or temporary agent workspaces in a contribution.

## Publish / 发布

Build and validate locally before pushing. Commit both the source changes and the generated `index.html`. GitHub Pages serves `main` from the repository root; `.nojekyll` bypasses Jekyll processing. Keep workflow files out of this repository.

The public entry is <https://geekan.github.io/HowToLiveLonger/>. The page embeds its data, translations, logo and cover; the social preview image is served from `assets/cover-social-v3.png`.

## Project map / 目录

| Path | Purpose |
| --- | --- |
| `src/` | HTML template and page interactions |
| `data/` | Research records, sources and glossary |
| `locales/` | Interface and research translations; reader cards in `readers/` |
| `scripts/` | Build and validation tools |
| `skills/howtolivelonger/` | Installable agent skill; fetches the public JSON |
| `assets/` | Logo, cover and source artwork |
| `docs/` | Original articles, review records and translated READMEs |
| `index.html` | Generated website for Pages and offline use |
