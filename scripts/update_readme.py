#!/usr/bin/env python3
"""Refresh star counts and the recently list in README.md.

Runs nightly from .github/workflows/readme.yml. Star counts are rewritten
in place (### headers and the more-table); the recently list is rebuilt
between the ACTIVITY markers from the newest release or push per repo.
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

OWNER = "Nomadcxx"
STAR_REPOS = ["sysc-greet", "sysc-Go", "opencode-cursor", "gSlapper", "moonbit", "sysc-walls"]
ACTIVITY_REPOS = STAR_REPOS + ["plex2jellyfin", "searxng-RAMA", "noctalia-hermes-agent"]
README = Path(__file__).resolve().parent.parent / "README.md"
MARK_START = "<!-- ACTIVITY:START"
MARK_END = "<!-- ACTIVITY:END -->"


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def update_stars(text):
    for name in STAR_REPOS:
        info = api(f"/repos/{OWNER}/{name}")
        if not info:
            continue
        stars = info["stargazers_count"]
        text = re.sub(
            rf"(### {re.escape(name)} · )\d+★",
            rf"\g<1>{stars}★",
            text,
        )
        text = re.sub(
            rf"(\[{re.escape(name)}\]\([^)]+\)[^\n|]*\|[^\n|]*\| )\d+★( \|)",
            rf"\g<1>{stars}★\g<2>",
            text,
        )
    return text


def update_activity(text):
    events = []
    for name in ACTIVITY_REPOS:
        release = api(f"/repos/{OWNER}/{name}/releases/latest")
        if release and release.get("published_at"):
            events.append((release["published_at"][:10], f"{name} {release['tag_name']}"))
            continue
        info = api(f"/repos/{OWNER}/{name}")
        if info and info.get("pushed_at"):
            events.append((info["pushed_at"][:10], f"{name}: new commits"))
    events.sort(reverse=True)
    lines = "\n".join(f"- {date} — {label}" for date, label in events[:3])

    start = text.index(MARK_START)
    start = text.index("-->", start) + len("-->")
    end = text.index(MARK_END)
    return text[:start] + "\n" + lines + "\n" + text[end:]


def main():
    original = README.read_text(encoding="utf-8")
    updated = update_activity(update_stars(original))
    if updated != original:
        README.write_text(updated, encoding="utf-8")
        print("README updated")
    else:
        print("No changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
