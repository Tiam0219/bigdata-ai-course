# 大数据与人工智能（bigdata-ai-course）

个人课程学习仓库 ——《大数据与人工智能》

## 一、仓库用途

本仓库用于存放《大数据与人工智能》课程的学习产物，当前包含两部分：

1. **AI 概念学习作业**（本周作业）：围绕 **Agent（智能体）、大模型的上下文（Context）、Skill（技能）** 三个概念，产出结构化学习资料（含自测题、Mermaid 机制图、自检报告）、概念关系说明，以及一个通过通用性实测的可复用概念学习 Skill；
2. 后续课程内容将按章节继续补充。

## 二、仓库结构

```
bigdata-ai-course/
├── README.md                                  # 仓库说明（本文件）
├── .gitignore                                 # Git 忽略规则（含敏感信息排除）
├── learning-materials/                        # 概念学习资料
│   ├── agent.md                               # 概念一：Agent（智能体）
│   ├── llm-context.md                         # 概念二：大模型的上下文
│   ├── skill.md                               # 概念三：Skill（技能）
│   └── concept-relationship.md                # 三者关系说明（1 总览图 + 2 专题图）
└── .workbuddy/
    └── skills/
        └── concept-learning/
            └── SKILL.md                       # 项目级 Skill：概念学习资料生成器
```

## 三、项目级 Skill

### 3.1 存放路径

`.workbuddy/skills/concept-learning/SKILL.md`（项目级 Skill，随仓库共享，clone 本仓库的人可直接使用）。

### 3.2 它是做什么的

`concept-learning` 是一个**通用的概念学习资料生成 Skill**：输入任意一个新概念（如 RAG、MCP、LoRA），它会按固定 8 步流程完成学习并产出结构化资料——检索白名单一手资料 → 交叉验证 → 费曼式个人解释 → 结构化撰写 → 绘制 Mermaid 机制图 → 编制自测题 → 验证来源 URL → 自检与双重审查。**它不绑定本次作业的三个概念**，换任何新学习主题均可复用，且已通过换新概念的通用性实测（见 5.2 节实测记录）。

### 3.3 如何在 WorkBuddy 中调用

1. 用 WorkBuddy 打开本仓库目录（本项目即 `bigdata-ai-course/`），项目级 Skill 会被自动发现并注册；
2. 在对话中直接描述任务，WorkBuddy 会根据 Skill 的 `description` 自动匹配并加载它，例如：
   > "帮我学习一下 RAG 这个概念，用 concept-learning 生成学习资料，输出到 learning-materials/"
3. 也可以显式点名调用（斜杠命令形式）：`/concept-learning 学习 MCP 概念`；
4. 产出文件默认保存在 `learning-materials/` 下，与本仓库现有资料并列。

## 四、已生成的学习资料

| 文件 | 概念 | 核心内容 |
|------|------|----------|
| `learning-materials/agent.md` | Agent（智能体） | 控制权视角区分 Agent 与聊天机器人；四大组成 + 核心循环 Mermaid 图；WorkBuddy 完成本作业的真实场景；4 道自测题；自检报告 |
| `learning-materials/llm-context.md` | 大模型的上下文 | "桌面"类比；五组成分 + 信息流入 Mermaid 图；Lost in the Middle 实证；4 道自测题；自检报告 |
| `learning-materials/skill.md` | Skill（技能） | "交接文档"类比；结构 + 生命周期 Mermaid 图；4 道自测题；自检报告 |
| `learning-materials/concept-relationship.md` | 三者关系 | 文字 + 对照表 + 1 张总览图 + 2 张专题图（上下文如何影响 Agent / Skill 如何沉淀知识） |

每份资料均为七段式结构：个人解释 → 核心机制（含图）→ 应用场景 → 易混淆边界 → **自测题（含答案解析）** → 一手资料来源（含验证日期）→ **自检报告**。

## 五、质量保障机制

### 5.1 来源质量规范（白名单 / 黑名单）

全部学习资料只引用**专业权威的一手资料**，规范定义在 SKILL.md 第五节：

- ✅ **白名单**：学术论文（arXiv / NeurIPS、ICLR 等顶会）、官方一手文档与工程博客（Anthropic、Claude Code、WorkBuddy 等）、开放标准官网、知名研究者本人撰写的一手技术博客（如 Lilian Weng）；
- ❌ **黑名单**：论坛帖子与问答区（知乎回答、Stack Overflow 等）、内容农场与转载站（CSDN 转载、公众号转载等）、营销软文——此类只可用作检索线索，不得列入来源表；
- 所有来源 URL 写入前实际访问验证，并在来源表中注明验证日期（本次为 2026-09-10）。

