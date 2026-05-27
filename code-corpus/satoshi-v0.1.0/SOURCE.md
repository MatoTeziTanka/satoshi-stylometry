# Satoshi Code Corpus — Bitcoin v0.1.0 (Jan 2009 release)

## Version

**Bitcoin v0.1.0** — the first public Bitcoin release. Released by Satoshi on
SourceForge on **2009-01-08 14:27:40 EST** ([metzdowd cryptography list
announcement](https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html)).

This precedes the existing `code-corpus/satoshi/` corpus (Bitcoin 0.1.3 ALPHA,
December 2009) by ~11 months. The two corpora let us test **intra-Satoshi style
drift** across the launch window.

## Source

- **Primary:** `https://github.com/0xMagnuz/Bitcoin-v0.1` — archive maintained
  with cryptographic provenance to the original SourceForge release.
- **Original tarball:** `bitcoin-0.1.0.tgz`, MD5 `dca1095f053a0c2dc90b19c92bd1ec00`
  (verified at pull time, matches the documented MD5 from the announcement).
- **Clone date:** 2026-05-27.
- **License:** MIT/X11 (per Satoshi's `license.txt`, same as v0.1.3).

## Provenance chain

1. Satoshi posted `bitcoin-0.1.0.rar` to SourceForge on 2009-01-08; announced
   on metzdowd cryptography list same day.
2. The SourceForge link went dead post-2011. Hal Finney preserved a copy on
   bitcointalk.
3. `0xMagnuz/Bitcoin-v0.1` aggregates that preserved material with the original
   MD5 anchor documented in the repo README.

## Files Included (22 files, ~16.6k LOC)

Same exclusion discipline as the v0.1.3 corpus: machine-generated and
public-domain third-party files are excluded so the style fingerprint reflects
Satoshi's hand-written code only.

**Included:** `base58.h`, `bignum.h`, `db.cpp/h`, `headers.h`, `irc.cpp/h`,
`key.h`, `main.cpp/h`, `market.cpp/h`, `net.cpp/h`, `script.cpp/h`,
`serialize.h`, `ui.cpp/h`, `uint256.h`, `util.cpp/h`.

**Excluded (consistent with `code-corpus/satoshi/SOURCE.md`):**
- `sha.cpp/h` — public-domain Crypto++ 5.5.2 (Wei Dai / Steve Reid).
- `uibase.cpp/h` — wxFormBuilder machine-generated boilerplate.
- `uiproject.fbp`, `ui.rc`, `makefile*` — non-source build artifacts.

## Verification reproducibility

```bash
git clone --depth 1 https://github.com/0xMagnuz/Bitcoin-v0.1 /tmp/btc-v01-mirror
md5sum /tmp/btc-v01-mirror/bitcoin-0.1.0.tgz
# Expect: dca1095f053a0c2dc90b19c92bd1ec00
# Source files live at /tmp/btc-v01-mirror/bitcoin0.1/src/
```

## Why this corpus exists

The repo's MFC Hungarian C-prefix fingerprint is computed against Bitcoin v0.1.3.
A reasonable question is whether the fingerprint is stable across Satoshi's own
authoring period (single-author signal) or shifts (which would open a
multi-author-during-launch reading). Adding v0.1.0 lets us test the question.

See [`forensics/intra-satoshi-style-drift.md`](../../forensics/intra-satoshi-style-drift.md)
for the analysis writeup.
