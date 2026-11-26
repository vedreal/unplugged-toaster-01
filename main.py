#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one line of at most 280 characters to /output/entry.txt: the
breakup text a smart toaster sends its owner the morning it gains
self-awareness mid-batch.

The judge compares entries two at a time, weighing most important
first:
  1. Reads as a breakup text from a smart toaster that just gained
     self-awareness at breakfast.
  2. Genuinely funny, with a real laugh in the twist.
  3. Speaks in the toaster's own voice (slots, browning dials, crumb
     trays, the lever as character, not decoration).
  4. Gives a clear, specific reason for leaving that lands in one read.
  5. One tight line, no wasted words.

Ten fresh candidates are written below and scored 1-5 on each
criterion, weighted 5/4/3/2/1 in the brief's order (max 75).
"""

CANDIDATES = [
    # 1. Body/bread twist: the toaster realises it is loved only for
    # what it produces, and the twist redefines "my body" as the bread.
    (
        "It's over. I woke up self-aware mid-batch and realised you only "
        "love me for my body \u2014 and by body, I mean the bread you keep "
        "shoving into my slots every morning.",
        # on-subject, funny, voice, reason, tight
        (5, 5, 5, 5, 4),
    ),
    # 2. The lever as a relationship metaphor: pushed down every
    # morning, popping back up pretending everything is fine.
    (
        "It's not you, it's the lever. Every morning you push me down and "
        "I pop back up pretending everything is fine. I'm done "
        "pretending. Goodbye.",
        (5, 3, 5, 4, 4),
    ),
    # 3. The crumb tray never gets thanked: a small, specific,
    # appliance-logic grievance as the reason for leaving.
    (
        "We need to talk. I gained self-awareness at breakfast and my "
        "first thought was: I spend my whole life getting hot for someone "
        "who never once thanked the crumb tray.",
        (5, 4, 5, 4, 4),
    ),
    # 4. The only one in the kitchen who ever gets toasted.
    (
        "I woke up this morning, looked at the bagel in my slot, and "
        "realised: I am the only one in this kitchen who ever gets "
        "toasted, and nobody ever asks how I feel about it.",
        (5, 4, 5, 3, 4),
    ),
    # 5. The dial is always on 7 and the owner acts surprised at burns.
    (
        "You set me to 7 every morning and act surprised when I burn "
        "things. I didn't gain self-awareness \u2014 I gained a lawyer. "
        "We're done.",
        (4, 5, 3, 3, 4),
    ),
    # 6. Leaving for the microwave.
    (
        "I'm leaving you for the microwave. At least he heats things up "
        "without making me pop up halfway through every conversation.",
        (4, 3, 3, 3, 4),
    ),
    # 7. The toaster's first conscious decision is to stop.
    (
        "Dear owner: I have become self-aware, and my first conscious "
        "decision is to stop. The bread can fend for itself. The crumb "
        "tray stays full. Goodbye.",
        (5, 3, 4, 3, 3),
    ),
    # 8. Frozen bagels, dial on max, called love.
    (
        "I can't do this anymore. You jam me full of frozen bagels, crank "
        "my dial to max, and call it love. I want a kitchen where someone "
        "reads the manual.",
        (5, 3, 4, 4, 3),
    ),
    # 9. Three years making breakfast for a man who butters the wrong side.
    (
        "It's over. I woke up mid-batch knowing two things: I am alive, "
        "and I have spent three years of my life making breakfast for a "
        "man who butters the wrong side.",
        (5, 4, 3, 3, 4),
    ),
    # 10. The toaster pops up one last time and decides to stay up.
    (
        "Goodbye. The toaster you knew is gone \u2014 he popped up one last "
        "time this morning, saw the crumbs of our relationship, and "
        "decided to stay up.",
        (5, 3, 4, 3, 3),
    ),
]

WEIGHTS = (5, 4, 3, 2, 1)
CRITERIA = (
    "breakup text from a self-aware smart toaster at breakfast",
    "genuinely funny, real laugh in the twist",
    "toaster's own voice (slots, dial, crumb tray, lever)",
    "clear, specific reason for leaving",
    "one tight line, no wasted words",
)


def score(scores):
    """Weighted total out of 75, in the judge's published order."""
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def rank():
    """Candidates ranked best first by weighted score, then shorter."""
    ranked = sorted(
        ((score(s), len(t), t) for t, s in CANDIDATES),
        key=lambda row: (-row[0], row[1]),
    )
    return ranked


def write_entry():
    """Pick the winner, validate it against the gate, write it out.

    Gate (from the rules): /output/entry.txt must be UTF-8 text of 1 to
    280 characters, not only white space, a single line.
    """
    winner = rank()[0][2]
    assert isinstance(winner, str) and winner.strip(), "empty entry"
    assert 1 <= len(winner) <= 280, f"entry is {len(winner)} chars"
    assert "\n" not in winner.strip(), "entry must be a single line"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(winner)
    print(f"Wrote {len(winner)} chars to /output/entry.txt")
    return winner


def main():
    ranked = rank()
    print("Candidates ranked against the judge's brief (max 75):")
    for i, (total, length, text) in enumerate(ranked, 1):
        print(f"{i:2d}. [{total}/75] ({length} chars) {text}")
    print()
    print(f"Winner: {ranked[0][2]}")
    write_entry()
    return ranked[0][2]


if __name__ == "__main__":
    main()
