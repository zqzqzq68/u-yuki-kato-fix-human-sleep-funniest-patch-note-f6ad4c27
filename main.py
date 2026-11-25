"""Fix Human Sleep: Funniest Patch Note.

A tiny deterministic program: it writes a single line of patch notes
announcing that human sleep has been fixed, to /output/entry.txt,
and prints the same line to stdout.

The line is one changelog-style sentence, under 160 characters,
written to be funny on a single read while still sounding like a
real release note.
"""

import os

PATCH_NOTE = "Fixed a bug where humans woke up at 2% battery after a full night's charge; sleep now charges to 100%."


def main() -> None:
    """Write the patch note to /output/entry.txt and print it."""
    if not 1 <= len(PATCH_NOTE) <= 160:
        raise ValueError("patch note must be 1 to 160 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PATCH_NOTE)
    print(PATCH_NOTE)


if __name__ == "__main__":
    main()
