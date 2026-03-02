#!/usr/bin/env python3
"""
Set SVG circle icons on Notion area pages based on area name.
Icons are hosted on GitHub: https://github.com/Jack02913/notion-assets
"""

import os
import requests

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
BASE_URL = "https://api.notion.com/v1"
ICON_BASE = "https://raw.githubusercontent.com/Jack02913/notion-assets/main"

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

AREAS = {
    "Totem":            ("3139030c-6d14-8130-8d6e-c4549f61293a", "totem.svg"),
    "BG Building":      ("1fb9030c-6d14-80db-a22e-d7990fcd0eab", "bg-building.svg"),
    "ParityAI":         ("3139030c-6d14-818f-abb1-de25b86e62a8", "parityai.svg"),
    "Ladmin":           ("20c9030c-6d14-80a5-959a-db16caf6e620", "ladmin.svg"),
    "Crown Plastering": ("1fb9030c-6d14-80c2-9dad-d1d656dd1d8f", "crown-plastering.svg"),
    "Personal Systems": ("3179030c-6d14-8184-a809-d272b4d3e035", "personal-systems.svg"),
    "Trading":          ("1fb9030c-6d14-8012-b306-ea9706d610ce", "trading.svg"),
    "Lifestyle":        ("1fb9030c-6d14-8000-9e2f-e4e7bf3f13c1", "lifestyle.svg"),
    "Gym":              ("1fb9030c-6d14-8059-adac-dd7ec133d5f4", "gym.svg"),
}


def set_icon(area_name, page_id, svg_file):
    url = f"{BASE_URL}/pages/{page_id}"
    payload = {
        "icon": {
            "type": "external",
            "external": {"url": f"{ICON_BASE}/{svg_file}"},
        }
    }
    response = requests.patch(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"✓ {area_name}")
    else:
        body = response.text or "(empty response)"
        print(f"✗ {area_name} — {response.status_code}: {body}")


if __name__ == "__main__":
    print("Setting icons on Notion area pages...\n")
    for name, (page_id, svg) in AREAS.items():
        set_icon(name, page_id, svg)
    print("\nDone.")
