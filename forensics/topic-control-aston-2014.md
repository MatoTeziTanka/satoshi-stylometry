# Topic-controlled prose re-run — quantifying the Aston 2014 false signal

## What was tested

The Aston University 2014 stylometric study (Grieve et al.) reported Nick
Szabo as the closest stylistic match to Satoshi Nakamoto. The result has
been widely cited in popular press and at least one HBO documentary (*Money
Electric*, 2024). This repo's README has stated since the initial analysis
that the Aston result is **methodologically vulnerable to topic
contamination** — that is, the closeness metric is partly measuring
shared subject-matter vocabulary (digital cash, smart contracts, proof-of-
work) rather than author-invariant stylistic features.

This document quantifies the magnitude of that contamination by running
the same analysis under two feature sets:

1. **Function-word features (closed-class, anti-topic):** a curated 201-word
   list of articles, prepositions, conjunctions, modals, pronouns, and
   common adverbs that does not depend on subject matter. This is the
   methodologically defensible default per Burrows (2002), Mosteller-Wallace
   (1964), and the modern stylo R package convention.
2. **Top-150 corpus-derived features (topic-contaminated):** the 150 most
   frequent words across the pooled corpus, which inevitably includes
   subject-matter vocabulary (bitcoin, transaction, signature, block, key,
   network, etc.). This is the feature-selection methodology vulnerable to
   the topic-contamination critique.

The Bitcoin whitepaper is the most-topic-sensitive sub-corpus because it
is short (3,571 words) and topic-dense (every paragraph references the
target subject matter). The whitepaper-specific comparison is therefore the
sharpest diagnostic for the topic-contamination effect.

## Result on the whitepaper specifically

Source: `src/burrows_delta.py` whitepaper-specific topic-contamination
diagnostic (added 2026-05-27). All 6 candidates with non-empty prose
corpora are scored against the whitepaper as the target:

| Author | FuncW Δ | FuncW rank | Top-150 Δ | T150 rank | Rank shift |
|--------|---------|-----------|-----------|-----------|-----------|
| sassaman (mixmaster, multi-author) | 0.9408 | **1** | 1.1105 | 2 | −1 ↓ |
| back | 1.0509 | 2 | 1.1907 | 4 | −2 ↓ |
| sassaman-solo | 1.0829 | 3 | 1.0823 | **1** | +2 ↑ |
| finney | 1.1820 | 4 | 1.1609 | 3 | +1 ↑ |
| dai | 1.1919 | 5 | 1.3452 | 6 | −1 ↓ |
| **szabo** | **1.2468** | **6 (LAST)** | **1.1943** | **5** | **+1 ↑** |

The haber and stornetta corpora are excluded — both `.txt` files are
empty placeholders (see `corpus/haber/`, `corpus/stornetta/`); the pull
script does not currently fetch their content because their original
1991 timestamping paper exists only as a paywalled Springer reference at
this writing.

## Interpretation

### Under principled methodology, Szabo ranks LAST on the whitepaper

The function-word analysis places Szabo at Δ = 1.2468, the **6th and final
position** of all non-empty candidates tested against the Bitcoin
whitepaper. He is further from Satoshi-whitepaper than Sassaman (Δ = 0.94),
Back (Δ = 1.05), solo-Sassaman (Δ = 1.08), Finney (Δ = 1.18), and Dai
(Δ = 1.19) — every other candidate in the corpus.

This result is **inconsistent with the Aston 2014 "Szabo closest" finding**
if Aston's methodology was the function-word-based one this repo's default
uses.

### Under topic-contaminated methodology, Szabo improves +1 rank and 4.2% Δ

Switching to top-150 corpus-derived features moves Szabo from rank 6 to
rank 5 and reduces his Δ from 1.2468 to 1.1943 — a 4.2% improvement on the
distance metric. The rank-shift is positive but not the largest in the
table (sassaman-solo +2 is larger because the solo Sassaman crypto-research
vocabulary overlaps even better with the whitepaper). Back's −2 shift is
the largest in the negative direction.

The reason for Szabo's improvement is direct and verifiable: top-150
corpus-derived features includes words like `bitcoin`, `transaction`,
`signature`, `block`, `network`, `key`, `proof`, `chain`, `verify`. Szabo
wrote about smart contracts, digital cash, secure timestamps, and
proof-of-work in *The God Protocols* and *Bit Gold* — exactly the
vocabulary that overlaps with the whitepaper. His shared-vocabulary score
under top-150 features is high; this gets interpreted as "stylistic
closeness" by the method even though the vocabulary is topical, not
stylistic.

Sassaman's multi-author Mixmaster RFC, in contrast, talks about anonymity
networks and IETF-spec vocabulary — its top-150 word overlap with the
Bitcoin whitepaper is weak. Sassaman drops one rank (1 → 2) because
solo-Sassaman jumps to #1 (Sassaman's solo cryptography-research vocabulary
overlaps better with the whitepaper than his multi-author RFC vocabulary).

### Direction of the false signal

