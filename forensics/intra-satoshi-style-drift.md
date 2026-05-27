# Intra-Satoshi style-drift test

> **Headline finding:** Satoshi's code-style fingerprint is **stable across the launch window** (Nov 2008 → Jan 2009 → Dec 2009). The MFC Hungarian C-prefix convention was already 9.6% of identifiers in the earliest publicly accessible source (the November 2008 pre-release sent privately to the cryptography mailing list). This rules out a "MFC convention added by a later collaborator" reading. The single-author hypothesis for Satoshi's code style is strengthened by direct evidence.

## What this test asks

Every other analysis in this repo compares Satoshi against *other* authors. This one asks the dual question: **is Satoshi's own style consistent across the launch window?**

If the MFC fingerprint emerged later (e.g., once a Windows-C++-trained collaborator joined the project mid-2009), it would show low Hungarian_C in the early material and high in the later material. If the fingerprint was baseline Satoshi from the start, it should appear at meaningful rates in the earliest material — even before the project went public.

The relevant time points:
- **2008-11 pre-release** (private distribution on the cryptography mailing list to Hal Finney and others)
- **2009-01 v0.1.0** (first public SourceForge release)
- **2009-12 v0.1.3 ALPHA** (the existing repo baseline; first version with source files attached at release time)

## Method

Two new corpora added alongside the existing `code-corpus/satoshi/` (v0.1.3):

- `code-corpus/satoshi-nov2008/`: 3 files / 3,305 LOC. The complete `nov08/` directory from `github.com/0xMagnuz/Bitcoin-v0.1`. Provenance traces to Hal Finney's preserved copy.
- `code-corpus/satoshi-v0.1.0/`: 22 files / 16,563 LOC. The full v0.1.0 source minus the same exclusions used for the v0.1.3 corpus (`sha.cpp/h`, `uibase.cpp/h` — third-party / machine-generated). MD5 anchor `dca1095f053a0c2dc90b19c92bd1ec00` matches the documented 2009-01-08 announcement.

Existing analysis pipeline (`src/code_style.py`) re-run with all three Satoshi corpora as separate "authors" so the Δ matrix shows intra-Satoshi distances.

## Results

### MFC Hungarian C-prefix convention (the most diagnostic single feature)

| Corpus | Hungarian_C rate |
|--------|------------------|
| satoshi-nov2008 (Nov 2008 pre-release) | **9.6%** |
| satoshi-v0.1.0 (Jan 2009 release) | 6.4% |
| satoshi (v0.1.3 ALPHA, Dec 2009) | 6.4% |
| Adam Back (Hashcash, comparator) | 0.2% |
| All other candidates (Dai/Finney/Sassaman/TrueCrypt) | 0.1–0.2% |

**The MFC convention is already present at higher density in the earliest material.** The 9.6% rate in Nov 2008 (vs 6.4% later) is consistent with the natural dynamic where early codebases have a few core MFC-style classes (`CTransaction`, `CBlock`, `CKey`) concentrated in a small file count, and the share dilutes as utility / non-class code is added.

### Indent style

| Corpus | Tabs | Spaces |
|--------|------|--------|
| satoshi-nov2008 | 0% | 100% |
| satoshi-v0.1.0 | 0% | 100% |
| satoshi (v0.1.3) | 0% | 100% |
| All other candidates and TrueCrypt | 23–95% tabs | 5–77% spaces |

**Identical across all three Satoshi corpora. Stable, idiosyncratic, and unique.**

### Comment density

