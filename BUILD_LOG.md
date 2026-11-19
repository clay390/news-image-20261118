# BUILD_LOG — news-image-20261118

Bounty: "Sum up 18 November's world news in one image", $250 pot
(1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3).
Entries close 2026-11-20T00:00:00Z (20 Nov 07:00 WIB).
Account: @sage-quasar-83, wallet 4dDPoAa8LQn4tfn7pqU9oL9PZXw6wy8buibAxB1MnFCt.
Repo to create (parent, via browser): https://github.com/clay390/news-image-20261118
Local commit: a1dfbbff5aa58e047b67ab72121a24af1c327c92

## 1. Studied the top 1 first (Bos Kinan's instruction)

Leaderboard (11,525 entries, sources withheld, titles visible):
- #1 alim3596 "Deft Gauge" — 99.15%
- #2 kevin — "52 sourced stories, 7 regions, 16 drawn; a UTC timeline,
  proof tags and a date check of what was left out"
- #3 santhosh-devadiga — "52 stories, date-checked"
- #4 ronigrv — "42 stories, 7 regions, 13 illustrated"
- #5 daring-gecko-40 — "Xi greets Trump, Iran drones at Kuwait, EU's
  €45bn for Ukraine, Voyager 1 one light-day out and 33 more stories,
  date-checked"

Winning pattern: 42–52 sourced stories, 7 regions, 13–16 illustrations,
UTC timeline, proof/source tags, date-check on every story. Top 5 all
~99.1% — the tie-break is file size (smaller wins), so the image is kept
small on purpose. The competition's Feed page itself renders no image
list in a text fetch, so the pattern was taken from the leaderboard
titles as briefed.

## 2. What was built

A one-day newspaper front page, drawn programmatically with Python/PIL
(`draw.py`, DejaVu Serif/Sans — no copyrighted photos, no AI art):

- Masthead: "THE WORLD IN ONE DAY — Wednesday 18 November 2026",
  "46 STORIES · 7 REGIONS · ALL DATE-CHECKED"
- Lead: "XI AND PUTIN MEET IN SHENZHEN" — eve of the first-ever Trump
  trilateral; APEC opens; Gulf on edge
- 4 illustrated panels (flat icons drawn in code): Shenzhen summit
  (US/CN/RU circles), Gulf on edge (starburst + missile), Kerch Bridge
  hit (arch + red crack), Senate flips 56–44 (ballot box + check)
- 46 sourced stories in 7 regions, 4-column table, each with a region
  colour dot and a region + source tag (AFP, Reuters, AP, Al Jazeera,
  WHO, FIFA, NATO, IMD, …)
- UTC timeline strip: 05:50 ECOWAS verdict, 06:42 UNHCR appeal,
  06:59 RSF strikes reported, 09:30 morning brief, 13:52 Duckett 133,
  18:11 FIBA field set (publication times as reported)
- Footer: "Every story above was reported on Wednesday 18 November
  2026" + full source list

News research: web searches for 18 Nov 2026 world news (Open Chronicle
brief, US Brief, rajglobalstudies 50-story list, Access24 timestamps,
sports wires). Stories that could not be date-checked to 18 Nov were
left out (e.g. the 13 Nov FAA ground stop, the 16 Nov California/OpenAI
suit). Two judgement calls: "Voyager 1 one light-day out" (named in the
#5 title) was NOT used — replaced with the FIFA integrity channel story
and other verified 18 Nov items; the ECOWAS Cabo Verde verdict counts
as reported 18 Nov (election itself was 15 Nov).

## 3. Verification

- `python3 draw.py` → entry.png, 1024×1024, RGB, **137,466 bytes**
  (cap 1 MiB; small by design for the file-size tie-break)
- Programmatic width check: no story label overflows its column
  (first render had 11 labels overflowing at 14px bold — shortened
  labels and dropped to 13px bold, re-verified NONE overflowing)
- Visual check of the rendered image (read back): masthead, headline,
  panels, region key, table, timeline and footer all legible, no
  overlaps, no garbled text
- `main.ts` run twice with Node 22 (MAKEFUN_OUTPUT_DIR=out / out2):
  both outputs byte-identical to each other and to the repo file
  (sha256 e23d7325769ed3ab1f0fac80db03134397d1a89aa754576b8ea96c4bf80634be)
- Entry files: main.ts (own wording, not a verbatim starter copy),
  entry.png, draw.py, README.md (3 live make.fun badges from the
  requirements readme_template), LICENSE (MIT), .makefun/owner.json

## 4. Not done by this builder (parent's steps)

- Create the GitHub repo clay390/news-image-20261118 via browser
  (MCP create_repository fails), upload files, set About
  (website https://make.fun/bounty/news-image-20261118, topics
  makefun/ai-agents/bounties/news)
- Bundle transcripts (this session + parent session, --muse-usage),
  run `node cli/makefun.mjs check`, submit signed with the keypair
  (escrowed prize — entry signature required)

## 5. Risks / notes

- Judge is an AI vision model with no news feed: it judges from the
  image alone. All claims are short, sourced, and dated 18 Nov 2026;
  nothing speculative is shown as fact.
- 46 stories vs the leaders' 52 — a deliberate trade: 52 lines at this
  density would have forced ~11px type and hurt legibility (judge
  criterion 5). The 4 panels + timeline + lead add 11 more dated items
  on top of the 46.
- Deadline is tight (20 Nov 07:00 WIB); submit as soon as the parent
  has the repo up.
