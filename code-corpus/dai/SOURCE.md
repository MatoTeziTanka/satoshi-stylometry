# Wei Dai — Crypto++ early-version source

## Source
- **Archive:** `https://sourceforge.net/projects/cryptopp/files/cryptopp/5.2.1/cryptopp521.zip/download`
- **Version:** Crypto++ 5.2.1 (released 2004; selected as the **earliest version available via SourceForge**)
- **Note on version selection:** cryptopp.com currently hosts only 5.6.2 (2013) and later. Crypto++ 5.2.1 from SourceForge is the **earliest still-distributed** archive. Wayback Machine has earlier-versioned listings but the actual zip downloads return HTML wrappers (not the binaries). 5.2.1 is appropriate for a Bitcoin-0.1 (2008) stylometric baseline — it pre-dates Bitcoin by 4 years and is still well within Dai's pre-mass-contribution era.
- **Pull date:** 2026-05-26
- **License:** Public domain (compilation copyright Wei Dai 1995-2004; individual files placed in public domain by their respective authors)

## Corpus contents
- **Files included:** 191 (`.cpp` and `.h`)
- **Total LOC:** 51,108
- **Filtering:** Strict author-attribution filter applied via `/tmp/code-pulls/filter_dai.py`:
  - **Kept (`KEEP`):** 93 files with explicit header `// X.cpp - written and placed in the public domain by Wei Dai` (no co-author, no "based on", no "from")
  - **Kept (`KEEP-NOHDR`):** 97 files with no explicit attribution line — these are header files, S-box constants files, glue code, etc. that ship inside Dai's distribution and bear his idiomatic style.
  - **Kept (`KEEP-DESC`):** 1 file with a descriptor-only first line (no author claim at all)
  - **Excluded (`EXCLUDE-EXPLICIT`):** 55 files matching the License.txt non-Dai contributor list (Joan Daemen's 3way, Leonard Janke's seal/cast, Phil Karn's des, Andrew Kuchling's md2/md4, Colin Plumb's md5, Kevin Springle's camellia/shacal2/ttmac/whrlpool/ripemd, Paulo Baretto's rijndael/skipjack/square, Richard De Moliner's safer, Matthew Skala's twofish, Brian Gladman's mars, Frank Palazzolo's base32, plus tea, wake, gost, tiger, panama, etc.)
  - **Excluded (`EXCLUDE-HEADER`):** 1 file whose first-line header named another author (`sha.cpp` — "modified by Wei Dai from Steve Reid's public domain sha1.c")
  - **Excluded (`EXCLUDE-COMPANION`):** 1 file (`squaretb.cpp` — S-box table companion to Paulo Baretto's `square.cpp`)
- The filter script (`/tmp/code-pulls/filter_dai.py`) is preserved for reproducibility.

## Attribution confidence: **HIGH** (after filtering)

- The 93 explicit-attribution files are unambiguously Dai's solo work.
- The 97 no-header files are Dai's by inclusion convention — they are header files for his own algorithms (`adler32.h`, `dh.h`, `dsa.h`, `rsa.h`, `cryptlib.h`, etc.), table-data files for Dai-implemented algorithms, and Dai's glue/build files (`pch.cpp`, `bench.h`).
- The "Copyright (c) 1995-2004 Wei Dai" header on the License.txt confirms Dai is the sole "compilation copyright" holder.

## Concerns / caveats
- Crypto++ contains many algorithm-import files. **Without strict filtering, this corpus would mis-attribute crypto-primitive authors (Daemen, Karn, Baretto, etc.) as Dai.** The filter applied removes 55 explicit non-Dai files plus 3 edge cases.
- 51K LOC is significantly **larger** than Bitcoin 0.1's 16K — for stylometric comparison this is a feature (more samples = better statistical power for the Dai class) but may require down-sampling depending on the analysis method.
- Crypto++ is library code (clean, abstract, template-heavy) while Bitcoin 0.1 is application code (concrete, network-bound, mixed paradigm). Style differences may reflect domain rather than author identity.
- Dai's style here is **C++** with heavy template metaprogramming; Bitcoin 0.1 is also C++ but with a much lower template/abstraction load. Useful baseline regardless.
