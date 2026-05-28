# Wright-BSV diff-only test — what the MFC composite actually measures

## What this test does

The companion `forensics/wright-cross-axis-test.md` documented two
Wright cross-axis results:

1. **Prose axis (clean):** Wright LAST in every Satoshi prose register
   at aggregate Δ=1.55 — the largest single-candidate Δ in the entire
   corpus. The prose result *quantitatively confirms* COPA v Wright
   [2024].

2. **Code axis (inheritance-confounded):** Wright-BSV v1.0.0 (full
   source tree, 568 files, 160k LOC) scored composite z = +2.83 — the
   only non-Satoshi codebase with a strongly positive composite. The
   full-tree result was acknowledged as inheritance-confounded: BSV
   v1.0.0 literally contains 245 commits by `s_nakamoto` plus the
   entire Bitcoin Core 2010–2018 lineage.

The handover left a follow-up question: *what does the MFC composite
say about BSV when we subtract the Satoshi/Core inheritance?* If the
team has its own house style, the composite should drop toward the
non-Satoshi range (≤ −1, where every named cypherpunk candidate sits).

This test answers that question.

## Methodology

The Bitcoin SV git history (15,710 commits) descends linearly from
Bitcoin ABC. The inflection point in master:

- **Last pre-BSV (ABC ancestor) commit:** `4fd0b1ba6c66...`
  (2018-05-30, Shammah Chancellor, "Update chainparams for release 0.17.2")
  — this is Bitcoin ABC v0.17.2.
- **First BSV-team-only commit:** `802629f614b9...`
  (2018-08-23, Chi Thanh NGUYEN, "disable GUI build option").
- **First explicit BSV rebrand:** `2ab777579...`
  (2018-08-24, Chi Thanh NGUYEN, "Rebrand to Bitcoin SV").

The diff-only corpus is the set of files added to `src/` between the
ABC ancestor commit and the v1.0.0 release tag (`7fd177c7c`):

