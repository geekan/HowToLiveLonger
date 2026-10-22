# A Programmer’s Guide to Longevity · HowToLiveLonger

**Helping everyone live a longer, healthier, happier life.**

[**Read online →**](https://geekan.github.io/HowToLiveLonger/#lang=en&view=table) · [简体中文](README.md) · [Contribute](CONTRIBUTING.md)

[![A Programmer’s Guide to Longevity](assets/cover-social-v3.png)](https://geekan.github.io/HowToLiveLonger/#lang=en&view=table)

Explore research on food, movement, sleep and everyday habits, and find changes that fit your life.

- **Eight languages:** Chinese, English, Spanish, French, German, Portuguese, Japanese and Arabic.
- **Easy to explore:** search topics, filter by category or evidence level, and sort by column heading. Read cards on your phone.
- **Research you can follow:** 61 records with plain-language findings, everyday takeaways and original sources. Hover over terms such as HR, or tap them, for an explanation.
- **Keep a copy:** export CSV, complete JSON or a share card. Download the repository and open `index.html` to browse offline.

[中文](https://geekan.github.io/HowToLiveLonger/#lang=zh&view=table) · [English](https://geekan.github.io/HowToLiveLonger/#lang=en&view=table) · [Español](https://geekan.github.io/HowToLiveLonger/#lang=es&view=table) · [Français](https://geekan.github.io/HowToLiveLonger/#lang=fr&view=table) · [Deutsch](https://geekan.github.io/HowToLiveLonger/#lang=de&view=table) · [Português](https://geekan.github.io/HowToLiveLonger/#lang=pt&view=table) · [日本語](https://geekan.github.io/HowToLiveLonger/#lang=ja&view=table) · [العربية](https://geekan.github.io/HowToLiveLonger/#lang=ar&view=table)

## Develop locally

Use Python 3.10 or newer. No packages or backend are required.

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 build_evidence.py
python3 validate_evidence.py --check-build
python3 -m http.server 8000
```

Visit <http://localhost:8000>. After editing the template or data, rebuild, validate and commit the generated `index.html`.

## Project map

| Content | Location |
| --- | --- |
| Website | [`index.html`](index.html); edit [`evidence-browser.template.html`](evidence-browser.template.html) and rebuild |
| Research and sources | [`evidence-data.json`](evidence-data.json) |
| Reader cards in eight languages | [`readers/`](readers/) |
| Interface and research translations | [`locale-interface.json`](locale-interface.json), [`evidence-i18n.en.json`](evidence-i18n.en.json), [`locales/`](locales/) |
| Term explanations | [`glossary.json`](glossary.json) |
| Artwork and logo | [`assets/`](assets/) |
| Original articles | [中文](docs/original-readme.zh.md) · [English](docs/original-readme.en.md) |

## Hosting and updates

GitHub Pages publishes the root of `main`. The `.nojekyll` file serves the already-built static files directly. This repository has no workflows: build and validate locally, then push the updated site for Pages to publish.

Contributions to research, translations and the reading experience are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

Created by [geekan and contributors](https://github.com/geekan/HowToLiveLonger/graphs/contributors) under the [Unlicense](LICENSE). Papers and other linked materials retain their own terms.
