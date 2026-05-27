# PGP for Windows 6.5.1i — provenance + use note

## Why this corpus is in the repo

The `code_style.py` analysis finds Satoshi's Bitcoin 0.1.x codebase uses
Microsoft Foundation Classes (MFC) Hungarian C-prefix class naming
(`CTransaction`, `CBlock`, `CKey`, `CCriticalSection`) at 5.4–9.6% of
identifiers — a 1990s–2000s Windows C++ enterprise pattern. None of the named
prose candidates (Back, Finney, Szabo, Dai, Sassaman) match it on the code
axis. The TrueCrypt 7.1a expansion (2026-05-27) ruled out the Le Roux /
Windows-C++ wildcard via TrueCrypt itself: TrueCrypt scores 0.1% Hungarian_C,
91% tab indent, 22 block + 35 line comments per KLOC — same fingerprint
profile as the other Unix-C / Unix-C++ candidates.

PGP for Windows 6.5.x is the most plausible *remaining* Windows-C++ MFC-era
codebase that has not been tested. PGP 6.5 was Network Associates' freeware
PGP release of 1999, the canonical cypherpunk-adjacent Windows-C++ codebase
of that era. It is the strongest available answer to the question "what does
the function-word distribution AND code style of a 1990s Windows-C++ MFC
codebase from this exact community actually look like?"

## Source

- **Mirror used:** `https://archive.org/details/pgp_sourcecode` (the
  `archive.org` curated collection of PGP source releases).
- **Specific archive:** `pgp651i-win-src.zip` (PGP 6.5.1i, the international
  release of PGP 6.5.1 — same source as the US release, distributed outside
  the US via book-form to comply with ITAR; stylometrically identical).
- **Direct download URL:**
  `https://archive.org/download/pgp_sourcecode/6.51i/pgp651i-win-src.zip`
- **Pull date:** 2026-05-27
- **Zip size:** 14,497,233 bytes (~13.8 MB)
- **Zip sha256:**
  `a2879e3b42988fe2bc7901e81ce6225174226009d8d1f492b0bc1f02c83cc8e6`
- **Top-level directory in zip:** `pgp651i/` (contents extracted into
  `code-corpus/pgp-6.5/` for analysis).
- **License:** PGP 6.5.1i was released under a non-commercial-use restrictive
  license (Network Associates source-code license, see `License.txt` in the
  archive). For this repo's purposes we **analyze** the source for stylistic
  features and **publish only aggregate statistics** — we do not redistribute
  PGP's source. The archive is reassembled at runtime via the pull commands
  below (`.gitignore` rule `code-corpus/**/*` excludes everything in this
  directory except this `SOURCE.md`).

## Corpus contents (after extraction)

- **C files (.c):** 733
- **C++ files (.cpp):** 261
- **Header files (.h):** 888
- **C++ header files (.hpp):** 2
- **Total source files:** 1,884
- **Total LOC (.cpp + .h + .c, recursive):** 567,408

Directory structure preserved (`clients/`, `libs/`, `pgpversion/`, `sdk/`,
etc.). `src/code_style.py` walks recursively via `rglob`. Build/installer/
packaging subdirectories contain no `.c`/`.cpp`/`.h` files and are ignored
implicitly.

## Authorship + scope

PGP 6.5 was developed by Network Associates' Total Network Security
division (the former Pretty Good Privacy Inc. team, acquired by NAI in 1997).
The codebase has multiple identified contributors visible in commit-corpus
artifacts and copyright headers (Phil Zimmermann, Will Price, Jon Callas,
Dave Del Torto, etc.). This is a **team codebase**, not a single-author
artifact. For stylometric purposes this is treated the same as the TrueCrypt
corpus: we analyze the codebase as a whole and read the result as the
**house style** of a Windows-C++ MFC-era cypherpunk-adjacent team.

The corpus is named `pgp-6.5` (the codebase) not after any individual
contributor.

## Why testing against Satoshi matters

Two hypotheses are being tested:

1. **Strong MFC fingerprint hypothesis:** If PGP 6.5 — the most plausible
   Windows-C++ MFC-era cypherpunk codebase — matches Satoshi's Hungarian_C
   rate, space-indent preference, and line-comment density simultaneously,
   then the MFC fingerprint is shared by a known community codebase from
   Satoshi's era and the "MFC matches nobody" claim must be narrowed to
   "MFC matches no individual candidate but matches the PGP team house style."

2. **Composite z-score discrimination hypothesis:** If PGP 6.5 matches on
   Hungarian_C alone (the single-axis test) but fails on the composite
   (Hungarian_C + space-indent + line-comment), then the composite score
   discriminates correctly where the single-axis test would have produced a
   false positive. This validates the composite z-score's reason for
   existing.

**Result (this analysis, 2026-05-27):** Hypothesis 2 is supported.
Hypothesis 1 is not.

- PGP 6.5 Hungarian_C rate: **0.8%** — 8× higher than every other named
  candidate (0.1–0.2%), but **8× below Satoshi** (6.4%) and 12× below the
  Bitcoin Nov-2008 pre-release corpus (9.6%).
- PGP 6.5 indent: 71% tabs / 29% spaces — opposite of Satoshi's 100% spaces.
- PGP 6.5 comments per KLOC: 67.4 block + 45.4 line — Satoshi is 1.0 block
  + 105.1 line (inverted ratio).
- PGP 6.5 Burrows' Delta from Satoshi (code function-words): 1.1055 — further
  than TrueCrypt's 0.8934.
- PGP 6.5 composite MFC z-score: **−1.27** (negative; mid-pack, *below*
  Sassaman at −1.17 and Back at −2.29 only). Satoshi composite: +3.35;
  Bitcoin Nov-2008: +4.92.

The MFC fingerprint as a composite remains uniquely Satoshi's. PGP 6.5 is
the closest non-Satoshi codebase on the Hungarian_C axis alone, but it
diverges on the indent and comment-density axes — exactly the failure mode
the composite z-score was designed to catch.

See `forensics/pgp-6.5-windows-mfc-test.md` for the full writeup.

## Verification reproducibility

```bash
mkdir -p /tmp/pgp-65-pull && cd /tmp/pgp-65-pull
curl -sL -o pgp651i-win-src.zip \
  "https://archive.org/download/pgp_sourcecode/6.51i/pgp651i-win-src.zip"
sha256sum pgp651i-win-src.zip
# Expect: a2879e3b42988fe2bc7901e81ce6225174226009d8d1f492b0bc1f02c83cc8e6
unzip -q pgp651i-win-src.zip
cp -r pgp651i/* /path/to/repo/code-corpus/pgp-6.5/
```

Then `python3 src/code_style.py` to regenerate `results/code-style-features.json`.
