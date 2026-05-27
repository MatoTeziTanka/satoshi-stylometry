# TrueCrypt 7.1a — provenance + use note

## Why this corpus is in the repo

The `code_style.py` analysis finds Satoshi's Bitcoin 0.1.3 codebase uses Microsoft Foundation Classes (MFC) Hungarian C-prefix class naming (`CTransaction`, `CBlock`, `CKey`, `CCriticalSection`) at 5.4–6.4% of identifiers — a 1990s–2000s Windows C++ enterprise pattern. None of the five named candidates (Back, Finney, Szabo, Dai, Sassaman) match it. The repo's `README.md` "What would strengthen this analysis" section calls out testing against Windows-era C++ codebases as the highest-value extension, naming **Paul Le Roux** as the wildcard candidate via TrueCrypt.

TrueCrypt's origin story:
- e4m (Encryption for the Masses) — Paul Le Roux, 1997–1999.
- TrueCrypt — anonymous "TrueCrypt Foundation," 2004–2014. Code lineage from e4m is documented.
- 7.1a is the last full TrueCrypt release before the May 2014 audit-advisory takedown.

## Source

- **Mirror used:** `https://github.com/AuditProject/truecrypt-verified-mirror` (Open Crypto Audit Project's verified archive).
- **Clone date:** 2026-05-27
- **HEAD at clone time:** Open Crypto Audit Project's published `file_digests.txt` lists SHA-256:
  - `e6214e911d0bbededba274a2f8f8d7b3f6f6951e20f1c3a598fc7a23af81c8dc  ./Source/TrueCrypt 7.1a Source.tar.gz`
- **Tarball:** `TrueCrypt 7.1a Source.tar.gz` extracted to `code-corpus/truecrypt/`.
- **License:** TrueCrypt License Version 3.0 (restrictive; redistribution requires the source tree be unmodified and licenses preserved). For this repo's purposes we **analyze** the source for stylistic features and **publish only aggregate statistics** — we do not redistribute TrueCrypt's source. The tarball is reassembled at runtime via the pull script per the repo convention (see `.gitignore` rule for `code-corpus/*/*.c|.cpp|.h`).

## Corpus contents (after extraction)

- **C++ files (.cpp):** 120
- **C files (.c):** 49
- **Header files (.h):** 208
- **Total LOC (.cpp + .h, recursive):** 53,014

Directory structure preserved (Boot/, Common/, Core/, Crypto/, Driver/, Format/, Main/, Mount/, Setup/, Volume/). `src/code_style.py` walks recursively via `rglob`.

## Authorship caveat

TrueCrypt's authorship has never been publicly confirmed. The "TrueCrypt Foundation" published under pseudonyms. **Paul Le Roux is widely speculated as the author of e4m, the TrueCrypt predecessor**, on the basis of code-comment artifacts and circumstantial evidence — but the attribution is contested and not primary-source defensible per this repo's citation discipline. The corpus is named `truecrypt` (the codebase) not `le-roux` (the speculated author).

## Why testing against Satoshi matters

The README hypothesis: if TrueCrypt's code style matches Satoshi's MFC fingerprint, that strengthens the "Le Roux / Windows-C++ enterprise developer" wildcard reading. If it doesn't, that further strengthens the "matches no candidate" finding.

**Result (this analysis, 2026-05-27):** TrueCrypt 7.1a does NOT use the MFC `C[Capital]` Hungarian class-name convention. Quick grep:

```
grep -rh "^class C[A-Z]" --include='*.cpp' --include='*.h' code-corpus/truecrypt | sort -u
(no matches)
```

TrueCrypt class names follow PascalCase without the C prefix: `WizardPage`, `TrueCryptFactory`, `TrueCryptFormatCom`, `BaseCom`. **The MFC fingerprint is absent from TrueCrypt.** See `results/code-style-features.json` after re-running `python3 src/code_style.py` for the full Burrows' Delta.

## Verification reproducibility

```bash
git clone --depth 1 https://github.com/AuditProject/truecrypt-verified-mirror.git /tmp/tc-mirror
cd /tmp/tc-mirror
# Verify SHA matches file_digests.txt
sha256sum "Source/TrueCrypt 7.1a Source.tar.gz"
# Expect: e6214e911d0bbededba274a2f8f8d7b3f6f6951e20f1c3a598fc7a23af81c8dc
tar xzf "Source/TrueCrypt 7.1a Source.tar.gz" -C /tmp/
cp -r /tmp/truecrypt-7.1a-source/* /path/to/repo/code-corpus/truecrypt/
```