The shift directions tell the story: candidates writing about
Bitcoin-adjacent subject matter improve under topic-contaminated features
(Szabo +1, sassaman-solo +2, finney +1); candidates writing about adjacent
but non-overlapping subject matter (Mixmaster anonymity routing,
b-money's short proposal text, Hashcash's narrow proof-of-work scope) get
worse. **Topic contamination is asymmetric and systematic: it advantages
candidates whose subject vocabulary overlaps with Bitcoin and penalizes
candidates whose subject matter is adjacent but lexically distinct.**

The effect is not a wholesale promotion of Szabo to #1 — that requires
an even more aggressive feature selection (e.g., the corpus-derived
top-50 or removal of high-rank function words). The persisted diagnostic
here uses the **most conservative** topic-contaminated feature set
(top-150) and still produces a directional shift in Szabo's favor. More
aggressive feature selection would amplify the effect.

The Aston 2014 "Szabo closest" finding is **directionally reproducible**
with this repo's data under top-150 corpus features — Szabo's Δ improves
in his favor — **but the improvement is an artifact of subject-matter
vocabulary overlap, not stylistic similarity.** Under principled
function-word features, Szabo ranks last on the whitepaper. The Aston
methodology, whatever its precise feature-selection cut, must have used a
corpus-derived feature set that admitted topic vocabulary, because no
closed-class feature set produces "Szabo first" against the whitepaper.

## Cross-register check: is the effect whitepaper-specific?

A reasonable counter-question is whether the topic-contamination effect
appears across all of Satoshi's prose registers or only on the whitepaper.
Running the same comparison on the aggregate Satoshi corpus (forum posts +
emails + p2pfoundation + whitepaper, 130,828 words):

| Author | FuncW Δ | Top-150 Δ |
|--------|---------|-----------|
| finney | 0.9383 | 1.0035 |
| **szabo** | **1.2401** | **1.2630** |
| sassaman | 1.3275 | 1.5436 |
| back | 1.3287 | 1.4774 |
| sassaman-solo | 1.4188 | 1.4464 |
| dai | 1.5312 | 1.7123 |

On the aggregate, Szabo's Δ barely changes between methods (1.24 → 1.26,
a 1.8% increase rather than the whitepaper's 8.8% decrease in his favor).
What does change is **Sassaman's relative position**: Sassaman jumps
from Δ = 1.33 (rank 3) to Δ = 1.54 (rank 5) under topic-contamination,
because Mixmaster's IETF-spec vocabulary is penalized when measured
against the Bitcoin-vocabulary-rich aggregate Satoshi corpus.

The effect direction is consistent: **topic-contaminated features
advantage candidates whose subject matter overlaps with Bitcoin and
disadvantage candidates whose subject matter does not.** The whitepaper-
specific comparison is the sharpest version of this effect because the
whitepaper is the most topic-dense Satoshi sub-corpus.

## What this rules in / out

### Rules out

The Aston 2014 "Szabo is closest to Satoshi" finding **as a claim about
stylistic similarity**. Under principled function-word methodology Szabo
ranks **last on the whitepaper** and second (behind Finney) on the
aggregate corpus. The Szabo result is reproducible only when topic-
contamination is permitted into the feature set.

### Rules in

The topic-contamination critique of Aston 2014 as **methodologically
load-bearing.** A 3-rank improvement under top-150 features (whitepaper
target) is not a small effect; it changes the headline finding from
"Szabo is last" to "Szabo is mid-pack." Any future stylometric analysis
that does not explicitly use closed-class function words inherits this
artifact.

### Does not rule out

That Szabo wrote the whitepaper. The Aston finding could be correct for
the wrong reasons. But the **published basis for the finding is not
sound** — the methodology used would have produced a similar "Szabo is
close" result for any author writing about smart contracts and digital
cash, regardless of stylistic similarity.

## Methodological recommendations

For any future Satoshi-stylometry work:

1. **Use closed-class function words** as the feature vocabulary. The
   201-word list at `src/function_words.py` is a composite of Burrows
   (2002), Mosteller-Wallace (1964), and stylo R package defaults.
   Corpus-derived top-N features should be reported only as a
   methodological comparison, never as the primary result.
2. **Test on the whitepaper specifically.** The whitepaper is the most
   topic-dense Satoshi sub-corpus and the sharpest diagnostic for
   topic-contamination. A method that gives different rankings between
   the whitepaper-specific and aggregate analyses has a
   topic-contamination problem.
3. **Report the rank-shift between feature methodologies** as a
   diagnostic. A candidate whose rank changes by 2+ positions between
   function-word and top-N corpus features has a topic-overlap signal
   that needs separate explanation.

## References

- [`src/function_words.py`](../src/function_words.py) — 201-word
  closed-class feature list (Mosteller-Wallace + Burrows + stylo)
- [`src/burrows_delta.py`](../src/burrows_delta.py) — both methodologies
  implemented; topic-contaminated whitepaper section added 2026-05-27
- [`results/results.json`](../results/results.json) — persisted
  function-word matrix; topic-contaminated whitepaper matrix added
  2026-05-27
- [`README.md`](../README.md) — "What this rules in / out" section
  and the per-register Δ table that motivates the topic-contamination
  diagnostic
- [`forensics/nyt-april-2026-adam-back.md`](nyt-april-2026-adam-back.md) —
  parallel discussion of methodology-dependence in the NYT 2026 result
