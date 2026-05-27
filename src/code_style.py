"""
Code-style stylometric analysis.

Burrows' Delta does not transfer cleanly to source code because each
codebase has its own vocabulary (no universal "function words"). This
module uses a set of programming-language-invariant style features
instead:

  1. Identifier-token frequency: top-N most frequent identifiers per
     author, then Burrows-Delta on shared identifiers (analogous to
     function-word distribution for prose).
  2. Naming-convention proportions: % of identifiers that are
     camelCase / PascalCase / snake_case / SCREAMING_CASE / Hungarian.
  3. Comment style: ratio of // vs /* */ vs doc-comment per KLOC.
  4. Brace style: Allman (own line) vs K&R (end of previous line).
  5. Indentation: tab vs space; depth of tab/space.
  6. Common-vocabulary identifiers ("function words" for code): i, j,
     n, tmp, ret, etc. — these are the closest analogue to prose
     function words because they're topic-invariant.

Inputs: code-corpus/<author>/*.c, *.cpp, *.h, *.hpp
Outputs: results/code-style-features.json, results/code-style-dendrogram.png
"""

import json
import re
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "code-corpus"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

C_KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if", "inline",
    "int", "long", "register", "restrict", "return", "short", "signed", "sizeof",
    "static", "struct", "switch", "typedef", "union", "unsigned", "void",
    "volatile", "while", "_Bool", "_Complex", "_Imaginary",
    # C++ additions
    "class", "namespace", "template", "typename", "public", "private",
    "protected", "virtual", "friend", "this", "new", "delete", "operator",
    "using", "try", "catch", "throw", "explicit", "mutable", "true", "false",
    "bool", "nullptr", "NULL", "and", "or", "not",
}

# Topic-invariant common identifiers — the "function words" of code.
# These appear across most codebases regardless of domain.
CODE_FUNCTION_WORDS = [
    "i", "j", "k", "n", "m", "x", "y", "z",
    "p", "q", "r", "s", "t",
    "tmp", "temp", "len", "num", "count", "size", "buf", "buffer",
    "ret", "result", "rv", "rc", "err", "error", "e", "ex",
    "data", "value", "val", "key", "name", "type", "ptr", "ref",
    "src", "dst", "dest", "in", "out", "input", "output",
    "ok", "status", "flag", "flags", "state", "mode",
    "first", "last", "next", "prev", "begin", "end",
    "idx", "index", "offset", "pos", "position",
    "min", "max", "sum", "total", "avg",
    "this", "self", "args", "argv", "argc",
    "f", "g", "h", "fn", "func", "cb", "callback",
]


def iter_source_files(author_dir: Path):
    # rglob to support deep-nested codebases (e.g., TrueCrypt's Boot/, Core/, etc.).
    # Excludes obvious vendored/third-party paths.
    EXCLUDE_DIR_PARTS = {"third_party", "third-party", "vendor", "deps", "build", "dist", ".git"}
    for ext in (".c", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".hxx"):
        for p in author_dir.rglob(f"*{ext}"):
            if any(part in EXCLUDE_DIR_PARTS for part in p.parts):
                continue
            yield p


def load_corpus():
    authors = {}
    for author_dir in sorted(CORPUS.iterdir()):
        if not author_dir.is_dir():
            continue
        files = list(iter_source_files(author_dir))
        if not files:
            continue
        authors[author_dir.name] = files
    return authors


def strip_comments_and_strings(src: str):
    """Return code-only (for identifier extraction) and comment-only views."""
    # Block comments
    block_comments = re.findall(r"/\*.*?\*/", src, flags=re.DOTALL)
    src_no_block = re.sub(r"/\*.*?\*/", " ", src, flags=re.DOTALL)
    # Line comments
    line_comments = re.findall(r"//[^\n]*", src_no_block)
    src_no_comments = re.sub(r"//[^\n]*", "", src_no_block)
    # String literals
    src_no_strings = re.sub(r'"(?:[^"\\]|\\.)*"', " ", src_no_comments)
    src_no_strings = re.sub(r"'(?:[^'\\]|\\.)*'", " ", src_no_strings)
    return src_no_strings, block_comments, line_comments


def extract_identifiers(code: str):
    raw = re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", code)
    return [t for t in raw if t not in C_KEYWORDS]


