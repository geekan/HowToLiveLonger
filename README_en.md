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
python3 scripts/build.py
python3 scripts/validate.py --check-build
python3 -m http.server 8000
```

Visit <http://localhost:8000>. After editing the template or data, rebuild, validate and commit the generated `index.html`.

## Project map

| Directory | Purpose |
| --- | --- |
| [`src/`](src/) | Page source: `index.template.html` |
| [`data/`](data/) | Research records, sources and glossary |
| [`locales/`](locales/) | Interface and research translations, with reader cards in `readers/` |
| [`scripts/`](scripts/) | `build.py` generates the site; `validate.py` checks data and reproducibility |
| [`assets/`](assets/) | Logo, artwork and their source files |
| [`docs/`](docs/) | [Original Chinese article](docs/original-readme.zh.md), [English article](docs/original-readme.en.md) and historical review records |
| [`index.html`](index.html) | Generated standalone website for GitHub Pages and offline reading |

## Hosting and updates

GitHub Pages publishes the root of `main`. The `.nojekyll` file serves the already-built static files directly. This repository has no workflows: build and validate locally, then push the updated site for Pages to publish.

Contributions to research, translations and the reading experience are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

Created by [geekan and contributors](https://github.com/geekan/HowToLiveLonger/graphs/contributors) under the [Unlicense](LICENSE). Papers and other linked materials retain their own terms.
