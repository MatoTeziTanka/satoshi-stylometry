# Adam Back — Hashcash C source

## Source
- **Repository:** `github.com/hashcash-org/hashcash` (canonical reference imported from www.hashcash.org)
- **Clone date:** 2026-05-26
- **Branch/commit:** master, HEAD = `66d5c9b Merge pull request #2 from ar-/add-java`
- **Upstream provenance:** README states "Imported original reference implementation from www.hashcash.org. Adding more in the future."
- **License:** Multi-license (CPL / public domain / BSD / LGPL 2.1 / GPL 2 at user's choice), per `c/LICENSE` in upstream

## Corpus contents
- **Files included:** 34 (all `.c` and `.h` under `c/` except `getopt.c` / `getopt.h`)
- **Total LOC:** 10,370
- **Filtering:** Excluded `getopt.c` / `getopt.h` (Copyright Free Software Foundation, 1987-1993 — not Back's code).
- **`contrib/hashfork.c`:** Excluded (not Back's primary code, contributed module)

## Attribution confidence: **HIGH**

Every `.c` and `.h` file in the included set carries Back's stylistic fingerprint:
- Distinctive first-line magic comment: `/* -*- Mode: C; c-file-style: "stroustrup" -*- */` (present in 30+ files)
- Email signature `Adam Back <adam@cypherspace.org>` in `libsha1.c` header block
- Stylistic conventions (4-space indent, Stroustrup brace style, `byte` typedef, `if defined(...)` blocks for portability) are uniform across the corpus.

The `fastmint_*` family of files (12 of 34) are speed-optimised mint kernels for different ISA/precision combinations (ANSI / MMX / Altivec), all written by Back as part of libfastmint. They share `libfastmint.c`'s code style and are credibly his.

The SHA1 implementation (`sha1.c`, `libsha1.c`, `sha1.h`, `sha1test.c`) is FIPS 180-1 reference math, but Back implemented these himself (header in `libsha1.c` confirms Back as author, not Steve Reid or another standard SHA1 author).

## Concerns / caveats
- Some files (e.g. `lock.c`, `random.c`, `types.h`) lack explicit attribution headers, but their style matches Back's other files exactly and they are part of the canonical hashcash package signed by Back.
- The repo also contains a `java/` directory (excluded — wrong language) and `sh/` (shell scripts — excluded by file-type filter).
- Final LOC (10.4k) is below the 16k Bitcoin 0.1 target but within the stated 5k-20k acceptable range.
