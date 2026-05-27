"""
Hyphenation-error stylometry — independent replication attempt of the
methodology reportedly used by the NYT April 2026 Adam Back investigation.

The NYT investigation's headline statistic (per secondary trade-press summaries
since the article is paywalled): Adam Back shares 67 of Satoshi's 325
hyphenation errors; the second-closest candidate shares 38.

A "hyphenation error" in this methodology is interpreted as: a compound word
that the author uses INCONSISTENTLY in their own corpus — e.g., writing both
"e-mail" and "email" in the same body of work. The author's set of such
inconsistent compounds is their hyphenation fingerprint. Overlap between two
authors' sets is the test statistic.

Method:
  1. Tokenize each author's full prose corpus.
  2. Find candidate compound words: any token containing a hyphen. For each
     hyphenated compound, check whether the corpus ALSO contains the same
     compound without the hyphen (lowercased).
  3. If both forms appear in the same corpus, the word is an "inconsistent
     compound" for that author.
  4. Build per-author inconsistent-compound sets.
  5. For each candidate, count overlap with Satoshi's set.
  6. Report overlap count + overlap rate + which specific words drive the result.

We use the same `corpus/<author>/*.txt` prose corpora that drive the standard
Burrows' Delta analysis. The script does NOT introduce new corpus material.

Output: results/hyphenation-overlap.json + per-candidate overlap words.

Caveats and disclaimers documented in results — the NYT's exact methodology
is not published; this is our best-faith reproduction from secondary summaries.
"""

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS_ROOT = ROOT / "corpus"
RESULTS_ROOT = ROOT / "results"
RESULTS_ROOT.mkdir(exist_ok=True)


def load_corpus():
    out = {}
    for author_dir in sorted(CORPUS_ROOT.iterdir()):
        if not author_dir.is_dir():
            continue
        texts = []
        for txt_file in sorted(author_dir.glob("*.txt")):
            texts.append(txt_file.read_text(errors="replace"))
        if texts:
            out[author_dir.name] = "\n\n".join(texts)
    return out


def extract_word_tokens(text):
    """Lowercased word tokens including hyphenated compounds.

    The token model: a "word" is a run of letters that MAY contain internal
    hyphens. Punctuation, numbers, URLs, emails are stripped. We deliberately
    lowercase to avoid sentence-initial casing inflating "inconsistency"
    counts.
    """
    text = text.lower()
    # Strip URLs first (they contain hyphens but aren't compound words)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\b\S+@\S+\.\S+\b", " ", text)  # emails
    # Word = letter-run with optional internal hyphen(s) between letter-runs
    tokens = re.findall(r"\b[a-z]+(?:-[a-z]+)+\b|\b[a-z]+\b", text)
    return tokens


def find_inconsistent_compounds(tokens):
    """Return the set of compounds the author uses BOTH hyphenated and not.

    A compound is "inconsistent" if its hyphenated form (e.g., "e-mail") and
    its un-hyphenated form (e.g., "email") both appear in the corpus. The
    function returns the un-hyphenated form as the canonical key.

    Bare frequency filter: each form must appear at least twice (>=2) to count.
    A single occurrence of one variant is plausibly a typo or a quoted
    artifact, not a stylistic inconsistency.
    """
    counts = Counter(tokens)
    inconsistent = {}
    for token, count in counts.items():
        if "-" not in token or count < 2:
            continue
        unhyphenated = token.replace("-", "")
        if counts.get(unhyphenated, 0) >= 2:
            inconsistent[unhyphenated] = {
                "hyphenated_form": token,
                "hyphenated_count": count,
                "unhyphenated_count": counts[unhyphenated],
            }
    return inconsistent


def main():
    corpora = load_corpus()
    print(f"Loaded {len(corpora)} authors: {list(corpora.keys())}")

    # Build per-author inconsistent-compound sets
    per_author = {}
    for author, text in corpora.items():
        tokens = extract_word_tokens(text)
        inconsistent = find_inconsistent_compounds(tokens)
        per_author[author] = {
            "total_word_tokens": len(tokens),
            "n_inconsistent_compounds": len(inconsistent),
            "inconsistent_compounds": inconsistent,
        }
        print(f"  {author:20s} {len(tokens):7d} tokens, {len(inconsistent):3d} inconsistent compounds")

    # Compute overlap of each candidate with Satoshi
    satoshi_set = set(per_author["satoshi"]["inconsistent_compounds"].keys())
    print(f"\nSatoshi inconsistent-compound set size: {len(satoshi_set)}")

    overlaps = {}
    for author in per_author:
        if author == "satoshi":
            continue
        cand_set = set(per_author[author]["inconsistent_compounds"].keys())
        overlap = satoshi_set & cand_set
        overlaps[author] = {
            "n_candidate_inconsistent": len(cand_set),
            "n_overlap_with_satoshi": len(overlap),
            "overlap_rate_of_satoshi_set": (
                len(overlap) / len(satoshi_set) if satoshi_set else 0.0
            ),
            "overlap_rate_of_candidate_set": (
                len(overlap) / len(cand_set) if cand_set else 0.0
            ),
            "overlap_words_sorted": sorted(overlap),
        }

    # Sort by overlap-with-Satoshi
    ranked = sorted(overlaps.items(), key=lambda kv: -kv[1]["n_overlap_with_satoshi"])
    print("\n=== Hyphenation-overlap with Satoshi (ranked) ===")
    print(f"{'Author':<20s} {'Cand-set':>10s} {'Overlap':>10s} {'%-of-Sat':>10s} {'%-of-Cand':>10s}")
    for author, info in ranked:
        print(f"  {author:<18s} {info['n_candidate_inconsistent']:>10d} "
              f"{info['n_overlap_with_satoshi']:>10d} "
              f"{100*info['overlap_rate_of_satoshi_set']:>9.1f}% "
              f"{100*info['overlap_rate_of_candidate_set']:>9.1f}%")

    payload = {
        "satoshi_set_size": len(satoshi_set),
        "satoshi_inconsistent_compounds_sorted": sorted(satoshi_set),
        "per_author": per_author,
        "overlaps_with_satoshi": overlaps,
        "method_caveat": (
            "Best-faith reproduction of NYT April 2026 methodology from "
            "secondary trade-press summaries. The NYT article is paywalled; "
            "exact tokenization rules, normalization choices, and threshold "
            "conventions are not published. Differences in those choices "
            "could move overlap counts by 10-30 percent."
        ),
        "tokenization_rules": (
            "Lowercase. Strip URLs and emails. Word = letter-run with optional "
            "internal hyphens. Frequency filter: each form must appear >=2 "
            "times in the corpus to be counted as 'used by the author' for "
            "the purposes of the inconsistency test (single occurrences may "
            "be quoted material or typos)."
        ),
    }
    out_path = RESULTS_ROOT / "hyphenation-overlap.json"
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
