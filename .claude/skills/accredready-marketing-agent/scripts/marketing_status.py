#!/usr/bin/env python3
"""Marketing status snapshot for the AccredReady marketing agent.

Reads the tracker CSVs and the LinkedIn content queue, prints a JSON summary:
prospect/consultant pipelines by stage, overdue follow-ups, content backlog
counts, and LinkedIn queue depth. Stdlib only.

Usage:
    python3 marketing_status.py [--repo-root PATH]
"""

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent


def read_rows(csv_path: Path) -> list[dict]:
    if not csv_path.exists():
        return []
    with open(csv_path, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if not r.get("id", "").startswith("EXAMPLE")]


def pipeline_summary(rows: list[dict], today: date) -> dict:
    stages = Counter(r.get("stage", "unknown") or "unknown" for r in rows)
    overdue = []
    for r in rows:
        d = (r.get("next_action_date") or "").strip()
        if not d:
            continue
        try:
            due = date.fromisoformat(d)
        except ValueError:
            continue
        if due <= today and r.get("stage") not in ("won", "lost", "dormant", "active", "declined"):
            overdue.append({
                "id": r.get("id"),
                "name": r.get("name"),
                "stage": r.get("stage"),
                "next_action": r.get("next_action"),
                "due": d,
            })
    return {"total": len(rows), "by_stage": dict(stages), "followups_due": overdue}


def content_summary(rows: list[dict]) -> dict:
    statuses = Counter(r.get("status", "unknown") or "unknown" for r in rows)
    next_up = sorted(
        (r for r in rows if r.get("status") == "planned"),
        key=lambda r: int(r.get("priority") or 99),
    )
    return {
        "total": len(rows),
        "by_status": dict(statuses),
        "next_up": [
            {"id": r["id"], "slug": r.get("slug"), "title": r.get("working_title")}
            for r in next_up[:3]
        ],
    }


def linkedin_queue_depth(repo_root: Path) -> dict:
    queue_path = repo_root / "marketing" / "linkedin" / "content-queue.json"
    if not queue_path.exists():
        return {"queue_file": str(queue_path), "found": False}
    try:
        data = json.loads(queue_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return {"queue_file": str(queue_path), "found": True, "error": f"invalid JSON: {e}"}
    posts = data.get("posts", [])
    return {"found": True, "post_count": len(posts), "needs_refill": len(posts) < 14}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=SKILL_DIR.parent.parent.parent,
        help="Repository root (defaults to three levels above the skill directory)",
    )
    args = parser.parse_args()
    today = date.today()

    data_dir = SKILL_DIR / "data"
    status = {
        "date": today.isoformat(),
        "prospects": pipeline_summary(read_rows(data_dir / "prospects.csv"), today),
        "consultants": pipeline_summary(read_rows(data_dir / "consultants.csv"), today),
        "content_backlog": content_summary(read_rows(data_dir / "content-backlog.csv")),
        "linkedin": linkedin_queue_depth(args.repo_root),
    }
    json.dump(status, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