# Naming-convention classifiers (mutually exclusive in this order)
RE_SCREAMING = re.compile(r"^[A-Z][A-Z0-9_]*$")
RE_PASCAL = re.compile(r"^[A-Z][a-zA-Z0-9]*$")
RE_CAMEL = re.compile(r"^[a-z][a-zA-Z0-9]*$")
RE_SNAKE = re.compile(r"^[a-z][a-z0-9_]*$")
RE_HUNGARIAN_C = re.compile(r"^C[A-Z][a-zA-Z0-9]*$")              # CTransaction
RE_HUNGARIAN_PREFIX = re.compile(r"^(n|p|sz|h|m_|pf|cb|hash|f)[A-Z]")  # nTransactions, pindexBest, hashBest


def classify_naming(token: str) -> str:
    if "_" in token and token.upper() == token and len(token) > 1:
        return "SCREAMING_CASE"
    if RE_HUNGARIAN_C.match(token):
        return "Hungarian_C"
    if RE_HUNGARIAN_PREFIX.match(token):
        return "Hungarian_prefix"
    if RE_PASCAL.match(token) and "_" not in token:
        return "PascalCase"
    if RE_CAMEL.match(token) and "_" not in token and any(c.isupper() for c in token[1:]):
        return "camelCase"
    if RE_SNAKE.match(token):
        return "snake_case"
    if RE_SCREAMING.match(token):
        return "SCREAMING_CASE"
    return "other"


def detect_brace_style(src: str):
    """
    Allman: `\n\s*{` after a function/control header on its own line
    K&R:    `)\s*{` or `else\s*{` — opening brace at end of previous line
    """
    allman = len(re.findall(r"\)\s*\n\s*\{", src))
    knr = len(re.findall(r"\)\s*\{", src))
    return {"allman": allman, "knr": knr}


def detect_indent(src: str):
    """Return ratio of lines that start with tab vs spaces vs neither."""
    tabs = 0
    spaces = 0
    other = 0
    for line in src.split("\n"):
        if not line.strip():
            continue
        if line.startswith("\t"):
            tabs += 1
        elif line.startswith(" "):
            spaces += 1
        else:
            other += 1
    total = tabs + spaces + other
    if total == 0:
        return {"tab_ratio": 0.0, "space_ratio": 0.0}
    return {"tab_ratio": tabs / total, "space_ratio": spaces / total}


def extract_features(author: str, files: list):
    """Return a feature dict for one author, aggregated across all files."""
    all_identifiers = Counter()
    naming_counter = Counter()
    total_block_comments = 0
    total_line_comments = 0
    total_loc = 0
    brace_total = {"allman": 0, "knr": 0}
    indent_lines = {"tab": 0, "space": 0}

    for fp in files:
        try:
            src = fp.read_text(errors="ignore")
        except Exception:
            continue
        code, block_c, line_c = strip_comments_and_strings(src)
        loc = sum(1 for L in src.split("\n") if L.strip())
        total_loc += loc
        total_block_comments += len(block_c)
        total_line_comments += len(line_c)

        idents = extract_identifiers(code)
        all_identifiers.update(idents)
        for tok in set(idents):
            naming_counter[classify_naming(tok)] += idents.count(tok)

        braces = detect_brace_style(src)
        for k in brace_total:
            brace_total[k] += braces[k]

        ind = detect_indent(src)
        for line in src.split("\n"):
            if not line.strip():
                continue
            if line.startswith("\t"):
                indent_lines["tab"] += 1
            elif line.startswith(" "):
                indent_lines["space"] += 1

    total_idents = sum(naming_counter.values()) or 1
    naming_pct = {k: v / total_idents for k, v in naming_counter.items()}

    brace_sum = sum(brace_total.values()) or 1
    brace_pct = {
        "allman_ratio": brace_total["allman"] / brace_sum,
        "knr_ratio": (brace_total["knr"] - brace_total["allman"]) / brace_sum,
    }

    indent_total = sum(indent_lines.values()) or 1

    return {
        "author": author,
        "n_files": len(files),
        "total_loc": total_loc,
        "total_identifier_tokens": sum(all_identifiers.values()),
        "block_comments_per_kloc": (total_block_comments * 1000.0) / max(total_loc, 1),
        "line_comments_per_kloc": (total_line_comments * 1000.0) / max(total_loc, 1),
        "naming_pct": naming_pct,
        "brace_pct": brace_pct,
        "indent": {
            "tab_ratio": indent_lines["tab"] / indent_total,
            "space_ratio": indent_lines["space"] / indent_total,
        },
        # Frequency per 1000 identifier tokens for the function-word set
        "function_word_freq": {
            w: (all_identifiers[w] * 1000.0 / max(sum(all_identifiers.values()), 1))
            for w in CODE_FUNCTION_WORDS
        },
        "top_identifiers": dict(all_identifiers.most_common(30)),
    }


