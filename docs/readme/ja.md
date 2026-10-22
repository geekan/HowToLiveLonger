# プログラマーの長寿ガイド · HowToLiveLonger

**誰もが健康で幸せに、より長く生きられるように。**

[**オンラインで読む →**](https://geekan.github.io/HowToLiveLonger/#lang=ja&view=table) · [貢献する](../../CONTRIBUTING.md)

[English](../../README.md) · [简体中文](zh-CN.md) · [Español](es.md) · [Français](fr.md) · [Deutsch](de.md) · [Português](pt.md) · [日本語](ja.md) · [العربية](ar.md)

[![プログラマーの長寿ガイド](../../assets/cover-social-v3.png)](https://geekan.github.io/HowToLiveLonger/#lang=ja&view=table)

食事、運動、睡眠、日々の習慣に関する研究を読み、自分の生活に合う変化を見つけましょう。

- **8言語に対応：** 中国語、英語、スペイン語、フランス語、ドイツ語、ポルトガル語、日本語、アラビア語。
- **探しやすく、読みやすく：** テーマを検索し、分類やエビデンスの等級で絞り込み、列名を押して並べ替えられます。スマートフォンではカード形式で読めます。
- **出典までたどれる研究紹介：** 61件の記録に、わかりやすい研究結果、日常生活へのヒント、原典へのリンクを掲載しています。HRなどの用語は、マウスを重ねるかタップすると説明が表示されます。
- **手元に保存：** CSV、全データのJSON、共有用カードをダウンロードできます。リポジトリをダウンロードして `index.html` を開けば、オフラインでも閲覧できます。

## ローカルで開発する

Python 3.10以降があれば使えます。追加パッケージやバックエンドは不要です。

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 scripts/build.py
python3 scripts/validate.py --check-build
python3 -m http.server 8000
```

<http://localhost:8000> を開きます。テンプレートやデータを変更したら、再ビルドと検証を行い、生成された `index.html` もコミットしてください。

## ディレクトリ構成

| ディレクトリ | 内容 |
| --- | --- |
| [`src/`](../../src/) | ページのテンプレート：`index.template.html` |
| [`data/`](../../data/) | 研究記録、出典、用語集 |
| [`locales/`](../../locales/) | 画面と研究内容の翻訳。読者向けカードは `readers/` に保存 |
| [`scripts/`](../../scripts/) | `build.py` でサイトを生成し、`validate.py` でデータとビルドの再現性を検証 |
| [`assets/`](../../assets/) | ロゴ、イラスト、元ファイル |
| [`docs/`](../../docs/) | 元の記事、過去の確認記録、各言語のREADME |
| [`index.html`](../../index.html) | GitHub Pagesへの公開とオフライン閲覧に使う、生成済みの単一HTMLファイル |

## 公開と更新

GitHub Pagesは `main` のルートディレクトリを公開します。`.nojekyll` により、生成済みの静的ファイルがそのまま配信されます。ローカルでビルドと検証を行ってから変更をプッシュしてください。独自のworkflowファイルは不要です。

研究の追加、翻訳の改善、読みやすさの向上へのご協力を歓迎します。詳しくは[貢献ガイド](../../CONTRIBUTING.md)をご覧ください。

作成： [geekanと貢献者](https://github.com/geekan/HowToLiveLonger/graphs/contributors) ライセンス： [Unlicense](../../LICENSE)。 リンク先の論文やその他の資料には、それぞれの利用条件が適用されます。
