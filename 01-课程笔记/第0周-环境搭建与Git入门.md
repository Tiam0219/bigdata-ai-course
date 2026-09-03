# 第 0 周笔记：环境搭建与 Git 入门

> 日期：2026-09-03

## 一、开发环境

- **Git 2.55.0**：版本控制工具，负责代码的 add / commit / push
- **Python 3.12.10**：课程主要编程语言
- **VSCode 24.18.1**：代码编辑器，推荐安装 Python 扩展

## 二、Git 核心概念

| 概念 | 说明 |
|------|------|
| 工作区 | 本地正在编辑的文件 |
| 暂存区 | `git add` 后待提交的改动 |
| 本地仓库 | `git commit` 后的版本历史 |
| 远程仓库 | GitHub 上托管的仓库 |

## 三、一次完整的提交流程

```bash
git status              # 1. 查看改动
git add .               # 2. 放入暂存区
git commit -m "说明"     # 3. 提交到本地仓库
git push origin main    # 4. 推送到 GitHub
```

## 四、遇到的问题与解决

- 首次 push 时 GitHub 需要登录授权，会弹出浏览器窗口，登录 GitHub 账号即可
- GitHub 已不支持密码推送，需使用浏览器授权或 Personal Access Token (PAT)
