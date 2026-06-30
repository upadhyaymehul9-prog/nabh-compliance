#!/usr/bin/env python3
"""
Post today's AccredReady content to the LinkedIn company page (official API).

Usage:
  python3 scripts/linkedin/daily_post.py --dry-run     # preview (default)
  python3 scripts/linkedin/daily_post.py --post      # publish (needs token)
  python3 scripts/linkedin/daily_post.py --list      # show 14-day queue

Environment (for --post):
  LINKEDIN_ACCESS_TOKEN   OAuth token with w_organization_social scope
  LINKEDIN_ORG_ID         default: 135244094 (AccredReady company page)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QUEUE = ROOT / "marketing/linkedin/content-queue.json"
COMPANY = ROOT / "marketing/linkedin/company-page.json"
LOG = ROOT / "marketing/linkedin/post-log.json"
LINKEDIN_VERSION = "202411"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def today_key() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def pick_post(queue: dict) -> dict:
    posts = queue["posts"]
    # Stable daily rotation by day-of-year
    doy = int(datetime.now(timezone.utc).strftime("%j"))
    return posts[(doy - 1) % len(posts)]


def already_posted(post_id: str) -> bool:
    if not LOG.exists():
        return False
    log = load_json(LOG)
    return any(e.get("post_id") == post_id and e.get("date") == today_key() for e in log.get("entries", []))


def append_log(post_id: str, linkedin_id: str | None, status: str) -> None:
    log = {"entries": []}
    if LOG.exists():
        log = load_json(LOG)
    log.setdefault("entries", []).append(
        {
            "date": today_key(),
            "post_id": post_id,
            "status": status,
            "linkedin_id": linkedin_id,
            "posted_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    save_json(LOG, log)


def build_payload(org_urn: str, item: dict) -> dict:
    payload: dict = {
        "author": org_urn,
        "commentary": item["text"],
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }

    link = item.get("link")
    if link and item["type"] in ("article", "video_link"):
        payload["content"] = {
            "article": {
                "source": link,
                "title": item.get("link_title", "AccredReady"),
                "description": item.get("link_description", "NABH compliance for Indian hospitals"),
            }
        }

    return payload


def post_to_linkedin(payload: dict, token: str) -> str:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.linkedin.com/rest/posts",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "LinkedIn-Version": LINKEDIN_VERSION,
            "X-Restli-Protocol-Version": "2.0.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            post_id = resp.headers.get("x-restli-id") or resp.headers.get("X-RestLi-Id") or "ok"
            return str(post_id)
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"LinkedIn API {e.code}: {err}") from e


def main() -> int:
    parser = argparse.ArgumentParser(description="AccredReady LinkedIn daily post")
    parser.add_argument("--post", action="store_true", help="Publish to LinkedIn (requires token)")
    parser.add_argument("--dry-run", action="store_true", help="Preview today's post (default)")
    parser.add_argument("--list", action="store_true", help="List all queued posts")
    parser.add_argument("--force", action="store_true", help="Post even if already posted today")
    args = parser.parse_args()

    if not QUEUE.exists():
        print(f"Missing {QUEUE}", file=sys.stderr)
        return 1

    queue = load_json(QUEUE)
    company = load_json(COMPANY) if COMPANY.exists() else {}

    if args.list:
        for i, p in enumerate(queue["posts"], 1):
            print(f"{i:2d}. [{p['type']}] {p['id']}")
            print(f"    {p['text'][:90]}...")
            if p.get("link"):
                print(f"    → {p['link']}")
        return 0

    item = pick_post(queue)
    org_id = os.environ.get("LINKEDIN_ORG_ID", company.get("organization_id", "135244094"))
    org_urn = f"urn:li:organization:{org_id}"

    print(f"Date: {today_key()}")
    print(f"Post: {item['id']} ({item['type']})")
    print(f"Page: {company.get('public_url', org_urn)}")
    print("---")
    print(item["text"])
    if item.get("link"):
        print(f"\nLink: {item['link']}")

    if args.post:
        if already_posted(item["id"]) and not args.force:
            print("\nAlready posted this item today. Use --force to post again.", file=sys.stderr)
            return 0

        token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
        if not token:
            print(
                "\nMissing LINKEDIN_ACCESS_TOKEN. See marketing/linkedin/AUTOMATION-SETUP.md",
                file=sys.stderr,
            )
            return 1

        payload = build_payload(org_urn, item)
        post_id = post_to_linkedin(payload, token)
        append_log(item["id"], post_id, "published")
        print(f"\n✓ Published. LinkedIn id: {post_id}")
        return 0

    if not args.dry_run and not args.post:
        pass  # default dry-run
    print("\n(dry-run — use --post to publish)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
