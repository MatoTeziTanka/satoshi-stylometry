# Bitcoin SV — diff-only corpus (BSV-team net-new files, fork→v1.0.0)

## Why this corpus exists

The companion corpus `code-corpus/wright-bsv/` contains the **full** Bitcoin
SV v1.0.0 source tree (568 files, ~160k LOC). That corpus is
**inheritance-confounded**: it includes 245 commits authored by Satoshi
(`s_nakamoto`) and 15,710 total commits across 610 author handles
spanning the entire Bitcoin Core lineage back to Satoshi's original
2008-2010 work. Any MFC-fingerprint match between full-tree BSV and
Satoshi is *expected* and does not constitute Wright→Satoshi evidence —
the codebase IS literally descended from Satoshi's code.

This corpus is the **diff-only** companion: only the files that BSV's
nChain-led team **added** after the BCH→BSV branch point. No file in this
corpus existed in the pre-fork Bitcoin ABC source tree, so none of it
inherits Satoshi/Core text. It is the methodologically clean code-axis
test of "what does Wright's team's house style look like, with the
Satoshi/Core inheritance subtracted out?"

Result expectation under the COPA judgment + the prose-axis Wright
result: if the prose result (Wright LAST at Δ=1.55) reflects an actual
Wright/team distinctness from Satoshi, the diff-only composite z-score
should fall toward the non-Satoshi range (≤ −1.0, where the other named
candidates sit) rather than the full-tree Satoshi-like +2.83.

## Fork point

The Bitcoin SV git history descends linearly from Bitcoin ABC. The
inflection point in BSV's master branch:

- **Last pre-BSV (ABC ancestor) commit:** `4fd0b1ba6c66...`
  Date: 2018-05-30. Author: Shammah Chancellor.
  Subject: "Update chainparams for release 0.17.2"
  (= Bitcoin ABC v0.17.2 release commit)

- **First BSV-team-only commit:** `802629f614b9...`
  Date: 2018-08-23. Author: Chi Thanh NGUYEN.
  Subject: "disable GUI build option - squash to a single commit"

- **First explicit BSV rebrand:** `2ab777579...`
  Date: 2018-08-24. Author: Chi Thanh NGUYEN.
  Subject: "Rebrand to Bitcoin SV with minimal changes"

The hash-war BCH→BSV chain split itself was 2018-11-15 (block 556767),
but BSV's code branch had already diverged from Bitcoin ABC in late
August 2018, roughly three months earlier.

The methodologically clean ancestor for "subtract pre-fork inheritance"
is **`4fd0b1ba6`** (ABC v0.17.2). Every file added to `src/` between
`4fd0b1ba6` and the v1.0.0 tag `7fd177c7c` is included in this corpus.

## Corpus contents

- **File count:** 91 source files
  (29 `.cpp`, 60 `.h`, plus a few headers in subdirs)
- **Total LOC:** 18,359
- **Top-level groups:**
  - `src/test/*` — 27 files (BSV-added unit tests)
  - `src/mining/*` — 17 files (new mining/journal/assembler module)
  - `src/script/*` — 6 files (script extensions)
  - `src/rpc/*` — 1 file
  - Individual root files — 40 files (`txn_validator.*`,
    `txn_propagator.*`, `txn_recent_rejects.*`, `time_locked_mempool.*`,
    `orphan_txns.*`, `blockfileinfostore.*`, `big_int.*`, `vmtouch.*`,
    `threadpool*.h`, `task*.h`, etc.)

## Authorship verification

Net-new file commits by author (top 15):

| Commits | Author |
|---------|--------|
| 142 | Richard Mills |
| 116 | Arkadiusz Kolodziejski |
| 112 | Chris Gibson |
| 72 | Daniel Connolly |
| 61 | Domen Vrankar |
| 17 | Neza Bizjak |
| 12 | Aleksander Bračko |
| 10 | Pascal Palmer |
| 8 | Boštjan Vižin |
| 7 | Ziga Kokelj |
| 6 | shaunOK |
| 5 | Neza Belej |
| 4 | Matej Trampus |
| 4 | Jaka Pust |
| 4 | Damijan Dolenc |

