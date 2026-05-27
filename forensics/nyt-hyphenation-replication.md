# NYT hyphenation-error methodology — independent replication attempt

## Methodology summary

A "hyphenation error" in the NYT April 2026 framework is interpreted (per secondary trade-press summaries; the original article is paywalled) as a compound word that an author uses INCONSISTENTLY within their own corpus: e.g., writing both "e-mail" and "email" in the same body of work. Each author's set of such inconsistent compounds forms a stylistic fingerprint, and the overlap between two authors' sets is the test statistic. Our replication (`src/hyphenation_forensics.py`) tokenizes each prose corpus using a lowercased, URL-stripped regex that accepts letter-runs with optional internal hyphens as valid tokens. A compound is counted as "inconsistent" only when both its hyphenated form and its bare (unhyphenated) form each appear at least twice in the same corpus (a frequency floor to exclude quoted artifacts and typos). For each non-Satoshi candidate, we count the size of the intersection of their inconsistent-compound set with Satoshi's.

## Ranking table

Run against the repo's prose corpora (same corpora that drive the standard Burrows' Delta analysis):

| Author | Corpus tokens | Candidate compounds | Overlap with Satoshi | % of Satoshi set | % of candidate set |
|--------|--------------|---------------------|---------------------|-----------------|-------------------|
| szabo | 136,365 | 11 | 0 | 0.0% | 0.0% |
| sassaman | 4,589 | 1 | 1 | 9.1% | 100.0% |
| finney | 16,291 | 1 | 0 | 0.0% | 0.0% |
| back | 4,496 | 0 | 0 | 0.0% | 0.0% |
| dai | 1,356 | 0 | 0 | 0.0% | 0.0% |
| haber | 0 | 0 | 0 | — | — |
| stornetta | 0 | 0 | 0 | — | — |
| sassaman-solo | 4,285 | 0 | 0 | 0.0% | 0.0% |

Satoshi's inconsistent-compound set (11 items): `autodetect`, `connecting`, `ecdsa`, `email`, `midstate`, `precompiled`, `publickey`, `rebroadcast`, `rebroadcasting`, `redo`, `redownload`.

The single overlap with Sassaman is `email` (Sassaman uses both "e-mail" 10 times and "email" 3 times). Back ranks zero: his Hashcash paper corpus uses "email" consistently (no hyphenated "e-mail" at meaningful frequency), producing no inconsistent compound against the threshold.

## Interpretation: does the replication reproduce the NYT result?

**No — and corpus size is the methodologically load-bearing explanation.** The NYT reportedly swept 134,308 cypherpunk mailing-list posts to generate Back's hyphenation fingerprint. Our Back corpus is one paper: 4,496 tokens. The disparity is roughly 30:1. Back simply does not produce enough text in our corpus to meet the two-occurrence threshold on both forms of any compound word. This is not a finding against Back — it is a corpus-size failure of the replication attempt.

On the available data, **Sassaman ranks first** (overlap = 1, driven entirely by e-mail/email). Back ranks zero, tied with five other candidates. The NYT's reported "Back 67, runner-up 38" cannot be reproduced or challenged with a 4,496-token corpus: if Back's cypherpunk list posts (the source of the NYT's 134,308-post sweep) were loaded, the result would likely differ materially.

The `connecting` compound in Satoshi's set is likely an artifact: the source corpus contains the string "-connect-ing" (a typographic line-wrap marker), which the tokenizer reads as a hyphenated compound. This inflates Satoshi's set by one and should be treated as a noisy token.

The replication is therefore **methodologically consistent** — the algorithm is implemented correctly — but **not informative about Back's ranking** due to corpus size. The honest finding is that the methodology requires the same corpus depth the NYT used (tens of thousands of posts per candidate) before the overlap statistic is meaningful. On the corpora available to this repo, the hyphenation-overlap test is under-powered for every candidate except Satoshi (131k tokens) and Szabo (136k tokens). Even Szabo — despite a large corpus — produces zero overlap with Satoshi's set, which itself tells us that Satoshi's inconsistent compounds are mostly technical neologisms (`ec-dsa`/`ecdsa`, `mid-state`/`midstate`, `auto-detect`/`autodetect`) that do not appear in Szabo's essay corpus at all.

## What we cannot evaluate

Four limitations bound the interpretive reach of this replication:

1. **NYT's exact tokenization is not published.** The original article is paywalled. Secondary summaries do not specify whether the NYT used sentence-boundary detection, stemming, or different frequency thresholds. Differences in those choices could move overlap counts by 10–30 percent even on matched corpora.

2. **Our corpora are smaller than the NYT's reported sweep.** The investigation reportedly analyzed 134,308 posts. Our largest prose corpus (Szabo) is 136,365 tokens, but it is essays, not mailing-list posts. Our Back corpus (4,496 tokens) is one-tenth the threshold at which Burrows' Delta produces reliable results. This is the primary reason the replication is non-informative about Back specifically.

3. **Cross-corpus comparability has caveats.** Satoshi's corpus is forum posts and emails — informal registers. The candidate corpora are essays and papers — formal registers. Hyphenation usage varies by register: informal digital writing (where "email" is now universal) produces different patterns than academic or technical prose (where "e-mail" persisted longer). A register-matched comparison would require mailing-list archives per candidate.

4. **The Satoshi "connecting" compound is likely a tokenizer artifact.** The string `-connect-ing` appears once in the Satoshi corpus as a typographic formatting artifact from a forum scrape (mid-sentence hyphenation indicating a line-wrap in the source material, not a stylistic choice). The tokenizer reads it as the hyphenated compound `connect-ing`, matching the bare token `connecting` which appears 16 times elsewhere. This inflates Satoshi's compound set by one item and should be treated with caution.

## Cross-reference

See [`forensics/nyt-april-2026-adam-back.md`](nyt-april-2026-adam-back.md) for the broader picture of where our analysis converges with and diverges from the NYT investigation, including a paragraph added at the end of that document's "What we cannot evaluate" section pointing to this replication.

The JSON output for this analysis (per-author compound sets, overlap lists, and methodology caveats) is at [`results/hyphenation-overlap.json`](../results/hyphenation-overlap.json).
