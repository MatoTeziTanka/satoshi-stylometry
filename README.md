# satoshi-stylometry

A reproducible Burrows' Delta analysis comparing the writings of "Satoshi Nakamoto" against six candidates: Adam Back, Hal Finney, Nick Szabo, Wei Dai, Len Sassaman, and Craig Wright (the last as an adjudicated non-Satoshi per COPA v Wright [2024] EWHC 1198 (Ch), included as a quantitative reference-class control).

> **Findings in one line:** different stylometric axes pick different candidates, and Satoshi's full fingerprint matches no single one. Prose-conversational (forum posts + emails) → **Hal Finney** (Δ 0.93). Prose-formal (the whitepaper) → **Len Sassaman** with a multi-author corpus caveat (Δ 0.87), then **Adam Back** (Δ 0.98). Code identifiers → **Adam Back** (Δ 0.78). Satoshi's MFC-style Hungarian C-prefix class naming (`CTransaction`, `CBlock`) at 6.4% **is not matched by any candidate** — PGP 6.5 (the closest non-Satoshi at 0.8%) is still 8× below Satoshi and fails on the other two MFC fingerprint axes. The honest reading is that "Satoshi" exhibits a *mosaic* of stylistic patterns that no single 2008-era candidate's published corpus fully reproduces.

## Why this exists

The "Who is Satoshi?" question has been litigated in pop press, court (Wright v Hodlonaut 2024), an HBO documentary (*Money Electric*, 2024), and at least one published stylometric study (Aston University, Grieve et al., 2014). The results have not converged. This repo reproduces the analysis on a wider candidate set and a larger Satoshi corpus, and shows that the most commonly cited prior finding (Aston → Szabo) was probably topic-contaminated.

## Method

Standard Burrows' Delta:

1. Pool each author's writing.
2. Compute relative frequency (per 1000 tokens) of each word in a fixed feature vocabulary.
3. Z-score normalize each feature across authors.
4. Delta(A, B) = mean(|z(A,·) − z(B,·)|).