### 5.2 自测题与双重自我审查机制

- **自测题**：每份资料 3~5 道（选择/判断/简答混合），题目必须命中该资料的易混淆点；答案与解析用 `<details>` 标签折叠（先自己作答再点开），用于检验读者是否真的理解而非背诵；
- **第一层·内容审查**：逐条核对来源支撑文中论断、Mermaid 图与正文一致、自测题答案与正文一致、无敏感信息——每份资料末尾的"自检报告"即执行留痕；
- **第二层·功能审查（通用性实测）**：换一个本次作业之外的新概念实际走一遍 Skill 流程，确认 Skill 可用。实测记录如下：

> **通用性实测记录（2026-09-10，实测概念：RAG）**
> - 步骤 1 检索白名单来源：可执行。候选一手来源已验证可达——Lewis et al., 《Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks》, NeurIPS 2020（arXiv:2005.11401），当天访问验证通过；另一类候选为各厂商官方 RAG 文档。
> - 步骤 2~6（交叉验证、个人解释、结构化撰写、机制图、自测题）：逐项走查均可执行，输出结构 1~5 节均可填写，无步骤绑定特定概念的情况。
> - 步骤 7~8（来源验证、自检与双重审查）：可执行，流程同本仓库三份资料。
> - **结论：通过**。Skill 的 8 步流程与七段式输出结构对"RAG"这一全新概念完整适用，确认其为通用 Skill 而非一次性提示词。

## 六、使用 AI 后的人工核查与修改

本作业在 AI（WorkBuddy Agent）辅助下完成，我对产出做了以下核查与修订：

**AI 侧完成的核查（已在生成过程中执行）：**

- **资料来源逐条验证**：两轮均对全部引用链接做实际访问验证。第一轮发现并处理了两个问题——Lilian Weng 博客的 context engineering 文章原定 URL 返回 404（弃用，改引其他来源）；`docs.claude.com` 的 Agent Skills 文档重定向后部分地区不可访问（改用 `code.claude.com/docs/en/skills`）。第二轮新增来源（ReAct 论文 arXiv:2210.03629、Anthropic Agent Skills 公告 claude.com/blog/skills、RAG 论文 arXiv:2005.11401）均于 2026-09-10 验证通过。
- **来源质量升级**：按白名单/黑名单制度复核全部来源，剔除非一手类别；来源表补注类别与验证日期。
- **多来源交叉验证**：Agent 的四大组成、上下文工程的机制等关键结论均有两个以上独立来源相互印证。
- **通用性实测**：用 RAG 走查 Skill 全流程并留痕（见 5.2 节）。
- **敏感信息检查**：确认全部提交内容不含 API Key、密码或个人隐私。

**本人复核与修改：**

- 通读三份资料与关系说明，删改与本人理解不符的表述，补充第一人称解释视角；
- 核对三张机制图、总览图、两张专题图与正文描述的一致性；
- 审阅自测题，确认题目命中易混淆点、答案与正文一致；
- 清理了仓库中与作业无关的文件（skill-dist 打包物），确认其未被 git 追踪、不影响仓库历史。

**第三轮复核（2026-09-10，经本人确认后由 AI 执行）：**

- **同步状态核查**：发现本地 2 个升级提交未推送到 GitHub，已补推并核实远端 main 与本地一致；
- **全部链接再验证**：对三份资料与本文引用的 11 个链接逐一重验——7 个非 arXiv 链接直接访问返回 200；4 个 arXiv 链接因本机代理拦截 curl 直连，改用备用通道逐一确认页面真实存在（ReAct / Lost in the Middle / Attention Is All You Need / RAG 四篇论文均核对到标题与作者）；
- **内容修正 3 处**：agent.md 自测题题干空格笔误；llm-context.md 的 Mermaid 图第五节点改为"记忆 / Skill 正文"，使其与第 2 节成分表真正一一对应（并同步修正自检报告措辞）；Lost in the Middle 来源补注 TACL 2023 录用状态（符合 Skill 白名单"arXiv 预印本须注明录用情况"的规则）；
- **体验优化**：三份资料的自测题答案改为 `<details>` 折叠展示。

## 七、环境信息

| 工具 | 版本 |
|------|------|
| Git | 2.55.0 |
| Python | 3.12.10 |
| VSCode | 24.18.1 |

## 八、常用 Git 命令

```bash
git clone https://github.com/Tiam0219/bigdata-ai-course.git   # 克隆仓库
git status                                                    # 查看文件状态
git add .                                                     # 添加所有改动到暂存区
git commit -m "提交说明"                                       # 提交到本地仓库
git push origin main                                          # 推送到 GitHub
```

---

Maintained by [Tiam0219](https://github.com/Tiam0219)
