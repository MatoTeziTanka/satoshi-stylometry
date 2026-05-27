# The Patoshi Pattern: On-Chain Forensics of Early Bitcoin Mining

**Status:** Research brief — primary sources fetched 2026-05-26  
**Author:** Research subagent (read-only)  
**Confidence tier key:** [V] verified this session, [I] inferred from verified facts

---

## 1. The Discovery

In April 2013, Sergio Demian Lerner, then chief scientist at RSK Labs, published a blockchain analysis on his blog Bitslog identifying a distinctive fingerprint in the coinbase transactions of early Bitcoin blocks. [V]

**Primary source:** https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/

The fingerprint lives in the `extraNonce` field of the coinbase transaction. In Bitcoin's original client, `extraNonce` increments each time the 32-bit nonce space overflows during hashing — it acts as a slow free-running counter that is not reset between blocks unless the mining software restarts. Lerner plotted `extraNonce` values against block height for the first 36,288 blocks and observed that the data fell into distinct straight-line segments on the graph. Each segment represents one continuous mining session by one miner; the slope of each segment is proportional to that miner's hash rate relative to others.

One set of segments stood apart: steep slopes appearing throughout the period, all attributed to a single entity mining at a consistently higher rate than anyone else, starting from block 1. Lerner named this entity "Patoshi" to avoid conflating the statistical inference with the identity claim "Satoshi." [V]

**Second key finding from the 2020 "mining machine" analysis:** Patoshi's nonce-space scanning behavior was itself anomalous. Instead of scanning the full 32-bit nonce range (0–255 in the least-significant byte), Patoshi used only specific subranges: [0–9], [19–28], [29–38], [39–48], [49–58]. This is five parallel 24-bit sequential intervals — consistent with five simultaneous threads on a single CPU, likely an Intel i7-965 or equivalent, running SSE2-optimized code. Critically, the nonce was *decremented* rather than incremented — the opposite of the reference Bitcoin 0.1 client. This makes the Patoshi fingerprint doubly distinctive: both the extraNonce slope pattern and the nonce-space coverage are signatures absent from any other miner in the sample. [V]

**Source:** https://bitslog.com/2020/08/22/the-patoshi-mining-machine/

---

## 2. Block Range, Quantity, and Dates

| Parameter | Value | Source |
|---|---|---|
| Analysis window | Blocks 0–50,000 (original) | Lerner 2013 |
| Patoshi blocks identified | ~22,000 of the first 50,000 | Lerner 2013, 2019 |
| Last Patoshi block | Block 54,316 (per Whale Alert / Lerner follow-up) | [V] |
| Mining period | January 3, 2009 – approximately May 2010 | [V] |
| Patoshi share of first 50k blocks | ~43% | Lerner 2019 |
| Block subsidy (entire period) | 50 BTC | [I] |
| Estimated BTC mined | ~1,125,150 BTC (22,000+ blocks × 50 BTC/block) | [V] |

**How the 1.1 million figure is calculated:** Approximately 22,500 blocks attributed to Patoshi × 50 BTC block subsidy = ~1,125,000 BTC. Lerner originally wrote that the miner accumulated "at least 1 million bitcoins" representing ~63% of all BTC awarded during the covered period; subsequent refinement produced the widely-cited 1,125,150 BTC figure. [V]

**Source for block 54,316 as last Patoshi block:** https://bitcoinethereumnews.com/bitcoin/satoshi-nakamotos-last-known-mined-bitcoin-block-uncovered/

---

## 3. Wallet Status: Have Any Patoshi Coins Moved?

**Short answer: No — with one notable exception predating the pattern analysis.**

The 10 BTC sent to Hal Finney on January 12, 2009 (in the first-ever Bitcoin transaction, block 170) came from a wallet attributed to Satoshi, not from the Patoshi pattern set. As of 2026, no coins from addresses identified by the Patoshi pattern have ever been spent or moved. The wallets have no outgoing transactions. Blockchain surveillance firms (Whale Alert, Arkham, Bitget) maintain live tracking of these addresses and have not recorded any movement. [V]

Some early-era wallets (mined 2009–2010 but NOT confirmed Patoshi) have periodically shown activity; these cause periodic media coverage that conflates non-Patoshi early coins with Satoshi's holdings. Researchers consistently clarify the distinction. [V]

**Sources:**
- https://nexo.com/blog/satoshi-nakamoto-bitcoin-wallet
- https://info.arkm.com/research/satoshi-nakamoto-net-worth-2025
- https://www.bitget.com/academy/satoshi-btc-wallets

---

## 4. Timezone Analysis

This is the most contested and least-resolved forensic question. The analysis separates cleanly into two tracks: (a) mining timestamp gaps, and (b) communication timestamp distribution. They do not fully agree.

### 4a. Mining Timestamp Gaps (Patoshi-specific)

Lerner's 2020 timestamp paper found a persistent ~312-second (~5-minute) gap between Patoshi blocks — Patoshi almost never mined a block within 5 minutes of the previous one. This appears to be a deliberate software behavior (either a pause to allow others to compete, or a timestamp-increment mechanism to prevent two blocks sharing the same second). This pattern does not identify a *circadian* sleep gap and provides no timezone signal. [V]

