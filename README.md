# 大数据与人工智能（bigdata-ai-course）

个人课程学习仓库 ——《大数据与人工智能》

## 一、仓库用途

本仓库用于存放《大数据与人工智能》课程的学习产物，当前包含两部分：

1. **AI 概念学习作业**（本周作业）：围绕 **Agent（智能体）、大模型的上下文（Context）、Skill（技能）** 三个概念，产出结构化学习资料、概念关系说明，以及一个可复用的概念学习 Skill；
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
│   └── concept-relationship.md                # 三个概念的关系说明（含 Mermaid 图）
└── .workbuddy/
    └── skills/
        └── concept-learning/
            └── SKILL.md                       # 项目级 Skill：概念学习资料生成器
```

## 三、项目级 Skill

### 3.1 存放路径

`.workbuddy/skills/concept-learning/SKILL.md`（项目级 Skill，随仓库共享，clone 本仓库的人可直接使用）。

### 3.2 它是做什么的

`concept-learning` 是一个**通用的概念学习资料生成 Skill**：输入任意一个新概念（如 RAG、MCP、LoRA），它会按固定流程完成学习并产出结构化资料——检索资料 → 交叉验证 → 费曼式个人解释 → 按"个人解释 / 核心机制 / 应用场景 / 易混淆问题 / 资料来源"五段式结构撰写 → 逐条验证来源 URL → 按自检清单验收。**它不绑定本次作业的三个概念**，换任何新学习主题均可复用。

### 3.3 如何在 WorkBuddy 中调用

1. 用 WorkBuddy 打开本仓库目录（本项目即 `bigdata-ai-course/`），项目级 Skill 会被自动发现并注册；
2. 在对话中直接描述任务，WorkBuddy 会根据 Skill 的 `description` 自动匹配并加载它，例如：
   > "帮我学习一下 RAG 这个概念，用 concept-learning 生成学习资料，输出到 learning-materials/"
3. 也可以显式点名调用（斜杠命令形式）：`/concept-learning 学习 MCP 概念`；
4. 产出文件默认保存在 `learning-materials/` 下，与本仓库现有资料并列。

## 四、已生成的学习资料

| 文件 | 概念 | 核心内容 |
|------|------|----------|
| `learning-materials/agent.md` | Agent（智能体） | Agent 与聊天机器人的本质区别（控制权）；规划/记忆/工具/LLM 四大组成；用 WorkBuddy 完成本作业的真实场景；Agent ≠ 工作流 ≠ 多轮对话 |
| `learning-materials/llm-context.md` | 大模型的上下文 | "桌面"类比；上下文的五个组成与注意力机制、上下文工程；Agent 按需检索代码的真实场景；上下文 ≠ 窗口 ≠ 长期记忆 |
| `learning-materials/skill.md` | Skill（技能） | "交接文档"类比；YAML 元数据 + 指令正文的结构与"注册→匹配→加载→复用"机制；Skill ≠ 提示词 ≠ 工具 ≠ Agent |
| `learning-materials/concept-relationship.md` | 三者关系 | 文字 + 对照表 + Mermaid 流程图；重点说明上下文如何影响 Agent 工作、Skill 如何沉淀可复用任务知识 |

## 五、使用 AI 后的人工核查与修改

本作业在 AI（WorkBuddy Agent）辅助下完成，我对产出做了以下核查与修订：

**AI 侧完成的核查（已在生成过程中执行）：**

- **资料来源逐条验证**：AI 在写入资料前对所有引用链接做了实际访问验证。过程中发现并处理了两个问题——Lilian Weng 博客的 context engineering 文章原定 URL 返回 404（已弃用，改引其他已验证来源）；`docs.claude.com` 的 Agent Skills 文档重定向到 `platform.claude.com` 后在当前地区不可访问（已改用可访问的 `code.claude.com/docs/en/skills`）。最终五个来源均验证可达。
- **多来源交叉验证**：Agent 的四大组成、上下文工程的机制等关键结论均有两个以上独立来源相互印证（见各资料末尾来源表）。
- **敏感信息检查**：确认全部提交内容不含 API Key、密码或个人隐私。

**本人复核与修改：**

- 通读了三份资料与关系说明，删改了与本人理解不符的表述，补充了第一人称的解释视角（如"我的个人解释"章节中根据自己的理解修正了类比）；
- 核对了 Mermaid 图与正文描述的一致性；
- 调整了 README 的仓库结构说明，使其与重构后的目录一致。

## 六、环境信息

| 工具 | 版本 |
|------|------|
| Git | 2.55.0 |
| Python | 3.12.10 |
| VSCode | 24.18.1 |

## 七、常用 Git 命令

```bash
git clone https://github.com/Tiam0219/bigdata-ai-course.git   # 克隆仓库
git status                                                    # 查看文件状态
git add .                                                     # 添加所有改动到暂存区
git commit -m "提交说明"                                       # 提交到本地仓库
git push origin main                                          # 推送到 GitHub
```

---

Maintained by [Tiam0219](https://github.com/Tiam0219)
