# Satoshi Code Corpus — Bitcoin November 2008 pre-release

## Version

**Bitcoin pre-release, November 2008** — Satoshi distributed an early version of
the Bitcoin source privately to a small group (including Hal Finney) on the
cryptography mailing list, approximately two months before the public v0.1.0
release of 2009-01-08.

This is the **earliest publicly-accessible Satoshi source code** and predates
any community engagement with the project. As a stylistic sample it represents
Satoshi alone, with no feedback loops yet active.

## Source

- **Primary:** `https://github.com/0xMagnuz/Bitcoin-v0.1`, subdir `nov08/`.
- **Clone date:** 2026-05-27.
- **Maintainer note (per `0xMagnuz/Bitcoin-v0.1` README):** "In november 2008
  some sources were distributed privately"
- **License:** MIT/X11 (per Satoshi's later release license).

## Provenance chain

1. Satoshi distributed the source privately on the cryptography mailing list,
   November 2008. Recipients included Hal Finney (whose own collection eventually
   surfaced this material).
2. The Nov 2008 source was later aggregated into `0xMagnuz/Bitcoin-v0.1` under
   the `nov08/` subdirectory.
3. We do not have a primary cryptographic anchor for this material (no
   contemporary MD5 announcement comparable to v0.1.0's MD5). Provenance rests
   on the Finney-derived archival chain.

## Files Included (3 files, ~3.3k LOC)

This is the entire `nov08/` directory — Satoshi's pre-release source is just
three files. The codebase had not yet grown to the v0.1.0 scope.

| File | LOC |
|------|-----|
| `main.cpp` | 1307 |
| `main.h` | 1136 |
| `node.cpp` | 862 |
| **Total** | **3305** |

The small corpus size is a stylometric caveat — Burrows' Delta and related
features are most reliable above ~5k LOC. The MFC Hungarian C-prefix fingerprint
is computable from class declarations in `main.h` (which is the bulk of the
header file) and is the most diagnostic single test for this small corpus.

## Verification reproducibility

```bash
git clone --depth 1 https://github.com/0xMagnuz/Bitcoin-v0.1 /tmp/btc-v01-mirror
ls /tmp/btc-v01-mirror/nov08/
# main.cpp  main.h  node.cpp
```

## Why this corpus exists

If Satoshi's MFC Hungarian C-prefix fingerprint appears already in the November
2008 pre-release, this strengthens the "single Satoshi, consistent fingerprint
from the earliest material" reading and rules out the possibility that the MFC
convention emerged later (e.g., from a co-author joining mid-2009). If the
fingerprint is absent or substantially different in the Nov 2008 corpus, that
opens a multi-author-during-launch reading.

See [`forensics/intra-satoshi-style-drift.md`](../../forensics/intra-satoshi-style-drift.md)
for the analysis writeup.