**Zero Satoshi (`s_nakamoto`) commits in any of these 91 files.**
**Zero Wright commits** (consistent with the full-corpus finding —
Wright is figurehead, not committer).

The author distribution shows a typical Slovenia-clustered nChain team
(`Bračko`, `Bizjak`, `Vižin`, `Kokelj`, `Belej`, `Trampus`, `Pust`,
`Dolenc`, `Palmer`, `Vrankar`) plus core nChain engineers (Richard
Mills, Daniel Connolly, Chris Gibson, Arkadiusz Kolodziejski).

## Methodological caveats

1. **Files only — modifications excluded.** Many BSV-team contributions
   are *modifications* to pre-existing Satoshi/Core files (added lines,
   refactors, bug fixes inside existing files like `validation.cpp`,
   `net.cpp`). Those modifications also reflect BSV team style but are
   harder to extract cleanly because the surrounding identifier choices
   (function names, variable naming) are inherited from Satoshi/Core
   and unavoidably confound the analysis. This corpus uses only
   wholly-new files where the BSV team chose all identifiers and
   conventions from scratch.

2. **Team house style, not Wright personal style.** Wright is not a
   committer to any of these files. This is a "Wright-era team
   codebase" test (analogous to PGP 6.5 = "Network Associates team
   codebase"), not a Wright-personal-authorship test. Wright-personal
   code style is unobtainable from public source — see
   `forensics/wright-cross-axis-test.md` §"Code axis".

3. **Bitcoin ABC inheritance for new directories.** Even files that did
   not exist in `4fd0b1ba6` may sit inside subdirectories whose layout
   conventions (`test/` test-naming, `mining/` module-boundary style)
   were inherited from Bitcoin ABC's broader patterns. Naming
   conventions for class names, however, are author choices and that's
   what the composite measures.

4. **Comparison corpus is sibling, not replacement.** The full BSV
   corpus (`code-corpus/wright-bsv/`) remains in the analysis as the
   inheritance-confounded baseline. Reading the two side-by-side in
   `results/code-style-features.json` lets the reader see the
   composite-z-score delta caused by removing Satoshi/Core inheritance.

## Reproducibility

```bash
mkdir -p /tmp/bsv-diff && cd /tmp/bsv-diff
git clone --branch v1.0.0 --single-branch \
  https://github.com/bitcoin-sv/bitcoin-sv _clone
cd _clone

# Fork ancestor (last pre-BSV ABC commit)
FORK_COMMIT=4fd0b1ba6
V100=7fd177c7c

# Enumerate net-new src/ files
git ls-tree -r --name-only "$FORK_COMMIT" -- src/ \
  | grep -E '\.(c|cpp|cc|cxx|h|hpp|hxx)$' | sort > /tmp/bsv-diff/files_at_fork.txt
git ls-tree -r --name-only "$V100" -- src/ \
  | grep -E '\.(c|cpp|cc|cxx|h|hpp|hxx)$' | sort > /tmp/bsv-diff/files_at_v100.txt
comm -13 /tmp/bsv-diff/files_at_fork.txt /tmp/bsv-diff/files_at_v100.txt \
  > /tmp/bsv-diff/files_netnew.txt
wc -l /tmp/bsv-diff/files_netnew.txt   # expect 91

# Copy into corpus
mkdir -p $REPO/code-corpus/wright-bsv-diff
while IFS= read -r f; do
  dest="$REPO/code-corpus/wright-bsv-diff/${f#src/}"
  mkdir -p "$(dirname "$dest")"
  cp "$f" "$dest"
done < /tmp/bsv-diff/files_netnew.txt

# Run the analysis
cd $REPO && python3 src/code_style.py
```

`wright-bsv-diff` then appears in `results/code-style-features.json`
alongside `wright-bsv` and the other corpora. The composite-z column
shows whether the inheritance subtraction moves Wright-team into or out
of the Satoshi MFC fingerprint band.

## License posture

Open BSV License (Copyright (c) 2019 Bitcoin Association). Per the
project's `.gitignore`, source files in this directory are not committed
to the repository — only this `SOURCE.md`. The corpus is reassembled at
runtime via the commands above.
