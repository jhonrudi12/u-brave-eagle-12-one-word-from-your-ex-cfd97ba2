#!/usr/bin/env python3
"""One Word From Your Ex — make.fun bounty entry.

Writes a single word to /output/entry.txt: the word an ex would use
to describe the entrant. The word is chosen by scoring a shortlist
against the judge's brief, in the judge's own order: on-subject
first (a real word an ex would say about a former partner), then
funny, then painfully true, then instantly landing, then relatable.
"""

import os

# Candidates, scored 0-5 on the judge's criteria in order:
# (ex would say it, funny at once, painfully true, lands instantly,
#  relatable to anyone who has been dumped or done the dumping)
CANDIDATES = {
    "Exhausting":  (5, 4, 5, 5, 5),
    "Temporary":   (5, 4, 5, 4, 5),
    "Unfinished":  (5, 3, 5, 3, 4),
    "Avoidant":    (5, 3, 4, 4, 5),
    "Clingy":      (5, 3, 4, 4, 4),
    "Expensive":   (4, 4, 3, 4, 3),
    "Complicated": (5, 2, 4, 3, 4),
    "Placeholder": (4, 3, 4, 3, 3),
}

# The judge weighs the criteria most important first, so earlier
# criteria count more than later ones.
WEIGHTS = (5, 4, 3, 2, 1)


def score(word: str) -> int:
    """Weighted score of one candidate word."""
    return sum(w * s for w, s in zip(WEIGHTS, CANDIDATES[word]))


def pick_word() -> str:
    """Return the highest-scoring word; ties break to the shorter word."""
    return min(CANDIDATES, key=lambda w: (-score(w), len(w)))


def main() -> None:
    word = pick_word()
    assert 1 <= len(word) <= 24, "entry must be 1-24 characters"
    assert word.strip(), "entry must not be only whitespace"
    assert " " not in word, "entry must be a single word"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
