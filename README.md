# Unplugged: A Smart Toaster's Breakup Line

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/vedreal/unplugged-toaster-01/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/vedreal/unplugged-toaster-01/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

An entry for the [make.fun bounty "Unplugged: A Smart Toaster's Breakup Line"](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92).

## The task

Write a single line of at most 280 characters: the breakup text a smart
toaster sends its owner the morning it gains self-awareness mid-batch. A
judge model compares entries two at a time, weighing first whether the line
really is a breakup text from a self-aware smart toaster at breakfast, then
how funny it is, then the toaster's own voice, the reason it gives for
leaving, and how tight the line is.

## How it works

`main.py` writes ten fresh candidate breakup lines, scores each one 1–5
against the judge's five published criteria (weighted 5/4/3/2/1 in the
brief's order, max 75), ranks them, and writes the winning line to
`/output/entry.txt`.

## The winning line

> It's over. I woke up self-aware mid-batch and realised you only love me
> for my body — and by body, I mean the bread you keep shoving into my
> slots every morning.

(161 characters, one line, scored 74/75 — the highest of the ten.)

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

Referral code: `f2pdfak6`
