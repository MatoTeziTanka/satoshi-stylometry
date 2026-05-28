# Bitcoin SV v1.0.0 — provenance + use note (Wright code-candidate corpus)

## Why this corpus is in the repo

The Burrows' Delta + composite MFC z-score analysis (Hungarian_C,
space-indent ratio, line-comment density) has been run against the named
prose-shortlist candidates (Back, Finney, Szabo, Dai, Sassaman) and against
two Windows-C++ MFC-era reference codebases (TrueCrypt 7.1a, PGP 6.5.1i).
None of those individuals match Satoshi's MFC fingerprint on the composite,
and the PGP house-style test established that even a 1990s Windows-C++
cypherpunk codebase fails the composite where Satoshi succeeds.

**Craig Wright** is a separate, well-known public claimant to the Satoshi
identity. The UK High Court decision **COPA v Wright [2024] EWHC 1198 (Ch)**
(Mellor J) ruled that Wright was not Satoshi Nakamoto, that he had forged
documents and lied on oath in support of his claim, and Wright was
subsequently enjoined from further "I am Satoshi" litigation in the UK.
Adding a Wright code-candidate corpus to this repository is consistent with
the existing scope of the project: empirical, public, named-candidate
stylometric comparison against Satoshi's Bitcoin 0.1.x code. The legal
posture is safe per the COPA judgment; no claim about Wright's identity is
made beyond what the data shows.

There is no public personal C/C++ codebase authored by Wright. His most
plausible proxy is **Bitcoin SV (BSV)** — the "Satoshi's Vision" hard fork
created in November 2018 under nChain's direction with Wright as figurehead
and Chief Scientist. Wright did not write most of the BSV source code (see
"Authorship + scope" below), but BSV is the codebase most closely
associated with him and the closest available analogue to a "Wright-era
team codebase" in the same way PGP 6.5 is a "Network Associates team
codebase." This corpus is therefore analyzed under the **house-style**
methodology (the team that worked under Wright's nominal technical
leadership), not the **author-personal** methodology.

## Source

- **Canonical repo:** `https://github.com/bitcoin-sv/bitcoin-sv`
  (verified 2026-05-27; the alternate `bsvblockchain/bitcoin-sv` namespace
  returns 404).
- **Specific tag:** `v1.0.0` — the first non-beta tagged release after the
  BSV / BCH split, representing the post-fork stabilization point closest
  to the November-2018 fork date.
- **Tag commit:** `7fd177c7c443ff7723d88c5465fbf39285388e30`
  (commit subject: "Fix Genesis post-merge compile error", 2020-01-15).
  Tag object: `d5154c232388ace70f196601de28c2c5acf74ee3` (peels to commit
  above).
- **Pull date:** 2026-05-27
- **git archive sha256** (verification anchor; tarball of the v1.0.0
  `src/` subtree):
  `b8b1c83581268167f49550504aa015d77338f45ab0a45133335fe11f17996df3`
- **License:** Open BSV License (Copyright (c) 2019 Bitcoin Association).
  See `_clone/LICENSE` in the cloned source. For this repository's
  purposes we **analyze** the source for stylistic features and **publish
  only aggregate statistics** — we do not redistribute BSV's source. The
  archive is reassembled at runtime via the pull commands below
  (`.gitignore` rule `code-corpus/**/*` excludes everything in this
  directory except this `SOURCE.md`).

## Corpus contents (after extraction)

Only the `src/` subtree of the BSV repository is included — this matches
the scoping convention applied to every other code corpus in this project
(`code-corpus/satoshi-v0.1.0/src/`, `code-corpus/truecrypt/src/`, etc.).

- **C files (.c):** 18
- **C++ files (.cpp):** 255
- **Header files (.h):** 295
- **C++ header files (.hpp):** 0
- **Total source files:** 568
- **Total LOC (.c + .cpp + .h + .hpp, recursive):** 159,921

Directory structure preserved (`src/wallet/`, `src/crypto/`, `src/script/`,
`src/primitives/`, `src/rpc/`, `src/policy/`, `src/consensus/`, `src/mining/`,
`src/secp256k1/`, `src/leveldb/`, `src/univalue/`, `src/zmq/`, `src/bench/`,
`src/test/`, `src/seeder/`, `src/support/`, `src/compat/`, `src/config/`).
`src/code_style.py` walks recursively via `rglob`.

