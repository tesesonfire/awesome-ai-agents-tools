<div align="center">

# Awesome AI Agent Tools

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [简体中文](README.zh-CN.md)

A curated index of AI Agent tools, covering CLI, IDE extensions, desktop apps, and web-based agents.

</div>

A curated list of AI Agent tools — coding agents, editors, extensions, frameworks, orchestration platforms, and supporting utilities. Entries are grouped by role so you can locate a tool by what it does rather than by who published it.

Each entry follows the same shape: a link, an objective description, supported platforms, and a pricing model. Version badges below are rendered live from each project's latest GitHub release.

## Contents

- [Featured Tools](#featured-tools)
- [Official Agent Tools](#official-agent-tools)
- [Third-Party Agent Tools](#third-party-agent-tools)
- [IDE Integrations and Extensions](#ide-integrations-and-extensions)
- [Agent Frameworks and SDKs](#agent-frameworks-and-sdks)
- [Multi-Agent Orchestration](#multi-agent-orchestration)
- [Tools and Utilities](#tools-and-utilities)
- [Tag Legend](#tag-legend)
- [Contributing](#contributing)
- [License](#license)

## Featured Tools

> A quick index of widely used, actively maintained projects across all categories. Version numbers and release dates are read live from each repository's latest GitHub release via [Shields.io](https://shields.io), so they track upstream automatically. Repositories without formal GitHub releases may show `no releases`; for those that publish only pre-releases (such as DeepSeek Harness), the `include_prereleases` parameter is enabled.

| Tool | Latest version | Released | Vendor | Form | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Codex** | ![Version](https://img.shields.io/github/v/release/openai/codex?label=&color=blue) | ![Date](https://img.shields.io/github/release-date/openai/codex?label=) | OpenAI | CLI / IDE | Open-source client / Subscription |
| **Claude Code** | ![Version](https://img.shields.io/github/v/release/anthropics/claude-code?label=&color=blue) | ![Date](https://img.shields.io/github/release-date/anthropics/claude-code?label=) | Anthropic | CLI / IDE | Commercial / Subscription |
| **Kimi Code** | ![Version](https://img.shields.io/github/v/release/MoonshotAI/kimi-code?label=&color=blue) | ![Date](https://img.shields.io/github/release-date/MoonshotAI/kimi-code?label=) | Moonshot AI | CLI | Free tier + Subscription |
| **DeepSeek Harness** | ![Version](https://img.shields.io/github/v/release/deepseek-ai/deepseek-harness?include_prereleases&label=&color=blue) | ![Date](https://img.shields.io/github/release-date-pre/deepseek-ai/deepseek-harness?label=) | DeepSeek | CLI / Web | Open source |
| **Oh My Pi** | ![Version](https://img.shields.io/github/v/release/can1357/oh-my-pi?label=&color=blue) | ![Date](https://img.shields.io/github/release-date/can1357/oh-my-pi?label=) | Community | CLI | Open source |
| **OpenCode** | ![Version](https://img.shields.io/github/v/release/anomalyco/opencode?label=&color=blue) | ![Date](https://img.shields.io/github/release-date/anomalyco/opencode?label=) | Anomaly | CLI / Web | Open source |
| **Gemini CLI** | ![Version](https://img.shields.io/github/v/release/google-gemini/gemini-cli?label=&color=blue) | ![Date](https://img.shields.io/github/release-date/google-gemini/gemini-cli?label=) | Google | CLI | Free tier + Open source |
| **GitHub Copilot** | ![Version](https://img.shields.io/github/v/release/microsoft/vscode-copilot-chat?label=&color=blue) | ![Date](https://img.shields.io/github/release-date/microsoft/vscode-copilot-chat?label=) | GitHub | IDE / CLI | Free tier + Subscription |

## Official Agent Tools

Agent tools published and maintained by model or platform vendors, typically integrated with their own models, accounts, and billing.

- [Claude Code](https://github.com/anthropics/claude-code#readme) - Anthropic's official terminal coding agent that reads your codebase and handles routine tasks, Git operations, and explanations. Platforms: CLI, VS Code, JetBrains. Pricing: Commercial subscription billed by usage. `[CLI]` `[IDE]` `[Paid]`
- [Codex](https://github.com/openai/codex#readme) - OpenAI's official lightweight coding agent that runs locally in the terminal, with IDE extension and cloud task support. Platforms: CLI, VS Code, macOS. Pricing: Open-source client; model usage billed via subscription or API. `[CLI]` `[IDE]` `[Open Source]`
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness#readme) - DeepSeek's official agent harness with a fully plugin-based architecture, offering both CLI and web interfaces. Platforms: CLI, Web. Pricing: Free and open source. `[CLI]` `[Web]` `[Free]` `[Open Source]`
- [Gemini CLI](https://github.com/google-gemini/gemini-cli#readme) - Google's official open-source terminal agent that brings Gemini models into command-line workflows. Platforms: CLI. Pricing: Free and open source, with a free tier for personal accounts. `[CLI]` `[Free]` `[Open Source]`
- [GitHub Copilot](https://github.com/microsoft/vscode-copilot-chat#readme) - GitHub's official completion and coding agent, providing completions, chat, and agent mode inside the editor. Platforms: VS Code, JetBrains, Neovim, Web. Pricing: Free tier available, otherwise subscription-based; extension source is open. `[IDE]` `[Free Tier]` `[Paid]`
- [GitHub Copilot CLI](https://github.com/github/copilot-cli#readme) - GitHub's official terminal-native coding agent with agentic task execution. Platforms: CLI. Pricing: Included with a Copilot subscription. `[CLI]` `[Paid]`
- [Kimi Code](https://github.com/MoonshotAI/kimi-code#readme) - Moonshot AI's official terminal coding agent built on Kimi models, offering an interactive TUI and scriptable invocation. Platforms: CLI. Pricing: Open-source client with a free tier and subscription plans. `[CLI]` `[Free Tier]` `[Paid]` `[Open Source]`
- [Qwen Code](https://github.com/QwenLM/qwen-code#readme) - The official coding agent CLI from Alibaba's Qwen team, supporting multiple model providers. Platforms: CLI. Pricing: Free and open source; model usage billed by consumption. `[CLI]` `[Free]` `[Open Source]`

## Third-Party Agent Tools

General-purpose agents built by communities or independent teams that work with a range of models.

- [Aider](https://github.com/Aider-AI/aider#readme) - AI pair programming in your terminal, with Git repository awareness and automatic commits. Platforms: CLI. Pricing: Free and open source; model usage billed by consumption. `[CLI]` `[Free]` `[Open Source]`
- [Amp](https://ampcode.com/) - An agentic coding tool from Sourcegraph, available as a CLI and editor extension. Platforms: CLI, VS Code. Pricing: Commercial subscription with a free tier. `[CLI]` `[IDE]` `[Free Tier]` `[Paid]`
- [Crush](https://github.com/charmbracelet/crush#readme) - A terminal coding agent from Charm with multi-model switching and LSP integration, built on a TUI component library. Platforms: CLI. Pricing: Free and open source; model usage billed by consumption. `[CLI]` `[Free]` `[Open Source]`
- [Goose](https://github.com/aaif-goose/goose#readme) - An open-source, extensible agent that goes beyond code suggestions to install, execute, and test, extensible through MCP. Platforms: CLI, Desktop. Pricing: Free and open source; model usage billed by consumption. `[CLI]` `[Desktop]` `[Free]` `[Open Source]`
- [Live Agent](https://github.com/Stack-Cairn/LiveAgent#readme) - A full-featured AI agent desktop client with WebUI remote access and customizable extensions. Platforms: Desktop, Web. Pricing: Free and open source; model usage billed by consumption. `[Desktop]` `[Web]` `[Free]` `[Open Source]`
- [Oh My Pi](https://github.com/can1357/oh-my-pi#readme) - A terminal coding agent evolved from a Pi fork, adding dedicated tools, model roles, MCP, plugins, and workflows. Platforms: CLI. Pricing: Free and open source; model usage billed by consumption. `[CLI]` `[Free]` `[Open Source]`
- [OpenCode](https://github.com/anomalyco/opencode#readme) - An open-source coding agent with a terminal interface and additional forms such as web. Platforms: CLI, Web. Pricing: Free and open source; model usage billed by consumption. `[CLI]` `[Web]` `[Free]` `[Open Source]`
- [OpenHands](https://github.com/OpenHands/OpenHands#readme) - An open-source AI development agent that can write code, run commands, browse the web, and submit changes autonomously. Platforms: Web, CLI, Cloud. Pricing: Free and open source; hosted cloud is a paid service. `[Web]` `[CLI]` `[Free]` `[Paid]` `[Open Source]`
- [Pi](https://github.com/earendil-works/pi#readme) - A minimal, extensible terminal coding harness with tree-structured sessions and custom model providers. Platforms: CLI. Pricing: Free and open source; model usage billed by consumption. `[CLI]` `[Free]` `[Open Source]`

## IDE Integrations and Extensions

Agent tools that run as editor or IDE extensions, with a graphical interface as the primary interaction model.

- [Cline](https://github.com/cline/cline#readme) - An autonomous coding agent in VS Code, also available as an SDK, supporting multiple model providers. Platforms: VS Code, JetBrains. Pricing: Free and open source; model usage billed by consumption. `[IDE]` `[Free]` `[Open Source]`
- [Continue](https://github.com/continuedev/continue#readme) - An open-source coding agent for building custom completion, chat, and edit experiences in the IDE. Platforms: VS Code, JetBrains. Pricing: Free and open source; model usage billed by consumption. `[IDE]` `[Free]` `[Open Source]`
- [Cursor](https://cursor.com/) - An AI-first code editor built on a VS Code fork, with built-in agent mode and codebase indexing. Platforms: Desktop, CLI, Web. Pricing: Commercial subscription with a free tier. `[Desktop]` `[IDE]` `[Free Tier]` `[Paid]`
- [Kilo Code](https://github.com/Kilo-Org/kilocode#readme) - An all-in-one agentic engineering platform available as editor extensions and a CLI. Platforms: VS Code, JetBrains, CLI. Pricing: Free and open source; model usage billed by consumption. `[IDE]` `[CLI]` `[Free]` `[Open Source]`
- [Roo Code](https://github.com/RooCodeInc/Roo-Code#readme) - A VS Code extension that assigns the agent different development roles through configurable modes. Platforms: VS Code. Pricing: Free and open source; model usage billed by consumption. `[IDE]` `[Free]` `[Open Source]`
- [Zed](https://github.com/zed-industries/zed#readme) - A high-performance collaborative editor with a built-in agent panel and support for external agents. Platforms: Desktop. Pricing: Editor is free and open source; agent features require a subscription. `[Desktop]` `[Free]` `[Paid]` `[Open Source]`

## Agent Frameworks and SDKs

Libraries and toolkits for developers building their own agents, including runtimes, orchestration primitives, and multi-model abstraction layers.

- [Agent Development Kit (ADK)](https://github.com/google/adk-python#readme) - Google's open-source, code-first Python toolkit for building, evaluating, and deploying agents. Platforms: SDK. Pricing: Free and open source. `[SDK]` `[Free]` `[Open Source]`
- [LangChain](https://github.com/langchain-ai/langchain#readme) - An agent engineering platform providing model abstractions, tool calling, and agent building blocks. Platforms: SDK. Pricing: Free and open source; the hosted platform is a paid service. `[SDK]` `[Free]` `[Paid]` `[Open Source]`
- [LangGraph](https://github.com/langchain-ai/langgraph#readme) - A graph-structured runtime for building stateful, resumable agents. Platforms: SDK. Pricing: Free and open source. `[SDK]` `[Free]` `[Open Source]`
- [LlamaIndex](https://github.com/run-llama/llama_index#readme) - An agent and data framework focused on document processing and retrieval augmentation. Platforms: SDK. Pricing: Free and open source. `[SDK]` `[Free]` `[Open Source]`
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python#readme) - OpenAI's lightweight framework for multi-agent workflows. Platforms: SDK. Pricing: Free and open source; model usage billed by consumption. `[SDK]` `[Free]` `[Open Source]`
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel#readme) - Microsoft's model integration SDK for bringing LLM capabilities and plugins into existing applications. Platforms: SDK. Pricing: Free and open source. `[SDK]` `[Free]` `[Open Source]`

## Multi-Agent Orchestration

Platforms for coordinating multiple agents, orchestrating workflows, or visually building agent pipelines.

- [AutoGen](https://github.com/microsoft/autogen#readme) - Microsoft's framework for agentic AI, supporting multi-agent conversation and collaboration patterns. Platforms: SDK. Pricing: Free and open source. `[SDK]` `[Free]` `[Open Source]`
- [CrewAI](https://github.com/crewAIInc/crewAI#readme) - A framework for orchestrating autonomous agent teams through role-playing and collaboration. Platforms: SDK. Pricing: Free and open source; enterprise edition is a paid service. `[SDK]` `[Free]` `[Paid]` `[Open Source]`
- [Dify](https://github.com/langgenius/dify#readme) - An integrated agentic workflow and RAG pipeline platform with a visual orchestration interface. Platforms: Web, Self-hosted. Pricing: Open-source edition is free, cloud service is paid, license includes commercial restrictions. `[Web]` `[Free Tier]` `[Paid]` `[Open Source]`
- [Flowise](https://github.com/FlowiseAI/Flowise#readme) - A low-code tool for visually building AI agents and LLM applications. Platforms: Web, Self-hosted. Pricing: Free and open source; cloud service is paid. `[Web]` `[Free Tier]` `[Paid]` `[Open Source]`
- [Langflow](https://github.com/langflow-ai/langflow#readme) - A visual platform for building and deploying AI agents and workflows. Platforms: Web, Self-hosted. Pricing: Free and open source. `[Web]` `[Free]` `[Open Source]`
- [n8n](https://github.com/n8n-io/n8n#readme) - A visual workflow automation platform with native AI capabilities, combining LLM nodes with external services. Platforms: Web, Self-hosted. Pricing: Fair-code license; self-hosting is free, cloud service is paid. `[Web]` `[Free Tier]` `[Paid]` `[Open Source]`

## Tools and Utilities

Supporting tools that supply agents with context, tool access, usage observability, and interface enhancements.

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers#readme) - A community-maintained index of MCP servers. Platforms: MCP. Pricing: Free and open source. `[MCP]` `[Free]` `[Open Source]`
- [ccusage](https://github.com/ccusage/ccusage#readme) - Analyzes token usage and cost for Claude Code and similar agents from local session data. Platforms: CLI. Pricing: Free and open source. `[CLI]` `[Free]` `[Open Source]`
- [Claude Code Usage Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor#readme) - A terminal dashboard that tracks Claude Code token consumption and remaining quota in real time. Platforms: CLI. Pricing: Free and open source. `[CLI]` `[Free]` `[Open Source]`
- [Context7](https://github.com/upstash/context7#readme) - An MCP service that supplies up-to-date, versioned documentation to LLMs and code editors. Platforms: Web, MCP. Pricing: Free and open source; hosted service offers a free tier. `[MCP]` `[Free Tier]` `[Open Source]`
- [FastMCP](https://github.com/PrefectHQ/fastmcp#readme) - A framework for building MCP servers and clients in a fast, Pythonic way. Platforms: SDK. Pricing: Free and open source. `[SDK]` `[MCP]` `[Free]` `[Open Source]`
- [MCP Servers](https://github.com/modelcontextprotocol/servers#readme) - The official reference collection of Model Context Protocol servers. Platforms: MCP. Pricing: Free and open source. `[MCP]` `[Free]` `[Open Source]`
- [opcode](https://github.com/winfunc/opcode#readme) - A GUI application and toolkit for Claude Code that manages sessions and runs background agents. Platforms: Desktop. Pricing: Free and open source. `[Desktop]` `[Free]` `[Open Source]`

## Tag Legend

| Tag | Meaning |
| :--- | :--- |
| `[CLI]` | Used through a command line or terminal interface |
| `[IDE]` | Runs as an editor or IDE extension or plugin |
| `[Desktop]` | Standalone desktop client application |
| `[Web]` | Browser-accessible or self-hostable web service |
| `[SDK]` | Library or framework called from developer-written code |
| `[MCP]` | Server or client related to the Model Context Protocol |
| `[Free]` | Completely free to use |
| `[Free Tier]` | Offers a free allowance or free plan, billed beyond that |
| `[Paid]` | Requires a paid subscription or usage-based billing |
| `[Open Source]` | Source code is publicly available |

## Contributing

Contributions of new tools and corrections to existing entries are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting, as it documents the entry format, inclusion criteria, and checklist.

- New tools should come with an official repository link and a one-sentence objective description.
- Marketing-oriented, unverifiable, or unmaintained projects are not accepted.
- If you find a broken link or an outdated description, a direct fix is welcome.

## License

This project is released under [CC0 1.0 Universal](LICENSE). You may freely copy, modify, and distribute this list without attribution.
