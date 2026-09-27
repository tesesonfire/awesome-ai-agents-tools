#!/usr/bin/env python3
"""Regenerate the Featured Tools table in README.md and README.en.md.

Run from the repository root:  python3 data/build_featured_table.py

The Released column encodes release age with a green badge whose shade darkens
over time. Values are computed from the GitHub releases API, except Grok Build,
which publishes no GitHub releases (see GROK_* below).
"""

import datetime
import re
import urllib.parse

# Reference "now" used for the relative-age labels. Update when regenerating.
NOW = datetime.datetime(2026, 9, 27, 4, 44, tzinfo=datetime.timezone.utc)

BLUE = "2563eb"      # every version badge
TIER_HOT = "4ade80"  # released within 24h
TIER_WEEK = "22c55e" # 2-7 days
TIER_MONTH = "16a34a"# 8-30 days
TIER_OLD = "14532d"  # >30 days

# Grok Build has no GitHub releases; version/date come from the vendor changelog.
GROK_CHANGELOG = "https://x.ai/build/changelog"
GROK_VERSION = "v1.0.40"
GROK_PUBLISHED = "2026-09-20T23:48:33Z"  # v1.0.40 publish time, from the npm registry
                                        # (@xai-official/grok); x.ai itself is unreachable here

# repo, en name, zh name, vendor en, vendor zh, form en, form zh,
# pricing en, pricing zh, published_at (None = unknown), prerelease
TOOLS = [
    ("openclaw/openclaw", "OpenClaw", "OpenClaw", "Community", "社区",
     "CLI / IM", "CLI / IM", "Open source", "开源", "2026-09-23T23:21:10Z", False),
    ("NousResearch/hermes-agent", "Hermes", "Hermes", "Nous Research", "Nous Research",
     "CLI", "CLI", "Open source", "开源", "2026-09-24T10:09:38Z", False),
    ("deepseek-ai/deepseek-harness", "DeepSeek", "DeepSeek", "DeepSeek", "DeepSeek",
     "CLI / Web", "CLI / Web", "Open source", "开源", "2026-09-24T14:10:21Z", True),
    ("anomalyco/opencode", "OpenCode", "OpenCode", "Anomaly", "Anomaly",
     "CLI / Web", "CLI / Web", "Open source", "开源", "2026-09-21T22:51:20Z", False),
    ("anthropics/claude-code", "Claude Code", "Claude Code", "Anthropic", "Anthropic",
     "CLI / IDE", "CLI / IDE", "Commercial / Subscription", "商业 / 订阅",
     "2026-09-25T21:50:12Z", False),
    ("openai/codex", "Codex", "Codex", "OpenAI", "OpenAI",
     "CLI / IDE", "CLI / IDE", "Open-source CLI + Subscription", "开源CLI + 订阅",
     "2026-09-26T01:02:31Z", False),
    ("earendil-works/pi", "Pi", "Pi", "Earendil Works", "Earendil Works",
     "CLI", "CLI", "Open source", "开源", "2026-09-22T19:43:43Z", False),
    ("google-gemini/gemini-cli", "Gemini CLI", "Gemini CLI", "Google", "Google",
     "CLI", "CLI", "Free tier + Open source", "免费额度 + 开源", "2026-09-23T23:59:15Z", False),
    ("can1357/oh-my-pi", "Oh My Pi", "Oh My Pi", "Community", "社区",
     "CLI", "CLI", "Open source", "开源", "2026-09-27T02:48:57Z", False),
    ("xai-org/grok-build", "Grok Build", "Grok Build", "xAI", "xAI",
     "CLI", "CLI", "Open source", "开源", None, False),
    ("microsoft/vscode-copilot-chat", "GitHub Copilot", "GitHub Copilot", "GitHub", "GitHub",
     "IDE / CLI", "IDE / CLI", "Free tier + Subscription", "免费额度 + 订阅",
     "2026-04-07T11:32:46Z", False),
]


def badge(text, color):
    return f"![{text}](https://img.shields.io/static/v1?label=&message={urllib.parse.quote(text)}&color={color})"


def age_label(iso, zh):
    """Return (label, colour) describing how long ago the release was."""
    if iso is None:
        return None, None
    dt = datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    hours = (NOW - dt).total_seconds() / 3600
    if hours < 24:
        return ("24h内" if zh else "within 24h"), TIER_HOT
    if hours <= 30 * 24:
        days = max(1, int(hours // 24))
        return (f"{days}天前" if zh else f"{days} days ago"), (TIER_WEEK if days <= 7 else TIER_MONTH)
    return dt.strftime("%m-%d"), TIER_OLD


def version_cell(repo, iso, prerelease, fallback=None, fallback_href=None):
    """Version badge. Projects without GitHub releases get a static badge in the
    same blue so the column stays visually consistent."""
    if iso is None:
        if fallback:
            b = badge(fallback, BLUE)
            return f"[{b}]({fallback_href})" if fallback_href else b
        return "\u2014"
    q = f"?label=&color={BLUE}" + ("&include_prereleases" if prerelease else "")
    return f"![Version](https://img.shields.io/github/v/release/{repo}{q})"


def build(lang):
    zh = lang == "zh"
    rows = []
    for repo, en, z, ven, vzh, fen, fzh, pen, pzh, iso, pre in TOOLS:
        name = z if zh else en
        vendor = vzh if zh else ven
        form = fzh if zh else fen
        price = pzh if zh else pen
        if iso is None:  # Grok Build: no GitHub releases, date from elsewhere
            ver = version_cell(repo, None, False, GROK_VERSION, GROK_CHANGELOG)
            release_href = GROK_CHANGELOG
            label, colour = age_label(GROK_PUBLISHED, zh)
        else:
            ver = version_cell(repo, iso, pre)
            release_href = f"https://github.com/{repo}/releases"
            label, colour = age_label(iso, zh)
        date = badge(label, colour) if label else "\u2014"
        rows.append(f"| **{name}** | {ver} | {date} | {vendor} | {form} | {price} | "
                    f"[{'发布页' if zh else 'Releases'}]({release_href}) |")
    # Short headers: GitHub sizes columns by content, and 4-character headers
    # were still being wrapped in the narrower columns.
    header = ("| 工具 | 版本 | 最近 | 出品方 | 形态 | 价格 | 链接 |" if zh
              else "| Tool | Version | Released | Vendor | Form | Pricing | Releases |")
    sep = "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
    return "\n".join([header, sep] + rows)


def replace_table(path, first_cell, block):
    lines = open(path, encoding="utf-8").read().split("\n")
    i = next(k for k, l in enumerate(lines) if l.startswith(f"| {first_cell} |"))
    j = i
    while j < len(lines) and lines[j].startswith("|"):
        j += 1
    lines[i:j] = block.split("\n")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return j - i


if __name__ == "__main__":
    print("README.md      lines replaced:", replace_table("README.md", "工具", build("zh")))
    print("README.en.md   lines replaced:", replace_table("README.en.md", "Tool", build("en")))