## Authorship + scope (THE LOAD-BEARING SECTION)

Bitcoin SV is a **team codebase**, not a Wright-personal codebase. This
must be stated explicitly because the stylometric inference is sensitive
to how the corpus is labeled.

### Wright's personal commit count: 0

```
git log --all --author="Craig Wright" --oneline
git log --all --author="craig wright" --oneline
git log --all --author="c.wright" --oneline
git log --all --author="S. Wright" --oneline
git log --all --author="wright" --oneline
```

All five queries return **zero** commits in the BSV v1.0.0 history. The
`wright-commits.txt` file in this corpus directory is therefore empty.
There is also no commit message in the BSV v1.0.0 history that mentions
"Wright" in any case.

This means **Approach 2 (Wright-personal stylometry) is not feasible from
the BSV codebase**. The corpus is analyzed under Approach 1 (house style)
only.

### Top-15 authors by commit count (BSV v1.0.0 history, total 15,710 commits)

```
4371  Wladimir J. van der Laan      (Bitcoin Core maintainer, pre-fork)
1271  Pieter Wuille                  (Bitcoin Core / Blockstream)
1101  Gavin Andresen                 (Bitcoin Core, post-Satoshi lead)
 639  Philip Kaufmann                (Bitcoin Core)
 533  Jeff Garzik                    (Bitcoin Core, BitPay)
 517  Cory Fields                    (Bitcoin Core)
 454  Matt Corallo                   (Bitcoin Core)
 440  Amaury SECHET                  (Bitcoin ABC / BCH lead)
 419  MarcoFalke                     (Bitcoin Core)
 412  Jonas Schnelli                 (Bitcoin Core)
 326  Amaury Séchet                  (same as #8, accented variant)
 291  Luke Dashjr                    (Bitcoin Core)
 273  Richard Mills                  (BSV / nChain era)
 247  Gregory Maxwell                (Bitcoin Core)
 245  s_nakamoto                     (Satoshi's own commit handle)
```

610 unique author handles total. The commit-history root is
**2009-08-30** — three days into the Satoshi-era public repository —
because BSV's history is the unbroken Satoshi → Bitcoin Core → Bitcoin
ABC → Bitcoin SV chain. This is the *forked-from-Bitcoin-Core inheritance
issue*: most of the 159,921 LOC in this corpus was not authored by anyone
associated with Wright. The codebase carries:

1. Direct Satoshi-era code (`s_nakamoto`, 245 commits, the actual Satoshi
   committer handle from the SourceForge / pre-GitHub bitcoin repository
   imported into the GitHub history).
2. The full Bitcoin Core development lineage 2010–2017 (van der Laan,
   Wuille, Andresen, Garzik, Corallo, Maxwell, Dashjr, etc.).
3. Bitcoin Cash divergence from August 2017 (`Amaury SECHET` / Bitcoin
   ABC lead) and the Bitcoin ABC team's ~2017–2018 work.
4. nChain / BSV-era post-November-2018 work (Richard Mills and other
   nChain engineers). This is the only layer plausibly attributable to
   Wright's technical leadership.

The corpus is named `wright-code` for catalog-symmetry with the existing
`wright-prose` corpus (Wright's whitepapers and public writings), and
because BSV is the codebase publicly associated with Wright. Despite the
directory name **this is not a Wright-personal corpus** and should not be
interpreted as one.

## Why testing against Satoshi matters

Two hypotheses are being tested:

1. **Wright-house-style hypothesis:** If BSV v1.0.0 — the codebase developed
   under Wright's nominal technical leadership at nChain — matches
   Satoshi's MFC fingerprint (Hungarian_C + space-indent + line-comment
   density) on the composite, this would be evidence that the cultural
   programming style of the BSV team includes the MFC pattern. Given the
   forked-from-Bitcoin-Core inheritance issue (the BSV codebase **contains
   actual Satoshi-era code** including 245 `s_nakamoto` commits), this
   hypothesis is essentially **guaranteed to be confirmed at some level**
   — the corpus literally contains Satoshi-authored files. The genuine
   question is *to what degree* the post-fork additions and modifications
   maintain the MFC fingerprint.

