"""
refresh_metrics.py
------------------
Pulls live data from the GitHub API for a chosen set of repos and rewrites the
block between <!--METRICS:START--> and <!--METRICS:END--> in README.md.

Runs on a schedule via .github/workflows/refresh.yml. No secrets needed beyond
the GITHUB_TOKEN that Actions injects automatically.
"""

import os
import re
import sys
import json
import urllib.request
from datetime import datetime, timezone

USER = "sidharthjatt"

# repo -> the one line you want shown next to it
TRACKED = {
    "honest-mistake":      "multi-layer ML audit agent",
    "predictive-engine-s1": "quant backtest thesis (strategy 1)",
    "regret-zero":         "decision-regret inventory optimizer",
}

TOKEN = os.environ.get("GITHUB_TOKEN", "")
README = "README.md"
START, END = "<!--METRICS:START-->", "<!--METRICS:END-->"


def api(path):
    """One GET against the GitHub REST API. Returns parsed JSON or None."""
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": USER,
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except Exception as e:                      # noqa: BLE001
        print(f"[warn] {path} -> {e}", file=sys.stderr)
        return None


def human_delta(iso_ts):
    """'2026-08-27T07:21:39Z' -> '3 hours ago'."""
    then = datetime.strptime(iso_ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    secs = (datetime.now(timezone.utc) - then).total_seconds()
    for limit, div, name in ((3600, 60, "min"), (86400, 3600, "hour"), (2592000, 86400, "day")):
        if secs < limit:
            n = int(secs // div)
            return f"{n} {name}{'s' if n != 1 else ''} ago"
    months = int(secs // 2592000)
    return f"{months} month{'s' if months != 1 else ''} ago"


SUBJECT_LIMIT = 58


def shorten(subject, limit=SUBJECT_LIMIT):
    """Trim to the last whole word inside `limit` and mark it with an ellipsis."""
    if len(subject) <= limit:
        return subject
    cut = subject[:limit].rstrip()
    if " " in cut:
        cut = cut[: cut.rindex(" ")].rstrip()
    return f"{cut}\u2026"


def build_rows():
    rows = []
    for repo, blurb in TRACKED.items():
        meta = api(f"/repos/{USER}/{repo}")
        commits = api(f"/repos/{USER}/{repo}/commits?per_page=1")
        if not meta:
            continue
        last = "—"
        msg = "—"
        if commits:
            last = human_delta(commits[0]["commit"]["committer"]["date"])
            msg = shorten(commits[0]["commit"]["message"].splitlines()[0])
        rows.append(
            f"| [`{repo}`](https://github.com/{USER}/{repo}) | {blurb} | "
            f"⭐ {meta.get('stargazers_count', 0)} | {last} | `{msg}` |"
        )
    return rows


def main():
    rows = build_rows()
    if not rows:
        print("[warn] no rows built; leaving README untouched")
        return

    stamp = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")
    block = "\n".join(
        [
            START,
            "",
            "| Repo | What it is | Stars | Last push | Latest commit |",
            "|---|---|---|---|---|",
            *rows,
            "",
            f"<sub>Auto-refreshed by a GitHub Action · last run {stamp}</sub>",
            "",
            END,
        ]
    )

    with open(README, encoding="utf-8") as f:
        text = f.read()

    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        block.replace("\\", "\\\\"),
        text,
        flags=re.DOTALL,
    )

    if new == text:
        print("no change")
        return

    with open(README, "w", encoding="utf-8") as f:
        f.write(new)
    print("README updated")


if __name__ == "__main__":
    main()