- 91 source files (29 `.cpp`, 60 `.h`, etc.)
- 18,359 LOC (15,628 non-blank after the analysis script's filter)
- Zero `s_nakamoto` commits in the history of any of these files
- Zero Wright commits (consistent with the full-corpus finding — Wright
  is figurehead, not committer)

Top-level groups: `src/test/` (27 files, BSV-added unit tests),
`src/mining/` (17 files, the new journal/candidate/assembler module),
`src/script/` (6 files), individual root files (40 files including
`txn_validator.*`, `txn_propagator.*`, `time_locked_mempool.*`,
`orphan_txns.*`, `blockfileinfostore.*`, `big_int.*`, `vmtouch.*`,
`threadpool*.h`, `task*.h`).

Authors: Richard Mills (142 commits), Arkadiusz Kolodziejski (116),
Chris Gibson (112), Daniel Connolly (72), Domen Vrankar (61), plus a
cluster of clearly Slovenia-based nChain engineers (Bizjak, Bračko,
Vižin, Kokelj, Belej, Trampus, Pust, Dolenc).

Full provenance: [`code-corpus/wright-bsv-diff/SOURCE.md`](../code-corpus/wright-bsv-diff/SOURCE.md).

## Result — composite MFC z-score table (12 corpora)

| Author | Hungarian_C | SpaceRatio | LineCmt/KLOC | zH | zS | zL | Composite |
|--------|-------------|-----------|--------------|----|----|----|-----------|
| satoshi-nov2008 | 9.6% | 100.0% | 136.5 | +1.99 | +1.07 | +1.47 | **+4.53** |
| **wright-bsv-diff** | **6.3%** | **99.9%** | **135.6** | **+1.01** | **+1.07** | **+1.45** | **+3.53** ⚠️ |
| satoshi-v0.1.0 | 6.4% | 100.0% | 105.6 | +1.04 | +1.07 | +0.88 | +2.98 |
| satoshi (v0.1.3) | 6.4% | 100.0% | 105.1 | +1.03 | +1.07 | +0.87 | +2.97 |
| wright-bsv (full) | 4.8% | 99.7% | 101.9 | +0.56 | +1.06 | +0.81 | +2.43 |
| sassaman | 0.2% | 77.0% | 0.1 | −0.83 | +0.50 | −1.15 | −1.47 |
| pgp-6.5 | 0.8% | 28.9% | 45.4 | −0.64 | −0.68 | −0.28 | −1.60 |
| dai | 0.1% | 4.8% | 52.3 | −0.83 | −1.27 | −0.15 | −2.25 |
| truecrypt | 0.1% | 9.3% | 34.6 | −0.84 | −1.16 | −0.49 | −2.49 |
| back | 0.2% | 32.2% | 0.2 | −0.81 | −0.60 | −1.15 | −2.56 |
| e4m | 0.1% | 13.5% | 1.4 | −0.85 | −1.06 | −1.13 | −3.03 |
| finney | 0.1% | 12.5% | 1.2 | −0.83 | −1.08 | −1.13 | −3.04 |

**The diff-only Wright-BSV scores HIGHER than the full Wright-BSV
corpus** (+3.53 vs +2.43), and sits between Satoshi-nov2008 (+4.53) and
Satoshi-v0.1.0 (+2.98). On the three composite axes:

- **Hungarian_C 6.3%** — matches Satoshi v0.1.0 (6.4%) to within 0.1
  percentage point.
- **Space ratio 99.9%** — matches Satoshi (100%) to within 0.1pp.
- **Line comments / KLOC 135.6** — matches Satoshi-nov2008 (136.5) to
  within 1 comment/KLOC.

This is the **opposite** of the predicted outcome. If Wright's team had
its own house style that differed from Satoshi's, subtracting the
Satoshi/Core inheritance should have moved the composite toward the
non-Satoshi range. Instead, it moved further *into* the Satoshi range.

## Burrows' Delta on code function-words (rank from satoshi)

| Rank | Author | Δ |
|------|--------|---|
| 1 | satoshi-v0.1.0 | 0.0033 |
| 2 | satoshi-nov2008 | 0.3625 |
| 3 | **wright-bsv-diff** | **0.7565** |
| 4 | back | 0.8028 |
| 5 | truecrypt | 0.8371 |
| 6 | wright-bsv (full) | 0.8478 |
| 7 | dai | 0.8615 |
| 8 | e4m | 0.9412 |
| 9 | finney | 0.9538 |
| 10 | pgp-6.5 | 1.0623 |
| 11 | sassaman | 1.4063 |

Wright-BSV-diff is the closest non-Satoshi corpus to Satoshi on the
code function-word distribution as well. The full Wright-BSV corpus
(rank 6) sits *further* from Satoshi than its own diff-only subset
(rank 3) — because the full corpus is diluted by vendored libraries
(leveldb, secp256k1, univalue, crypto, support) whose styles drag the
function-word distribution away from Satoshi's.

## Why this happens (and why it is not a Wright-is-Satoshi finding)

Inspection of the BSV-team-authored files confirms deliberate
stylistic preservation. From `mining/journal.h`, `mining/factory.h`,
`orphan_txns.h`, `time_locked_mempool.h`, etc.:

```
class CJournal final
class CJournalChangeSet
class CJournalTester
class CJournalBuilder final
class CJournalEntry
class CMiningCandidate
class CMiningCandidateManager
class CMiningFactory
class CBlockStreamReader
class CBlockStream : public CForwardReadonlyStream
class COrphanTxns
class CBlockValidationStatus
class CBlockFileInfoStore
class CDiskFiles
class CBestBlockAttachmentCancellation : public std::exception
```

The BSV team explicitly chose the Satoshi `C[Capital]` Hungarian-MFC
naming convention for new classes they created from scratch.
Side-by-side with non-Hungarian classes also present in their code
(`BlockAssembler`, `JournalingBlockAssembler`, `Config`,
`BlockTemplate`), the pattern shows a team that adopted Satoshi's
convention for the *new* core types while occasionally diverging in
helper / refactor classes.

Combined with the indentation choice (100% spaces, matching Satoshi's
100% in every Satoshi-era corpus) and the `//` line-comment density
(135.6 / KLOC, matching Satoshi-nov2008's 136.5 within rounding), this
is the signature of a team **deliberately preserving the inherited
codebase's style** — which is consistent with BSV's stated mission
("Satoshi's Vision") and is what good software engineering practice
demands when extending an existing codebase.

## The methodological lesson

The MFC composite is a measure of **adoptable conventions**, not a
unique author signature. The composite distinguishes:

- **Authors who use Satoshi's conventions** (Satoshi himself, +2.97 to
  +4.53; Wright-BSV team, +2.43 to +3.53) — high positive composite.
- **Authors who do not** (all six named cypherpunk candidates +
  PGP/TrueCrypt/e4m reference codebases) — negative composite, range
  −1.47 to −3.04.

The composite is a *necessary but not sufficient* signal:

- **Necessary:** Any candidate who fails the composite (low Hungarian_C,
  high tab ratio, low // density) cannot be Satoshi without explaining
  why their style differs across an entire codebase. All five named
  prose-shortlist candidates (Back, Finney, Szabo, Dai, Sassaman) fail
  the composite. The composite **rules them out** as Satoshi by code
  style.
- **Not sufficient:** A high composite does not prove the author is
  Satoshi. It proves the author is **using Satoshi-style conventions**,
  which can be done deliberately (BSV team) or by coincidence (a 1990s
  Windows-C++ Visual-Studio default).

The Wright result therefore should be read as: **the BSV team adopted
Satoshi's coding conventions in their net-new code.** It says nothing
about Wright personally (he authored none of these files; his personal
code style is unmeasured because no public personal codebase exists)
and it does not contradict the prose-axis finding (Wright LAST at
Δ=1.55) which discriminates Wright from Satoshi on the more
authorship-bound prose function-word axis.

## Why the prose axis is the discriminating axis (corollary)

Prose function-word distributions are **harder to consciously
preserve** than code naming conventions. Naming conventions are visible
in a codebase's existing files and can be matched by a new contributor
through ordinary code-review enforcement. Function-word distributions
(rate of "the", "of", "and", "but", "however") are subconscious and
vary author-to-author at a fine-grained level that requires explicit
quantitative analysis to detect.

When an author tries to write in someone else's prose register, the
result is detectable as register mimicry (formal vs casual, technical
vs accessible) but not at the function-word-frequency level. The
Wright prose-axis result (LAST in every Satoshi register, Δ=1.55) is
therefore not vulnerable to the "BSV-team-deliberately-mimics-Satoshi"
critique that the code-axis result is.

## What this updates in the overall analysis

The README + cross-axis-test conclusions should be updated to reflect:

1. **The composite is a convention-test, not a signature.** Authors who
   want to score "Satoshi-like" can do so by adopting the conventions
   (Hungarian_C, spaces, // comments). The test rules out candidates
   whose conventions differ.
2. **The Wright code-axis result is not evidence FOR Wright→Satoshi.**
   It is consistent with deliberate style preservation by the BSV team
   in a codebase explicitly built around "Satoshi's Vision."
3. **The Wright prose-axis result (Δ=1.55 LAST) remains the
   discriminating finding** for the Wright claim — the prose axis is
   resistant to the convention-mimicry confound.
4. **The diff-only methodology should be the default** for inherited
   codebases (any future fork-analysis), because it isolates the
   contributor team's actual style from the inherited base.
5. **Full corpus + diff-only side-by-side is the correct framing** —
   both are shown to make the methodology audit-able. The drop from
   full +2.43 to diff-only +3.53 is the size of the inheritance
   confound when measured this way.

## What this does NOT change

- Sassaman remains the prose-axis #1 candidate (Δ=0.83 whitepaper).
- Finney remains the prose-axis aggregate #1 (Δ=0.91 across all
  registers).
- Wright remains LAST in every Satoshi prose register at Δ=1.55.
- The COPA v Wright [2024] judgment is unaffected; this analysis
  produces evidence consistent with it.
- The four-fold Windows-OS consensus (code MFC, PGP MingW32, UA literal,
  PDF font fingerprint) still holds for Satoshi.

## Reproduction

```bash
mkdir -p /tmp/bsv-diff && cd /tmp/bsv-diff
git clone --branch v1.0.0 --single-branch \
  https://github.com/bitcoin-sv/bitcoin-sv _clone
cd _clone

FORK_COMMIT=4fd0b1ba6
V100=7fd177c7c

git ls-tree -r --name-only "$FORK_COMMIT" -- src/ \
  | grep -E '\.(c|cpp|cc|cxx|h|hpp|hxx)$' | sort > /tmp/bsv-diff/files_at_fork.txt
git ls-tree -r --name-only "$V100" -- src/ \
  | grep -E '\.(c|cpp|cc|cxx|h|hpp|hxx)$' | sort > /tmp/bsv-diff/files_at_v100.txt
comm -13 /tmp/bsv-diff/files_at_fork.txt /tmp/bsv-diff/files_at_v100.txt \
  > /tmp/bsv-diff/files_netnew.txt
wc -l /tmp/bsv-diff/files_netnew.txt   # expect 91

mkdir -p $REPO/code-corpus/wright-bsv-diff
while IFS= read -r f; do
  dest="$REPO/code-corpus/wright-bsv-diff/${f#src/}"
  mkdir -p "$(dirname "$dest")"
  cp "$f" "$dest"
done < /tmp/bsv-diff/files_netnew.txt

cd $REPO && python3 src/code_style.py
# Read results/code-style-features.json:
#   features[*].author == "wright-bsv-diff"
#   mfc_composite_ranking → wright-bsv-diff composite ≈ +3.53
```

Date: 2026-05-28.
