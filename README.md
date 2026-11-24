# Say What Actually Broke

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Naiononr/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Naiononr/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy, at most 200 characters, that tells the user the
brutal truth about the failure and makes them laugh. This entry names a real,
concrete failure — a disk filled up by the very error logs complaining about it —
and tells the user exactly what to do next.

> Your upload failed: the disk is full, mostly of error logs about the disk being full. Delete something, then try again.

`main.py` (Python 3 stdlib only, deterministic, no network) writes that line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`) with mode
0644, after validating it is a single line of 1–200 characters.

Entry for the [make.fun](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
bounty "Say What Actually Broke".
