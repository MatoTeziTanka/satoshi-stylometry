# Hypothesis: UK descent, US Eastern resident

> **Status:** working hypothesis, not a claim. This document articulates the framing, supporting evidence, falsifiable predictions, and what it would imply for candidate selection. The hypothesis is *introduced* here, not *proved*.

## The framing

The standard candidate analyses pick a single geographic identity (London-resident, California-resident, Belgian, etc.) and look for evidence to fit. They fail to converge because the evidence itself doesn't converge — it points to multiple locations simultaneously.

A simpler explanation: **Satoshi was UK-born/educated but living in US Eastern Time during 2008–2010.** Writing style and cultural references reflect origin; timestamps and infrastructure reflect residence.

Under this hypothesis:

- *Origin signals* (writing style, cultural references, headline choice) are British.
- *Residence signals* (timestamp distribution, commit/post hour patterns) are US Eastern.
- The mix is not a contradiction; it's what a long-resident emigré looks like.

## Supporting evidence in our data

### Origin signals (British)

| Signal | Source |
|--------|--------|
| Word `favour` (British spelling) in section 6 of the whitepaper: *"such rules that favour him with more new coins"* | Direct extraction from [whitepaper-versions/whitepaper-v2.txt](../whitepaper-versions/whitepaper-v2.txt) by `pdftotext`. [VF] |
| Two-space-after-period typography throughout the whitepaper | Visible in the rendered v1 and v2 PDFs. Style associated with older British academic typography (though also with pre-2000 American typewriter-era typing). [VF visual] |
| Genesis block coinbase: `The Times 03/Jan/2009 Chancellor on brink of second bailout for banks` | The Times is a British newspaper, not distributed in US editions on that date. The headline references UK political events (the bailout of Royal Bank of Scotland). Choice of source is itself a cultural marker. [VF on-chain] |
| Phrase "bloody hard" in Satoshi's forum posts | Mild British colloquialism; not exclusive to UK speakers but more characteristic. [VF, Satoshi corpus] |

### Mixed-spelling pattern (consistent with long-term emigré)

| Signal | Source |
|--------|--------|
| `favour` (British) **and** `realizes`, `characterized` (American) in same whitepaper | Both extracted directly from the v2 PDF. A pure UK author would write `realises`, `characterised`. A pure US author would write `favor`. [VF] |
| Adam Back's Hashcash paper shows the same mixed pattern: `parameterised` (British) alongside `favor`, `defense`, `practice` (American) | Direct extraction. This is suggestive evidence that mixed spellings are *the* cypherpunk-era cryptographer norm in IETF-style writing, not unique to Satoshi. [VF, but weakens the British-signal-uniqueness argument] |

The mixed-spelling pattern is *consistent with* a UK-origin author who has been writing in US/IETF technical contexts for years, but is not by itself diagnostic of it.

### Residence signals (US Eastern)

| Signal | Source |
|--------|--------|
| Stefan Thomas's analysis of 539 BitcoinTalk posts: near-zero activity 05:00–11:00 UTC | [As reported in patoshi-pattern.md §4b](patoshi-pattern.md). 05:00 UTC = 00:00 EST; 11:00 UTC = 06:00 EST. Sleep window from midnight to 6 AM Eastern is the modal pattern for a working professional. [VF via secondary] |
| Code-commit timestamps correlate with British Summer Time (BST = UTC+1) per published analyses | BST also = EDT+5; American developers commonly commit during US daytime evening, which lines up with mid-afternoon BST. This data is *compatible with* both London and Eastern US. [VF] |
| Patoshi mining timestamps: no timezone signal identifiable | [patoshi-pattern.md §4a, citing Lerner 2020.](patoshi-pattern.md) The mining data does *not* support any specific timezone claim; the timezone arguments are all from communication timestamps. [VF] |

### Why the existing London vs Eastern dispute resolves under this hypothesis

The same 05:00–11:00 UTC sleep gap is read as:

