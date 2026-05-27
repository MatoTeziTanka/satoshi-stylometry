"""
Pull the analysis corpora from public sources.

Sources:
  - Satoshi Nakamoto: forum posts + emails archived by the Satoshi Nakamoto
    Institute (https://github.com/nakamotoinstitute/nakamotoinstitute.org),
    licensed AGPL-3.0.
  - Bitcoin whitepaper: bitcoin.org canonical PDF.
  - Adam Back: Hashcash 2002 paper (PDF on cdn.nakamotoinstitute.org).
  - Nick Szabo: 42 essays archived by Nakamoto Institute (markdown).
  - Hal Finney: 12 essays archived by Nakamoto Institute (markdown).
  - Wei Dai: b-money proposal (markdown).

Requires `git` and `pdftotext` (poppler-utils) on PATH.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus"
TMP = Path("/tmp") / "satoshi-stylo-pull"


def run(cmd, **kw):
    print(f"  $ {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    return subprocess.run(cmd, check=True, **kw)


def clone_ni():
    """Shallow-clone the Nakamoto Institute site repo (~150MB)."""
    target = TMP / "ni-site"
    if target.exists():
        print(f"  (cached: {target})")
        return target
    TMP.mkdir(parents=True, exist_ok=True)
    run(["git", "clone", "--depth", "1",
         "https://github.com/nakamotoinstitute/nakamotoinstitute.org.git",
         str(target)])
    return target


def strip_html(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def strip_markdown(text):
    if text.startswith("---"):
        end = text.find("---", 3)
        text = text[end + 3 :] if end > 0 else text
    text = re.sub(r"```[^\n]*\n.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*+([^*]+)\*+", r"\1", text)
    text = re.sub(r"_+([^_]+)_+", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def pull_satoshi(ni_root: Path):
    """Filter forum_posts.json and emails.json for Satoshi-authored items."""
    out = CORPUS / "satoshi"
    out.mkdir(parents=True, exist_ok=True)

    with open(ni_root / "server/data/forum_posts.json") as f:
        posts = json.load(f)
    s_posts = [p for p in posts if p.get("satoshi_id") is not None]
    s_posts.sort(key=lambda p: p["satoshi_id"])
    print(f"  Satoshi forum posts: {len(s_posts)}")

    # Split by source
    bt = [p for p in s_posts if "bitcointalk" in (p.get("url") or "")]
    p2p = [p for p in s_posts if "p2pfoundation" in (p.get("url") or "")]
    (out / "bitcointalk.txt").write_text("\n\n----\n\n".join(strip_html(p["text"]) for p in bt))
    (out / "p2pfoundation.txt").write_text("\n\n----\n\n".join(strip_html(p["text"]) for p in p2p))
    (out / "forum_posts.txt").write_text("\n\n----\n\n".join(strip_html(p["text"]) for p in s_posts))

    with open(ni_root / "server/data/emails.json") as f:
        emails = json.load(f)
    s_emails = [e for e in emails if e.get("sent_from") == "Satoshi Nakamoto"]
    print(f"  Satoshi emails (sent_from): {len(s_emails)}")
    (out / "emails.txt").write_text(
        "\n\n----\n\n".join(strip_html(e["text"]) for e in s_emails)
    )


def pull_whitepaper():
    out = CORPUS / "satoshi" / "whitepaper.txt"
    if out.exists():
        return
    pdf_path = TMP / "bitcoin.pdf"
    if not pdf_path.exists():
        urllib.request.urlretrieve("https://bitcoin.org/bitcoin.pdf", pdf_path)
    run(["pdftotext", "-layout", str(pdf_path), str(out)])


def pull_essays_by_author(ni_root: Path, author_slug: str, dest_subdir: str):
    """Extract every .en.md whose YAML frontmatter lists the given author slug."""
    out_dir = CORPUS / dest_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    texts = []
    for src_dir in ["library", "mempool"]:
        for fp in (ni_root / "server" / "content" / src_dir).glob("*.en.md"):
            content = fp.read_text()
            if not content.startswith("---"):
                continue
            end = content.find("---", 3)
            if end < 0:
                continue
            fm = content[3:end]
            if f"- {author_slug}" not in fm:
                continue
            body = strip_markdown(content)
            if body:
                texts.append(body)
    if texts:
        (out_dir / "essays.txt").write_text("\n\n----\n\n".join(texts))
    print(f"  {author_slug}: {len(texts)} essay(s)")


def pull_hashcash():
    out = CORPUS / "back" / "hashcash_paper.txt"
    if out.exists():
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    pdf_path = TMP / "hashcash.pdf"
    if not pdf_path.exists():
        urllib.request.urlretrieve(
            "https://cdn.nakamotoinstitute.org/docs/hashcash.pdf", pdf_path
        )
    run(["pdftotext", "-layout", str(pdf_path), str(out)])


def main():
    print("=== Cloning Nakamoto Institute site repo (~150MB shallow clone) ===")
    ni_root = clone_ni()

    print("\n=== Pulling Satoshi corpus ===")
    pull_satoshi(ni_root)
    print("\n=== Pulling Bitcoin whitepaper ===")
    pull_whitepaper()

    print("\n=== Pulling candidate essays ===")
    pull_essays_by_author(ni_root, "nick-szabo", "szabo")
    pull_essays_by_author(ni_root, "hal-finney", "finney")
    pull_essays_by_author(ni_root, "wei-dai", "dai")

    print("\n=== Pulling Hashcash paper ===")
    pull_hashcash()

    print("\nDone. Corpus written to", CORPUS)
    for d in sorted(CORPUS.iterdir()):
        if d.is_dir():
            wc = sum(len(f.read_text().split()) for f in d.glob("*.txt"))
            print(f"  {d.name:14s} {wc:>7,} words")


if __name__ == "__main__":
    main()