**Source:** https://bitslog.com/2020/06/22/a-new-mystery-in-patoshi-timestamps/

A separate finding from the 2019 paper: there are **zero timestamp inversions** among Patoshi blocks across the entire 50,000-block window. Because Patoshi mined 43% of all blocks, this is statistically extraordinary and constitutes the strongest evidence for a single computer clock — not a distributed operation. [V]

**Source:** https://bitslog.com/2019/04/16/the-return-of-the-deniers-and-the-revenge-of-patoshi/

Neither of these findings identifies a sleep pattern tied to a geographic timezone. Lerner's published work does not claim a specific UTC offset from the mining data alone.

### 4b. Communication Timestamps (Forum Posts, Emails, Commits)

This track analyzes when Satoshi was *communicating* (not mining), which may or may not correspond to Patoshi's timezone:

**Stefan Thomas analysis (early and influential):** Plotting all 539 Bitcointalk posts by UTC timestamp showed almost no activity between 05:00 and 11:00 UTC. This 6-hour gap is most consistent with a sleep window. [I from verified source]

**Interpretation by timezone:**
- If sleep is 05:00–11:00 UTC, the approximate local midnight would be around 01:00–03:00 local time for a **GMT/London** resident (UTC+0 to UTC+1 in winter/summer).
- For **Eastern US (UTC-5)**: 05:00 UTC = midnight Eastern; 11:00 UTC = 06:00 Eastern. Sleep from midnight to 6am Eastern is plausible.
- For **Pacific US (UTC-8)**: 05:00 UTC = 21:00 PST; 11:00 UTC = 03:00 PST. Sleep from 9pm to 3am is an unusually early bedtime.

**Jameson Lopp's analysis (bitslog-cited, 2019):** Compiling public activity timestamps from emails, forum posts, and code commits, Lopp concluded "Satoshi maintained a sleep schedule consistent with someone staying in the Pacific time zone." He uses this to explain the "double helix" mining anomaly in blocks 1400–1916 (starting ~4pm Pacific January 22, 2009, crash discovered ~8am Pacific January 23). [V]

**Source:** https://blog.lopp.net/was-satoshi-a-greedy-miner/

**Chain Bulletin / London hypothesis:** A separate analysis of 742 timestamped instances (posts + commits + emails) concluded with "reasonable confidence" that Satoshi was located in London, citing the inactive hours as consistent with a GMT night-owl (bulk of last-daily-activity between 01:00–03:00 local London time) and the Genesis block's inclusion of a Times of London headline not distributed in US editions. [V]

**Source:** https://chainbulletin.com/satoshi-nakamoto-lived-in-london-while-working-on-bitcoin-heres-how-we-know

**The UTC+8 / Japan claim refuted:** CoinDesk and others cited a UTC+8 timezone in Satoshi's email Date headers. The Chain Bulletin demonstrated this reflects the AnonymousSpeech.com webmail server location (Tokyo), not Satoshi's local clock. Satoshi used this anonymous remailer, making email headers unreliable for geographic inference. [V]

**Source:** https://chainbulletin.com/no-coindesk-satoshis-local-time-zone-wasnt-utc8

### 4c. Synthesis: What the Timezone Analysis Actually Shows

**The honest finding is that the data is consistent with multiple timezones and no single answer is definitive.** The most defensible summary:

- **GMT/London (UTC+0):** Supported by the Chain Bulletin analysis of 742 data points and the Genesis block newspaper reference. The "5pm to 3am" work window fits London perfectly. This is the strongest single-source geographic argument.
- **US Eastern (UTC-5):** Consistent with Stefan Thomas's posting gap (midnight–6am Eastern). The 2018 finding that code commits correlate with British Summer Time timestamps is compatible with Eastern US (BST = UTC+1 = EST+6; American developers commonly push code during US daytime hours).
- **US Pacific (UTC-8):** Supported by Lopp's forum/email analysis; his specific narrative of mining restarts fits Pacific timestamps. Hal Finney lived in Santa Barbara, California (Pacific time).
- **CET (UTC+1, Belgium/Netherlands):** No primary-source evidence specifically supports CET from the communication or mining data.

**The mining data itself (Patoshi pattern) does not identify a timezone.** Lerner's papers do not claim a sleep-gap signal from block timestamps. The timezone arguments for Satoshi are entirely derived from *communication* timestamps, not the Patoshi forensics.

---

## 5. Open-Source Replications

### Lerner's own code
Lerner has not published a standalone replication repository, but all methodology is documented across his Bitslog posts with graphs and sufficient technical detail for replication.

**Bitslog tag index:** https://bitslog.com/tag/patoshi/

### jratcliff63367 / blockchain21
John W. Ratcliff published a Bitcoin blockchain parser at https://github.com/jratcliff63367/blockchain21 described as "a very simple bitcoin blockchain parser." The repository parses blockchain data files and can extract coinbase data, making it usable for extraNonce analysis. However, the README does not specifically document Patoshi pattern replication — it is a general-purpose parser. [V]

