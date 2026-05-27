# Bitcoin Whitepaper — Version Inventory

Pulled 2026-05-26 for the satoshi-stylometry per-version analysis. The community sometimes describes "three versions" (2008-10-31 mailing-list / 2009-03 bitcoin.org / 2009-05 revised). Direct evidence supports **two distinct PDFs**; the supposed "May 2009 revised" version is not corroborated by any archive I could reach. See section 3.

## 1. whitepaper-v1.pdf — 2008 mailing-list pre-print

| Field | Value |
| --- | --- |
| Source URL | `https://archive.org/download/bitcoin-a-peer-to-peer-electronic-cash-system/bitcoin.pdf` |
| Internet Archive item | `bitcoin-a-peer-to-peer-electronic-cash-system` |
| File size | 183,697 bytes |
| SHA256 | `427c63b364c6db914cf23072a09ffd53ee078397b7c6ab2d604e12865a982faa` |
| MD5 | `b7026c5be02de23871fc1d80a49e087b` (per IA metadata) |
| PDF CreationDate | 2008-10-03 16:49:58 EDT |
| Producer | OpenOffice.org 2.4 |
| Pages | 9 |
| Word count (pdftotext -layout) | 3,514 |
| Author email on title page | `satoshi@vistomail.com` |
| Cross-corroboration | metzdowd.com cryptography list post 2017-08 (https://www.metzdowd.com/pipermail/cryptography/2017-August/032668.html) cites the same 183,697 size and SHA256 |

This is the PDF attached to Satoshi's 2008-10-31 metzdowd cryptography-list announcement (creation date predates the announcement by ~4 weeks). Date-order earliest, so labelled v1.

## 2. whitepaper-v2.pdf — 2009-03 bitcoin.org release

| Field | Value |
| --- | --- |
| Source URL | `https://bitcoin.org/bitcoin.pdf` (also identical to `https://cdn.nakamotoinstitute.org/docs/bitcoin.pdf`) |
| File size | 184,292 bytes |
| SHA256 | `b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553` |
| PDF CreationDate | 2009-03-24 13:33:15 EDT |
| Producer | OpenOffice.org 2.4 |
| Pages | 9 |
| Word count (pdftotext -layout) | 3,571 |
| Author email on title page | `satoshin@gmx.com` |

This file has been served from `bitcoin.org/bitcoin.pdf` continuously from the earliest Wayback Machine snapshot (2010-07-04) to today — same SHA256 across every snapshot I sampled (9 distinct CDX digests 2010-2014, all dereferenced to the same content via Wayback's `id_` raw replay; the CDX digests vary because of capture-side metadata, not file content). The `x-archive-orig-last-modified` header on the 2010-07-04 capture is `Tue, 24 Mar 2009 17:33:15 GMT`, matching the PDF's own CreationDate.

## 3. Claimed "May 2009 revised" version — NOT FOUND

I searched the following and found **no third distinct PDF**:

- Wayback Machine CDX index of `bitcoin.org/bitcoin.pdf` from 2008-2010 (earliest snapshot is 2010-07-04 — by which time the file is already the 2009-03-24 build).
- All 9 distinct Wayback CDX digests 2010-2014 dereferenced via `id_` raw replay — every one returns the same `b16741...` 184,292-byte file.
- Satoshi Nakamoto Institute CDN (`cdn.nakamotoinstitute.org/docs/bitcoin.pdf`) — same `b16741...` hash.
- Live `bitcoin.org/bitcoin.pdf` today — same `b16741...` hash.
- 0xB10C bitcoin-development-history JSON (`github.com/0xB10C/bitcoin-development-history`) — only references the 2008 announcement, no second/third revision event.
- scottgriv/bitcoin-white_paper GitHub repo — single PDF only.
- bitcoin/bitcoin git repo — no PDF in `doc/` tree on `master`, and v0.1 tag doesn't exist on the current GitHub mirror (the earliest 2009 sourceforge releases predate the GitHub mirror).

Honest read of the evidence: the "three-version" framing in community discussion appears to conflate (a) the late-October 2008 mailing-list pre-print, (b) the 2009-03-24 bitcoin.org release (which went up around Bitcoin 0.1 in early January 2009 — same content, just published a few months later), and (c) the fact that bitcoin.org served this PDF unchanged through subsequent months including May 2009. Unless a third PDF surfaces from a private archive, **v1 and v2 are the corpus**.

## 4. Key textual differences (v1 → v2)

Diff files: `v1-v2.diff` (full raw diff, 209 lines) and `v1-v2-substantive.diff` (138 lines after stripping pagination/whitespace noise).

Substantive changes Satoshi made between 2008-10 and 2009-03:

1. **Email address swap on title page.** `satoshi@vistomail.com` → `satoshin@gmx.com`. (Stylometric note: domain change + handle change; affects metadata only, not body text.)

2. **Abstract rewrite (the biggest single change).**
   - "without the burdens of going through a financial institution" → "without going through a financial institution"
   - "trusted party" → "trusted third party"
   - "honest nodes control the most CPU power on the network, they can generate the longest chain and outpace any attackers" → "**a majority of CPU power is controlled by nodes that are not cooperating to attack the network, they'll generate the longest chain and outpace attackers**"
   - "Messages are broadcasted on a best effort" → "Messages are broadcast on a best effort"
   The v2 abstract is more careful: removes "honest" (subjective) for a non-cooperation game-theoretic framing, and corrects "broadcasted" → "broadcast".

3. **Transaction-fee paragraph (NEW in v2).** Section 6 (Incentive) gains an entirely new paragraph that does not exist in v1:
   > "The incentive can also be funded with transaction fees. If the output value of a transaction is less than its input value, the difference is a transaction fee that is added to the incentive value of the block containing the transaction. Once a predetermined number of coins have entered circulation, the incentive can transition entirely to transaction fees and be completely inflation free."
   This is the conceptual genesis of the modern Bitcoin fee market — added between October 2008 and March 2009.

4. **Section reordering.** The "moving average difficulty" paragraph moves from the end of Section 6 (Incentive) in v1 to the end of Section 4 (Proof-of-Work) in v2 — its logically correct home.

5. **Tense softening.** "The incentive **may also** help encourage nodes to stay honest" → "The incentive **may** help encourage nodes to stay honest" (the new fee-funding paragraph absorbs the "also").

6. **Simplified Payment Verification cleanup (Section 8).**
   - "only vulnerable to reversal, the simplified method..." — v1 has redundant clause "transactions for themselves and are only vulnerable to reversal" that v2 trims to "transactions for themselves, the simplified method".
   - "reported transactions" → "alerted transactions".

7. **Grammar fix in step 1 of Section 5.** "New transactions are broadcasted to all nodes" → "New transactions are broadcast to all nodes" (matches abstract fix).

8. **Layout/typography.** v2 adds a missing page-number on the SPV/Privacy page break; column alignment of the Poisson probability table is tightened; whitespace around section headers normalised.

## Stylometric implications for this corpus

For Burrows' Delta against cypherpunk-era candidates, **v2 is the right primary input** — it's the version Satoshi most-publicly endorsed (signed on bitcoin.org from March 2009 onward) and contains the new transaction-fee paragraph that's distinctively his. **v1 is the right secondary input** for an internal-consistency check: the same author re-authored substantially the same paper five months apart, so Delta(v1, v2) is a useful lower-bound for the within-author distance under the chosen feature set. If Delta(candidate, v2) is in the same range as Delta(v1, v2), that's a signal that the within-author noise floor swamps the candidate-vs-Satoshi signal at the current feature dimensionality.
