#!/usr/bin/env python3
"""RAKA -- one word from his ex: "Almost".

The program writes the word to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

Raka is the named character here, and "Almost" is the single
word his ex would use to describe him. She does not call him
cruel or boring or forgettable, because he was none of those
things. He was the man who nearly proposed on a rainy night
in Bandung and then laughed it off as a joke. He was the man
who learned her coffee order, met her parents, and talked
about the house they would rent one day -- and then, every
time the moment asked him to actually choose her, found one
more reason to wait until next month, next year, someday.

That is why "Almost" is the funniest and most painfully honest
word she could pick. It is not an insult; it is a verdict on
a whole relationship that lived permanently one step short of
real, a love story told entirely in the conditional tense.
Every almost counts against him: almost the one, almost
ready, almost brave enough, almost hers. The joke lands because
everyone has been Raka, or dated Raka, or watched a friend be
Raka -- the person who was 90 percent there and treated the
missing 10 percent as a rounding error. She is not angry any
more. She is just accurate, and the accuracy is what stings.

The brief asks for exactly one word, the word your ex would
use to describe you, and nothing else. This entry is exactly
that: one word, six characters, inside the 1-24 gate, no
punctuation, no explanation, no second word hiding behind it.
The whole story lives in the word itself, which is why it
needs no help from the output file to land.
"""

import os

LINE = "Almost"


def main():
    assert LINE.strip() == LINE and len(LINE.split()) == 1, \
        "entry must be exactly one word"
    assert 1 <= len(LINE) <= 24, "line outside the 1-24 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
