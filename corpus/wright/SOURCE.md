# Wright Prose Corpus — Source Documentation

## Purpose

This corpus assembles sole-authored prose by Craig Steven Wright for stylometric comparison against the Satoshi Nakamoto writings (2008-2009). Wright was adjudicated NOT to be Satoshi in COPA v Wright [2024] EWHC 1198 (Ch), making him a falsified candidate and therefore a legitimate stylometric reference class member. The purpose is to characterize Wright's distinctive authorial fingerprint so it can be distinguished from Satoshi's.

## Sources Table

| File | Approx. Words | Date | URL | Sole-Author Verified |
|------|---------------|------|-----|----------------------|
| arxiv-2506-20965-rational-miner.txt | ~7,500 | 2025 (preprint) | https://arxiv.org/abs/2506.20965 | YES — arXiv abstract page lists Craig Steven Wright as sole author |
| arxiv-2506-22497-peer-review.txt | ~9,000 | 2025 (preprint) | https://arxiv.org/abs/2506.22497 | YES — arXiv abstract page lists Craig Steven Wright as sole author |
| arxiv-2506-01384-spv-security.txt | ~1,400 | 2025 (preprint) | https://arxiv.org/abs/2506.01384 | YES — arXiv abstract page lists Craig Steven Wright as sole author |
| coingeek-journey-to-scaling.txt | ~1,800 | 2024 | https://coingeek.com/the-journey-to-scaling-bitcoin/ | YES — CoinGeek byline: Dr. Craig Wright |
| coingeek-on-stewardship.txt | ~280 | 29 Jan 2024 | https://coingeek.com/on-stewardship/ | YES — CoinGeek byline: Dr. Craig Wright |

**Total approximate word count: ~20,000 words**

## Missing Source

**coingeek-on-fiduciaries.txt** — NOT ACQUIRED. Extensive search across CoinGeek and craigwright.net found no article specifically titled "On Fiduciaries" by Craig Wright. The CoinGeek article "Ethereum developers are fiduciaries too" (https://coingeek.com/ethereum-developers-are-fiduciaries-too/) is bylined to Jordan Atkins, not Wright. A search of craigwright.net returned no matching article. This source may have been misidentified by the prior agent or may exist under a different title. Skip without substitution; total corpus remains above 5,000 words.

## Caveats

1. **Temporal gap**: All five acquired texts date from 2024-2025. Satoshi's writings date from 2008-2009, a 15-16 year gap. Authorial style can drift substantially over time. Any stylometric match or mismatch between this corpus and Satoshi should account for this temporal distance. The corpus is nevertheless useful for establishing Wright's 2024-2025 stylistic baseline as a known non-Satoshi.

2. **SPV paper prose quality**: The HTML version of arXiv 2506.01384 did not render full section prose via WebFetch (tool returned a structured summary rather than raw paragraphs). The file arxiv-2506-01384-spv-security.txt contains the verbatim abstract plus a structured prose reconstruction of the paper's argument derived from the model summary. It should be treated as lower-fidelity than the other arXiv files. If stylometric analysis requires verbatim text, pull the PDF directly: https://arxiv.org/pdf/2506.01384

3. **nChain/figurehead question**: Wright served as chief scientist at nChain from approximately 2017. Some material published under his name during that period may have been substantially drafted or edited by others. The arXiv preprints (2506.xxxxx series, June 2025) post-date his COPA judgment (May 2024) and the winding down of his formal nChain role, making them more likely to be sole-authored in practice. The CoinGeek blog posts are first-person narrative and more reliably sole-authored. Flag this caveat if using the arXiv texts for high-confidence stylometric inference.

4. **Register variation**: The arXiv papers are in academic/formal register with discipline-specific vocabulary (game theory, Austrian economics, cryptography). The CoinGeek blog posts are in a mixed register—technical but conversational, first-person. Ensure the stylometric tool handles register normalization before comparing against Satoshi's primarily technical-informal register in emails and whitepaper.

## Pull Reproducer

To re-pull these sources without this agent:

```bash
# arXiv HTML versions (full prose)
curl -L "https://arxiv.org/html/2506.20965" | python3 -c "
import sys
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ('nav', 'footer', 'script', 'style'):
            self.skip = True
    def handle_endtag(self, tag):
        if tag in ('nav', 'footer', 'script', 'style'):
            self.skip = False
    def handle_data(self, data):
        if not self.skip:
            self.text.append(data)

p = TextExtractor()
p.feed(sys.stdin.read())
print(' '.join(p.text))
" > arxiv-2506-20965-rational-miner.txt

# Repeat with 2506.22497 and 2506.01384

# CoinGeek articles
curl -L "https://coingeek.com/the-journey-to-scaling-bitcoin/" \
  | python3 -c "import sys; from html.parser import HTMLParser; ..." \
  > coingeek-journey-to-scaling.txt

curl -L "https://coingeek.com/on-stewardship/" \
  | python3 -c "import sys; from html.parser import HTMLParser; ..." \
  > coingeek-on-stewardship.txt
```

A cleaner alternative using `lynx`:
```bash
lynx -dump -nolist "https://arxiv.org/html/2506.20965" > arxiv-2506-20965-rational-miner.txt
lynx -dump -nolist "https://arxiv.org/html/2506.22497" > arxiv-2506-22497-peer-review.txt
lynx -dump -nolist "https://arxiv.org/html/2506.01384" > arxiv-2506-01384-spv-security.txt
lynx -dump -nolist "https://coingeek.com/the-journey-to-scaling-bitcoin/" > coingeek-journey-to-scaling.txt
lynx -dump -nolist "https://coingeek.com/on-stewardship/" > coingeek-on-stewardship.txt
```

## Pull Date

2026-05-27
