[简体中文](CONTRIBUTING.md) | [English](CONTRIBUTING.en.md)

# Contributing

Thank you for wanting to contribute to this list. This document explains the inclusion criteria, entry format, and submission process, with the goal of keeping the list accurate and maintainable over time.

## What You Can Contribute

- **New tools**: add an AI Agent tool that is not yet listed.
- **Entry updates**: fix broken links, outdated descriptions, platform support, or pricing.
- **Category fixes**: point out entries that are filed under the wrong category.
- **Documentation improvements**: fix typos, broken anchors, or table rendering issues.

## Inclusion Criteria

A tool must meet all of the following to be listed:

1. **Directly related to AI Agents**: the tool itself drives, hosts, orchestrates, or supports an agent in completing tasks. Plain chat clients that only call an LLM API to generate text are not accepted.
2. **Publicly accessible**: an accessible official homepage or public repository, with functionality that can be understood without an invite code or private authorization.
3. **Usable today**: a public release or installable form of use, with signs of recent maintenance. Abandoned or concept-stage-only projects are not accepted.
4. **Verifiable description**: the facts in the one-sentence description must be directly checkable against official documentation, the repository README, or the product page.
5. **Non-promotional**: affiliate links, referral links, pure marketing landing pages, and traffic-driven submissions are not accepted.

The following will be rejected:

- Projects of unverifiable authenticity or unclear origin.
- Descriptions containing subjective marketing terms such as "best", "most powerful", or "number one".
- Links pointing to aggregator pages, download sites, or third-party mirrors rather than official sources.
- Entries functionally identical to an existing entry with no differentiating information.

## Entry Format

Each entry occupies one line and strictly follows this format:

```markdown
- [Tool Name](https://github.com/owner/repo#readme) - One-sentence objective description. Platforms: platform list. Pricing: pricing model. `[Platform]` `[Price]`
```

Rules:

- **Link**: prefer the GitHub repository link, ending with `#readme`. For closed-source commercial products, the official product page may be used.
- **Description**: sentence case, ending with a period; explain in one sentence what the tool does without piling up feature lists.
- **Platforms and pricing**: use the `Platforms:` and `Pricing:` prefixes, matching the wording style of existing entries.
- **Tags**: optional, chosen from the Tag Legend table in the README, wrapped in backticks, placed at the end of the line.

Example:

```markdown
- [Crush](https://github.com/charmbracelet/crush#readme) - A terminal coding agent from Charm with multi-model switching and LSP integration. Platforms: CLI. Pricing: Free and open source; model usage billed by consumption. `[CLI]` `[Free]` `[Open Source]`
```

## Category Placement

An entry belongs in the single category that best matches its **primary mode of use**. Do not list the same tool in multiple places:

| Category | Applies to |
| :--- | :--- |
| Official Agent Tools | Published and maintained by a model or platform vendor |
| Third-Party Agent Tools | General-purpose agents from communities or independent teams |
| IDE Integrations and Extensions | Primarily editor extensions or graphical interfaces |
| Agent Frameworks and SDKs | For developers building agents in code |
| Multi-Agent Orchestration | Coordinating multiple agents or visually orchestrating pipelines |
| Tools and Utilities | Context, usage observability, tool access, and supporting capabilities |

Within a category, entries are ordered alphabetically by name.

## Pre-Submission Checklist

Before opening a pull request, confirm each item:

- [ ] I opened the newly added link in a browser and confirmed it loads and matches the description.
- [ ] The link points to an official source, and GitHub links end with `#readme`.
- [ ] The description is objective, free of marketing terms such as "best", and ends with a period.
- [ ] Platform support and pricing information is accurate and consistent with official documentation.
- [ ] The entry is filed under the single most appropriate category, maintaining alphabetical order.
- [ ] I rendered the README locally and confirmed the new entry is well-formed and the tables are not misaligned.
- [ ] The tool is not already present in the list, introducing no duplicate entry.
- [ ] If I changed a section heading, I updated the table of contents links at the top of the README.
- [ ] I updated both [README.md](README.md) and [README.en.md](README.en.md) so the entries and links stay in sync.

## Submission Process

1. Search existing issues and pull requests first to avoid duplicates.
2. Fork this repository and make your changes on a new branch.
3. Open a pull request describing what you added or changed and why.
4. If an entry is disputed, maintainers may ask for official sources or evidence of use.

## Maintenance Cycle

Maintainers periodically check link validity and project maintenance status:

- Entries whose links are broken with no official replacement available will be removed.
- Projects with no updates for a long period that are officially marked as deprecated will be annotated in the description or removed from the list.

## Languages

This repository maintains the list in two languages, and their content must stay consistent:

| File | Language |
| :--- | :--- |
| [README.md](README.md) | Simplified Chinese (default) |
| [README.en.md](README.en.md) | English |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Simplified Chinese (default) |
| [CONTRIBUTING.en.md](CONTRIBUTING.en.md) | English |

When adding or changing an entry, **please update both README files**, keeping the entry name, link, platform, and pricing information identical and translating only the description text. CI checks link validity across both files.

Issues and pull requests are welcome in either English or Chinese.

## Code of Conduct

Please stay friendly and professional. Discussion should focus on the facts about the tools and their use cases, avoiding attacks on individuals, teams, or products.

## License

By contributing to this repository, you agree that your contribution is released under the [MIT](LICENSE) license.