- "01:00–03:00 London bedtime, awake at 06:00 London" (Chain Bulletin's London argument)
- "00:00–06:00 Eastern bedtime" (Stefan Thomas's Eastern argument)

Both are mathematically valid. The London reading requires Satoshi to keep late hours by London standards; the Eastern reading requires only a normal working-hours schedule by Eastern US standards. **By Occam's razor, the Eastern reading is the more parsimonious explanation of the same data.** The London-newspaper choice and British spellings are then independently explained by UK origin, not UK residence.

## What this hypothesis does NOT explain

1. **The Windows-MFC code style fingerprint** (`CTransaction`, `CBlock`, 100% space indent, line-comment preference). MFC training was equally common in UK and US enterprise developers in the 1990s-2000s. The code style is orthogonal to the UK/US question.
2. **Specific identity.** This hypothesis reframes the *geographic* question but does not pick out a specific person. It points to a *type* of candidate, not a name.
3. **Why no candidate matches all axes.** Of our 5 named candidates, none fits "UK descent + Eastern US resident":
   - **Adam Back:** UK-resident throughout the 2008–2010 period. Origin fits; residence doesn't.
   - **Hal Finney:** US-born, lifelong California (Pacific). Neither origin nor residence fits.
   - **Wei Dai:** Born in China, raised in Washington state (Pacific). Doesn't fit.
   - **Nick Szabo:** US-born, Washington state (Pacific). Doesn't fit.
   - **Len Sassaman:** US-born, Belgian resident at the time of his death. Doesn't fit.

   This hypothesis **points outside the current candidate set**.

## Testable predictions

If the hypothesis is true:

1. **Hourly distribution of Satoshi communications** should peak in US Eastern evening hours (after typical 9-to-5 work). Specifically: 22:00–02:00 UTC = 17:00–21:00 EST. Testable from BitcoinTalk + email corpus we already have.
2. **Bitcoin source-control commits** should cluster in US Eastern evenings, NOT London evenings. Sourceforge / GitHub commit hours are public.
3. **Public-holiday gaps** in Satoshi's activity should correlate with US Eastern holidays (Memorial Day, Thanksgiving, July 4), NOT UK bank holidays.
4. **Email response latency** should be lowest when correspondents are in EST/EDT, regardless of whether they themselves are in the UK or US.
5. **British spellings should appear at a low but nonzero rate consistent with passive retention** rather than active use. Specifically: function words and high-frequency terms should be American (`is`/`the`/`a` distributions match US norms), but content words from primary education (`favour`, `colour`) should retain British spellings.

Predictions (1)-(4) are testable from our existing corpus. (5) is testable but harder.

## What candidate-type this hypothesis would point to

A 2008-2010 candidate fitting this profile would be:

- Born or raised in the UK (Britain, Scotland, Wales, Northern Ireland).
- Educated at UK universities or schools (would explain `favour`, `colour` retention, two-space typography).
- Living in US Eastern timezone in 2008-2010 (DC, NYC, Boston, or anywhere in the EST corridor).
- Working in a technical role with C++ exposure (likely Windows-MFC for the code-style fingerprint).
- Active in cypherpunk circles enough to have read Hashcash, b-money, and the Haber/Stornetta timestamping papers.

This profile fits a number of UK-emigré academic cryptographers and fintech engineers who were active in the East Coast US in the late 2000s. It is *not* the profile of the named cypherpunk-era candidates this repo has analyzed so far.

## How to operationalize

To turn this from hypothesis into testable claim, the next concrete work is:

1. **Hour-of-day histogram** of Satoshi's BitcoinTalk + bitcoin-list activity. Bin by UTC hour. Visually compare to the predicted patterns for: GMT-resident, BST-resident, EST-resident, PST-resident.
2. **Specific holiday-gap analysis:** Are there ~3-day silences around US Eastern Thanksgiving 2009 / 2010? Around UK bank holidays?
3. **Add UK-descent-East-Coast candidates to the prose stylometry.** Possible candidates to research: any UK-trained cryptographers at NYC/DC/Boston institutions in 2008. This is a corpus-collection task, not a quick search.

## TEST RESULTS (run 2026-05-27)

We ran the hour-of-day histogram described under "Testable predictions" against the primary corpus (543 BitcoinTalk posts + 39 emails sent by Satoshi, n=582 timestamped events). Source: [`results/hour-of-day-by-timezone.png`](../results/hour-of-day-by-timezone.png), [`results/hour-of-day-summary.json`](../results/hour-of-day-summary.json).

### Result: "Satoshi was in UK time" is **falsified** by the data

The fraction of total activity falling in the 00:00-06:00 local hours (the modal human sleep window):

| Hypothesized timezone | % of activity at 00:00-06:00 local | Compatible with normal human sleep? |
|----------------------|-----------------------------------|-------------------------------------|
| GMT (UK winter)      | **17.0%**                         | **No** — orders of magnitude too high |
| BST (UK summer)      | **24.1%**                         | **No** — even worse |
| EST (US Eastern)     | 1.5%                              | Yes |
| EDT (US East summer) | 3.3%                              | Yes |
| PST (US Pacific)     | 1.5%                              | Yes |
| PDT (US Pac summer)  | 0.7%                              | Yes |

A human resident in the UK would, by primary timestamp evidence, show < 5% of activity in their local 00:00-06:00 window. Satoshi's pattern in GMT/BST shows 17-24%. **The "Satoshi was in London" claim (Chain Bulletin and similar) is incompatible with the timestamp data.**

This does not require an interpretive judgment — it's arithmetic on public timestamps.

### Result: the data does **not** discriminate between EST and PST

Both EST and PST produce sleep windows compatible with normal human activity:

- **EST quiet hours:** 02:00-06:00 local (5-hour window). Implies "bedtime around 2am, wake at 6-7am." Late-night working professional pattern.
- **PST quiet hours:** 23:00-03:00 local (5-hour window wrapping midnight). Implies "bedtime 11pm-midnight, wake at 4-6am." Normal early-rising pattern.

Both are biologically plausible. Our data does not pick between them.

### What this means for the original hypothesis

- The **"US Eastern resident"** half of the hypothesis is **compatible** with the data but **not uniquely required** by it. PST is equally compatible from this test alone.
- The **"UK descent"** half of the hypothesis is **unchanged** by this test — it rests on writing-style and cultural-reference evidence, not timestamps.
- The combined hypothesis is therefore **partially supported (residence half cannot be uniquely confirmed but is compatible) and partially independent (origin half is unaffected by this test)**.
- The competing **"UK resident"** claim (Chain Bulletin's 2021 London analysis) is **directly falsified** by this same primary-data test.

### What was wrong about prior claims (debunking)

- **Chain Bulletin "Satoshi was in London"** ([source](https://chainbulletin.com/satoshi-nakamoto-lived-in-london-while-working-on-bitcoin-heres-how-we-know)) cited 742 data points and concluded London. Our 582-point primary test on the same corpus shows GMT/BST produce 17-24% activity in 00:00-06:00 local — far too high to be a sleeping human. Either Chain Bulletin's interpretation of their 742 data points is wrong, or the data sets differ substantially. The arithmetic on our publicly verifiable corpus refutes the conclusion.
- **My earlier in-thread assertion that "Patoshi was Pacific timezone"** was speculation without primary evidence. The data is compatible with both Eastern and Pacific. Marking that as [INC] (incorrect) — corrected to "consistent with Eastern OR Pacific."
- **Lopp's specific Pacific narrative** (citing Hal Finney fit) is *consistent with* our data but not *uniquely supported by* it. Eastern is equally well-supported by the sleep-window test.

### What this analysis does NOT do

- It does not identify a specific person.
- It does not discriminate between EST and PST.
- It does not test whether Satoshi was a UK national who *had been* in the US (the origin question is independent).
- It is one analysis on one corpus. The 582-event sample is what's publicly archived; it may be incomplete.

## Honest caveats

- This hypothesis is **not original** to this repo. Variants have been raised in Bitcoin-forensic discussions for years. The Chain Bulletin (London) and Lopp (Pacific) analyses already exhibit the failure mode of forcing a single-location reading; the UK-descent-EST framing is the natural reconciliation.
- The hypothesis is **not falsifiable from the data we have on disk.** Testing it requires hour-of-day analysis we haven't run yet (see "Testable predictions" above).
- The hypothesis **does not identify a person.** It reframes the suspect-type. Naming a specific person on the basis of "UK descent + Eastern US" alone would be reckless.

## FOLLOW-UP TESTS (run 2026-05-27, same session)

The original write-up listed three follow-ups; (1) was already shipped. We have now run (2) and (3); we report what they did and did not discriminate.

### Test A: independent-corpus replication via Bitcoin source-control commits

We pulled the bitcoin/bitcoin Git log and extracted 279 unique commits attributed to Satoshi (245 from the SVN-imported `s_nakamoto@<SVN-UUID>` author, 34 from the post-2010-08-28 `satoshin@gmx.com` author, deduplicated by commit hash). Timestamps are author dates preserved through the SourceForge SVN → GitHub import. This is a fully independent corpus from the 582 forum-post / email events. Source: [`results/commit-hour-of-day-summary.json`](../results/commit-hour-of-day-summary.json), reproducer in [`src/time_forensics.py`](../src/time_forensics.py).

Sleep-window arithmetic on the commit corpus:

| Hypothesized timezone | % of commits at 00:00-06:00 local | Compatible with human sleep? |
|----------------------|-----------------------------------|------------------------------|
| GMT (UK winter)      | **29.4%**                         | **No** — far worse than the forum corpus |
| BST (UK summer)      | **34.4%**                         | **No** — even worse |
| EST (US Eastern)     | 3.2%                              | Yes |
| EDT (US East summer) | 6.8%                              | Yes — borderline |
| PST (US Pacific)     | 2.5%                              | Yes |
| PDT (US Pac summer)  | 0.4%                              | Yes |

**The UK-resident hypothesis is doubly falsified.** Two independent corpora — public communications and source-code commits — both place 17-34% of Satoshi's activity in the UK 00:00-06:00 local window. No working professional would commit code from 1am to 6am as their normal pattern across 279 commits.

The commit-corpus replication is also a methodological check: if our prior result depended on something idiosyncratic about how forum-post timestamps are recorded, the commit corpus would disagree. It agrees.

### Test B: morning-onset gradient (the weak EST-vs-PST tell)

The wake-up edge — the hour at which activity sharply rises — is the most informative single signal for residence timezone. We tabulated morning activity 5am-noon local for each timezone hypothesis.

Forum corpus (n=582):

| Timezone | 5am | 6am | 7am | 8am | 9am | 10am | 11am | 12pm |
|----------|-----|-----|-----|-----|-----|------|------|------|
| EST      | 0   | 0   | 3   | 5   | 14  | 19   | **52** | 68 |
| PST      | 5   | 14  | 19  | **52** | 68  | 72   | 46   | 46 |

Commit corpus (n=279):

| Timezone | 5am | 6am | 7am | 8am | 9am | 10am | 11am | 12pm |
|----------|-----|-----|-----|-----|-----|------|------|------|
| EST      | 0   | 0   | 0   | 6   | 5   | 11   | **28** | 22 |
| PST      | 6   | 5   | 11  | **28** | 22  | 21   | 18   | 20 |

In both corpora the "wake-up jump" is at 11am EST or at 8am PST. **8am PST is a normal early-rising professional pattern. 11am EST is a late-starting evening-developer pattern.** Both are biologically plausible. The PST reading produces a smoother monotonic morning ramp (5→14→19→52→68 in forum; 6→5→11→28→22 in commits); the EST reading produces a flatter ramp with a sharper isolated jump at 11am.

If forced to pick, the PST reading is slightly more typical of a working-hours pattern. But this is a soft preference, not a falsification. **The test does NOT discriminate EST from PST.**

### Test C: holiday-gap analysis (limited utility for EST vs PST)

We ran activity counts in a ±1-day window around each US federal holiday (observed in BOTH EST and PST) and around UK-only bank holidays (Good Friday, Easter Monday, Early/Spring/Summer Bank Holidays, Boxing Day). Source: [`results/holiday-gap-summary.json`](../results/holiday-gap-summary.json).

**Methodological limit found:** of the 12 UK-only holidays in Satoshi's active window (2008-11-01 to 2010-12-13), 10 fall in early-Bitcoin sparse-activity phases (UK 2009 spring/summer) where the local ±7-day neighbor baseline is itself zero. Only 2 UK-only holidays (2010-05-31 Spring Bank Holiday and 2010-08-30 Summer Bank Holiday) sit in periods of meaningful baseline activity for comparison. Both show silence (0 events and 1 event respectively, vs neighbor baselines of 0.83 and 2.25 events/day), but n=2 is too thin for a strong claim.

US federal holidays (n=9 with meaningful neighbor baseline) show a mixed pattern: Memorial Day 2010 and Columbus Day 2010 silenced (0 events each in the 3-day window); Thanksgiving 2010 and July 4 2010 ELEVATED above baseline (2.0-3.2× neighbor mean). This is consistent with a single-developer pattern where "stay-home" holidays (Thanksgiving, July 4) produce MORE coding, "go-out" holidays (Memorial Day, Columbus Day) produce silence.

**Critically:** US federal holidays are observed at the same calendar dates in BOTH EST and PST. Holiday-gap analysis cannot in principle discriminate EST from PST. The test that was originally specified ("US Eastern Thanksgiving 2009 / 2010 vs UK bank holidays") tests US-resident vs UK-resident, which we already have from the sleep-window test.

The test is therefore reframed: we did not find new EST-vs-PST evidence from holidays. The two-meaningful-data-point UK-only silence is suggestive of "Satoshi observed a UK working calendar" but the sample is too small to defend as a strong finding. We report it and decline to lean on it.

### Test D: day-of-week distribution (unexpected Sunday > Saturday pattern)

Day-of-week local-to-residence (forum corpus, n=582), totals across all timezones:

| Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|-----|-----|-----|-----|-----|-----|-----|
| 66  | 51  | 95  | 110 | 96  | 53  | 111 |

The Sunday-greater-than-Saturday inversion is unusual for a typical Western working pattern (where Saturday is typically the lowest-activity day and Sunday is moderate). Two readings:
- A pattern where Saturday is "off" (errands, family, social) and Sunday is "catch up on stuff" before Monday.
- An observer with a Saturday sabbath observance (Seventh-Day Adventist, Jewish, some Sabbatarian Christian denominations).

This is at most weak suggestive evidence, not load-bearing. The Thursday peak (110) is unusual but unremarkable. We report the distribution and decline to over-read it.

### Net conclusions from the follow-up tests

- The **UK-resident hypothesis is doubly falsified** by independent corpora — the result is robust to the choice of timestamp source.
- The **EST-vs-PST discrimination remains open**. Morning-onset gradient slightly favors PST; holiday-gap analysis cannot discriminate; day-of-week is suggestive but not load-bearing.
- The **UK-emigré-East-Coast hypothesis remains under-tested**. Hour-of-day analysis is compatible with it but does not uniquely select it; the same data is compatible with any US-resident interpretation.

The honest reading is: the test set we have was designed to falsify the UK-resident claim, which it did, twice. It was not designed to fingerprint EST vs PST, and reasonable arithmetic on this corpus cannot do that. A stronger discriminator would require: (a) much more granular timestamps such as keystroke logs, which don't exist publicly; (b) a corpus whose timestamps include the timezone offset itself, which neither forum posts nor SVN commits do; or (c) a higher-resolution behavioral signal correlated with circadian rhythm (e.g. response-latency distributions to specific correspondents in known timezones).

## What I'd commit to ship next on this thread (updated)

Now that (A) and (B) are shipped:

1. ✅ Hour-of-day histogram on the Satoshi corpus — shipped.
2. ✅ Independent-corpus replication via commits — shipped this session.
3. ⚠️ Holiday-gap analysis — shipped but found to have limited statistical power for EST/PST discrimination; result reported honestly.
4. ❓ Candidate-set expansion with UK-emigré-East-Coast profile — see [`uk-emigre-east-coast-candidates.md`](uk-emigre-east-coast-candidates.md) for the negative finding (zero candidates fit all four axes).
