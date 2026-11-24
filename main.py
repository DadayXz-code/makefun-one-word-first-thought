#!/usr/bin/env python3
"""One Word, First Thought - make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that came
to mind, picked for surprise, vividness and a spark of wit.

The program is fully deterministic: no randomness, no clock, no network,
no input. It always writes the same single word.
"""

import os

# The word. A snollygoster is a shrewd, unprincipled person - usually a
# politician - who will say or do anything to stay in power. It sounds
# like a playground insult, looks like a typo, and turns out to be a real
# 19th-century American word with a very specific bite. Twelve letters,
# one word, well inside the gate's 1-24 character limit.
WORD = "snollygoster"

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
