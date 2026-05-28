# Craig Wright cross-axis test — adjudicated non-Satoshi added as quantitative reference

## What was tested

Craig Wright publicly claimed to be Satoshi Nakamoto for approximately eight years (2016–2024). The claim was rejected by UK courts in **COPA v Wright [2024] EWHC 1198 (Ch)** (Mellor J, May 2024), which found Wright to have committed forgery and given false evidence. Wright was subsequently enjoined from further "I am Satoshi" litigation in the UK without permission.

The COPA judgment is legal-process evidence; this repo's discipline (issue [#1](https://github.com/MatoTeziTanka/satoshi-stylometry/issues/1)) operates on quantitative stylometric evidence. Wright is a **legitimate reference-class candidate** for stylometric testing — an adjudicated non-Satoshi against whom we can verify that the repo's cross-axis filter produces the expected "not Satoshi" result. If the filter does NOT produce that result, the methodology is broken.

This test was added 2026-05-27.

## Sources

### Prose corpus (~20,000 words)

Five sole-authored Wright texts, mixed academic/blog register:

| File | Words | Source | Register |
|------|-------|--------|----------|
| `arxiv-2506-20965-rational-miner.txt` | ~7,500 | [arXiv 2506.20965](https://arxiv.org/abs/2506.20965) "Rational Miner Behaviour" | Academic |
| `arxiv-2506-22497-peer-review.txt` | ~9,000 | [arXiv 2506.22497](https://arxiv.org/abs/2506.22497) "Peer Review as Structured Commentary" | Academic |
| `arxiv-2506-01384-spv-security.txt` | ~1,400 | [arXiv 2506.01384](https://arxiv.org/abs/2506.01384) "Formal Security Analysis of SPV Clients" | Academic (lower fidelity — HTML extraction caveat) |
| `coingeek-journey-to-scaling.txt` | ~1,800 | [CoinGeek "The Journey to Scaling Bitcoin"](https://coingeek.com/the-journey-to-scaling-bitcoin/) | Conversational blog |
| `coingeek-on-stewardship.txt` | ~280 | [CoinGeek "On Stewardship"](https://coingeek.com/on-stewardship/) | Conversational blog |

Provenance + sole-author verification at [`corpus/wright/SOURCE.md`](../corpus/wright/SOURCE.md).

**Temporal caveat:** all five texts date from 2024–2025; Satoshi's writings date from 2008–2009. The 15–16 year gap is the largest temporal stretch of any candidate in the corpus. Authorial style can drift across that interval; the Wright result should be read with this in mind. The corpus nevertheless establishes Wright's 2024–2025 stylistic baseline as a known non-Satoshi.

### Code corpus (Bitcoin SV v1.0.0)

Bitcoin SV is Wright's "Satoshi's Vision" fork starting from the 2018 BCH→BSV fork point. Provenance + the load-bearing **inheritance confound caveat** at [`code-corpus/wright-bsv/SOURCE.md`](../code-corpus/wright-bsv/SOURCE.md).

- Repo: `bitcoin-sv/bitcoin-sv` on GitHub
- Tag: `v1.0.0` at commit `7fd177c7c443ff7723d88c5465fbf39285388e30` (2020-01-15)
- 568 source files (18 .c, 255 .cpp, 295 .h), 159,921 LOC

**Wright's personal commit count in BSV: ZERO** across all author-name variants (`Craig Wright`, `craig wright`, `c.wright`, `S. Wright`, `wright`). Wright is the figurehead of nChain (the BSV development sponsor); commits are by nChain engineers and the broader BSV team. The codebase contains 245 Satoshi-authored commits plus the entire Bitcoin Core development lineage (15,710 commits, 610 unique author handles).

## Result — prose axis

### Aggregate Satoshi (function-word Δ)

| Rank | Author | Δ |
|------|--------|---|
| 1 | finney | 0.9142 |
| 2 | szabo | 1.1836 |
| 3 | sassaman | 1.2839 |
| 4 | back | 1.2873 |
| 5 | sassaman-solo | 1.3852 |
| 6 | dai | 1.4830 |
| **7 (LAST)** | **wright** | **1.5481** |

### Per-register

| Register | Wright rank | Wright Δ | Winner |
|----------|-------------|----------|--------|
| forum_posts | 7 of 7 (LAST) | 1.4579 | finney 0.87 |
| p2pfoundation | 7 of 7 (LAST) | 1.4164 | sassaman 1.02 |
| whitepaper | 7 of 7 (LAST) | 1.2364 | sassaman 0.83 |
| whitepaper (top-150 topic-contaminated) | 6 of 7 | 1.2204 | sassaman-solo 1.05 |

**Wright is last in every principled-methodology register against every Satoshi sub-corpus.** Under topic-contaminated features Wright rises one rank (6 of 7) but is still below mid-pack.

### Interpretation

This is the largest single-candidate Δ in the entire corpus. Wright is stylometrically further from Satoshi than any of the cypherpunk candidates — including Dai whose b-money corpus is tiny (1,356 words) and Szabo whose subject matter overlaps with Bitcoin substantially.

**The prose axis quantitatively confirms COPA v Wright [2024]:** Wright is not Satoshi by stylometric measure. The result is robust across all four Satoshi prose registers and survives the topic-contamination diagnostic.

The temporal gap (Wright 2024–2025 vs Satoshi 2008–2009) is a confounding variable, but its effect is to *narrow* the apparent distance (authors drift toward common late-2010s/2020s academic conventions over time). The observed Wright Δ is therefore likely an **under-estimate** of the genuine 2008-vs-2008 Wright-vs-Satoshi distance.

## Result — code axis (load-bearing inheritance confound)

### Composite MFC z-score, full table

| Author | Hungarian_C | Space ratio | Line cmts/KLOC | Composite z |
|--------|-------------|-------------|----------------|-------------|
| satoshi-nov2008 | 9.6% | 100% | 136.5 | **+4.98** |
| satoshi-v0.1.0 | 6.4% | 100% | 105.6 | **+3.39** |
| satoshi (v0.1.3) | 6.4% | 100% | 105.1 | **+3.37** |
| **wright-bsv** | **4.8%** | **99.7%** | **101.9** | **+2.83** ⚠️ |
| sassaman | 0.2% | 77% | 0.1 | −1.22 |
| pgp-6.5 | 0.8% | 29% | 45.4 | −1.30 |
| dai | 0.1% | 5% | 52.3 | −1.95 |
| truecrypt | 0.1% | 9% | 34.6 | −2.21 |
| back | 0.2% | 32% | 0.2 | −2.31 |
| e4m | 0.1% | 13% | 1.4 | −2.79 |
| finney | 0.1% | 13% | 1.2 | −2.80 |

### What the table appears to say at face value

Wright-BSV is the **only non-Satoshi codebase with a strongly positive composite z-score**. The next non-Satoshi candidate (Sassaman) is at −1.22 — a 4-point z-score gap. At face value, Wright-BSV "looks like Satoshi" on every measured code-style axis (Hungarian_C 4.8% vs Satoshi 6.4%; space-indent 99.7% vs 100%; line comments 101.9 vs 105.1).

### What is actually going on (the confound)

**Bitcoin SV v1.0.0 literally contains Satoshi's original code.** Per [`code-corpus/wright-bsv/SOURCE.md`](../code-corpus/wright-bsv/SOURCE.md):

- 245 commits authored by `s_nakamoto` (Satoshi's SourceForge handle from the SVN-to-git import)
- The entire Bitcoin Core development lineage 2010–2017: Wladimir van der Laan 4,371 commits, Pieter Wuille 1,271, Gavin Andresen 1,101, etc.
- 610 unique author handles total across 15,710 commits
- **Wright's personal commit count: ZERO**

Bitcoin SV is a fork of Bitcoin Core (via the August 2017 BCH fork and the November 2018 BSV fork). It carries forward the Bitcoin Core house style — which IS Satoshi's house style for the early-2009 core files and IS the Bitcoin Core team's style for the 2010–2017 modifications. The composite z = +2.83 result is therefore evidence of **inheritance from Satoshi's original codebase**, not evidence of Wright's authorship.

The result is a textbook case of a confounded stylometric test: the corpus boundary (everything tagged `v1.0.0` in BSV) does not match the analytical claim (Wright's house style). The clean test would require a **diff-only corpus** — BSV commits added since the 2018 BCH→BSV fork point, excluding all Satoshi/Bitcoin Core inheritance.

### The right next step (diff-only Wright corpus, not done here)

The honest read of this analysis is that **the code axis cannot rule Wright in or out** given the available codebase. The snapshot-style code-axis test is *structurally unable* to discriminate Wright's house style from Satoshi's inherited house style. To get a clean Wright-house-style code signal, future work would need to:

1. Identify the 2018 BCH→BSV fork commit (probably tag `v0.1.0` or similar in the BSV repo).
2. Extract only commits authored *after* that fork point AND authored by nChain engineers (excluding any remaining Satoshi/Core-lineage cherry-picks).
3. Build a corpus from those commits' net diff (added lines, not the full inherited base).
4. Run the MFC composite on that diff-only corpus.

This is non-trivial and was out of scope for this 2026-05-27 fan-out. Flagged as a methodologically warranted follow-up.

## Cross-axis ruling on Wright

| Axis | Wright result | Reading |
|------|---------------|---------|
| Prose function-word Δ (aggregate) | Δ=1.55, rank 7 of 7 (LAST) | **Quantitatively rules Wright OUT** |
| Prose function-word Δ (whitepaper) | Δ=1.24, rank 7 of 7 (LAST) | **Quantitatively rules Wright OUT** |
| Prose function-word Δ (commit messages) | Not in this analysis; Wright has no 2008–2009 commit messages in the corpus | n/a |
| Prose top-150 (topic-contaminated) | Δ=1.22, rank 6 of 7 | **Wright stays bottom-half even under his most favorable methodology** |
| Code identifier Δ | Δ=0.91, rank 4 of 8 non-Satoshi candidates | Misleading — inheritance-confounded (BSV contains Satoshi's code) |
| MFC composite z-score | +2.83 (4th overall, only behind 3 Satoshi corpora) | Misleading — inheritance-confounded (see above) |
| Hyphenation overlap | Not run on Wright in this analysis (Wright corpus too small for the methodology and from a different era) | n/a |
| Timestamp distribution | Not testable — Wright's 2024–2025 corpus is not in the Bitcoin-mining era | n/a |

**Cross-axis verdict: WRIGHT IS NOT SATOSHI**, confirmed quantitatively by the prose axis (last in every register) and consistent with the COPA legal judgment.

The code-axis Wright-BSV result is **uninformative as positive evidence** because the BSV codebase contains Satoshi's original code by direct inheritance. It is **not evidence that Wright is Satoshi**; it is evidence that BSV's snapshot includes Satoshi's snapshot. Anyone forking Bitcoin Core would produce a similar result.

## Why this matters as a stress test

A stylometric methodology that produced "Wright IS close to Satoshi" on the prose axis would be a failed methodology — COPA v Wright [2024] established Wright is not Satoshi through forgery findings, expert evidence, and document discovery beyond what stylometry can deliver. The repo's prose methodology produces the correct quantitative ruling (Wright last) against an external ground truth.

The code-axis result is more interesting as a methodological lesson: **forked codebases pollute stylometric signal by direct inheritance.** This affects any future test involving a Bitcoin-Core-lineage codebase (BCH, BSV, Bitcoin XT, Bitcoin Knots, Bitcoin ABC). The honest reading is "the snapshot doesn't discriminate; the diff would."

## Limitations

1. **Temporal gap.** Wright corpus is 2024–2025; Satoshi is 2008–2009. A 15-year gap. Authorial style drifts over time; the observed Wright Δ is likely an under-estimate of the genuine 2008-vs-2008 distance.
2. **Mixed register.** Wright corpus pools academic preprints with conversational blog posts. The repo handles this by per-register Satoshi sub-corpus analysis (Wright Δ is last in every register, so the pooling doesn't change the conclusion).
3. **Sole-authorship caveat for arXiv preprints.** Wright's arXiv preprints are formally bylined sole-author, but ghostwriter / editor involvement during his nChain tenure (2017–2024) is documented in some contemporaneous press. The June 2025 arXiv preprints post-date COPA and the winding down of his formal nChain role, making them more likely sole-authored in practice. The CoinGeek blog posts are first-person narrative and more reliably sole-authored.
4. **No code diff-only analysis.** The BSV snapshot test is inheritance-confounded; the diff-only follow-up was out of scope.
5. **Wright corpus excludes legal-process material.** COPA witness statements + cross-examination transcripts would be the most relevant Satoshi-claim-era Wright prose but are paywalled or under court protection. The 2024–2025 arXiv + CoinGeek material is the best accessible alternative.

## References

- COPA v Wright [2024] EWHC 1198 (Ch), Mellor J — judicial finding that Wright is not Satoshi
- [`corpus/wright/SOURCE.md`](../corpus/wright/SOURCE.md) — prose corpus provenance
- [`code-corpus/wright-bsv/SOURCE.md`](../code-corpus/wright-bsv/SOURCE.md) — BSV codebase provenance including inheritance caveat
- [`results/results.json`](../results/results.json) — prose Δ matrix including Wright row
- [`results/code-style-features.json`](../results/code-style-features.json) — code feature matrix including wright-bsv row
- [`forensics/hidden-artifacts-survey.md`](hidden-artifacts-survey.md) — four-axis Windows + locale + timezone consensus from the same 2026-05-27 fan-out session
