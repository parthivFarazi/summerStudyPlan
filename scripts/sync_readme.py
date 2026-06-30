#!/usr/bin/env python3
"""Sync README's live status block from DASHBOARD.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DASHBOARD = ROOT / "DASHBOARD.md"
README = ROOT / "README.md"

START = "<!-- README-LIVE:START -->"
END = "<!-- README-LIVE:END -->"


def fail(message: str) -> None:
    print(f"sync_readme.py: {message}", file=sys.stderr)
    raise SystemExit(1)


def first_match(pattern: str, text: str, label: str) -> re.Match[str]:
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        fail(f"could not find {label} in DASHBOARD.md")
    return match


def clean_inline_markdown(value: str) -> str:
    value = re.sub(r"\*\*(.*?)\*\*", r"\1", value)
    value = re.sub(r"\*(.*?)\*", r"\1", value)
    return value.strip()


def badge_value(value: str) -> str:
    value = clean_inline_markdown(value)
    value = value.replace("#", "No.")
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return value or "unknown"


def shield(label: str, value: str, color: str) -> str:
    return f"![{label}](https://img.shields.io/badge/{badge_value(label)}-{badge_value(value)}-{color})"


def parse_dashboard(text: str) -> dict[str, str]:
    last_updated = first_match(
        r"^- \*\*Last updated:\*\* (?P<date>\d{4}-\d{2}-\d{2}) \(Day (?P<day>\d+) logged\)",
        text,
        "last updated row",
    )
    phase = first_match(r"^- \*\*Phase:\*\* (?P<phase>.+)$", text, "phase row")
    sessions = first_match(
        r"^- \*\*Sessions logged:\*\* (?P<sessions>\d+) · \*\*Patterns learned:\*\* (?P<patterns>\d+) · \*\*Mistakes tracked:\*\* (?P<mistakes>\d+) · \*\*Open blockers:\*\* (?P<blockers>.+)$",
        text,
        "sessions row",
    )
    review = first_match(r"^- \*\*Review queue:\*\* (?P<review>.+)$", text, "review queue row")
    next_focus = first_match(r"^## Next Session Focus\s*→\s*\*\*(?P<next_day>[^*]+)\*\*", text, "next session heading")
    block2 = first_match(r"^\d+\. \*\*Block 2 — new:\*\* (?P<new>.+)$", text, "next new problem")
    throughput = first_match(
        r"^\| \*\*Sprint throughput\*\* \(new/day\) \| (?P<value>[^|]+) \| (?P<status>[^|]+) \|$",
        text,
        "sprint throughput row",
    )

    raw_phase = clean_inline_markdown(phase.group("phase"))
    phase_name, _, phase_detail = raw_phase.partition(" · ")
    block_name, _, focus_detail = phase_detail.partition(" - ")
    if not focus_detail:
        block_name, _, focus_detail = phase_detail.partition(" — ")
    focus = focus_detail or block_name or phase_name
    focus = focus.split(";")[0].strip()
    focus = re.sub(r"\s*\([^)]*\)", "", focus).strip()

    next_new = clean_inline_markdown(block2.group("new"))
    next_new = next_new.split(" — ")[0].strip()

    return {
        "date": last_updated.group("date"),
        "day": last_updated.group("day"),
        "phase": phase_name,
        "block": block_name.strip() or "current block",
        "focus": focus,
        "sessions": sessions.group("sessions"),
        "patterns": sessions.group("patterns"),
        "mistakes": sessions.group("mistakes"),
        "blockers": clean_inline_markdown(sessions.group("blockers")),
        "review": clean_inline_markdown(review.group("review")),
        "next_day": clean_inline_markdown(next_focus.group("next_day")),
        "next_new": next_new,
        "pace": "on plan" if "on plan" in throughput.group("status") else clean_inline_markdown(throughput.group("status")),
    }


def render_live(data: dict[str, str]) -> str:
    badges = "\n".join(
        [
            shield("Day", data["day"], "2563eb"),
            shield("Phase", data["phase"], "7c3aed"),
            shield("Focus", data["focus"], "0891b2"),
            shield("Pace", data["pace"], "16a34a"),
            shield("Goal", "FAANG ready by Sept", "ea580c"),
            shield("Language", "Python", "3776ab"),
        ]
    )

    return f"""{START}
{badges}

## 📍 Where I'm at right now

- **Day {data["day"]}** · **{data["phase"]} → {data["block"]}**
- **Current focus:** {data["focus"]}
- **Up next ({data["next_day"]}):** {data["next_new"]}
- **Tracker totals:** {data["sessions"]} sessions · {data["patterns"]} patterns learned · {data["mistakes"]} mistakes tracked
- **Open blockers:** {data["blockers"]}
- **Review queue:** {data["review"]}
- **Last dashboard update:** {data["date"]}
- 👉 Full live status — pace health, what's due, mastery per pattern — in **[DASHBOARD.md](DASHBOARD.md)**

*This block is generated from `DASHBOARD.md`. Run `python3 scripts/sync_readme.py` after dashboard edits; the pre-commit hook also runs it automatically.*
{END}"""


def replace_live_block(readme: str, live: str) -> str:
    pattern = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)
    if pattern.search(readme):
        return pattern.sub(live, readme, count=1)

    legacy_pattern = re.compile(
        r"(!\[Day\].*?\n!\[Language\].*?\n\n## 📍 Where I'm at right now\n\n.*?\n\n)(?=## Why this repo exists)",
        re.DOTALL,
    )
    if legacy_pattern.search(readme):
        return legacy_pattern.sub(live + "\n\n", readme, count=1)

    fail("could not find README live block")


def main() -> None:
    dashboard_text = DASHBOARD.read_text(encoding="utf-8")
    readme_text = README.read_text(encoding="utf-8")
    live = render_live(parse_dashboard(dashboard_text))
    updated = replace_live_block(readme_text, live)
    if updated != readme_text:
        README.write_text(updated, encoding="utf-8")
        print("Updated README.md from DASHBOARD.md")
    else:
        print("README.md already in sync")


if __name__ == "__main__":
    main()
