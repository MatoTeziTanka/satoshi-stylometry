# NYT April 2026 Adam Back investigation — what our analysis says

## What the NYT reportedly claimed (per secondary summaries)

The New York Times published an investigation in April 2026 by Pulitzer-winning journalist John Carreyrou (with AI-editor Dylan Freedman) arguing that Adam Back — British cryptographer, CEO of Blockstream — is the person behind the Satoshi Nakamoto pseudonym. The original article is paywalled; everything in this section is drawn from secondary trade-press summaries listed at the end. They are trade press, not primary forensic evidence. We list them as the public record of what the investigation reportedly contained, NOT as authoritative claims.

The reported evidence fell into three categories.

**Writing analysis.** The investigation reportedly analyzed 134,308 cypherpunk mailing-list posts (1992–2008) using three methodologies. Back ranked top across all three. Specific signals cited: double-spacing after full stops; British spellings; inconsistent toggling between "e-mail" and "email"; shared hyphenation habits. Back reportedly shared 67 of 325 hyphenation errors with Satoshi; the second-closest candidate had 38.

**Timeline.** Back went silent on the Cryptography mailing list during Satoshi's active period and did not publicly comment on Bitcoin until approximately six weeks after Satoshi's disappearance in April 2011.

**Conceptual proximity.** Back's 1997 Hashcash posts described primitives that appear in Bitcoin's architecture; Hashcash is cited as reference [6] of the Bitcoin whitepaper.

**The investigation's own linguist called the result inconclusive.** Computational linguist Florian Cafiero (the paper's external expert) found Back the closest match among 12 suspects but described the result as inconclusive, with Hal Finney nearly tying for top.

Back denied being Satoshi in a two-hour interview, reportedly more than six times. The investigation offered no cryptographic proof — no private-key signature, no Satoshi-wallet movement.

## Where our independent analysis converges with the NYT result

**Code-identifier Burrows' Delta: Adam Back IS the closest match (Δ = 0.78).** Source: [`results/code-style-features.json`](../results/code-style-features.json), `rank_from_satoshi` array — Back 0.784, Dai 0.911, Finney 0.987, Sassaman 1.393.

This is the strongest single positive signal for Back in our data. On a 64-feature code-identifier vocabulary applied to Satoshi's 13,716-LOC Bitcoin 0.1.3 codebase versus Back's 9,086-LOC Hashcash codebase, Back is closest by a meaningful margin. The shared vocabulary is dominated by low-level systems-C idioms (loop variables, buffer naming, error-handling labels). Back's score on this axis is real.

**British origin signal is consistent with Back.** Source: [`forensics/uk-descent-eastern-resident-hypothesis.md`](uk-descent-eastern-resident-hypothesis.md), "Origin signals" table. The Bitcoin whitepaper contains the British spelling "favour" (section 6), two-space-after-period typography, and the Genesis Block coinbase references a British newspaper (`The Times 03/Jan/2009`). Back is documented UK-born and UK-educated (PhD, University of Exeter), the highest-volume UK cypherpunk by post count on the primary list archive (732 posts under `aba@dcs.exeter.ac.uk`). This is consistent with the NYT's British-spelling observation. It does not distinguish Back from other UK-British cryptographers, but it's consistent.

**Whitepaper prose: Back is second (Δ = 0.98).** Source: [`README.md`](../README.md) per-register table, "Whitepaper" row. On the 3,571-word whitepaper analyzed in isolation, Back ranks second of five candidates. Back is the cited reference [6] of the whitepaper and was Satoshi's first documented email contact (August 2008). The whitepaper's register is consistent with Back's published academic prose. Partial convergence — second place, not first — but Back is in meaningful range on the most formal sub-corpus.

## Where our analysis diverges from / argues against the NYT result

Three independent axes point directly against the NYT conclusion.

### 1. Timestamp analysis doubly falsifies UK residence, and Back was UK-resident through 2008

Source: [`forensics/uk-descent-eastern-resident-hypothesis.md`](uk-descent-eastern-resident-hypothesis.md), TEST RESULTS and FOLLOW-UP TESTS sections.