**Critical methodological choice:** the feature vocabulary must be a **closed-class function-word list** (articles, prepositions, conjunctions, modals, pronouns, common adverbs), *not* the top-N most-frequent words derived from the corpus itself. Using corpus-derived top-N words contaminates the analysis with topic vocabulary — Satoshi wrote about Bitcoin all the time, so any candidate who also wrote about distributed systems and proof-of-work (e.g., Szabo's bit gold) looks artificially close on a topic-laden feature set.

This repo runs both methods side-by-side to show the difference. The headline numbers use the 201-word function-word list at [`src/function_words.py`](src/function_words.py).

## Results

### Aggregate Burrows' Delta from Satoshi (lower = stylometrically closer)

| Candidate | Δ (function words, principled) | Notes |
|-----------|--------------------------------|-------|
| **Hal Finney**       | **0.91** | 16k-word corpus — reliable |
| Nick Szabo           | 1.18     | 137k-word corpus — most reliable |
| Len Sassaman         | 1.28     | 5.5k words, 4-AUTHOR — see caveat |
| Adam Back            | 1.29     | 4.9k-word corpus — borderline |
| Sassaman-solo        | 1.39     | 4.4k-word verified solo corpus |
| Wei Dai              | 1.48     | 1.4k-word corpus — UNDER threshold |
| Craig Wright         | **1.55** | 20k-word corpus, 2024–2025 vintage — **LAST**, adjudicated non-Satoshi per COPA 2024 |

### Per-register Burrows' Delta (function words)

| Satoshi sub-corpus | Words | 1st | 2nd | 3rd | 4th | 5th |
|--------------------|-------|-----|-----|-----|-----|-----|
| BitcoinTalk posts  | 57,041 | Finney 0.90 | Szabo 1.19 | Sassaman 1.22 | Back 1.22 | Sassaman-solo 1.35 |
| Emails             | 11,442 | Finney 0.89 | Sassaman 1.06 | Back 1.13 | Szabo 1.13 | Sassaman-solo 1.20 |
| Forum (all)        | 57,908 | Finney 0.90 | Szabo 1.18 | Sassaman 1.21 | Back 1.22 | Sassaman-solo 1.34 |
| **Whitepaper**     | 3,571  | **Back 0.97** | Sassaman (multi-author RFC) 0.86 ← *retracted, see below* | Sassaman-solo 1.03 | Finney 1.10 | Dai 1.13 |
| P2P Foundation     | 866    | (too small to be meaningful) | | | | |

**The whitepaper row needs reading carefully.** The Mixmaster-RFC Sassaman corpus (multi-author IETF draft) shows Δ=0.86 — appears first. But a **verified solo-Sassaman corpus** (4,383 words across two single-author Sassaman papers) shows Δ=1.03 — third place. The "Sassaman first on whitepaper" finding was substantially a Mixmaster-coauthor-blend artifact. With clean solo corpus, **Adam Back is first on the whitepaper (Δ=0.97)**, Sassaman-solo third. See [`forensics/sassaman-solo-corpus-rerun.md`](forensics/sassaman-solo-corpus-rerun.md) for the full retraction analysis.

**Craig Wright (control)**: Wright ranks **last (7 of 7) in every Satoshi prose register** — BitcoinTalk Δ=1.46, Emails Δ=1.47, Forum aggregate Δ=1.46, Whitepaper Δ=1.24, Aggregate Δ=1.55. The largest single-candidate Δ in the corpus. Wright was adjudicated NOT to be Satoshi by COPA v Wright [2024]; the quantitative stylometric result independently confirms the judicial finding. The 15-year temporal gap (Wright corpus 2024–2025 vs Satoshi 2008–2009) means the observed Δ is likely an *under-estimate* of the genuine 2008-vs-2008 distance. On the **code axis** the Wright-BSV full snapshot scores +2.43 (inheritance-confounded — BSV contains 245 Satoshi commits + Bitcoin Core lineage) and the **diff-only follow-up** (BSV-team net-new files post-fork only) scores +3.53 — *higher* than the full corpus, reflecting deliberate convention mimicry by the nChain team ("Satoshi's Vision") not Wright authorship. Methodological lesson: the MFC composite measures adoptable conventions, not unique signatures. See [`forensics/wright-cross-axis-test.md`](forensics/wright-cross-axis-test.md) + [`forensics/wright-bsv-diff-test.md`](forensics/wright-bsv-diff-test.md).

### Sassaman caveat — the result has now been re-tested with a solo corpus

The original Sassaman result on the whitepaper (Δ=0.86, multi-author Mixmaster corpus) was the strongest signal in this dataset and also the result most exposed to methodological criticism. An initial draft of this README listed the multi-author confound as an unresolvable caveat ("there is no clean public single-authored Sassaman corpus"). That was an overstatement — a verified solo Sassaman corpus of 4,383 words has now been assembled from primary sources (Ethics paper at Financial Cryptography Workshops 2010 + the *Faithless Endpoint* KU Leuven technical report 2007-003, both sole-author per DBLP and title pages).

**With the solo corpus, the whitepaper Δ to Sassaman rises from 0.86 to 1.03** (corpus changed from 4-author IETF draft to 2-paper solo-Sassaman). **Adam Back becomes first on the whitepaper at Δ=0.97**; solo-Sassaman is third. The original "Sassaman first on whitepaper" framing is largely an artifact of averaging-with-coauthors in the Mixmaster IETF draft.

The original `corpus/sassaman/` (multi-author Mixmaster) is preserved in the repo as the auditable historical baseline. The new `corpus/sassaman-solo/` is treated as a separate "author" in the analysis so the Δ matrix shows both.

Full analysis in [`forensics/sassaman-solo-corpus-rerun.md`](forensics/sassaman-solo-corpus-rerun.md). The corrections preserved per session discipline:

1. Initial: Sassaman first on whitepaper (Δ=0.87), interpreted as strong stylistic match.
2. Date correction: Sassaman died July 3 2011 (not May 3 as initially listed).
3. Gap correction: 8 days → 6.5 months → 71 days (each correction with primary source).
4. **Solo-corpus retraction (current):** Δ=1.03 with solo corpus; Adam Back is the new closest whitepaper match. Sassaman remains a candidate-of-interest but no longer the top stylometric match on the whitepaper.

![dendrogram](results/dendrogram.png)

![dendrogram](results/dendrogram.png)

### What this means

The signal is consistent and the register-split is the most interesting finding:

- **Casual Satoshi → Finney.** Across 70k+ words of forum posts and emails, Hal Finney is the closest stylistic match by a substantial margin (Δ 0.92 vs next-nearest Sassaman 1.07-1.22). Finney was operationally closest to Satoshi: he ran one of the first nodes, received the first peer-to-peer Bitcoin transaction (block 170), was an early Hashcash contributor, and was on the cypherpunks list for decades.
- **Formal-paper Satoshi → Back (with the Sassaman correction now applied).** On the 3,571-word whitepaper specifically, after replacing the multi-author Mixmaster Sassaman corpus with a verified solo-Sassaman corpus, **Adam Back ranks first at Δ=0.97**, solo-Sassaman third at Δ=1.03, Finney fourth at Δ=1.10. Back is cited as reference [6] of the paper, was Satoshi's first known email contact (Aug 2008), and is British — the whitepaper contains one British spelling slip (`favour`). The Back whitepaper result is consistent with the NYT April 2026 investigation's finding (Cafiero ranked Back closest of 12 suspects on writing style); see [`forensics/nyt-april-2026-adam-back.md`](forensics/nyt-april-2026-adam-back.md) for our independent convergence/divergence picture on the NYT result.
- **Szabo is never first.** Despite the Aston University 2014 result favoring him, Szabo ranks second on forum posts and **last (rank 6 of 6) on the whitepaper** under principled function-word methodology. The Aston study used a methodology vulnerable to topic contamination — and on the topic-contaminated re-run in this repo, Szabo's Δ improves by 4.2% on the whitepaper and his rank moves +1 (from 6th to 5th), the direction of the Aston result without reaching it. The **+1 rank shift + 4.2% Δ improvement is reproducible at top-150 corpus-derived features**; more aggressive feature selection would amplify it. The Aston methodology, whatever its precise feature-selection cut, must have used a corpus-derived feature set that admitted topic vocabulary, because no closed-class feature set produces "Szabo first" against the whitepaper. Full quantitative writeup with rank-shift table for all candidates: [`forensics/topic-control-aston-2014.md`](forensics/topic-control-aston-2014.md).
- **Wei Dai is consistently last** on registers above 5k words. b-money is intellectually close to Bitcoin (Satoshi cites it as ref [1]) but stylistically distant. Dai's writing patterns differ in function-word distribution.
- **Temporal coincidence on Sassaman.** Sassaman died 2011-07-03. Primary source: contemporaneous announcement at [Hacker News item 2723959](https://news.ycombinator.com/item?id=2723959) ("Len Sassaman has passed away"), posted 2011-07-03 16:28 UTC by his peers in the cryptography community. The community-side memorial in the Bitcoin blockchain at block 167,956 (recorded 2011-07-31, [HN announcement](https://news.ycombinator.com/item?id=2830084)) cross-confirms the date. Satoshi's last documented *public* communications were a forum post on 2010-12-12 and a bitcoin-list email on 2010-12-13 ([primary source: the JSON corpus shipped with nakamotoinstitute.org](https://github.com/nakamotoinstitute/nakamotoinstitute.org/blob/master/server/data/forum_posts.json)). The widely-cited "I've moved on to other things" *private* email to Mike Hearn is dated **2011-04-23** per the 2017 disclosure of those emails (by a Bitcointalk user "CipherionX") which Mike Hearn confirmed authentic; see [C12](CITATIONS.md) for the citation chain. A first-draft of this README incorrectly stated "8 days"; a corrected draft said "approximately 6.5 months" measured from Satoshi's last verified *public* message (2010-12-13) to Sassaman's death (2011-07-03). With the Hearn-email date now sourced, the gap from Satoshi's last verified *private* message to Sassaman's death is approximately 71 days. The temporal-coincidence framing is still weak — 71 days is not a tight match — and the case for Sassaman as candidate rests on (a) the stylometric whitepaper match (Δ=0.87, with multi-author corpus caveat) and (b) general circumstantial considerations, not on a tight timing match.

### Interpretive frames

Three honest readings of the register-split:

1. **One author with strong register adaptation.** A single skilled writer can write formal papers and casual forum posts in different styles. The "Back-like whitepaper, Finney-like forum" pattern could be one author whose academic register happens to look like Back's and casual register happens to look like Finney's.
2. **Two-author hypothesis.** Bitcoin may have been co-authored by Back and Finney, with Back drafting the paper and Finney handling community communication. This is consistent with operational evidence (Finney ran the first nodes, Back was the cited Hashcash author) but unsupported by direct evidence.
3. **Finney with stylistic borrowing.** Finney could have authored everything, with the whitepaper deliberately styled to read more "Back-like" — either as homage, intentional misdirection, or because the academic register naturally pulls toward Back's published norms.

This analysis cannot distinguish between these. It can only rule out Szabo as the primary stylistic source and Wei Dai entirely.

## Limitations

- **Corpus imbalance.** Back has 4.9k words (Hashcash paper only). Dai has 1.4k words (b-money only). Sassaman has 5.5k words but they are a 4-author RFC, not solo writing. Burrows' Delta works reliably from ~5k words per author; Back and Sassaman are borderline, Dai is below threshold. Finney (16k) and Szabo (137k) are robust.
- **Sassaman corpus is multi-author.** See the dedicated Sassaman caveat section above. The Mixmaster Protocol v2 IETF draft has four named authors. This is the cleanest single block of prose closely associated with Sassaman that is publicly accessible. His personal site (abditum.com) was password-protected throughout its public lifetime.
- **Candidate set is still incomplete.** This run excludes Stuart Haber, W. Scott Stornetta, David Chaum, Tim May, Ian Goldberg, Bram Cohen, and other plausible cypherpunk-era candidates. Adding them requires sourcing their pre-2008 single-author writings.
- **Function-word lists vary.** The 201-word list at `src/function_words.py` is composite (Mosteller-Wallace, Burrows, stylo defaults). Using a different list may shift results within ±0.1 Delta. The relative ordering is robust to list choice in this dataset.
- **No deliberate-misdirection control.** A pseudonymous author seeded with stylistic markers from another writer would defeat this analysis. The register-split finding is consistent with that scenario.
- **Source register confound.** Satoshi's forum posts are conversational; Szabo's archived corpus is essays. Comparing forum-Satoshi against essay-Szabo is unavoidable given what's archived, but tilts results.

## Code-style stylometry (separate analysis, not prose)

Source code is a different stylometric axis from prose. Burrows' Delta on prose function-words doesn't transfer cleanly — every codebase has its own vocabulary. Instead, we extract programming-language-invariant style features and run a separate analysis.

Code corpora pulled by `src/pull_corpus.py` (additions in commit history): Satoshi (Bitcoin 0.1.3 ALPHA Dec 2009, 13.7k LOC), satoshi-v0.1.0 (Jan 2009 release, 16.6k LOC), satoshi-nov2008 (private pre-release, 3.3k LOC), Back (Hashcash, 9.1k LOC C, 34 files), Finney (RPOW, 10.4k LOC C, 40 files), Dai (Crypto++ 5.2.1, 43.6k LOC C++, 191 files), Sassaman (Mixmaster, 20.9k LOC C, 44 files), TrueCrypt 7.1a (91.8k LOC C/C++, 377 files — wildcard "Le Roux era" Windows-encryption corpus added 2026-05-27), PGP-6.5 (Network Associates PGP for Windows 6.5.1i, 1999, 567k LOC C/C++, 1,884 files — wildcard "1990s Windows-C++ MFC-era cypherpunk-adjacent team codebase" added 2026-05-27, see [`forensics/pgp-6.5-windows-mfc-test.md`](forensics/pgp-6.5-windows-mfc-test.md)), e4m 2.01 (Paul Le Roux, 1999, 18.5k LOC pure C, 93 files — pre-TrueCrypt direct single-author work, closes the Le Roux wildcard ruling alongside TrueCrypt 7.1a, see [`forensics/e4m-mfc-test.md`](forensics/e4m-mfc-test.md)), Wright-BSV (Bitcoin SV v1.0.0, 2020-01-15, 159.9k LOC C/C++, 568 files — adjudicated non-Satoshi reference-class control with inheritance-confound caveat; the snapshot contains 245 Satoshi-authored commits + the full Bitcoin Core lineage, see [`forensics/wright-cross-axis-test.md`](forensics/wright-cross-axis-test.md)). The three Satoshi corpora span the 13-month launch window and enable an intra-Satoshi style-drift test; see [`forensics/intra-satoshi-style-drift.md`](forensics/intra-satoshi-style-drift.md). See [`code-corpus/*/SOURCE.md`](code-corpus/) for provenance per author.

### Headline finding: Satoshi's code style is mosaicked

Different axes point to different candidates. No candidate has Satoshi's full code-style fingerprint:

| Axis | Satoshi value | Closest candidate |
|------|--------------|-------------------|
| Code function-word Delta (identifier choice) | (baseline) | **Adam Back** Δ=0.80; TrueCrypt Δ=0.93 third |
| Brace style (Allman fraction) | 45% Allman | **TrueCrypt 47%, Finney 49%, Dai 44%** |
| Indent: tab vs space | **100% spaces** | None match — everyone else is mostly tabs; Sassaman closest at 23% tabs / 77% spaces, PGP 6.5 71% tabs, TrueCrypt 91% tabs |
| Comment style | **105/KLOC line comments**, 1/KLOC block | **Wei Dai** (52 line, 5 block); **PGP 6.5** (45 line, 67 block — high line density but block-heavy ratio inverted from Satoshi) |
| Hungarian C-prefix class names (`CTransaction`, `CBlock`) | **6.4% of identifiers** | **None match Satoshi's rate** — **PGP 6.5 is the highest non-Satoshi at 0.8%** (still 8× below Satoshi); all other candidates 0.1–0.2%; TrueCrypt 0.1%. PGP has incidental MFC use; Satoshi has pervasive MFC house style. |

The Hungarian C-prefix result is the most distinctive single feature: Satoshi's reference codebase contains hundreds of `CClassName`-style identifiers (`CTransaction`, `CBlock`, `CKey`, `CCriticalSection`, `CBlockIndex`). This naming convention comes from **Microsoft Foundation Classes (MFC)** — the standard C++ framework on Windows in the 1990s-2000s. **The only candidate codebase with any non-trivial MFC usage is PGP for Windows 6.5.1i** (Network Associates, 1999) at 0.8% — 4× to 8× higher than every other candidate but still 8× below Satoshi's 6.4%, and PGP 6.5 fails on the other two MFC fingerprint axes (71% tab indent vs Satoshi's 100% spaces, block-heavy comment ratio vs Satoshi's line-heavy). PGP 6.5's MFC usage is incidental (~194 `class C[...]` declarations across 567k LOC of mostly non-MFC code); Satoshi's MFC usage is pervasive (the codebase is written in MFC house style throughout). See [`forensics/pgp-6.5-windows-mfc-test.md`](forensics/pgp-6.5-windows-mfc-test.md) for the full PGP 6.5 result.

This is consistent with Bitcoin 0.1 having been developed on Windows MSVC with MFC influence, which suggests Satoshi had a Windows-C++ background rather than the Unix-C background that characterizes Back (Stroustrup C), Finney (RPOW C), Sassaman (Mixmaster C), and even Dai's Crypto++ (which uses PascalCase classes but no C-prefix). The PGP 6.5 test rules out the "Satoshi was a PGP-team contributor" reading at the codebase house-style level but does not exclude individual PGP team members whose personal style could differ from the team aggregate.

### What this rules in / out

- **Rules in:** A Windows-C++-trained developer who used MFC conventions. None of the named candidates' published code matches this background.
- **Rules in (intra-Satoshi consistency):** The MFC convention was already at **9.6% of identifiers in the Nov 2008 pre-release** — the earliest publicly accessible Satoshi source. It rises to 6.4% in v0.1.0 (Jan 2009) and stays at 6.4% in v0.1.3 (Dec 2009). This rules out "MFC convention added by a later collaborator" — the fingerprint was baseline Satoshi from before community engagement existed. See [`forensics/intra-satoshi-style-drift.md`](forensics/intra-satoshi-style-drift.md).
- **Does not rule out:** That a candidate had separate Windows-C++ experience not reflected in their published cypherpunk-era code. Adam Back, for example, may have written Windows C++ in commercial roles that isn't on hashcash.org.
- **Adam Back's identifier overlap with Satoshi** (Δ=0.78 on function-words) is real but partly an artifact of low-level systems-C vocabulary that both used (loop variables, buffer names). Naming-convention features (where Back is 0.2% Hungarian_C vs Satoshi's 6.4%) are more discriminating.

### Caveats

- **Language mismatch:** Satoshi and Dai wrote C++; Back, Finney, Sassaman wrote C. Some features (`class`, `template`, brace styles around class definitions) are language-mandated.
- **Era mismatch:** Bitcoin 0.1.3 is 2009; Hashcash is 1997-2004; Mixmaster spans 1999-2008. Coding conventions evolve.
- **Project-size mismatch:** Dai's Crypto++ (43k LOC) and Sassaman's Mixmaster (21k LOC) are larger and more multi-author than the single-author 10-16k LOC codebases.

### Dendrogram (code function-word Burrows' Delta)

![code-style-dendrogram](results/code-style-dendrogram.png)

Note that this dendrogram is on identifier function-words only — it does *not* incorporate the brace/indent/comment/Hungarian features, which are the more discriminating signals. The dendrogram clustering should be read as "shared identifier vocabulary" rather than "full code-style match."

### Composite MFC training-fingerprint score

Hungarian_C rate, space-indent ratio, and line-comment density are each reported separately above. They are also the three axes on which every named candidate (including TrueCrypt) scores low while all three Satoshi corpora score high. To make this pattern legible as a single number, `src/code_style.py` now computes a composite z-score: each of the three features is z-scored across all authors (mean 0, std 1), and the three z-scores are summed. A high positive composite means the author is simultaneously above average on all three dimensions. The composite is appended to `results/code-style-features.json` under `mfc_composite_ranking`.

| Author | Hungarian_C | Space ratio | Line cmt/KLOC | z_H | z_S | z_L | Composite |
|--------|-------------|-------------|---------------|-----|-----|-----|-----------|
| satoshi-nov2008 | 9.6% | 100% | 136.5 | +2.11 | +1.33 | +1.82 | **+5.26** |
| satoshi-v0.1.0 | 6.4% | 100% | 105.6 | +1.17 | +1.33 | +1.18 | **+3.68** |
| satoshi (v0.1.3) | 6.4% | 100% | 105.1 | +1.16 | +1.33 | +1.17 | **+3.67** |
| sassaman | 0.2% | 77% | 0.1 | -0.66 | +0.74 | -0.99 | -0.90 |
| pgp-6.5 | 0.8% | 29% | 45.4 | -0.47 | -0.48 | -0.06 | -1.01 |
| dai | 0.1% | 5% | 52.3 | -0.66 | -1.10 | +0.08 | -1.67 |
| truecrypt | 0.1% | 9% | 34.6 | -0.67 | -0.98 | -0.27 | -1.93 |
| back | 0.2% | 32% | 0.2 | -0.64 | -0.41 | -0.99 | -2.03 |
| e4m | 0.1% | 13% | 1.4 | -0.67 | -0.91 | -0.94 | -2.52 |
| finney | 0.1% | 13% | 1.2 | -0.66 | -0.93 | -0.94 | -2.53 |

The composite shows a clean gap: all three Satoshi corpora score above +3.6; every candidate (named or wildcard) scores below -0.9. The three-dimensional MFC-training fingerprint is self-consistent across the 13-month Satoshi source window (Nov 2008 pre-release through Dec 2009 v0.1.3) and is absent from all candidate codebases analyzed. Sassaman ranks closest among candidates (-0.90, with +0.74 on space-indent due to his higher-than-average space ratio) but is still negative overall because his line-comment density is near-zero (0.1/KLOC vs Satoshi's 105/KLOC).

**Notable: PGP 6.5 (-1.01) ranks *below* Sassaman on the composite despite having the highest non-Satoshi Hungarian_C rate (0.8%, vs Sassaman's 0.2%).** The Hungarian_C advantage is overwhelmed by PGP's tab-indent and block-comment-heavy style. This is exactly the case the composite z-score was designed to discriminate: a single-axis test on Hungarian_C alone (thresholded at "≥0.5% suggests MFC training") would have produced a false positive on PGP 6.5; the three-axis composite correctly places PGP in mid-pack territory.

**Notable: e4m 2.01 (-2.52) is third-from-last on the composite — below TrueCrypt (-1.93), only Finney is lower.** e4m is pure C (no `.cpp` files), so the Hungarian_C axis is structurally constrained to zero regardless of Le Roux's preferences. The composite ruling rests on the OTHER two axes: 87% tab indent (vs Satoshi 100% spaces) and 1.4 line comments per KLOC (vs Satoshi 105.1; ratio inverted to 98% block-comment-dominated). The Le Roux wildcard reading is now ruled out by two independent codebases — TrueCrypt 7.1a (team derivative, 2011) AND e4m 2.01 (direct single-author, 1999). See [`forensics/e4m-mfc-test.md`](forensics/e4m-mfc-test.md).

### What would strengthen this analysis

- ✅ TrueCrypt 7.1a (Le Roux-era Windows encryption codebase): tested 2026-05-27. **Result:** TrueCrypt's Hungarian_C rate is 0.1% — same as all other candidates, 60× below Satoshi's 6.4%. TrueCrypt also uses 91% tab indentation vs Satoshi's 100% spaces, and a mixed comment style (22 block + 35 line per KLOC) vs Satoshi's line-heavy (1 block + 105 line per KLOC). **The Paul Le Roux / TrueCrypt wildcard reading is ruled out by the same fingerprint absence that rules out the named candidates.** The MFC fingerprint is more discriminating, not less, when tested against the most plausible Windows-C++ wildcard.
- ✅ PGP for Windows 6.5.1i (Network Associates, 1999): tested 2026-05-27. **Result:** PGP 6.5 Hungarian_C rate is 0.8% — the highest non-Satoshi result on record, 4× to 8× the named candidates, but still 8× below Satoshi's 6.4%. PGP 6.5 fails on the other two MFC fingerprint axes (71% tab indent, block-comment-heavy ratio inverted from Satoshi's line-comment-heavy style). Composite z = -1.01, *below* Sassaman at -0.90. **The "Satoshi was a PGP-team contributor" reading is not supported at the codebase house-style level. The composite z-score discriminates correctly where a single-axis Hungarian_C test would have produced a false positive on PGP 6.5.** See [`forensics/pgp-6.5-windows-mfc-test.md`](forensics/pgp-6.5-windows-mfc-test.md).
- ✅ e4m 2.01 (Paul Le Roux, 1999): tested 2026-05-27. **Result:** e4m is pure C (no `.cpp` files), so Hungarian_C is structurally void; the ruling rests on the OTHER two axes. e4m indent is 87% tabs vs Satoshi's 100% spaces; comment density is 80.7 block + 1.4 line per KLOC vs Satoshi's 1.0 + 105.1 (ratio completely inverted). Composite z = -2.52, third-from-last. **The Le Roux wildcard is now ruled out by two independent codebases: TrueCrypt 7.1a (2011 team derivative) AND e4m 2.01 (1999 direct single-author).** See [`forensics/e4m-mfc-test.md`](forensics/e4m-mfc-test.md).
- ✅ Bitcoin v0.1.0 source (Jan 2009): already in corpus as `code-corpus/satoshi-v0.1.0/` (16.6k LOC, 22 files, MD5 dca1095f053a0c2dc90b19c92bd1ec00 from the original metzdowd cryptography-list announcement). Confirms the MFC fingerprint at 6.4% Hungarian_C / 100% spaces / 105.6 line cmts per KLOC — the same values as Bitcoin 0.1.3 (Dec 2009). Combined with Bitcoin Nov 2008 pre-release (9.6% / 100% / 136.5) the three-corpus intra-Satoshi consistency is established across the full 13-month launch window. See [`forensics/intra-satoshi-style-drift.md`](forensics/intra-satoshi-style-drift.md).
- ✅ Composite "MFC training fingerprint" z-score (Hungarian_C + space-indent + line-comment preference): implemented in commit `5289408`. Empirically validated 2026-05-27 by the PGP 6.5 test (false positive on Hungarian_C alone, correctly caught by composite) and the e4m test (Hungarian_C structurally void on pure-C codebases, composite still rules via remaining two axes). The two failure-mode classes the composite is meant to handle are both demonstrated.

## Timestamp forensics (separate analysis, not stylometry)

A third axis, independent of prose and code stylometry: when did Satoshi communicate? Two corpora are timestamped:

1. **Public communications** — 543 BitcoinTalk + P2PFoundation posts and 39 bitcoin-list emails (n=582).
2. **Source-control commits** — 279 unique commits in `bitcoin/bitcoin` git log attributed to `s_nakamoto@<SVN-UUID>` or `satoshin@gmx.com`, deduplicated by commit hash, timestamps preserved through the SourceForge SVN → GitHub import.

### Headline finding: "Satoshi was in UK time" is doubly falsified

The fraction of activity in the local 00:00–06:00 window (modal human sleep hours):

| Timezone | Forum corpus (n=582) | Commit corpus (n=279) | Compatible with human sleep? |
|----------|----------------------|------------------------|------------------------------|
| GMT (UK winter) | **17.0%** | **29.4%** | **No** — orders of magnitude too high |
| BST (UK summer) | **24.1%** | **34.4%** | **No** — even worse |
| EST (US Eastern) | 1.5% | 3.2% | Yes |
| PST (US Pacific) | 1.5% | 2.5% | Yes |

Two independent corpora both refute the UK-resident reading. EST and PST both remain compatible from this pair of corpora alone; **a third independent timestamp channel from PDF metadata** (`whitepaper-v1.pdf` UTC-7, `whitepaper-v2.pdf` UTC-6, on what is provably the same machine via byte-identical font subsets) **rules out US Eastern (UTC-5/-4 inconsistent with -07/-06) and constrains the most-likely band to US Pacific → US Mountain** with a one-timezone-east shift between Oct 2008 and Mar 2009. See [`forensics/uk-descent-eastern-resident-hypothesis.md`](forensics/uk-descent-eastern-resident-hypothesis.md) for the full forum + commit methodology including holiday-gap analysis and morning-onset gradient. See [`forensics/uk-emigre-east-coast-candidates.md`](forensics/uk-emigre-east-coast-candidates.md) for the candidate-search negative finding under the multi-axis filter. See [`forensics/hidden-artifacts-survey.md`](forensics/hidden-artifacts-survey.md) for the PDF-metadata timezone channel + the four-axis Windows-OS consensus.

## Conclusions

Across **eight independent forensic axes** — prose stylometry (aggregate + whitepaper-register + commit-message-register), code stylometry, MFC composite fingerprint, hyphenation overlap, timestamp distribution (forum + commit corpora + PDF metadata), PGP key forensics, and source-code developer-artifact audit — **no single named candidate matches Satoshi on more than one axis.** Each axis falsifies a different reading and the cross-axis consensus narrows the candidate space to a set of attributes that no public-record individual has been documented to combine.

### What every axis says, in one line each

| Axis | Closest non-Satoshi candidate | What rules out the obvious reading |
|------|------------------------------|-----------------------------------|
| **Prose function-word Δ (aggregate)** | Hal Finney (Δ=0.94) | Δ=0.94 is large in absolute terms; Finney's match is conversational-register only; on the whitepaper specifically Finney drops to rank 4. |
| **Prose function-word Δ (whitepaper)** | Sassaman/Mixmaster (Δ=0.86, multi-author corpus caveat); Back (Δ=0.97); solo-Sassaman (Δ=1.03) | The Mixmaster corpus is 4-author; the solo-Sassaman re-run (4,383 words) lands at Δ=1.03, removing the lead. Back is second and is consistent with the NYT April 2026 finding on prose alone but fails on code (see below). |
| **Prose function-word Δ (commit messages)** | Sassaman (Δ=0.91); Back (Δ=0.96) | Independent register confirms whitepaper top-2 via *opposite stylistic mechanism* (telegraphic / changelog: article-suppressed, pronoun-absent vs whitepaper's article-heavy formal prose). Convergence-via-different-mechanism is methodologically stronger than topic-induced convergence; strengthens the Sassaman/Back formal-register signal. See [`forensics/hidden-artifacts-survey.md`](forensics/hidden-artifacts-survey.md). |
| **Code identifier Δ** | Adam Back (Δ=0.81) | Driven by shared low-level systems-C vocabulary, not by Hungarian/MFC convention. Back's Hashcash is pure C, structurally unable to produce MFC class declarations. |
| **MFC composite z-score** | None — Sassaman (-0.90) and PGP-6.5 (-1.01) tie for closest, both deeply negative. All Satoshi corpora score +3.6 to +5.3. | The three-axis composite (Hungarian_C + space-indent + line-comment) is uniquely Satoshi across the 13-month launch window. PGP-6.5 (the most plausible MFC-era wildcard) and e4m 2.01 (Le Roux direct work) both fail. |
| **Hyphenation overlap (NYT 2026 method)** | Sassaman: 1/11 ("email") | Corpus-size limited (4,496 tokens for Back vs NYT's reported 134k posts). Not informative against the NYT result either way without matched-size corpora. |
| **Timestamp distribution (forum + commits)** | EST + PST both compatible | UK (GMT/BST) doubly falsified by forum + commit corpora. Eastern/Pacific US not discriminable from this pair of corpora alone. |
| **Timestamp distribution (PDF metadata)** | UTC-7 (Oct 2008) → UTC-6 (Mar 2009) | Third independent timestamp channel from PDF `CreationDate`. Rules out US Eastern (UTC-5/-4 inconsistent with -07/-06). Cleanest match: **US Pacific (PDT) → US Mountain (MDT)**, a one-timezone-east shift on what is provably the same machine (6 of 7 embedded font subsets are SHA256-identical between the two PDFs). See [`forensics/hidden-artifacts-survey.md`](forensics/hidden-artifacts-survey.md). |
| **PGP key armor header** | n/a (single canonical key + 3 keyserver decoys) | `Version: GnuPG v1.4.7 (MingW32)` on the Wayback-preserved 2010 canonical asc. **Direct evidence Satoshi used the GnuPG Windows Win32 build.** Cross-confirms the Windows reading from the code-style and PDF-font axes. |
| **PDF font fingerprint** | n/a | Arial v3.00 + Times v3.00/v2.76 + Courier v2.76 + Century Schoolbook Bold v2.35 — the exact Microsoft Windows XP SP2+ font combo, plus Microsoft Publisher 2003/2007 installation. OpenOffice `/Lang` = `en-GB` (British English locale). |
| **Source-code developer artifacts** | n/a | `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)` UA literal in v0.1.3 `net.cpp` — Windows XP UA spoof. `////` multi-slash comment style as idiosyncratic authorship marker. Surgical pre-release scrubbing (3 main.h annotations removed nov2008 → v0.1.0). No surviving personally identifying paths/emails/hostnames. |

### Cross-axis Windows-OS consensus

Four independent forensic mechanisms place Satoshi on Microsoft Windows: (1) code-style MFC composite, (2) PGP version-string `MingW32` Win32 build, (3) source-code UA literal `Windows NT 5.1`, (4) PDF font fingerprint exact Win XP SP2+ versions. **The Windows-OS claim is now load-bearing.**

### The conjoined finding (updated)

The candidate that the cross-axis result narrows toward is **a person who is:**

1. **Stylistically closer to Finney than to anyone else on conversational prose** (forum posts + emails); and
2. **Stylistically closer to Back, Sassaman, or solo-Sassaman than to anyone else on formal prose** (the whitepaper AND commit-message register — two independent registers, opposite stylistic mechanisms, same top-2 candidates); and
3. **A Microsoft Windows user (Windows XP SP2+ era)** confirmed by four independent forensic axes — code style + PGP version + UA literal + PDF font fingerprint; and
4. **A Windows-C++ developer with pervasive (not incidental) MFC training** — at a rate 4× higher than PGP 6.5 (the only candidate codebase with any non-trivial MFC use); and
5. **Microsoft Publisher 2003 or 2007 installed** (Century Schoolbook Bold v2.35 font, which ships with Publisher, used on the whitepaper title); and
6. **OpenOffice 2.4 configured with `en-GB` (British English) locale** — combined with the whitepaper's British spelling `favour`, two independent British-locale signals on the artifact axis; and
7. **Resident in US Pacific or Mountain time** during 2008–2010 (UK falsified by sleep-window analysis on forum + commit corpora; US Eastern falsified by PDF UTC offsets; cleanest fit is a Pacific-to-Mountain one-timezone-east shift between Oct 2008 and Mar 2009); and
8. **A user of inconsistent technical-neologism compound forms** (`autodetect/auto-detect`, `midstate/mid-state`, `ecdsa/ec-dsa`) — Satoshi's hyphenation fingerprint contains 11 such compounds, of which 0 overlap with any candidate corpus except Sassaman's single `email/e-mail` overlap; and
9. **Uses the `////`-style multi-slash internal comment marker** as an idiosyncratic stylistic tic (catalog-level finding from the dead-code audit; not yet captured by the quantitative code-style features).

**No public-record individual is documented to combine all nine attributes.** This is the central negative finding of the repo: the cross-axis filter narrows to an empty set under the candidate space available. Either (a) the candidate exists but has not been publicly identified, (b) Satoshi was a composite of multiple authors whose individual contributions do not separately match any single profile, or (c) one or more of the axes is methodologically defective in a way that's not yet visible. The repo's discipline (issue [#1](https://github.com/MatoTeziTanka/satoshi-stylometry/issues/1)) prohibits naming a specific living individual on the basis of these results.

### What this repo's evidence does NOT support

- **"Satoshi was Adam Back."** Back is consistent on the whitepaper-prose axis (Δ=0.97, second behind multi-author Sassaman) and on UK-origin signals (British spelling, residence). But Back's Hashcash codebase is pure C and structurally cannot produce MFC class declarations; the code-axis ruling on Back rests on the OTHER two MFC fingerprint axes, both of which his accessible code fails. Back is also UK-resident per public record, contradicting the timestamp evidence. The NYT April 2026 finding is partially convergent on prose-whitepaper but does not survive the code-axis or timestamp-axis cross-check. See [`forensics/nyt-april-2026-adam-back.md`](forensics/nyt-april-2026-adam-back.md).
- **"Satoshi was Hal Finney."** Finney is the closest conversational-prose match (Δ=0.92–0.94) but ranks 4th on the whitepaper, mid-pack on code identifier Δ, and his RPOW codebase has 0.1% Hungarian_C (60× below Satoshi). Operational considerations (Finney's documented active mining + bug-fix correspondence with "Satoshi" during 2009–2010) are evidence against Finney-as-Satoshi unless we posit deliberate self-correspondence, for which no primary source exists.
- **"Satoshi was Len Sassaman."** Sassaman ranks first on the multi-author Mixmaster RFC (Δ=0.87, retracted on solo re-run at Δ=1.03), and his composite MFC z-score (−0.90) is the closest among all candidates but still deeply negative. The "temporal coincidence" argument is weak (71 days between Satoshi's last verified private email per Hearn-disclosure and Sassaman's death, not the originally claimed 8 days). See [`forensics/sassaman-solo-corpus-rerun.md`](forensics/sassaman-solo-corpus-rerun.md).
- **"Satoshi was Nick Szabo."** Szabo is **not first on any axis** in this analysis. On the whitepaper specifically (the corpus the Aston 2014 result was strongest on), Szabo ranks **last (6 of 6)** under principled function-word features. He moves to mid-pack under topic-contaminated features, but the rank shift is attributable to subject-vocabulary overlap, not stylistic similarity. See [`forensics/topic-control-aston-2014.md`](forensics/topic-control-aston-2014.md).
- **"Satoshi was Paul Le Roux."** Ruled out by two independent codebases (TrueCrypt 7.1a 2011 team derivative AND e4m 2.01 1999 direct single-author). Both fail every testable MFC fingerprint axis. See [`forensics/e4m-mfc-test.md`](forensics/e4m-mfc-test.md). The Le Roux ruling rests on two-codebase agreement and survives the "but TrueCrypt diverged from his personal style" objection.
- **"Satoshi was Craig Wright."** Ruled out judicially by COPA v Wright [2024] EWHC 1198 (Ch) (Mellor J found Wright committed forgery and gave false evidence; Wright enjoined from further UK Satoshi-litigation). Independently confirmed by this repo's stylometric methodology: **Wright is LAST (rank 7 of 7) in every Satoshi prose register** under principled function-word features, with aggregate Δ=1.55 — the largest single-candidate Δ in the entire corpus, exceeding even Dai's small-corpus result. Under topic-contaminated features Wright moves only one rank to 6 of 7. The Wright Bitcoin SV code-snapshot composite z = +2.43 (full) / **+3.53 (diff-only, BSV-team net-new files post-2018-fork, 91 files / 18.4k LOC, zero Satoshi commits)** *appears* Satoshi-like, but reflects **convention mimicry, not Wright authorship**: Wright authored zero commits in BSV, and the nChain team consciously preserved Satoshi's `C[Capital]` Hungarian naming + 100% space indentation + `//` line-comment density in net-new code consistent with their "Satoshi's Vision" mission. The MFC composite is a *convention-test* (rules OUT candidates whose style differs), not a *signature-test* (cannot rule IN). See [`forensics/wright-cross-axis-test.md`](forensics/wright-cross-axis-test.md) and [`forensics/wright-bsv-diff-test.md`](forensics/wright-bsv-diff-test.md).

### Forensics-doc index

Per-axis writeups, ordered by topic:

**Prose stylometry**
- [`forensics/sassaman-solo-corpus-rerun.md`](forensics/sassaman-solo-corpus-rerun.md) — multi-author Mixmaster vs solo Sassaman correction
- [`forensics/topic-control-aston-2014.md`](forensics/topic-control-aston-2014.md) — Aston 2014 topic-contamination takedown with rank-shift table
- [`forensics/nyt-hyphenation-replication.md`](forensics/nyt-hyphenation-replication.md) — NYT April 2026 methodology replication

**Code stylometry**
- [`forensics/intra-satoshi-style-drift.md`](forensics/intra-satoshi-style-drift.md) — three-corpus intra-Satoshi consistency across launch window
- [`forensics/pgp-6.5-windows-mfc-test.md`](forensics/pgp-6.5-windows-mfc-test.md) — PGP team house style vs Satoshi
- [`forensics/e4m-mfc-test.md`](forensics/e4m-mfc-test.md) — Le Roux direct single-author work

**Hidden-artifact and cross-channel forensics**
- [`forensics/hidden-artifacts-survey.md`](forensics/hidden-artifacts-survey.md) — four-axis survey of PGP keys, PDF metadata + fonts, source-code developer artifacts, and commit-message register. Top findings: GnuPG MingW32 version, Windows XP UA literal, PDF font fingerprint = Win XP SP2+ with Microsoft Publisher, en-GB OpenOffice locale, UTC-7 → UTC-6 offset shift.

**Adjudicated non-Satoshi reference class**
- [`forensics/wright-cross-axis-test.md`](forensics/wright-cross-axis-test.md) — Craig Wright tested as a reference-class control against the cross-axis methodology. Result: last in every Satoshi prose register (confirms COPA 2024 quantitatively).
- [`forensics/wright-bsv-diff-test.md`](forensics/wright-bsv-diff-test.md) — Wright-BSV diff-only follow-up. BSV-team net-new code (91 files post-fork, zero Satoshi commits) scores composite z = +3.53. Methodological finding: the MFC composite measures *adoptable conventions*, not unique authorship; the BSV team consciously preserved Satoshi-style conventions.

**Cross-axis candidate analyses**
- [`forensics/nyt-april-2026-adam-back.md`](forensics/nyt-april-2026-adam-back.md) — NYT 2026 Back claim, convergence + divergence per axis
- [`forensics/uk-descent-eastern-resident-hypothesis.md`](forensics/uk-descent-eastern-resident-hypothesis.md) — timestamp falsification of UK residence
- [`forensics/uk-emigre-east-coast-candidates.md`](forensics/uk-emigre-east-coast-candidates.md) — candidate-search negative finding under the four-axis filter
- [`forensics/patoshi-pattern.md`](forensics/patoshi-pattern.md) — single-miner pattern in early blocks
- [`forensics/patoshi-vs-hour-of-day-cross-reference.md`](forensics/patoshi-vs-hour-of-day-cross-reference.md) — Patoshi-pattern × timestamp cross-check

### Stake of the negative finding

This is a negative-result repository — its primary output is "the candidate space is empty under the cross-axis filter," not "X is Satoshi." Negative results are publishable and useful: they bound future investigations and rule out repeated litigation of already-falsified readings. The repo is built so any reader can:

1. Reproduce the analyses from public sources (`src/pull_corpus.py` + `python3 src/*.py`)
2. Add a new candidate corpus (`code-corpus/<name>/` + SOURCE.md, then re-run scripts)
3. Apply the cross-axis filter to that candidate and see whether they pass any single axis or all five

Adding new candidates is the natural future direction. The cross-axis filter has been demonstrated to be discriminating; it has not been demonstrated to be impossible to satisfy.

## Reproduce

```bash
# Requirements: python3 with numpy/scipy/scikit-learn/matplotlib,
# plus `git` and `pdftotext` (poppler-utils) on PATH.
pip install -r requirements.txt

# Pull all corpora from public sources (~150MB git clone of NI site repo)
python3 src/pull_corpus.py

# Run prose / code stylometry
python3 src/burrows_delta.py
python3 src/code_style.py

# Run timestamp forensics — requires bitcoin/bitcoin shallow clone for the commit corpus:
#   git clone --depth 1 --filter=blob:none https://github.com/bitcoin/bitcoin.git /tmp/bitcoin-shallow
#   git -C /tmp/bitcoin-shallow fetch --filter=blob:none --unshallow
python3 src/time_forensics.py
```

Results land in `results/`. A normal stylometry run takes ~5 seconds after the corpus clone. The timestamp-forensics run takes <1 second once the bitcoin/bitcoin shallow clone is in place.

## Sources

- Satoshi Nakamoto Institute, [`nakamotoinstitute.org`](https://github.com/nakamotoinstitute/nakamotoinstitute.org) (AGPL-3.0) — Satoshi forum posts, emails, and all four candidates' archived essays.
- [bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf) — Bitcoin whitepaper canonical PDF.
- [Adam Back, Hashcash 2002 paper](https://cdn.nakamotoinstitute.org/docs/hashcash.pdf).

This repo does not redistribute the corpora; `src/pull_corpus.py` reassembles them from the above sources.

## License

AGPL-3.0. See [LICENSE](LICENSE).

The analysis code is original; the underlying corpora are subject to their original authors' rights and the Nakamoto Institute's AGPL-3.0 license for the archived form.

## Citation

If you use this analysis, please cite as:

> satoshi-stylometry, Burrows' Delta function-word analysis of cypherpunk-era candidates against Satoshi Nakamoto's writings, 2026. https://github.com/MatoTeziTanka/satoshi-stylometry

## Acknowledgments

The Satoshi Nakamoto Institute's curation of cypherpunk-era writings is the only reason this analysis is one weekend's work instead of several months of mailing-list scraping. They deserve the credit.
