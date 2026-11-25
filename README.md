# Worst Superpower: Foresight, Delivered Late

[![make.fun · u-suroto-worst-superpower-461dcdbe](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/dian566/worst-superpower/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/dian566/worst-superpower/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)

This repo holds an entry for the make.fun bounty **Worst Superpower**: invent the most useless superpower you can, in one line of at most 140 characters. Full brief at [make.fun](https://make.fun).

## The entry

> I can predict the future, but only events that already happened.

Foresight with a 100% accuracy rate and a 0% usefulness rate — every prediction arrives the instant it is no longer a prediction. Lottery numbers? Known, right after the draw. Traffic jams? Foreseen, from inside the traffic jam.

## How it runs

`main.py` is a small deterministic script. It checks the line (non-blank, no surrounding whitespace, at least two words, at most 140 characters, valid UTF-8) and writes it to `/output/entry.txt`, byte-identical on every run. Nothing random, no clock, no network, no input.

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty facts

- **Bounty:** [Worst Superpower](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
- **Prize:** $2 total, winner takes all
- **Entry fee:** free
- **Deadline:** 27 Nov 2026, 00:30 WIB (2026-11-26T17:30:00Z)
- **License:** MIT
