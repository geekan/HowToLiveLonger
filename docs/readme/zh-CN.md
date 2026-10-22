# 程序员延寿指南 · HowToLiveLonger

**帮助每个人健康快乐地活得更久。**

[**在线阅读 →**](https://geekan.github.io/HowToLiveLonger/#lang=zh&view=table) · [参与贡献](../../CONTRIBUTING.md)

[English](../../README.md) · [简体中文](zh-CN.md) · [Español](es.md) · [Français](fr.md) · [Deutsch](de.md) · [Português](pt.md) · [日本語](ja.md) · [العربية](ar.md)

[![程序员延寿指南](../../assets/cover-social-v3.png)](https://geekan.github.io/HowToLiveLonger/#lang=zh&view=table)

从饮食、运动、睡眠到日常习惯，看看研究发现了什么，找到适合自己的改变。

- **八种语言**：中文、英语、西班牙语、法语、德语、葡萄牙语、日语、阿拉伯语。
- **好找、好读**：搜索主题，按分类和证据等级筛选，点击列名排序；手机上以卡片阅读。
- **有据可查**：61 条研究记录，每条都有研究发现、日常参考和原始来源；HR 等术语可悬停或点按查看解释。
- **随时带走**：导出 CSV、完整 JSON 或分享卡片。下载仓库后，双击 `index.html` 也能离线浏览。

## 本地开发

只需 Python 3.10+，无需安装依赖或运行后端。

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 scripts/build.py
python3 scripts/validate.py --check-build
python3 -m http.server 8000
```

访问 <http://localhost:8000>。修改模板或数据后，重新构建并检查，再提交生成的 `index.html`。

## 文件入口

| 目录 | 职责 |
| --- | --- |
| [`src/`](../../src/) | 页面源码：`index.template.html` |
| [`data/`](../../data/) | 研究记录、来源和术语解释 |
| [`locales/`](../../locales/) | 八语界面、研究译文，以及 `readers/` 中的读者卡片 |
| [`scripts/`](../../scripts/) | `build.py` 构建页面，`validate.py` 检查数据和构建一致性 |
| [`assets/`](../../assets/) | 标志、封面及其源文件 |
| [`docs/`](../../docs/) | 原始文章、历史核对记录和多语言 README |
| [`index.html`](../../index.html) | 自动生成的单文件网站，供 GitHub Pages 和离线阅读使用 |

## 托管与更新

GitHub Pages 从 `main` 分支根目录发布，`.nojekyll` 让已构建的静态文件直接上线。本地构建、校验后推送更新，无需维护 workflow 文件。

欢迎补充研究、纠正内容、润色翻译和改进阅读体验。具体方法见 [贡献指南](../../CONTRIBUTING.md)。

由 [geekan 与贡献者](https://github.com/geekan/HowToLiveLonger/graphs/contributors) 共同维护，使用 [Unlicense](../../LICENSE)。 研究论文及其他链接材料遵循各自的使用条款。
