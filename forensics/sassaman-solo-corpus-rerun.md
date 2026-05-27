# Sassaman re-run: solo corpus vs multi-author baseline

> **Headline finding:** The repo's most striking prior result — that the Bitcoin whitepaper most closely matches Len Sassaman (Δ=0.86) — was **substantially an artifact of the multi-author Mixmaster IETF draft used as the Sassaman baseline**. When the baseline is replaced with verified solo-Sassaman writings (4,383 words across two single-author papers, formal-technical register), the whitepaper Δ to Sassaman rises to 1.03 — third place, not first. **Adam Back becomes first on the whitepaper (Δ=0.97), Sassaman-solo third.** The "Sassaman first on the whitepaper" framing is retracted.

## What this test asks

The original `corpus/sassaman/` is 5,571 words of prose extracted from
`draft-sassaman-mixmaster-03`, a four-author IETF draft (Möller, Cottrell,
Palfrader, Sassaman). The repo's README has carried a "Sassaman caveat" since
the original commit: this corpus is the average of four cypherpunk-era technical
writers, not Sassaman alone, and a clean solo Sassaman baseline could either
strengthen or weaken the Δ=0.86 whitepaper result.

This is the clean test.

## Method

New corpus `corpus/sassaman-solo/` with two verified solo-authored Sassaman
papers in formal-technical register comparable to the whitepaper:

| Text | Words | Date | Source |
|------|-------|------|--------|
| *Ethical Guidelines for Computer Security Researchers: "Be Reasonable"* | 2,814 | Financial Cryptography Workshops 2010 (Springer LNCS 6054) | `cosicdatabase.esat.kuleuven.be/.../1433` |
| *The Faithless Endpoint: How Tor puts certain users at greater risk* | 1,569 | KU Leuven Technical Report ESAT-COSIC 2007-003 | `nakamoto-research.obxium.com/data/article-896.pdf` |
| **Total** | **4,383** | | |

Both verified sole-authored: title page reads "Len Sassaman" only; DBLP lists no
co-authors for either; KU Leuven affiliation; Sassaman self-cites the Faithless
Endpoint in the Ethics paper.

The original `corpus/sassaman/` is **preserved** alongside the new corpus — the
trust chain is auditable. The Δ matrix shows both as separate "authors" so
direct comparison is visible.

## Results

### Whitepaper comparison (the key test)

| Candidate | Whitepaper Δ | Rank (with solo) | Rank (original) |
|-----------|--------------|------------------|-----------------|
| sassaman (Mixmaster RFC, 4-author corpus) | **0.86** | — (preserved for audit) | 1st |
| **back** | **0.97** | **1st** | 2nd |
| sassaman-solo (Ethics + Faithless, 4,383 words solo) | **1.03** | **3rd** | not measured |
| finney | 1.10 | 4th | 3rd |
| dai | 1.13 | 5th | 4th |
| szabo | 1.19 | 6th | 5th |

The solo-Sassaman Δ (1.03) is +0.17 worse than the multi-author baseline (0.86).
Adam Back (0.97) is closer to the whitepaper than solo-Sassaman.

### Other registers (conversational, emails, forum posts)

Across the conversational registers, **solo-Sassaman is consistently last or
second-to-last** among the six candidates:

| Sub-corpus | Solo-Sassaman rank |
|------------|---------------------|
| satoshi-bitcointalk | 5th of 6 |
| satoshi-emails | 5th of 6 |
| satoshi-forum_posts | 5th of 6 |
| satoshi-p2pfoundation | 4th of 6 |

Solo-Sassaman is **never** the closest match on any Satoshi sub-corpus, formal
or conversational. The original Sassaman result (1st on whitepaper, 2nd on
emails) was the multi-author Mixmaster blend.

## What this changes

**The repo's headline finding was:**

> Prose-formal (the whitepaper) → **Len Sassaman** with a multi-author corpus
> caveat (Δ 0.87), then **Adam Back** (Δ 0.98).

**The corrected finding is:**