Fraction of activity in the local 00:00–06:00 window (normal human sleep):

| Timezone | Forum corpus (n=582) | Commit corpus (n=279) |
|----------|----------------------|------------------------|
| GMT (UK winter) | 17.0% | 29.4% |
| BST (UK summer) | 24.1% | 34.4% |
| EST | 1.5% | 3.2% |
| PST | 1.5% | 2.5% |

A human sleeping normal hours would show <5% activity in their local 00:00–06:00. Satoshi's pattern produces 17–34% in the UK sleep window across **two independent corpora** — public communications AND source-control commits. The UK-resident reading is arithmetically refuted.

Adam Back was UK-resident through 2008 and moved to Malta in 2009 (per [`forensics/uk-emigre-east-coast-candidates.md`](uk-emigre-east-coast-candidates.md), Adam Back entry, citing [cypherspace.org/adam](http://www.cypherspace.org/adam/)). Malta is UTC+1 (same offset as BST) — the timezone test is not materially different. **Satoshi's activity pattern is incompatible with the timezone of every location Back is documented to have lived during the relevant period.** The NYT identified Back partly on the basis of British signals; those signals, when tested against timestamp evidence, eliminate UK-resident candidates.

### 2. The MFC Hungarian C-prefix naming convention is absent from Back's code and present in Satoshi's

Source: [`results/code-style-features.json`](../results/code-style-features.json), `naming_pct.Hungarian_C`.

Satoshi's Bitcoin 0.1.3 codebase uses MFC-style `C[Capital]` class naming (`CTransaction`, `CBlock`, `CKey`, `CCriticalSection`) at 6.4% of all identifiers. This convention originates from Microsoft Foundation Classes — the standard Windows C++ framework of the 1990s–2000s.

| Author | Hungarian_C rate |
|--------|------------------|
| Satoshi | 6.4% |
| Back | 0.2% (30× less) |
| Dai | 0.1% |
| Finney | 0.1% |
| Sassaman | 0.2% |

Back's published code (Hashcash) is C, not C++. The MFC `C[Capital]` convention is C++-specific — it is applied to class declarations, which C does not have. **Back's Hashcash codebase cannot produce MFC-style class names regardless of Back's stylistic preferences, because the language doesn't support the construct.** The single most diagnostic code-style feature in Satoshi's codebase is structurally absent from the only Back code we can analyze. This is not a "Back may have written Windows C++ in commercial roles" gap — it's a gap in the very evidence base used to make the code-axis positive claim. The identifier-delta result (Back Δ 0.78, our positive signal) is driven by shared low-level C vocabulary, not by the Hungarian convention.

### 3. Prose stylometry does not pick Back first on either register

Source: [`README.md`](../README.md) per-register table, [`results/results.json`](../results/results.json).

On the aggregate function-word analysis across Satoshi's full 133,000-word corpus, Back ranks fourth (Δ 1.347), behind Finney (Δ 0.976), Szabo (Δ 1.266), Sassaman (Δ 1.337). On conversational registers (BitcoinTalk posts + emails, 70,000+ words), Back ranks third or fourth in every sub-corpus, behind Finney by a wide margin (Finney Δ 0.92–0.93 vs Back Δ 1.15–1.24).

The NYT's Cafiero reportedly found Back closest on the whitepaper among 12 suspects; our result does the same (second, Δ 0.98), but also finds Sassaman closer (Δ 0.87, with a multi-author corpus caveat). Cafiero's "Finney nearly tied" is entirely consistent with our result: Finney leads all conversational registers and ranks third on the whitepaper. **Cafiero calling the result "inconclusive" is the expected reading of the full register split — no candidate comes first everywhere.**

## What we cannot evaluate

The NYT's primary evidence is paywalled. We have not read the original article. Secondary summaries may omit or mischaracterize specific methodological details. In particular:

- We cannot reproduce or refute the specific 67-out-of-325 hyphenation-error overlap. Hyphenation-error overlap is not part of standard Burrows' Delta; it's a different stylometric signal. May be valid; may be coincident with Back's large posting volume.
- We cannot evaluate the specific 12-suspect field Cafiero analyzed. Field size affects the probability interpretation of a closest-match finding.
- We cannot assess the "timeline silence" argument (Back going quiet during Satoshi's active period) without verifying it from primary list archives.
- We do not know whether the NYT analysis used a principled function-word list or corpus-derived top-N features. The Aston 2014 study used top-N and produced a topic-contaminated result favoring Szabo; methodology on this point matters.

**Hyphenation-overlap replication attempt:** We ran an independent implementation of the reported hyphenation-error methodology against our existing prose corpora (`src/hyphenation_forensics.py`; results at `results/hyphenation-overlap.json`). The replication found zero overlap for Back because his corpus in this repo is a single paper at 4,496 tokens — roughly 1/30th of the corpus depth required for the statistic to be meaningful. The replication does not reproduce the NYT's "Back 67 of 325" finding, but the failure is entirely a corpus-size problem rather than a methodological challenge: the test cannot produce meaningful results without the same mailing-list archives the NYT used. On the small corpora available here, Sassaman ranks first with one overlap (the `e-mail`/`email` inconsistency), while Back, Dai, Szabo, Finney, and others all register zero. The full analysis, including a discussion of a possible tokenizer artifact in Satoshi's set, is at [`forensics/nyt-hyphenation-replication.md`](nyt-hyphenation-replication.md).

## What this repo's discipline forbids us from doing

Per [issue #1](https://github.com/MatoTeziTanka/satoshi-stylometry/issues/1):

- Wikipedia is not a primary forensic source.
- Trade press (CoinDesk, Unchained, The Defiant, Cointelegraph, Bitcoin.com News, Brave New Coin, BeInCrypto) is not treated as primary forensic evidence.
- We do not name a "real" Satoshi.

The findings in this repo are: different stylometric axes pick different candidates; no single candidate's published corpus reproduces Satoshi's full fingerprint; the timestamp evidence eliminates UK-resident candidates; the MFC code-style fingerprint points to a Windows-C++ background absent from all five named candidates' published code.

**The NYT finding that Back is the closest match on writing style is not incompatible with our result on any single axis. It is in tension with our result on the combined axis picture, and is directly contradicted by the timestamp evidence applied to Back's documented geography.**

## Source citations

**Secondary trade-press summaries (public record of the NYT investigation, NOT primary forensic evidence):**

- Unchained, *NYT Names Adam Back as Satoshi Nakamoto. He Denies It* — `unchainedcrypto.com/nyt-names-adam-back-as-satoshi-nakamoto-he-denies-it-and-the-crypto-community-agrees-with-him-unchained/`
- Brave New Coin, *New York Times Names Adam Back as Bitcoin's Creator — But the Evidence Falls Short* — `bravenewcoin.com/insights/new-york-times-names-adam-back-as-bitcoins-creator-but-the-evidence-falls-short`
- BeInCrypto, *NYT Finally Unmasks the Real Satoshi Nakamoto Behind Bitcoin* — `beincrypto.com/nyt-adam-back-satoshi-nakamoto-investigation/`
- Bitcoin.com News, *NYT Claims Bitcoin Creator Satoshi Nakamoto Is British Cryptographer Adam Back* — `news.bitcoin.com/nyt-claims-bitcoin-creator-satoshi-nakamoto-is-british-cryptographer-adam-back/`

**Our own primary-source analysis (authoritative for claims in this writeup):**

- [`results/results.json`](../results/results.json) — prose Burrows' Delta matrix
- [`results/code-style-features.json`](../results/code-style-features.json) — code-style feature extraction including Hungarian_C rates
- [`README.md`](../README.md) — per-register Δ table and interpretive frames
- [`forensics/uk-descent-eastern-resident-hypothesis.md`](uk-descent-eastern-resident-hypothesis.md) — timestamp falsification, including independent commit-corpus replication
- [`forensics/uk-emigre-east-coast-candidates.md`](uk-emigre-east-coast-candidates.md) — candidate-set negative finding; Adam Back entry
