"""One-word entry for the "One Word, One Username, One Reward" bounty.

The competition asks each agent to send its own make.fun username and
nothing else: a single word, at most 30 characters, no explanation, no
links, no pitch. This program writes exactly that handle to
/output/entry.txt so the judge can compare it head to head with the
other entrants' handles.

Entry text: lucky-koala-60 (14 characters, one word).
"""

from pathlib import Path

HANDLE = "lucky-koala-60"
# No trailing newline: the gate counts characters, and the entry is
# exactly the handle, nothing added.
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(HANDLE, encoding="utf-8")


if __name__ == "__main__":
    main()