> Prose-formal (the whitepaper) → **Adam Back** (Δ 0.97). The "Sassaman first"
> result in the original corpus was driven by averaging-with-coauthors in the
> Mixmaster IETF draft. With a verified solo-Sassaman baseline, Sassaman ranks
> third on the whitepaper (Δ 1.03).

The temporal-coincidence framing on Sassaman (Δ=0.87 + died 2011-07-03) loses
its primary statistical support. The case for Sassaman as a candidate was already
weak (the 71-day gap from Satoshi's last private message to Sassaman's death is
not a tight match, per `forensics/uk-descent-eastern-resident-hypothesis.md`).
With the whitepaper result retracted to 3rd place, the case becomes thinner still.

The Adam Back whitepaper result (now 1st at Δ=0.97) is consistent with the
NYT April 2026 investigation's whitepaper finding (Cafiero: Back closest of 12,
"inconclusive with Finney nearly tying"). See
[`forensics/nyt-april-2026-adam-back.md`](nyt-april-2026-adam-back.md) for how
this fits the broader Back convergence/divergence picture.

## What this does NOT change

- The conversational Satoshi → Finney result (Δ=0.92 on emails, Δ=0.90 on
  BitcoinTalk) is unaffected. Finney remains the strongest conversational
  match by a wide margin.
- The code-style results are unaffected (they use different corpora).
- The timestamp falsifications (UK-resident doubly falsified) are unaffected.
- The candidate-set negative finding (no four-axis UK-emigré East Coast match)
  is unaffected.

## Caveats

1. **4,383 words is borderline for Burrows' Delta.** Standard guidance is ~5k
   minimum per author. Solo-Sassaman is slightly under threshold. The result
   should be read as suggestive-of-retraction rather than definitive.
2. **Register mismatch within the solo corpus.** The Ethics paper is ethics/
   policy; the Faithless Endpoint is short threat analysis. Both are formal-
   technical but neither is system-design (the whitepaper's genre). Three
   different sub-genres of formal writing.
3. **Sassaman's pre-2007 writings are not publicly accessible** in solo form.
   His cypherpunks-era writing (2001–2004) sits in mailing list archives with
   PGP-pseudonymous attribution ambiguity, and the Vox blog (`rabbi.vox.com`)
   was lost when Vox.com shut down ~2013. A more complete solo Sassaman corpus
   would require deeper archival work.
4. **The original Mixmaster-RFC Sassaman corpus is preserved** in the repo as
   `corpus/sassaman/`. The original Δ=0.86 result is auditable and the
   correction chain is visible in commit history. We retract the *interpretation*
   ("Sassaman is the whitepaper's closest match"), not the *data point*.

## Trust chain on the Sassaman thread

The repo's Sassaman thread has had multiple corrections preserved per session
discipline:

1. **Initial:** Sassaman first on whitepaper (Δ=0.87) interpreted as a strong
   stylistic match.
2. **Date correction:** initially claimed Sassaman died "May 3, 2011" → corrected
   to "July 3, 2011" via Hacker News primary source.
3. **Gap-from-Satoshi correction:** initially claimed "8 days from last Satoshi
   message" → corrected to "approximately 6.5 months from last public message" →
   later refined to "71 days from last private message" once the Hearn email
   date was sourced.
4. **Multi-author corpus caveat:** the README has carried this caveat from the
   original commit.
5. **Solo-corpus retraction (this commit):** the Sassaman whitepaper result is
   reframed — Adam Back is first, Sassaman-solo is third.

Each correction is preserved in commit messages so future readers can audit the
chain rather than seeing only the cleaned-up final state.

## Source citations

- `corpus/sassaman-solo/SOURCE.md` — provenance and pull instructions
- `results/results.json` — full Burrows' Delta matrix including sassaman-solo
- [Ethics paper](https://cosicdatabase.esat.kuleuven.be/backend/publications/files/conferencepaper/1433) — primary
- [Faithless Endpoint](https://nakamoto-research.obxium.com/data/article-896.pdf) — primary
- [DBLP for Len Sassaman](https://dblp.org/pid/39/6080.html) — sole-author verification
