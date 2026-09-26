<div align="center">

# Awesome AI Agent Tools

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [简体中文](README.zh-CN.md)

一个精选的 AI Agent 工具索引，覆盖 CLI、IDE 插件、桌面端、Web 端等多种形态。

</div>

本列表收录 AI Agent 相关工具，涵盖编码 Agent、编辑器、扩展插件、框架、编排平台及配套实用程序。条目按工具承担的职责分组，便于按用途而非按出品方进行查找。

每条条目结构一致：链接、客观描述、支持平台与价格模式。下表中的版本徽章从各项目最新 GitHub Release 实时渲染。

## Contents

- [Agent 框架与 SDK](#agent-框架与-sdk)
- [IDE 集成与插件](#ide-集成与插件)
- [多 Agent 编排工具](#多-agent-编排工具)
- [官方 Agent 工具](#官方-agent-工具)
- [工具与实用程序](#工具与实用程序)
- [标签说明](#标签说明)
- [第三方 Agent 工具](#第三方-agent-工具)
- [精选工具速览](#精选工具速览)
- [许可证](#许可证)
- [贡献](#贡献)

## 精选工具速览

> 本表为快速索引，收录各分类中维护活跃、使用广泛的代表项目，并已覆盖 DeepSeek 官方 Agent 接入列表中的全部工具。版本号通过 [Shields.io](https://shields.io) 从各仓库最新 Release 实时读取，因此会随上游自动更新；对于仅发布预发布版本的仓库（如 DeepSeek Harness），已启用 `include_prereleases` 参数。「最近发布」一列取最新正式版本：24 小时内发布的显示 `24h内`，更早的显示具体日期，格式为 `MM-DD`。

| 工具 | 最新版本 | 最近发布 | 出品方 | 形态 | 价格 | 发布页 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Codex** | ![Version](https://img.shields.io/github/v/release/openai/codex?label=&color=blue) | 24h内 | OpenAI | CLI / IDE | 开源客户端 / 订阅 | [发布页](https://github.com/openai/codex/releases) |
| **Claude Code** | ![Version](https://img.shields.io/github/v/release/anthropics/claude-code?label=&color=blue) | 24h内 | Anthropic | CLI / IDE | 商业 / 订阅 | [发布页](https://github.com/anthropics/claude-code/releases) |
| **Kimi Code** | ![Version](https://img.shields.io/github/v/release/MoonshotAI/kimi-code?label=&color=blue) | 09-24 | Moonshot AI | CLI | 免费 + 订阅 | [发布页](https://github.com/MoonshotAI/kimi-code/releases) |
| **DeepSeek Harness** | ![Version](https://img.shields.io/github/v/release/deepseek-ai/deepseek-harness?include_prereleases&label=&color=blue) | 09-24 | DeepSeek | CLI / Web | 开源 | [发布页](https://github.com/deepseek-ai/deepseek-harness/releases) |
| **Pi** | ![Version](https://img.shields.io/github/v/release/earendil-works/pi?label=&color=blue) | 09-22 | Earendil Works | CLI | 开源 | [发布页](https://github.com/earendil-works/pi/releases) |
| **Oh My Pi** | ![Version](https://img.shields.io/github/v/release/can1357/oh-my-pi?label=&color=blue) | 24h内 | 社区 | CLI | 开源 | [发布页](https://github.com/can1357/oh-my-pi/releases) |
| **OpenCode** | ![Version](https://img.shields.io/github/v/release/anomalyco/opencode?label=&color=blue) | 09-21 | Anomaly | CLI / Web | 开源 | [发布页](https://github.com/anomalyco/opencode/releases) |
| **Gemini CLI** | ![Version](https://img.shields.io/github/v/release/google-gemini/gemini-cli?label=&color=blue) | 09-23 | Google | CLI | 免费额度 + 开源 | [发布页](https://github.com/google-gemini/gemini-cli/releases) |
| **GitHub Copilot** | ![Version](https://img.shields.io/github/v/release/microsoft/vscode-copilot-chat?label=&color=blue) | 04-07 | GitHub | IDE / CLI | 免费额度 + 订阅 | [发布页](https://github.com/microsoft/vscode-copilot-chat/releases) |
| **AstrBot** | ![Version](https://img.shields.io/github/v/release/AstrBotDevs/AstrBot?label=&color=blue) | 09-14 | 社区 | Web / 聊天平台 | 开源 | [发布页](https://github.com/AstrBotDevs/AstrBot/releases) |
| **Cherry Studio** | ![Version](https://img.shields.io/github/v/release/CherryHQ/cherry-studio?label=&color=blue) | 09-24 | CherryHQ | 桌面端 | 开源 | [发布页](https://github.com/CherryHQ/cherry-studio/releases) |
| **Codewhale（DeepSeek-TUI）** | ![Version](https://img.shields.io/github/v/release/Hmbown/Codewhale?label=&color=blue) | 09-22 | 社区 | CLI | 开源 | [发布页](https://github.com/Hmbown/Codewhale/releases) |
| **Hermes** | ![Version](https://img.shields.io/github/v/release/NousResearch/hermes-agent?label=&color=blue) | 09-24 | Nous Research | CLI | 开源 | [发布页](https://github.com/NousResearch/hermes-agent/releases) |
| **LobeHub** | ![Version](https://img.shields.io/github/v/release/lobehub/lobehub?label=&color=blue) | 09-20 | LobeHub | Web / 桌面端 | 开源 | [发布页](https://github.com/lobehub/lobehub/releases) |
| **OpenClaw** | ![Version](https://img.shields.io/github/v/release/openclaw/openclaw?label=&color=blue) | 09-23 | 社区 | CLI / 聊天平台 | 开源 | [发布页](https://github.com/openclaw/openclaw/releases) |
| **Deep Code** | ![Version](https://img.shields.io/github/v/release/lessweb/deepcode-cli?label=&color=blue) | 09-17 | 社区 | CLI / IDE | 开源 | [发布页](https://github.com/lessweb/deepcode-cli/releases) |
| **Reasonix** | ![Version](https://img.shields.io/github/v/release/esengine/DeepSeek-Reasonix?label=&color=blue) | 24h内 | 社区 | CLI | 开源 | [发布页](https://github.com/esengine/DeepSeek-Reasonix/releases) |

## 官方 Agent 工具

由模型或平台厂商官方发布和维护的 Agent 工具，通常与自家模型、账号体系和计费方式深度集成。

- [Claude Code](https://github.com/anthropics/claude-code#readme) - Anthropic 官方终端编码 Agent，可读取代码库、执行常规任务与 Git 操作。平台：CLI、VS Code、JetBrains。价格：商业订阅，按用量计费。 `[CLI]` `[IDE]` `[Paid]`
- [Codex](https://github.com/openai/codex#readme) - OpenAI 官方轻量级编码 Agent，在终端中本地运行，也可通过 IDE 扩展与云端任务使用。平台：CLI、VS Code、macOS。价格：客户端开源，模型按订阅或 API 计费。 `[CLI]` `[IDE]` `[Open Source]`
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness#readme) - DeepSeek 官方 Agent 运行框架，采用全插件化架构，提供 CLI 与 Web 界面。平台：CLI、Web。价格：开源免费。 `[CLI]` `[Web]` `[Free]` `[Open Source]`
- [Gemini CLI](https://github.com/google-gemini/gemini-cli#readme) - Google 官方开源终端 Agent，将 Gemini 模型接入命令行工作流。平台：CLI。价格：开源免费，附带个人账号免费额度。 `[CLI]` `[Free]` `[Open Source]`
- [GitHub Copilot](https://github.com/microsoft/vscode-copilot-chat#readme) - GitHub 官方代码补全与编码 Agent，在编辑器中提供补全、对话和 Agent 模式。平台：VS Code、JetBrains、Neovim、Web。价格：提供免费额度，其余为订阅制；扩展源码开放。 `[IDE]` `[Free Tier]` `[Paid]`
- [GitHub Copilot CLI](https://github.com/github/copilot-cli#readme) - GitHub 官方终端原生编码 Agent，具备 Agent 化任务执行能力。平台：CLI。价格：随 Copilot 订阅提供。 `[CLI]` `[Paid]`
- [Kimi Code](https://github.com/MoonshotAI/kimi-code#readme) - 月之暗面官方终端编码 Agent，基于 Kimi 模型，提供交互式 TUI 与脚本化调用。平台：CLI。价格：开源客户端，提供免费额度与订阅方案。 `[CLI]` `[Free Tier]` `[Paid]` `[Open Source]`
- [Qwen Code](https://github.com/QwenLM/qwen-code#readme) - 阿里云通义千问团队官方编码 Agent CLI，支持多模型提供商配置。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`

## 第三方 Agent 工具

由社区或独立团队构建、可搭配多种模型使用的通用 Agent 工具。

- [Aider](https://github.com/Aider-AI/aider#readme) - 终端中的 AI 结对编程工具，支持 Git 仓库感知与自动提交。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`
- [Amp](https://ampcode.com/) - Sourcegraph 推出的 Agent 化编码工具，提供 CLI 与编辑器扩展。平台：CLI、VS Code。价格：商业订阅，提供免费额度。 `[CLI]` `[IDE]` `[Free Tier]` `[Paid]`
- [AstrBot](https://github.com/AstrBotDevs/AstrBot#readme) - 开源 Agent 助手与开发框架，可接入多种消息平台、LLM、插件与 MCP。平台：Web、自托管。价格：开源免费。 `[Web]` `[Free]` `[Open Source]`
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio#readme) - 开源跨平台桌面 AI 客户端，内置智能对话、自主 Agent、知识库与 300+ 助手。平台：桌面端。价格：开源免费。 `[Desktop]` `[Free]` `[Open Source]`
- [Codewhale (DeepSeek-TUI)](https://github.com/Hmbown/Codewhale#readme) - Rust 编写的终端编码 Agent，采用 Codex 风格架构，提供沙箱化工具、MCP 客户端与服务端以及大上下文支持。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`
- [Crush](https://github.com/charmbracelet/crush#readme) - Charm 出品的终端编码 Agent，支持多模型切换与 LSP 集成，界面由 TUI 组件库构建。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`
- [Goose](https://github.com/aaif-goose/goose#readme) - 开源可扩展 Agent，除代码建议外还能安装、执行与测试，支持通过 MCP 扩展能力。平台：CLI、桌面端。价格：开源免费，模型按用量计费。 `[CLI]` `[Desktop]` `[Free]` `[Open Source]`
- [Hermes](https://github.com/NousResearch/hermes-agent#readme) - Nous Research 推出的开源自我进化 AI Agent。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`
- [Live Agent](https://github.com/Stack-Cairn/LiveAgent#readme) - 功能完整的 AI Agent 桌面客户端，支持 WebUI 远程访问和自定义扩展。平台：桌面端、Web。价格：开源免费，模型按用量计费。 `[Desktop]` `[Web]` `[Free]` `[Open Source]`
- [LobeHub](https://github.com/lobehub/lobehub#readme) - Agent 运营平台，通过招聘、排班与汇报将多个 Agent 组织成 7×24 小时运作。平台：Web、桌面端。价格：开源免费，托管服务提供免费额度。 `[Web]` `[Desktop]` `[Free Tier]` `[Open Source]`
- [Oh My Pi](https://github.com/can1357/oh-my-pi#readme) - 基于 Pi 分支演进的终端编码 Agent，增加专用工具、模型角色、MCP、插件与工作流能力。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`
- [OpenClaw](https://github.com/openclaw/openclaw#readme) - 开源个人 AI 助手，可接入各类聊天平台，并通过 Skill 扩展能力。平台：CLI、自托管。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`
- [OpenCode](https://github.com/anomalyco/opencode#readme) - 开源编码 Agent，提供终端界面，并有 Web 等多种形态。平台：CLI、Web。价格：开源免费，模型按用量计费。 `[CLI]` `[Web]` `[Free]` `[Open Source]`
- [OpenHands](https://github.com/OpenHands/OpenHands#readme) - 开源 AI 开发 Agent，可自主编写代码、执行命令、浏览网页并提交变更。平台：Web、CLI、云端。价格：开源免费，云端托管为付费服务。 `[Web]` `[CLI]` `[Free]` `[Paid]` `[Open Source]`
- [Pi](https://github.com/earendil-works/pi#readme) - 极简且可扩展的终端编码框架，支持树状会话结构与自定义模型提供商。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`
- [Reasonix](https://github.com/esengine/DeepSeek-Reasonix#readme) - DeepSeek 原生的终端编码 Agent，围绕前缀缓存稳定性设计，原生支持 MCP。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`

## IDE 集成与插件

作为编辑器或 IDE 扩展运行、以图形界面为主要交互方式的 Agent 工具。

- [Cline](https://github.com/cline/cline#readme) - VS Code 中的自主编码 Agent，同时以 SDK 和编辑器扩展形式提供，支持多家模型提供商。平台：VS Code、JetBrains。价格：开源免费，模型按用量计费。 `[IDE]` `[Free]` `[Open Source]`
- [Continue](https://github.com/continuedev/continue#readme) - 开源编码 Agent，可在 IDE 中构建自定义补全、对话与编辑体验。平台：VS Code、JetBrains。价格：开源免费，模型按用量计费。 `[IDE]` `[Free]` `[Open Source]`
- [Cursor](https://cursor.com/) - 基于 VS Code 分支构建的 AI 优先代码编辑器，内置 Agent 模式与代码库索引。平台：桌面端、CLI、Web。价格：商业订阅，提供免费额度。 `[Desktop]` `[IDE]` `[Free Tier]` `[Paid]`
- [Deep Code](https://github.com/lessweb/deepcode-cli#readme) - 专为 DeepSeek-V4 系列模型优化的终端 AI 编码助手，支持深度思考、推理强度控制与 Agent Skills。平台：CLI、VS Code。价格：开源免费，模型按用量计费。 `[CLI]` `[IDE]` `[Free]` `[Open Source]`
- [Kilo Code](https://github.com/Kilo-Org/kilocode#readme) - 一体化 Agent 化工程平台，以编辑器扩展和 CLI 形式提供。平台：VS Code、JetBrains、CLI。价格：开源免费，模型按用量计费。 `[IDE]` `[CLI]` `[Free]` `[Open Source]`
- [Langcli](https://github.com/LangcliTeam/langcli#readme) - 开源 AI 编程助手，兼容 Claude Code 配置并支持主流 LLM 模型。平台：CLI。价格：开源免费，模型按用量计费。 `[CLI]` `[Free]` `[Open Source]`
- [Qoder](https://qoder.com/) - 提供 IDE、CLI 与 JetBrains 插件三种形态的 Agentic Coding 产品，内置模型并支持接入自定义 API 密钥。平台：桌面端、CLI、JetBrains。价格：商业订阅，提供免费额度。 `[Desktop]` `[CLI]` `[IDE]` `[Free Tier]` `[Paid]`
- [Roo Code](https://github.com/RooCodeInc/Roo-Code#readme) - VS Code 扩展，通过可配置的多种模式让 Agent 承担不同开发角色。平台：VS Code。价格：开源免费，模型按用量计费。 `[IDE]` `[Free]` `[Open Source]`
- [WorkBuddy/CodeBuddy](https://www.codebuddy.ai/) - 腾讯推出的 AI Agent 与编程助手，支持通过配置文件接入自定义 OpenAI 兼容模型。平台：桌面端、IDE。价格：商业订阅，提供免费额度。 `[Desktop]` `[IDE]` `[Free Tier]` `[Paid]`
- [Zed](https://github.com/zed-industries/zed#readme) - 高性能多人协作编辑器，内置 Agent 面板与外部 Agent 接入能力。平台：桌面端。价格：编辑器开源免费，Agent 功能按订阅提供。 `[Desktop]` `[Free]` `[Paid]` `[Open Source]`

## Agent 框架与 SDK

供开发者构建自有 Agent 的代码库与工具包，包含运行时、编排原语和多模型抽象层。

- [Agent Development Kit (ADK)](https://github.com/google/adk-python#readme) - Google 开源的代码优先 Python 工具包，用于构建、评估与部署 Agent。平台：SDK。价格：开源免费。 `[SDK]` `[Free]` `[Open Source]`
- [LangChain](https://github.com/langchain-ai/langchain#readme) - Agent 工程平台，提供模型抽象、工具调用与 Agent 构建组件。平台：SDK。价格：开源免费，托管平台为付费服务。 `[SDK]` `[Free]` `[Paid]` `[Open Source]`
- [LangGraph](https://github.com/langchain-ai/langgraph#readme) - 面向有状态、可恢复 Agent 的图结构编排运行时。平台：SDK。价格：开源免费。 `[SDK]` `[Free]` `[Open Source]`
- [LlamaIndex](https://github.com/run-llama/llama_index#readme) - 面向文档处理与检索增强的 Agent 与数据框架。平台：SDK。价格：开源免费。 `[SDK]` `[Free]` `[Open Source]`
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python#readme) - OpenAI 官方的轻量级多 Agent 工作流框架。平台：SDK。价格：开源免费，模型按用量计费。 `[SDK]` `[Free]` `[Open Source]`
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel#readme) - 微软的模型集成 SDK，支持将 LLM 能力与插件接入现有应用。平台：SDK。价格：开源免费。 `[SDK]` `[Free]` `[Open Source]`

## 多 Agent 编排工具

用于协调多个 Agent 协作、编排工作流，或以可视化方式搭建 Agent 流水线的平台。

- [AutoGen](https://github.com/microsoft/autogen#readme) - 微软的 Agentic AI 编程框架，支持多 Agent 对话与协作模式。平台：SDK。价格：开源免费。 `[SDK]` `[Free]` `[Open Source]`
- [CrewAI](https://github.com/crewAIInc/crewAI#readme) - 通过角色扮演与协作编排自主 Agent 团队的框架。平台：SDK。价格：开源免费，企业版为付费服务。 `[SDK]` `[Free]` `[Paid]` `[Open Source]`
- [Dify](https://github.com/langgenius/dify#readme) - 一体化 Agentic 工作流与 RAG 流水线平台，提供可视化编排界面。平台：Web、自托管。价格：开源版免费，云服务付费，许可证含商用限制。 `[Web]` `[Free Tier]` `[Paid]` `[Open Source]`
- [Flowise](https://github.com/FlowiseAI/Flowise#readme) - 可视化搭建 AI Agent 与 LLM 应用的低代码工具。平台：Web、自托管。价格：开源免费，云服务付费。 `[Web]` `[Free Tier]` `[Paid]` `[Open Source]`
- [Langflow](https://github.com/langflow-ai/langflow#readme) - 用于构建和部署 AI Agent 与工作流的可视化平台。平台：Web、自托管。价格：开源免费。 `[Web]` `[Free]` `[Open Source]`
- [n8n](https://github.com/n8n-io/n8n#readme) - 具备原生 AI 能力的可视化工作流自动化平台，可组合 LLM 节点与外部服务。平台：Web、自托管。价格：fair-code 许可，自托管免费，云服务付费。 `[Web]` `[Free Tier]` `[Paid]` `[Open Source]`

## 工具与实用程序

为 Agent 提供上下文、工具接入、用量观测与界面增强的配套工具。

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers#readme) - 社区维护的 MCP 服务端索引。平台：MCP。价格：开源免费。 `[MCP]` `[Free]` `[Open Source]`
- [ccusage](https://github.com/ccusage/ccusage#readme) - 从本地会话数据统计 Claude Code 等 Agent 的 Token 用量与费用。平台：CLI。价格：开源免费。 `[CLI]` `[Free]` `[Open Source]`
- [Claude Code Usage Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor#readme) - 实时监控 Claude Code Token 消耗与额度余量的终端面板。平台：CLI。价格：开源免费。 `[CLI]` `[Free]` `[Open Source]`
- [Context7](https://github.com/upstash/context7#readme) - 为 LLM 与代码编辑器提供最新版本化文档的 MCP 服务。平台：Web、MCP。价格：开源免费，托管服务提供免费额度。 `[MCP]` `[Free Tier]` `[Open Source]`
- [FastMCP](https://github.com/PrefectHQ/fastmcp#readme) - 以 Pythonic 方式快速构建 MCP 服务端与客户端的框架。平台：SDK。价格：开源免费。 `[SDK]` `[MCP]` `[Free]` `[Open Source]`
- [MCP Servers](https://github.com/modelcontextprotocol/servers#readme) - Model Context Protocol 官方维护的参考服务端集合。平台：MCP。价格：开源免费。 `[MCP]` `[Free]` `[Open Source]`
- [opcode](https://github.com/winfunc/opcode#readme) - 面向 Claude Code 的图形界面应用与工具集，可管理会话并运行后台 Agent。平台：桌面端。价格：开源免费。 `[Desktop]` `[Free]` `[Open Source]`

## 标签说明

| 标签 | 含义 |
| :--- | :--- |
| `[CLI]` | 通过命令行或终端界面使用 |
| `[IDE]` | 作为编辑器或 IDE 的扩展、插件运行 |
| `[Desktop]` | 独立的桌面客户端应用 |
| `[Web]` | 浏览器访问或可自托管的 Web 服务 |
| `[SDK]` | 供开发者编写代码调用的库或框架 |
| `[MCP]` | 与 Model Context Protocol 相关的服务端或客户端 |
| `[Free]` | 完全免费使用 |
| `[Free Tier]` | 提供免费额度或免费套餐，超量后收费 |
| `[Paid]` | 需要付费订阅或按用量计费 |
| `[Open Source]` | 源代码公开可获取 |

## 贡献

欢迎补充新工具或修正现有条目。提交前请阅读 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)，其中说明了条目格式、收录标准和检查清单。亦可阅读 [英文版贡献指南](CONTRIBUTING.md)。

- 新增工具请同时提供官方仓库链接与一句话客观描述。
- 不接受营销性质、无法验证或长期无人维护的项目。
- 如发现链接失效或描述过时，欢迎直接提交修正。

## 许可证

本项目采用 [MIT](LICENSE) 许可证。你可以自由使用、修改和分发本列表内容，惟须保留版权声明与许可声明。