### Peer-reviewed extension
A 2021 PLOS ONE paper ("Strangely mined bitcoins: Empirical analysis of anomalies in the Bitcoin blockchain transaction network") independently analyzed the anomalous mining signature and **found recurrent instances of the pattern extending from 2010 through 2018**, suggesting either multiple actors adopted the same technique or coordinated dispersal activities. This is a partial challenge to the single-entity-Satoshi interpretation. [V]

**Source:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8483420/  
**DOI:** 10.1371/journal.pone.0258001

---

## 6. The 1.1 Million BTC Estimate: Confidence Assessment

**Derivation:** ~22,500 Patoshi blocks × 50 BTC = ~1,125,000 BTC, rounded to "1.1 million."

**Confidence factors:**

| Factor | Assessment |
|---|---|
| ExtraNonce slope clustering | Strong — visually unambiguous in Lerner's graphs |
| Nonce subrange fingerprint | Very strong — narrow, specific, consistent |
| Zero timestamp inversions | Very strong — statistically near-impossible by chance |
| Single entity (vs. coordinated group) | Strong but not certain — the PLOS ONE paper raises the multi-actor possibility |
| Patoshi = Satoshi | Inferential — highest prior probability, not mathematically proven |
| Exact BTC count | Estimate — block attribution is probabilistic, not block-by-block certain |

The 1.1 million BTC figure should be understood as a well-founded *estimate with a narrow confidence interval*, not a precise accounting. Lerner's 2019 defense of the methodology substantially increased confidence in the single-entity claim, but the PLOS ONE recurrence finding is a live challenge.

---

## 7. Challenges and Refinements

### Challenge 1: Sequential nonce bias (nullc / Gregory Maxwell)
Bitcoin Core developer "nullc" argued the pattern could result from all early miners evaluating nonces sequentially (starting low), which would create a bias toward low nonce values and produce apparent slope patterns as an artifact. Lerner's 2019 rebuttal: the probability of a valid nonce is ~2^32/difficulty; with difficulty near 1 in 2009, valid nonces are essentially uniformly distributed — sequential evaluation cannot produce the observed slopes. [V]

### Challenge 2: Early mining pool hypothesis
Some researchers proposed an informal early mining pool or coordinated group of friends could explain the consistent fingerprint. Lerner's counter: each Patoshi block links backward to another Patoshi block (by coinbase address relationships and extraNonce continuity), but never to a non-Patoshi block. A pool of independent miners would show cross-chain linkages. [V]

### Challenge 3: PLOS ONE recurrence (2021)
The most substantive challenge. The 2021 academic paper found similar extraNonce anomalies recurring through 2018, which is long after Satoshi's known withdrawal. This implies either: (a) someone else later adopted the same nonce-skipping technique, (b) the 2009 Patoshi blocks represent an early coordinated group that continued operating, or (c) the pattern-detection method has false positives at later difficulty levels. This challenge has not been fully resolved in the literature. [V]

### Refinement: Deliberate hash-rate throttling
Multiple analyses confirmed Patoshi consistently mined at approximately 50% of its estimated hardware capacity. Lerner's interpretation: Satoshi intentionally limited hash rate to avoid monopolizing block production during the network's infancy, consistent with the 5-minute self-imposed pause between blocks. This throttling is forensically consistent with a network steward, not a purely profit-motivated miner. [V]

---

## Primary Sources Index

| Source | URL |
|---|---|
| Lerner 2013 original | https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/ |
| Lerner 2013 first-half 2010 | https://bitslog.com/2013/04/17/more-on-block-mining-history-1st-half-of-2010/ |
| Lerner 2019 rebuttal | https://bitslog.com/2019/04/16/the-return-of-the-deniers-and-the-revenge-of-patoshi/ |
| Lerner 2020 timestamp mystery | https://bitslog.com/2020/06/22/a-new-mystery-in-patoshi-timestamps/ |
| Lerner 2020 mining machine | https://bitslog.com/2020/08/22/the-patoshi-mining-machine/ |
| Bitslog Patoshi tag | https://bitslog.com/tag/patoshi/ |
| PLOS ONE 2021 academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC8483420/ |
| Lopp timezone / greedy miner | https://blog.lopp.net/was-satoshi-a-greedy-miner/ |
| Chain Bulletin London claim | https://chainbulletin.com/satoshi-nakamoto-lived-in-london-while-working-on-bitcoin-heres-how-we-know |
| Chain Bulletin UTC+8 refutation | https://chainbulletin.com/no-coindesk-satoshis-local-time-zone-wasnt-utc8 |
| jratcliff63367 blockchain21 | https://github.com/jratcliff63367/blockchain21 |
| Last Patoshi block (block 54,316) | https://bitcoinethereumnews.com/bitcoin/satoshi-nakamotos-last-known-mined-bitcoin-block-uncovered/ |
| Arkham Satoshi tracking | https://info.arkm.com/research/satoshi-nakamoto-net-worth-2025 |