2. **Composite-bias-confirmation hypothesis:** If BSV v1.0.0 matches
   Satoshi on the composite, this confirms the composite **cannot
   distinguish a forked-from-Satoshi codebase from Satoshi itself**, which
   is the expected and correct behavior — Satoshi's code is the genetic
   ancestor of this code. The negative result (composite high on both
   Satoshi and BSV) is the *evidence-of-inheritance* signal.

A more discriminating test is running the analysis on **post-fork
diff-only** code (files added to BSV after the August-2018 split from
Bitcoin ABC). This follow-up was completed 2026-05-28 — see
[`code-corpus/wright-bsv-diff/SOURCE.md`](../wright-bsv-diff/SOURCE.md)
and [`forensics/wright-bsv-diff-test.md`](../../forensics/wright-bsv-diff-test.md).

**Result:** 91 net-new files (18.4k LOC, zero Satoshi commits,
exclusively authored by 15 named nChain/Slovenia engineers — Richard
Mills, Arkadiusz Kolodziejski, Chris Gibson, Daniel Connolly, Domen
Vrankar, et al.) score composite z = **+3.53** — *higher* than this
full-snapshot's +2.43. The nChain team consciously preserved Satoshi's
`C[Capital]` Hungarian naming + 100% space indentation + `//` line-comment
density in net-new code, consistent with BSV's stated "Satoshi's Vision"
mission. **The MFC composite is therefore a measure of adoptable
conventions, not unique authorship**; it rules OUT candidates whose
conventions differ from Satoshi but cannot rule IN any author whose
conventions match.

## Caveats (read before using)

1. **Forked-from-Bitcoin-Core inheritance.** This is the dominant effect.
   The corpus contains 245 commits authored by `s_nakamoto` (Satoshi's
   own committer handle) and 4,371 commits by Wladimir J. van der Laan
   (Bitcoin Core lead maintainer). Any MFC-fingerprint match between BSV
   and Satoshi is *expected* and does not constitute Wright→Satoshi
   evidence of any kind. The opposite is the live question: would BSV
   diverge from Satoshi's style on the composite?
2. **Zero Wright commits.** Approach 2 (Wright-personal stylometry) yields
   nothing from the BSV codebase. If the analysis goal is "what does
   Wright's individual code style look like?", the BSV corpus cannot
   answer that — Wright is a figurehead, not a committer, in this
   codebase.
3. **Tag selection is not value-neutral.** v1.0.0 (Jan 2020) is ~14 months
   after the BCH→BSV fork (Nov 2018). The post-fork divergence had time to
   accumulate. Earlier snapshots (v0.1.0, Nov-2018) might show less
   post-fork mutation, but they were beta releases and the brief
   specifies the "earliest tagged release closest to fork-from-BCH point"
   — v1.0.0 is the chosen interpretation as the earliest non-beta v1.x
   tag.
4. **License posture.** Open BSV License is restrictive about
   redistribution. This corpus directory's `.gitignore` policy treats
   source files as not-for-redistribution; only this `SOURCE.md` and
   `wright-commits.txt` are checked into the project repository.

## Verification reproducibility

```bash
mkdir -p /tmp/wright-code-pull && cd /tmp/wright-code-pull
git clone --branch v1.0.0 --single-branch \
  https://github.com/bitcoin-sv/bitcoin-sv _clone
cd _clone
git rev-parse HEAD
# Expect: 7fd177c7c443ff7723d88c5465fbf39285388e30
git archive --format=tar v1.0.0 src | sha256sum
# Expect: b8b1c83581268167f49550504aa015d77338f45ab0a45133335fe11f17996df3
find src -type f \( -name '*.c' -o -name '*.cpp' -o -name '*.h' \
  -o -name '*.hpp' \) | wc -l
# Expect: 568
find src -type f \( -name '*.c' -o -name '*.cpp' -o -name '*.h' \
  -o -name '*.hpp' \) -print0 | xargs -0 cat | wc -l
# Expect: 159921
git log --all --author="Craig Wright" --oneline | wc -l
# Expect: 0
```

Then copy `_clone/src/` into `code-corpus/wright-code/src/` and run
`python3 src/code_style.py` to regenerate `results/code-style-features.json`.
