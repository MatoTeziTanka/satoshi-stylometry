# Hal Finney — RPOW (Reusable Proofs of Work) C source

## Source
- **Repository:** `github.com/nakamotoinstitute/RPOW`
- **Clone date:** 2026-05-26
- **Branch:** master (depth=1)
- **Upstream provenance:** Per README, "Special thanks to Fran and Jason Finney, Hal's wife and son, for sharing the original RPOW code and website files." Archived by the Satoshi Nakamoto Institute after rpow.net went down in 2014.
- **License:** AGPL-3.0 (per repo) — the **original repo contains two branches**: `master` (with maintainer fixes for modern compilers) and a branch with code "exactly as Hal Finney wrote it". We pulled `master` from depth=1, which captures the modern-friendly variant. If pure-Finney baseline matters, the unmodified branch should be re-pulled.
- **Original software:** RPOW 1.0 (2004), targeting IBM 4758 secure cryptographic coprocessor

## Corpus contents
- **Files included:** 40 (all `.c` / `.h` under `client/`, `common/`, `scc/`, `server/`)
- **Total LOC:** 11,940
- **Filename convention:** Files are prefixed by source directory to disambiguate (e.g. `client__gbignum.c` vs `scc__gbignum.c` — same logical module compiled against different SDKs)
- **Filtering:** Excluded `server/sha1.c` and `server/sha.h` (Steve Reid / Aaron D. Gifford public-domain SHA1 — explicitly marked "NO COPYRIGHT - THIS IS 100% IN THE PUBLIC DOMAIN" in the file header, derived from `ftp://ftp.funet.fi/pub/crypt/hash/sha/sha1.c`).
- Excluded the `scc/installed/` directory (compiled binaries `.rod`/`.xld`/`.map`, not source).

## Attribution confidence: **VERY HIGH**

- 38 of 40 included files carry explicit `Copyright (C) 2004 Hal Finney` headers.
- The remaining 2 (`scc/persist.c`, `scc/rpowscc.h`) lack copyright headers but are unmistakably Finney's by content (RPOW SCC server internals, with Finney's signature inline doc style — see e.g. the Calvin Coolidge quote at top of `persist.c`).
- No co-author markers found anywhere in the codebase.
- This is the closest thing to a Finney-solo C corpus that exists publicly.

## Concerns / caveats
- RPOW targets the IBM 4758 SCC and uses vendor headers (`<scctypes.h>`, `<scc_int.h>`, `<sccModMath.h>`) — some constructs (data types, error codes) reflect the SDK rather than Finney's organic style. The reverse is also true: the file structure and idiomatic glue ("DEFAGENT;", "sccRequestHeader_t request;" patterns) are Finney's.
- Total LOC (11.9k) is within the 5k-20k target range and close to Bitcoin 0.1's 16k.
- The 2004 timestamp puts this **4 years before** Bitcoin 0.1 — temporal gap should be acknowledged in stylometric comparison.
