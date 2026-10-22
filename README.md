# 程序员延寿指南 · HowToLiveLonger

**帮助每个人健康快乐地活得更久。**

[**在线阅读 →**](https://geekan.github.io/HowToLiveLonger/) · [English](README_en.md) · [参与贡献](CONTRIBUTING.md)

[![程序员延寿指南](assets/cover-social-v3.png)](https://geekan.github.io/HowToLiveLonger/)

从饮食、运动、睡眠到日常习惯，看看研究发现了什么，找到适合自己的改变。

- **八种语言**：中文、英语、西班牙语、法语、德语、葡萄牙语、日语、阿拉伯语。
- **好找、好读**：搜索主题，按分类和证据等级筛选，点击列名排序；手机上以卡片阅读。
- **有据可查**：61 条研究记录，每条都有研究发现、日常参考和原始来源；HR 等术语可悬停或点按查看解释。
- **随时带走**：导出 CSV、完整 JSON 或分享卡片。下载仓库后，双击 `index.html` 也能离线浏览。

[中文](https://geekan.github.io/HowToLiveLonger/#lang=zh&view=table) · [English](https://geekan.github.io/HowToLiveLonger/#lang=en&view=table) · [Español](https://geekan.github.io/HowToLiveLonger/#lang=es&view=table) · [Français](https://geekan.github.io/HowToLiveLonger/#lang=fr&view=table) · [Deutsch](https://geekan.github.io/HowToLiveLonger/#lang=de&view=table) · [Português](https://geekan.github.io/HowToLiveLonger/#lang=pt&view=table) · [日本語](https://geekan.github.io/HowToLiveLonger/#lang=ja&view=table) · [العربية](https://geekan.github.io/HowToLiveLonger/#lang=ar&view=table)

## 本地开发

只需 Python 3.10+，无需安装依赖或运行后端。

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 build_evidence.py
python3 validate_evidence.py --check-build
python3 -m http.server 8000
```

访问 <http://localhost:8000>。修改模板或数据后，重新构建并检查，再提交生成的 `index.html`。

## 文件入口

| 内容 | 位置 |
| --- | --- |
| 网站 | [`index.html`](index.html)；修改 [`evidence-browser.template.html`](evidence-browser.template.html) 后构建 |
| 研究与来源 | [`evidence-data.json`](evidence-data.json) |
| 八语卡片 | [`readers/`](readers/) |
| 界面与研究译文 | [`locale-interface.json`](locale-interface.json)、[`evidence-i18n.en.json`](evidence-i18n.en.json)、[`locales/`](locales/) |
| 术语解释 | [`glossary.json`](glossary.json) |
| 封面与标志 | [`assets/`](assets/) |
| 原始文章 | [中文](docs/original-readme.zh.md) · [English](docs/original-readme.en.md) |

## 托管与更新

网站由 GitHub Pages 从 `main` 分支根目录发布，`.nojekyll` 让已构建的静态文件直接上线。仓库不使用 workflow；构建、校验在本地完成，推送后由 Pages 发布。

欢迎补充研究、纠正内容、润色翻译和改进阅读体验。具体方法见[贡献指南](CONTRIBUTING.md)。

由 [geekan 与贡献者](https://github.com/geekan/HowToLiveLonger/graphs/contributors)共同维护，使用 [Unlicense](LICENSE)。研究论文及其他链接材料遵循各自的使用条款。
