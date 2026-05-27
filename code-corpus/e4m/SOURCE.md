# E4M 2.01 (Encryption for the Masses) — provenance + use note

## Why this corpus is in the repo

The PGP 6.5.1i Windows expansion (2026-05-27, commit `0d12155`) closed the
"could a 1990s Windows-C++ MFC-era cypherpunk-adjacent team codebase match
Satoshi" question — PGP 6.5 was the most plausible such codebase, scoring
0.8% Hungarian_C (8× below Satoshi's 6.4%) and composite z = −1.27.

The remaining untested code-axis wildcard was **e4m** (Encryption for the
Masses), Paul Le Roux's pre-TrueCrypt direct work from 1998–2000. e4m is
the direct predecessor of TrueCrypt — TrueCrypt v1.0 in 2004 was a fork of
e4m 2.0.2. The repo's TrueCrypt 7.1a test (2026-05-27, commit `a36eb31`)
ruled out TrueCrypt's house style as Satoshi-matching, but TrueCrypt is a
2004–2014 codebase that may have diverged from e4m's 1998–2000 original.
Testing e4m directly closes the Le Roux ruling.

Secondary sources describe e4m as "MFC-styled" (see Wikipedia, HandWiki,
LDAPWiki entries on E4M circa 1999). This corpus tests that claim against
the same fingerprint axes used for every other candidate.

## Source

- **Mirror used:** `https://github.com/SophiaAtkinson/E4M` (community
  preservation repo with the original binary + source distributions).
- **Specific archive:** `E4M201s.zip` (the source distribution for E4M 2.01,
  Windows 95/98/NT; the `s` suffix is the 1990s shareware convention for
  "source distribution," distinct from `E4M201.exe` which is the binary
  installer).
- **Direct download URL:**
  `https://github.com/SophiaAtkinson/E4M/raw/main/E4M201s.zip`
- **Pull date:** 2026-05-27
- **Zip size:** 414,052 bytes (~414 KB)
- **Zip sha256:**
  `65b4b94bd724b19be90680003003f1bd85c7174af3c7318ba1ef0a72b384f570`
- **Top-level directory in zip:** `e4m201/` (contents extracted into
  `code-corpus/e4m/` for analysis).
- **Internal dates:** files dated 1997-11 through 1999-09 (the codebase was
  active 1998–2000; v2.01 froze in September 1999, with v2.02a as the
  final release in 2000).
- **License:** E4M was distributed under a non-commercial-use restrictive
  license (see `License-E4M.TXT`, also preserved in
  `DrWhax/truecrypt-archive`). For this repo's purposes we **analyze** the
  source for stylistic features and **publish only aggregate statistics** —
  we do not redistribute e4m's source. The archive is reassembled at
  runtime via the pull commands below (`.gitignore` rule `code-corpus/**/*`
  excludes everything in this directory except this `SOURCE.md`).

### Why 2.01 and not 2.02a

E4M 2.02a (2000) was the final release. The community-preservation archive
at `SophiaAtkinson/E4M` ships 2.00 and 2.01 source distributions but not
2.02a source. The TrueCrypt v1.0 (2004) source — derived from "e4m 2.0.2"
per its own README — would in principle let us approximate 2.02a, but
TrueCrypt v1.0 already mixes in non-e4m TrueCrypt-team additions and is
not a clean snapshot of the e4m codebase. We use 2.01 as the
best-available pure-Le-Roux artifact. The 2.01 → 2.02a delta is small
(~6 months of bug fixes per the Wikipedia article on E4M) and is unlikely
to shift the stylistic profile materially.

## Corpus contents (after extraction)

- **C files (.c):** 41
- **Header files (.h):** 52
- **C++ files (.cpp):** 0
- **C++ header files (.hpp):** 0
- **Total source files:** 93
- **Total LOC (.c + .h, recursive):** 18,515

Directory structure preserved (`crypto/`, `ntdriver/`, `volmount/`,
`volformat/`, `pwddlg/`, `setup/`, etc.). `src/code_style.py` walks
recursively via `rglob`.

### Structural note: e4m is pure C, not C++

E4M 2.01 contains **zero `.cpp` files**. The codebase is implemented entirely
in C with Windows NT driver headers (`ntdriver/`) and Win32 GUI code
(`volmount/`). This has a direct stylometric consequence: **the Hungarian_C
class-name pattern (`class C[Capital]`) cannot appear in e4m**, because C has
no `class` keyword. Le Roux's preferences on this axis are structurally
invisible in this corpus — the same gap as Back's Hashcash (also pure C),
discussed in `forensics/nyt-april-2026-adam-back.md`.

The other two MFC fingerprint axes (space-indent ratio, line-comment
density) are not language-restricted and remain testable.

## Authorship + scope

E4M was copyrighted "Paul Le Roux 1998–2000" per the `License-E4M.TXT`
shipped with every distribution. The codebase is sole-authored in
attribution; commit history is not preserved (the distribution model was
versioned zips, not VCS). For stylometric purposes this is treated as
**Le Roux's direct single-author code style** — the cleanest such artifact
available, since TrueCrypt's "TrueCrypt Foundation" pseudonymous successor
team mixed Le Roux's lineage with anonymous later contributors.

The corpus is named `e4m` (the codebase) not `le-roux` to maintain the
codebase-not-author naming convention used for `truecrypt` and `pgp-6.5`.

## Why testing against Satoshi matters

The Le Roux wildcard has been argued in popular press as a plausible Satoshi
candidate on the basis of (a) Windows-C++-crypto background, (b) operational
secrecy, (c) capability to author cryptographic systems. TrueCrypt 7.1a was
ruled out 2026-05-27. e4m 2.01 closes the prior question by testing
Le Roux's actual single-author code rather than the multi-author TrueCrypt
team derivative.

**Result (this analysis, 2026-05-27):** e4m 2.01 does **not** match
Satoshi's fingerprint on any testable axis.

- Hungarian_C: 0.1% (structurally constrained — no .cpp files), same as
  Back, Finney, Dai, TrueCrypt.
- Indent: 87% tabs / 13% spaces (Unix-on-Windows convention; opposite of
  Satoshi's 100% spaces).
- Comment density: 80.7 block + 1.4 line per KLOC (block-comment-dominated;
  Satoshi is line-comment-dominated at 1.0 block + 105.1 line — the ratio
  is completely inverted).
- Composite MFC z-score: **−2.52** (third-from-last; only Finney is lower).
  Satoshi composite: +3.67. The 6.2 z-score gap is the quantitative measure
  of "e4m is not Satoshi's house style."

The Le Roux ruling now stands on **two independent codebases** — TrueCrypt
7.1a (the derivative team work, 2011) and e4m 2.01 (the pre-TrueCrypt
direct single-author work, 1999). Both fail on every testable MFC
fingerprint axis. See `forensics/e4m-mfc-test.md` for the full writeup.

## Verification reproducibility

```bash
mkdir -p /tmp/e4m-pull && cd /tmp/e4m-pull
curl -sL -o E4M201s.zip \
  "https://github.com/SophiaAtkinson/E4M/raw/main/E4M201s.zip"
sha256sum E4M201s.zip
# Expect: 65b4b94bd724b19be90680003003f1bd85c7174af3c7318ba1ef0a72b384f570
unzip -q E4M201s.zip
cp -r e4m201/* /path/to/repo/code-corpus/e4m/
```

Then `python3 src/code_style.py` to regenerate `results/code-style-features.json`.
