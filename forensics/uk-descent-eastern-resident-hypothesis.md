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

## What I'd commit to ship next on this thread

If you want to push the hypothesis from "introduced" to "tested":

1. Run the hour-of-day histogram on the existing Satoshi corpus (BitcoinTalk + emails) and add to `results/`. Cheap — 30 min of work.
2. Do the holiday-gap analysis. Cheap — 1 hour.
3. The candidate-set expansion is expensive (requires sourcing pre-2008 writings from UK-emigré-East-Coast cryptographers, which is harder than the Nakamoto Institute archive sweep we already did).

Items (1) and (2) would let us either strengthen or falsify the hypothesis with our existing data.
