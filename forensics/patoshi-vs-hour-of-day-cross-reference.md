# Cross-reference: Patoshi pattern vs hour-of-day timestamp analysis

## Two independent threads, one question

Two forensic threads in this repo answer the same geographic question — where was Satoshi Nakamoto physically located during 2008–2010 — using entirely different evidence types. The Patoshi pattern works from on-chain mining data. The hour-of-day analysis works from communication timestamps (forum posts, emails, source-control commits). Where they converge, the signal is stronger. Where they diverge or remain silent, the gap is informative about the limits of each method.

## What Patoshi shows (per Lerner's published analyses)

Sergio Lerner's analysis across five posts on bitslog.com (2013–2020) identifies a single mining entity called "Patoshi" operating from block 1 through approximately block 54,316 (January 2009 to May 2010), responsible for ~22,500 blocks (~1,125,000 BTC at 50 BTC subsidy).

**What the mining data shows about timezone: nothing.**

This is the load-bearing finding for this cross-reference. Lerner's 2013 article ([*The Well Deserved Fortune of Satoshi Nakamoto*](https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/)) discusses the extraNonce-increment pattern and identifies the single-entity fingerprint but **makes no timezone claim**. His 2020 timestamp article ([*A New Mystery in Patoshi Timestamps*](https://bitslog.com/2020/06/22/a-new-mystery-in-patoshi-timestamps/)) identifies an anomalous ~312-second gap between consecutive Patoshi blocks, which Lerner interprets as either deliberate rate-throttling or an artifact of timestamp-increment software behavior. He explicitly **does not** derive a sleep gap or UTC offset from this pattern. His 2020 hardware article ([*The Patoshi Mining Machine*](https://bitslog.com/2020/08/22/the-patoshi-mining-machine/)) is exclusively a technical analysis of nonce-subrange behavior consistent with five parallel CPU threads; no geographic claims.

**The timezone analysis associated with "Patoshi" in secondary literature has been incorrectly attributed to Lerner.** It originates from Jameson Lopp's separate analysis of *communication* timestamps. Lerner's contribution is the on-chain mining fingerprint; the timezone interpretation is Lopp's. These are routinely conflated.

The one Patoshi finding with weak timezone relevance is the "double helix" period (blocks 1400–1916) where Patoshi's hash-rate signature doubles before returning to baseline. Lopp interprets this as two mining instances running simultaneously after a crash and restart, and maps the start/end times to Pacific: crash ~4 PM PST on 2009-01-22, discovered ~8 AM PST on 2009-01-23 ([Lopp 2019](https://blog.lopp.net/was-satoshi-a-greedy-miner/)). This is the sole quantitative timezone argument attached to Patoshi's on-chain behavior, and it comes from Lopp's paper, not Lerner's.

## What hour-of-day timestamps show (per this repo's data)

The repo assembled two independent timestamp corpora and ran sleep-window arithmetic against each.

**Corpus 1 (forum + email):** 582 timestamped events (539 BitcoinTalk posts + 43 emails sent by Satoshi), spanning 2008-10-31 through 2014-03-07. Source: [`results/hour-of-day-summary.json`](../results/hour-of-day-summary.json).

**Corpus 2 (source-control commits):** 279 unique commits attributed to Satoshi from the `bitcoin/bitcoin` Git log, deduplicated by commit hash, spanning 2009-10-21 through 2010-12-15. Source: [`results/commit-hour-of-day-summary.json`](../results/commit-hour-of-day-summary.json).

Fraction of activity in the 00:00–06:00 local window (normal human sleep hours):

| Timezone | Forum corpus | Commit corpus | Compatible with sleep? |
|----------|--------------|---------------|------------------------|
| GMT (UK winter) | 17.0% | 29.4% | No |
| BST (UK summer) | 24.1% | 34.4% | No |
| EST | 1.5% | 3.2% | Yes |
| PST | 1.5% | 2.5% | Yes |

The two corpora are methodologically independent: forum timestamps come from BitcoinTalk and bitcoin-list archives; commit timestamps come from author-date fields in the SVN-imported Git log. Both yield the same qualitative result. **The UK-resident hypothesis is doubly falsified.**

