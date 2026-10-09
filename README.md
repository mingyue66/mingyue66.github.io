# Mingyue Huo — personal homepage

A minimal academic homepage for `mingyue66.github.io`. Four static pages, one shared stylesheet, system fonts, and no client-side JavaScript or third-party tracking. The homepage highlights projects with paper figures and research keywords.

## 更新内容

- 简介、联系方式、教育、实习和项目：`content/profile.json`
- 论文题目、作者、年份、发表状态和链接：`content/publications.json`
- 下载的简历：`file/CV_MingyueHuo.pdf`
- 排版样式：`stylesheet.css`

编辑内容后，在仓库根目录运行：

```sh
python3 scripts/build.py
```

生成的 `index.html`、`publications/index.html`、`projects/index.html`、`cv/index.html` 一起提交到 GitHub。发布无需安装依赖或运行服务；GitHub Pages 直接读取已生成的静态文件。生成器只使用 Python 标准库。

本地预览：

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

然后打开 `http://127.0.0.1:8765/`。

## GitHub Pages

沿用现有仓库的发布方式。若需重新配置，GitHub 仓库 Settings → Pages → Deploy from a branch，选择 `master`、`/(root)`。`.nojekyll` 让这些静态文件直接发布。

## 内容核对

此版根据用户提供的 2026 年 9 月 CV，以及 2026 年 10 月 8 日检索的公开记录整理。10 篇 arXiv 论文按作者全名匹配，另有 CV 中的 4 篇非 arXiv 论文，共 14 条；不把预印本标成已录用论文。

- 姓名、邮箱、经历、求职信息、项目链接：最新 CV。
- 公开预印本的题名和作者：arXiv 最新记录。CV 中 “Misgrounded Rationales” 对应 arXiv 的 “Underspecified Rationales”；“Fooling Reward Models with Gibberish” 对应 arXiv 的 “Beyond Semantic Manipulation”。本站使用 arXiv 题名，避免同一稿件重复计数。
- TagSpeech 和音频预训练论文：ACL Anthology 2026 正式页面；TagSpeech 的 Oral 状态见最新 CV 和 arXiv v2 评论。
- Auden-Voice 的 ICASSP 2026 状态：最新 CV 与会议官方日程。
- Applied Linguistics 论文：正式卷期是 2026 年，online-first 为 2025 年；按用户要求放在 2025 年列表最后，保留卷期与 online-first 信息。
- 肖像来自用户的 UIUC 公开个人资料；原来的动漫图片仍保留在 `images/go.jpg`。
- 最新 PDF 原样保存；旧 PDF 路径继续保留，避免既有外部链接失效。

### 主要来源

- https://linguistics.illinois.edu/directory/profile/mhuo5
- https://export.arxiv.org/api/query?search_query=au:%22Mingyue_Huo%22&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending
- https://aclanthology.org/2026.acl-long.1938/
- https://aclanthology.org/2026.acl-long.1581/
- https://www.cmsworkshops.com/ICASSP2026/view_session.php?SessionID=1312&bare=1
- https://academic.oup.com/applij/article/47/2/406/8341053

删除了旧模板中另一位作者的教育、论文、奖项、LinkedIn、Google Scholar 和 Google Analytics 追踪代码。旧版本可从 Git 历史恢复。

## 项目图与关键词

`content/profile.json` 的 `highlights` 决定首页项目顺序，项目中的 `keywords` 与 `figure` 同步用于首页和 Projects 页。

- SpeechCritic：Figure 1，来源 https://arxiv.org/html/2609.34582v1/Fig1.png
- TagSpeech：Figure 2，来源 https://arxiv.org/html/2601.06896v2/model_structure.png

原论文图片无损转换为 WebP；SVG 的 viewBox 仅将周围空白移出显示范围，原图内容保留，点击可查看完整原图。
