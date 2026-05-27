# Len Sassaman — Mixmaster source (ATTRIBUTION CAVEAT — READ FIRST)

## Source
- **Repository:** `github.com/crooks/mixmaster`
- **Pull date:** 2026-05-26
- **Clone depth:** Initial shallow (`--depth 1`), then `--unshallow` for git-blame analysis (commit history goes back to 2004-06-07; pre-2004 history was lost in the SVN→Git migration)
- **License:** Mixmaster License Agreement (per `Mix/COPYRIGHT`) — derived from Anonymizer Inc. license, with seven copyright holders listed (see below)
- **Software:** Mixmaster 3.0 (anonymous remailer, the C implementation referenced by RFC draft-sassaman-mixmaster)

## Corpus contents
- **Files included:** 44 (`.c` / `.h` files from `Mix/Src/` — the Mixmaster 3.0 source tree)
- **Total LOC:** 23,450
- **Filtering:** No author-level filtering applied — the codebase is co-authored and per-line attribution is unrecoverable (see below).
- Excluded: `Mix2.0/Src/*` (Mixmaster 2.0, originally by Lance Cottrell 1995; less Sassaman content), `debian/`, `Docs/`, `web/`

## Attribution confidence: **LOW** — **THIS IS A CO-AUTHORED CORPUS, NOT A SASSAMAN-SOLO CORPUS**

This is the **honest gap** to flag for the stylometric analysis. The `Mix/COPYRIGHT` file lists SEVEN copyright holders 1999-2008:

```
Copyright (c) 1999-2000 Anonymizer Inc.
Copyright (c) 2000-2002 Ulf Moeller
Copyright (c) 2001-2002 Janis Jagars
Copyright (c) 2001-2007 Peter Palfrader
Copyright (c) 2001-2008 Len Sassaman
Copyright (c) 2004-2008 Colin Tuckley
Copyright (c) 2007-2008 Steve Crook
```

Git-blame analysis of the cloned repo (post-unshallow) shows Sassaman ("rabbi" username) authored at most **3% of lines in any single file**. The highest-Sassaman files by blame % are:

| file | rabbi% | rabbi lines / total |
|---|---|---|
| `service.c` | 3% | 11/331 |
| `chain.c` | 1% | 5/388 |
| `config.h` | 1% | 7/404 |
| `main.c` | 0.2% | 2/842 |

**Caveats on the blame numbers:** The repo's git history starts in 2004 (SVN→Git import collapsed all pre-2004 history into a single initial commit by "colin"). So git-blame credits "colin" with code that was *originally* written by Cottrell, Moeller, Sassaman, Palfrader between 1995-2003. The blame numbers above understate Sassaman's true contribution but the underlying problem is unfixable from this repo alone.

## What this corpus IS useful for
1. **Negative control / cypherpunk-tradition reference:** Bitcoin 0.1 emerged from the same cypherpunk community that produced Mixmaster. Even without single-author attribution, the corpus represents the *style cluster* Satoshi was writing within.
2. **Counter-example:** If Satoshi's style strongly matches Mixmaster, that suggests Satoshi was steeped in the anonymity-remailer tradition (Sassaman/Cottrell/Palfrader/Moeller circle). If it doesn't match, it weakens an indirect Sassaman hypothesis.

## What this corpus is NOT useful for
- Individual Sassaman authorship attribution. Treat any "Sassaman match" finding as **community-style match, not personal-style match**.

## Alternative Sassaman-attributed sources investigated and rejected
- **Mixminion** (`github.com/nmathewson/mixminion`): Python implementation by Nick Mathewson; Sassaman co-authored the *spec* and *RFC drafts* but not the C code. Wrong language anyway.
- **`github.com/sassaman/*`**: No publicly indexed Sassaman code repo exists.
- **Code Manuscript / Memorial repos** (e.g. `vecna/Rabbisteg`): JavaScript memorial library written *for* Sassaman after his death, not by him.

If a stronger Sassaman-specific corpus surfaces (e.g. Wayback Machine recovery of his personal site `abditum.com`, or release of his university work), it should replace this one.

## Concerns / caveats
- LOC (23,450) is the highest of the 4 candidates but the lowest in real attribution density.
- Recommend results for "sassaman" candidate be reported with an explicit caveat in the public paper.