| Corpus | Line (//) per KLOC | Block (/* */) per KLOC |
|--------|--------------------|-----------------------|
| satoshi-nov2008 | **136.5** | 0.0 |
| satoshi-v0.1.0 | 105.6 | 1.0 |
| satoshi (v0.1.3) | 105.1 | 1.0 |

**The Nov 2008 pre-release has even more extreme line-comment preference than the later code.** Zero block comments in the entire pre-release, and 30% higher line-comment density. This is consistent with code in active heavy-comment authoring early in a project, with the rate softening as the codebase matures.

### Brace style

| Corpus | Allman | K&R |
|--------|--------|-----|
| satoshi-nov2008 | 49% | 2% |
| satoshi-v0.1.0 | 45% | 11% |
| satoshi (v0.1.3) | 45% | 11% |

Roughly stable; slight Allman preference in the earliest material.

### Burrows' Delta on shared identifiers (intra-Satoshi distances)

| Corpus pair | Δ |
|-------------|---|
| satoshi-v0.1.0 vs satoshi (v0.1.3) | **0.0034** |
| satoshi-nov2008 vs satoshi (v0.1.3) | **0.3729** |
| satoshi (v0.1.3) vs Adam Back (closest non-Satoshi) | 0.78 |

The v0.1.0 ↔ v0.1.3 distance (0.003) is essentially noise — expected for the same project 11 months apart. The Nov 2008 ↔ v0.1.3 distance (0.37) is larger because the pre-release codebase is much smaller (only 3 files vs 22) and has different identifier coverage (no `db.*`, no `irc.*`, no `script.*` yet). Even so, **the Nov 2008 distance to v0.1.3 is half the distance from v0.1.3 to Adam Back** (0.37 vs 0.78), and one-quarter the distance to the most stylistically distant candidate (Sassaman at 1.44).

## What this rules in / out

**Rules in:**
- A single-author signal for Satoshi's code style across the 13-month launch window.
- The MFC Hungarian C-prefix convention as baseline Satoshi style from the earliest publicly accessible source, not an artifact of a later joiner.
- The 100% space-indent and line-comment preference as stable, idiosyncratic, and consistent across all three time points.

**Rules out:**
- A "multi-author Bitcoin during launch" reading where the MFC convention was contributed by a collaborator joining mid-2009. The convention was already present in November 2008, before any collaborator had even seen the code.
- A "Satoshi changed style after community feedback" reading. The post-public code (v0.1.0, v0.1.3) is stylistically continuous with the pre-public code (Nov 2008).

**Does not rule out:**
- That the entity behind "Satoshi" was a tight pair or small group who shared a single style from before launch. The intra-Satoshi consistency is consistent with a single author *and* with a group who calibrated on shared conventions before going public.
- That Satoshi's style was deliberately adopted to mimic an MFC-trained Windows developer as a misdirection. This is a low-probability scenario but the data cannot exclude it.

## Caveats

1. **Nov 2008 corpus is small** (3,305 LOC). Burrows' Delta is most reliable above ~5k LOC. We rely on the MFC Hungarian C-prefix proportion (which is robust even at small sample size because it's a percentage-of-identifiers measure, not a low-frequency word measure) rather than the Δ value itself.
2. **Provenance for Nov 2008** rests on the Finney-derived archival chain (Hal Finney preserved the privately distributed copy; it was later aggregated into `0xMagnuz/Bitcoin-v0.1`). We do not have a contemporary cryptographic anchor comparable to the v0.1.0 MD5.
3. **The MFC convention is a *trained-developer* fingerprint, not a *single-person* fingerprint.** Two MFC-trained developers writing in the same project would both produce the convention. This test rules out "MFC was added later," not "Satoshi is one person."

## Source citations

- `code-corpus/satoshi-nov2008/SOURCE.md` — Nov 2008 pre-release provenance.
- `code-corpus/satoshi-v0.1.0/SOURCE.md` — Jan 2009 v0.1.0 provenance with MD5 anchor.
- `code-corpus/satoshi/SOURCE.md` — Dec 2009 v0.1.3 ALPHA provenance (existing).
- `results/code-style-features.json` — full feature extraction for all three corpora.
- `https://github.com/0xMagnuz/Bitcoin-v0.1` — mirror used for both new corpora.
- `https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html` — Satoshi's v0.1.0 announcement, primary date anchor.
