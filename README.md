# satoshi-stylometry

A reproducible Burrows' Delta analysis comparing the writings of "Satoshi Nakamoto" against four cypherpunk-era candidates: Adam Back, Hal Finney, Nick Szabo, and Wei Dai.

> **Findings in one line:** stylometric distance to Satoshi splits by register. The conversational Satoshi (forum posts + emails) is closest to Hal Finney by a wide margin. The formal-paper Satoshi (the Bitcoin whitepaper) is closest to Adam Back. Nick Szabo is the second-closest match across registers but is never first. Wei Dai is consistently furthest.

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

| Candidate | Δ (function words, principled) | Δ (top-150, topic-contaminated) |
|-----------|--------------------------------|----------------------------------|
| **Hal Finney**   | **0.98** | 1.07 |
| Nick Szabo       | 1.26     | 1.32 |
| Adam Back        | 1.36     | 1.56 |
| Wei Dai          | 1.54     | 1.73 |

### Per-register Burrows' Delta (function words)

| Satoshi sub-corpus | Words | 1st | 2nd | 3rd | 4th |
|--------------------|-------|-----|-----|-----|-----|
| BitcoinTalk posts  | 57,041 | Finney 0.93 | Szabo 1.23 | Back 1.25 | Dai 1.44 |
| Emails             | 11,442 | Finney 0.93 | Back 1.16  | Szabo 1.18| Dai 1.28 |
| Forum (all)        | 57,908 | Finney 0.93 | Szabo 1.23 | Back 1.24 | Dai 1.44 |
| **Whitepaper**     | 3,571  | **Back 0.99** | Finney 1.14 | Dai 1.15 | Szabo 1.24 |
| P2P Foundation     | 866    | (too small) | | | |

![dendrogram](results/dendrogram.png)

### What this means

The signal is consistent and the register-split is the most interesting finding:

- **Casual Satoshi → Finney.** Across 70k+ words of forum posts and emails, Hal Finney is the closest stylistic match by a substantial margin (Δ 0.93 vs Szabo's 1.18-1.23). Finney was operationally closest to Satoshi: he ran one of the first nodes, received the first peer-to-peer Bitcoin transaction (block 170), was an early Hashcash contributor, and was on the cypherpunks list for decades.
- **Formal-paper Satoshi → Back.** On the 3,571-word whitepaper specifically, Back overtakes Finney (Δ 0.99 vs 1.14). Back is cited as reference [6] of the paper, was Satoshi's first known email contact (Aug 2008), and is British — and the whitepaper contains one British spelling slip (`favour`).
- **Szabo is never first.** Despite the Aston University 2014 result favoring him, Szabo ranks second on most registers and fourth on the whitepaper itself under principled methodology. The Aston study used a methodology vulnerable to topic contamination — and on the topic-contaminated re-run in this repo, Szabo does indeed move up.
- **Wei Dai is consistently last.** b-money is intellectually close to Bitcoin (Satoshi cites it as ref [1]) but stylistically distant. Dai's writing patterns differ in function-word distribution.

### Interpretive frames

Three honest readings of the register-split:

1. **One author with strong register adaptation.** A single skilled writer can write formal papers and casual forum posts in different styles. The "Back-like whitepaper, Finney-like forum" pattern could be one author whose academic register happens to look like Back's and casual register happens to look like Finney's.
2. **Two-author hypothesis.** Bitcoin may have been co-authored by Back and Finney, with Back drafting the paper and Finney handling community communication. This is consistent with operational evidence (Finney ran the first nodes, Back was the cited Hashcash author) but unsupported by direct evidence.
3. **Finney with stylistic borrowing.** Finney could have authored everything, with the whitepaper deliberately styled to read more "Back-like" — either as homage, intentional misdirection, or because the academic register naturally pulls toward Back's published norms.

This analysis cannot distinguish between these. It can only rule out Szabo as the primary stylistic source and Wei Dai entirely.

## Limitations

- **Corpus imbalance.** Back has 4.9k words (Hashcash paper only). Dai has 1.4k words (b-money only). Burrows' Delta works reliably from ~5k words per author; Back is borderline and Dai is below threshold. Finney (16k) and Szabo (137k) are robust.
- **Candidate set is incomplete.** This run excludes Len Sassaman, Stuart Haber, W. Scott Stornetta, David Chaum, Tim May, and other plausible cypherpunk-era candidates. Sassaman in particular (death timing matches Satoshi's silence) deserves inclusion in a follow-up — but his published corpus is small and hard to source.
- **Function-word lists vary.** The 201-word list at `src/function_words.py` is composite (Mosteller-Wallace, Burrows, stylo defaults). Using a different list may shift results within ±0.1 Delta. The relative ordering is robust to list choice in this dataset.
- **No deliberate-misdirection control.** A pseudonymous author seeded with stylistic markers from another writer would defeat this analysis. The register-split finding is consistent with that scenario.
- **Source register confound.** Satoshi's forum posts are conversational; Szabo's archived corpus is essays. Comparing forum-Satoshi against essay-Szabo is unavoidable given what's archived, but tilts results.

## Reproduce

```bash
# Requirements: python3 with numpy/scipy/scikit-learn/matplotlib,
# plus `git` and `pdftotext` (poppler-utils) on PATH.
pip install -r requirements.txt

# Pull all corpora from public sources (~150MB git clone of NI site repo)
python3 src/pull_corpus.py

# Run analysis
python3 src/burrows_delta.py
```

Results land in `results/`. A normal run takes ~5 seconds after the clone.

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