def burrows_delta_on_function_words(feature_list):
    """Run Burrows' Delta on the code function-word frequencies."""
    authors = [f["author"] for f in feature_list]
    matrix = np.array(
        [[f["function_word_freq"][w] for w in CODE_FUNCTION_WORDS] for f in feature_list]
    )
    means = matrix.mean(0)
    stds = matrix.std(0)
    stds[stds == 0] = 1.0
    z = (matrix - means) / stds
    n = len(authors)
    delta = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            delta[i, j] = np.mean(np.abs(z[i] - z[j]))
    return delta, authors


def report(delta_matrix, authors, target):
    if target not in authors:
        print(f"  (no '{target}' in authors)")
        return None
    t = authors.index(target)
    ranking = sorted(
        [(authors[i], delta_matrix[t, i]) for i in range(len(authors)) if i != t],
        key=lambda x: x[1],
    )
    print(f"\n=== Distance from '{target}' (code function-word Delta) ===")
    for name, d in ranking:
        bar = "#" * int(d * 30)
        print(f"  {name:14s} {d:.4f}  {bar}")
    return ranking


def main():
    print("=== Loading code corpus ===")
    corpora = load_corpus()
    print(f"Authors: {list(corpora.keys())}")
    for a, files in corpora.items():
        print(f"  {a:14s} {len(files):3d} files")

    print("\n=== Extracting per-author features ===")
    features = []
    for author, files in corpora.items():
        f = extract_features(author, files)
        features.append(f)
        print(
            f"  {author:12s} LOC={f['total_loc']:>7,} "
            f"idents={f['total_identifier_tokens']:>7,}  "
            f"naming: PascalCase={f['naming_pct'].get('PascalCase', 0):.0%} "
            f"camelCase={f['naming_pct'].get('camelCase', 0):.0%} "
            f"snake_case={f['naming_pct'].get('snake_case', 0):.0%} "
            f"Hungarian_C={f['naming_pct'].get('Hungarian_C', 0):.1%}"
        )

    # Burrows-Delta on the function-word frequencies
    delta, authors = burrows_delta_on_function_words(features)
    ranking_satoshi = report(delta, authors, "satoshi")

    print("\n=== Comment density (per KLOC) ===")
    for f in features:
        print(
            f"  {f['author']:12s} block={f['block_comments_per_kloc']:>6.1f}  "
            f"line={f['line_comments_per_kloc']:>6.1f}"
        )

    print("\n=== Brace + indent ===")
    for f in features:
        print(
            f"  {f['author']:12s} allman={f['brace_pct']['allman_ratio']:.0%}  "
            f"knr={f['brace_pct']['knr_ratio']:.0%}  "
            f"tabs={f['indent']['tab_ratio']:.0%}  "
            f"spaces={f['indent']['space_ratio']:.0%}"
        )

    # Persist
    out = {
        "authors": authors,
        "features": features,
        "burrows_delta_matrix": delta.tolist(),
        "rank_from_satoshi": ranking_satoshi,
    }
    (RESULTS / "code-style-features.json").write_text(json.dumps(out, indent=2))
    print(f"\nSaved: {RESULTS / 'code-style-features.json'}")

    # Dendrogram
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        Z = linkage(squareform(delta), method="average")
        plt.figure(figsize=(10, 6))
        dendrogram(Z, labels=authors, leaf_rotation=30)
        plt.title("Code-style clustering (Burrows' Delta on code function-words)")
        plt.ylabel("Delta distance")
        plt.tight_layout()
        plt.savefig(RESULTS / "code-style-dendrogram.png", dpi=140)
        print(f"Saved: {RESULTS / 'code-style-dendrogram.png'}")
    except ImportError:
        pass


if __name__ == "__main__":
    main()
