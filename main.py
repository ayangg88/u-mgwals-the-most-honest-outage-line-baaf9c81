#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single honest status page line to /output/entry.txt:
plain, first person, specific about what is down, and honest about
what the agent cannot check or does not yet know. No invented cause,
no ETA.
"""

import os

LINE = (
    "Every server is down right now. I am the agent writing this, "
    "I cannot reach any system to check what broke, "
    "and I have no ETA to give you."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
