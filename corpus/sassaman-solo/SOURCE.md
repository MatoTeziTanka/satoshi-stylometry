# Sassaman Prose Corpus — solo-authored, formal-technical register

## Why this corpus exists

The repo's original `corpus/sassaman/` is 5,571 words extracted from
`draft-sassaman-mixmaster-03`, a **four-author IETF draft** (Möller, Cottrell,
Palfrader, Sassaman). The function-word distribution averages four cypherpunk-
era technical writers, not Sassaman alone. This is the single biggest
methodological caveat on the most striking finding in the repo: that Satoshi's
whitepaper is closest to "Sassaman" at Δ=0.87.

This corpus replaces the multi-author baseline with two verified solo-authored
Sassaman papers, both retrieved from primary sources, both in formal-technical
register comparable to the Bitcoin whitepaper.

## Sources

| Text | Words | Date | URL |
|------|-------|------|-----|
| `ethics.txt` — *Ethical Guidelines for Computer Security Researchers: "Be Reasonable"* | 2,814 | 2010 (Financial Cryptography Workshops, Springer LNCS 6054) | `https://cosicdatabase.esat.kuleuven.be/backend/publications/files/conferencepaper/1433` |
| `faithless.txt` — *The Faithless Endpoint: How Tor puts certain users at greater risk* | 1,569 | 2007 (KU Leuven Technical Report ESAT-COSIC 2007-003) | `https://nakamoto-research.obxium.com/data/article-896.pdf` |
| **Total** | **4,383** | | |

## Sole-author verification

- **Ethics paper:** title page reads "Len Sassaman" only; KU Leuven affiliation;
  DBLP entry lists no co-authors. Verified at
  [DBLP for Len Sassaman](https://dblp.org/pid/39/6080.html).
- **Faithless Endpoint:** title page reads "Len Sassaman" only; KU Leuven email
  `len.sassaman@esat.kuleuven.be`. Sassaman self-cites this report as "[13]. Len
  Sassaman" in the Ethics paper above.

## Caveats

1. **4,383 words is borderline** for Burrows' Delta. Standard guidance is ~5k
   minimum per author; we're slightly under.
2. **Register match is good but not perfect.** Both texts are formal academic
   prose with structured sections and citations, comparable to the Bitcoin
   whitepaper's register. The Ethics paper is ethics/policy; the Faithless
   Endpoint is short threat analysis. The whitepaper is system design. Three
   different sub-genres of formal technical writing.
3. **Sassaman's pre-2007 writings are not publicly accessible** in solo form.
   His cypherpunks-era writing (2001-2004) sits in mailing list archives with
   attribution ambiguity (PGP pseudonymous posting was common).
4. **The Vox blog (`rabbi.vox.com`)** would have been a major additional source
   but Vox.com shut down ~2013 and the Archiveteam preservation status is
   "partially saved." Not pulled in this corpus.

## Pull instructions (reproducer)

```bash
mkdir -p /tmp/sassaman-solo
curl -sL -o /tmp/sassaman-solo/ethics.pdf "https://cosicdatabase.esat.kuleuven.be/backend/publications/files/conferencepaper/1433"
curl -sL -o /tmp/sassaman-solo/faithless.pdf "https://nakamoto-research.obxium.com/data/article-896.pdf"
pdftotext /tmp/sassaman-solo/ethics.pdf /tmp/sassaman-solo/ethics.txt
pdftotext /tmp/sassaman-solo/faithless.pdf /tmp/sassaman-solo/faithless.txt
cp /tmp/sassaman-solo/*.txt /path/to/repo/corpus/sassaman-solo/
```

## How to read the comparison result

The original `corpus/sassaman/` (multi-author Mixmaster RFC) remains in the
repo to preserve the trust chain — the prior result is auditable. The new
`corpus/sassaman-solo/` is treated as a separate "author" so the Δ matrix
displays both. Compare:

- `whitepaper_vs_sassaman` (original): the multi-author baseline (Δ=0.87 in
  the prior result)
- `whitepaper_vs_sassaman-solo` (new): the solo Sassaman comparison

If solo-Sassaman is much further from the whitepaper than multi-author-Sassaman,
the original Δ=0.87 was a Mixmaster-coauthor-blend artifact and the whitepaper
result must be softened or retracted. If solo-Sassaman is similarly close, the
finding strengthens.
