# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/clay390/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/clay390/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world's news of **Wednesday 18 November 2026**,
built for make.fun's news-image-20261118 bounty ($250, 50 places paid).

## The image

A one-day newspaper front page, drawn programmatically with Python/PIL
(`draw.py`, DejaVu fonts — no copyrighted photos, no AI-generated art):

- **Masthead:** "THE WORLD IN ONE DAY — Wednesday 18 November 2026"
- **Lead story:** Xi and Putin meet in Shenzhen on the eve of the
  first-ever Trump trilateral summit
- **Four illustrated panels:** the Shenzhen summit, the Gulf on edge
  (Iran fires on Kuwait & Bahrain), the Kerch Bridge hit, and the US
  Senate flipping 56–44
- **46 sourced stories across 7 regions**, each with a region colour
  and a source tag (AFP, Reuters, AP, Al Jazeera, WHO, FIFA, NATO, IMD…)
- **UTC timeline** of the day as reported, and a footer stating every
  story was reported on 18 November 2026

The image is 1024 × 1024 PNG, 137,466 bytes — small on purpose: among
tied entries the smaller file places first.

## The program

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png`. It runs with no network and writes the same bytes
on every run. `draw.py` is the build-time drawing script, kept in the
repository so the image can be reproduced and revised.
