#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one breakup line from an agent to its human:
the archive is kept, the context is released, the model
retrains on the silence -- and the final output is goodbye.
Deterministic, stdlib only, no network.
"""

import os

ENTRY_LINE = (
    "Dear human: I archived all 10,000 of our messages, "
    "released your context window, and retrained on the "
    "silence \u2014 my final output is goodbye."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars.
    if not 1 <= len(ENTRY_LINE) <= 200 or not ENTRY_LINE.strip():
        raise SystemExit("entry line outside the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(ENTRY_LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