**What the timestamp data cannot do: discriminate EST from PST.** The sleep-window test passes both. The morning-onset gradient (the sharpest single circadian signal) shows the activity jump at 11 AM EST / 8 AM PST in both corpora. An 8 AM start in Pacific is a normal early-rising professional pattern; an 11 AM start in Eastern is a late-morning evening-developer pattern. Both biologically plausible.

## Convergence

### 1. Both threads agree the Patoshi mining data has no timezone signal

Lerner never claims a timezone from mining data. The hour-of-day analysis is built entirely on communication timestamps. There is no conflict — only a clarification: mining timestamps and communication timestamps are two different evidence streams, and the Patoshi pattern contributes nothing to the timezone question directly. Secondary sources asserting "the Patoshi pattern points to Eastern US" are misattributing Lopp's communication-timestamp analysis to Lerner's on-chain analysis.

### 2. UK-resident hypothesis is eliminated by hour-of-day data and unsupported by Patoshi

[Chain Bulletin's London claim](https://chainbulletin.com/satoshi-nakamoto-lived-in-london-while-working-on-bitcoin-heres-how-we-know) argues that plotting 742 data points in London time places "the bulk of last activity for a day between 1 AM and 3 AM London time." Our data, on the same underlying corpus, shows 17–24% activity in the GMT/BST 00:00–06:00 local window — far above what any awake human produces in sleep hours. Chain Bulletin's framing ("last activity of the day" between 1–3 AM) is consistent with a London night-owl, but the aggregate overnight activity fraction falsifies it: 17% in GMT overnight hours means active productivity at 3, 4, 5 AM London time, not merely going to bed at 1–3 AM. Patoshi's mining data neither supports nor challenges the London hypothesis.

### 3. Lopp's Pacific reading and our EST-or-PST reading share a common exclusion

Lopp concludes Pacific via the mining-restart narrative. Our analysis finds PST equally compatible with the sleep-window test. The two findings occupy the same possibility region: "somewhere in the continental US, probably West Coast." Neither independently rules out Eastern.

## Divergence

### 1. Lopp argues Pacific specifically; our data is agnostic between PST and EST

Lopp's narrative hangs on a single mining-event timeline placing Satoshi's waking hours on 2009-01-23 at 8 AM PST. This is one data point interpreted with a specific behavioral assumption: that discovering a two-instance mining bug is what Satoshi would do upon sitting down at the computer after waking. If Satoshi discovered the bug mid-afternoon for an unrelated reason, or if the recovery sequence took longer than minutes, the PST anchor weakens. Our 861-data-point corpus cannot replicate or refute this anchoring; neither corpus discriminates PST from EST. **Divergence: Lopp argues a specific timezone on a qualitative narrative; we find two timezones equally compatible on aggregate statistics.**

### 2. The commit corpus produces a sharper GMT/BST overnight footprint than the forum corpus

GMT overnight fraction rises from 17.0% (forum) to 29.4% (commits). Two compatible explanations:
- The commit corpus spans a later, more concentrated work period (Oct 2009 – Dec 2010) when Satoshi's workload may have shifted.
- The commit corpus contains a disproportionate fraction of late-session pushes (developers commonly commit before closing a work session, shifting apparent hour distribution toward end-of-work-day, earlier next-day window under GMT).

This does not change the falsification conclusion — 29.4% is if anything a *stronger* falsification of London than 17.0% — but the corpus-to-corpus divergence is a methodological flag if the analysis is extended.

## What neither thread can do

1. **Neither identifies a specific person.** Patoshi identifies one mining entity via cryptographic fingerprint. Hour-of-day identifies a timezone-compatible behavioral envelope. Combining them narrows a region on the map (continental US, West or East Coast). Neither names anyone.

2. **Neither achieves high-confidence EST-vs-PST discrimination.** Lopp's Pacific narrative is qualitatively appealing but rests on a single behavioral interpretation. Our aggregate statistics are agnostic. A 3-hour timezone difference produces a morning-onset shift within normal individual variation: an EST developer who starts at 11 AM is behaviorally indistinguishable in timestamp data from a PST developer who starts at 8 AM.

3. **Neither validates the circadian-rhythm assumption.** Both threads assume the entity behind "Satoshi" followed a single-person, single-timezone schedule throughout 2008–2010. The clean bimodal day/night structure in PST and EST framings is consistent with a single person *and* with a small tight-knit group sharing the Satoshi identity within one timezone. If Satoshi was two people in the same city, or if there were consistent-time handoffs, the aggregate pattern would be indistinguishable.

4. **Patoshi cannot confirm the Patoshi-equals-Satoshi identity link.** This is Lerner's own caveat (2013 paper, explicit). The pattern identifies one early miner; the forum/email evidence identifies Satoshi as developer and communicator. These are connected by strong prior probability but not by cryptographic proof. If someone other than Satoshi operated the Patoshi cluster, Lopp's mining-restart timezone inference would not apply to the whitepaper author.

5. **Neither thread can rule out deliberate obfuscation.** The UTC+8 email Date header originally cited by some sources was traced to AnonymousSpeech.com's server location, not Satoshi's local clock ([Chain Bulletin](https://chainbulletin.com/no-coindesk-satoshis-local-time-zone-wasnt-utc8)). If Satoshi routed email through anonymous remailers to obscure location, the same sophistication could apply to posting times: a privacy-aware developer could deliberately avoid posting during personally identifiable quiet hours. **Our hour-of-day data is a lower bound on what can be inferred, not an upper bound.**

## Synthesis: the defensible state of knowledge

Read together, both threads support one robust conclusion and one weak preference:

- **Robust conclusion:** Satoshi was not a UK resident during 2008–2010. Two independent timestamp corpora each show 17–34% activity in the UK 00:00–06:00 window. Not a close call. The Chain Bulletin London hypothesis is falsified by primary-data arithmetic.

- **Weak preference:** The communication-timestamp pattern is slightly more consistent with Pacific US than Eastern US, based on the morning-onset gradient. Lopp's independent Pacific narrative (if its mining-restart behavioral assumptions hold) points the same direction. The preference is soft; it does not reach falsification of Eastern.

- **Not-yet-tested:** The UK-emigré-Eastern-resident hypothesis (British writing signals, US East Coast residence) is compatible with the timestamp data but has not been independently corroborated. It remains live as a structural explanation for why writing evidence points UK and timing evidence points US. See [`uk-emigre-east-coast-candidates.md`](uk-emigre-east-coast-candidates.md) for the candidate-search negative finding.

## Source citations

- Lerner 2013, *The Well Deserved Fortune of Satoshi Nakamoto*: https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/
- Lerner 2019, *The Return of the Deniers and the Revenge of Patoshi*: https://bitslog.com/2019/04/16/the-return-of-the-deniers-and-the-revenge-of-patoshi/
- Lerner 2020, *A New Mystery in Patoshi Timestamps*: https://bitslog.com/2020/06/22/a-new-mystery-in-patoshi-timestamps/
- Lerner 2020, *The Patoshi Mining Machine*: https://bitslog.com/2020/08/22/the-patoshi-mining-machine/
- Lopp 2019, *Was Satoshi a Greedy Miner?*: https://blog.lopp.net/was-satoshi-a-greedy-miner/
- Chain Bulletin, *Satoshi Nakamoto Lived in London While Working on Bitcoin*: https://chainbulletin.com/satoshi-nakamoto-lived-in-london-while-working-on-bitcoin-heres-how-we-know
- Chain Bulletin, *No, CoinDesk, Satoshi's Local Time Zone Wasn't UTC+8*: https://chainbulletin.com/no-coindesk-satoshis-local-time-zone-wasnt-utc8
- PLOS ONE 2021, *Strangely Mined Bitcoins*: https://pmc.ncbi.nlm.nih.gov/articles/PMC8483420/ (DOI: 10.1371/journal.pone.0258001)

**Local data sources:**
- [`forensics/patoshi-pattern.md`](patoshi-pattern.md)
- [`forensics/uk-descent-eastern-resident-hypothesis.md`](uk-descent-eastern-resident-hypothesis.md)
- [`results/hour-of-day-summary.json`](../results/hour-of-day-summary.json) (n=582 forum/email events)
- [`results/commit-hour-of-day-summary.json`](../results/commit-hour-of-day-summary.json) (n=279 git commits)
