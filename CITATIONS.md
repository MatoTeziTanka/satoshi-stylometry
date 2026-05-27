# Citations

Source-discipline policy: see [issue #1](https://github.com/MatoTeziTanka/satoshi-stylometry/issues/1).

**No Wikipedia. No encyclopedic aggregators. Primary sources required.** Tags:

- `[VF]` — Verified, primary source linked.
- `[UV]` — Unverified primary source. Cited only if commonly accepted in community knowledge; otherwise the claim is removed from the README.

## Date and event citations

| # | Claim | Status | Source |
|---|-------|--------|--------|
| C1 | Bitcoin whitepaper announced 2008-10-31, 14:10 EDT, from `satoshi@vistomail.com` | `[VF]` | [metzdowd cryptography list archive](https://www.metzdowd.com/pipermail/cryptography/2008-October/014810.html) |
| C2 | Bitcoin whitepaper exists in 2 versions (2008-10-31 SHA `427c63b3...`, 2009-03-24 SHA `b1674191...`) | `[VF]` | [archive.org item](https://archive.org/details/bitcoin-a-peer-to-peer-electronic-cash-system) + Wayback CDX of bitcoin.org/bitcoin.pdf |
| C3 | Genesis block: 2009-01-03 18:15:05 UTC, contains `The Times 03/Jan/2009` headline | `[VF]` | The blockchain itself (block 0) |
| C4 | First Satoshi → Hal Finney peer-to-peer transaction: 2009-01-12 | `[VF]` | Hal Finney's own BitcoinTalk and Bitcoin Forum posts; multiple contemporaneous sources. Block-number "170" specifically: `[UV]` in our search |
| C5 | Bitcoin 0.1.3 was the first source release (0.1.0–0.1.2 Windows-binary-only on SourceForge) | `[VF]` | [trottier/original-bitcoin GitHub archive](https://github.com/trottier/original-bitcoin) curated from bitcointrading.com forum's "Original Bitcoin Source Code Archives" thread |
| C6 | Hashcash announcement: 1997-03-28 16:52:26 GMT, from Adam Back `<aba@dcs.ex.ac.uk>` to cypherpunks@toad.com | `[VF]` | [hashcash.org/papers/announce.txt](http://www.hashcash.org/papers/announce.txt) — Back's own published announcement file |
| C7 | Hashcash formal paper: 2002-08 | `[VF]` | Title page of [draft-sassaman-mixmaster-…](https://cdn.nakamotoinstitute.org/docs/hashcash.pdf) shows "1st August 2002"; Bitcoin whitepaper reference [6] also cites 2002 |
| C8 | b-money proposed by Wei Dai, hosted at weidai.com/bmoney.txt; 1998 conception | `[UV]` | The text on weidai.com has no date header. "1998" attribution is bibliographic via subsequent citations (including Satoshi's whitepaper reference [1]). Primary source for date specifically: not located in our search |
| C9 | Bit Gold by Nick Szabo: canonical essay 2005-12-29; conception "a long time ago" | `[VF]` for 2005 publication, `[UV]` for the often-cited 1998 conception year | [unenumerated.blogspot.com/2005/12/bit-gold.html](https://unenumerated.blogspot.com/2005/12/bit-gold.html) — Szabo's own blog post |
| C10 | Satoshi's last public forum post: 2010-12-12 | `[VF]` | [`forum_posts.json` in nakamotoinstitute/nakamotoinstitute.org repo](https://github.com/nakamotoinstitute/nakamotoinstitute.org/blob/master/server/data/forum_posts.json) — direct corpus inspection |
| C11 | Satoshi's last public email: 2010-12-13 | `[VF]` | Same NI JSON corpus, bitcoin-list 0.3.19 release announcement |
| C12 | Satoshi → Mike Hearn "moved on to other things" email | `[UV]` for exact date | Primary source is Mike Hearn's January 2016 Medium post (blog.plan99.net), but the post is JS-rendered and was not scraped in our search. Year `2011` is in common circulation; exact day is `[UV]` |
| C13 | Len Sassaman died 2011-07-03, in Leuven Belgium, age 31, suicide | `[VF]` | [HN item 2723959](https://news.ycombinator.com/item?id=2723959) — contemporaneous announcement with confirmation from his wife Meredith Patterson ("maradydd") on the day of police notification: "I got the call from the Leuven police department a couple of hours ago"; "unambiguously suicide... He was 31" |
| C14 | Sassaman memorialized in Bitcoin blockchain block 167,956 (recorded 2011-07-31) | `[VF]` | [HN item 2830084](https://news.ycombinator.com/item?id=2830084) + the blockchain itself |
| C15 | Hal Finney's death: 2014-08-28, in Phoenix Arizona, from ALS complications | `[UV]` in our search for primary source | Common-knowledge in the Bitcoin community; primary source likely the BitcoinTalk announcement thread and family announcements that we didn't locate in our search. Don't claim without primary citation |
| C16 | Patoshi pattern discovered 2013 by Sergio Demian Lerner; ~1.1M BTC mined; coins never spent | `[VF]` | [Lerner 2013 original analysis](https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/) and subsequent follow-up posts on bitslog.com — primary publication by the researcher |
| C17 | Patoshi mining stopped ~May 2010, near block 54,316 | `[VF]` | Lerner bitslog.com follow-up posts; per the agent-produced [`forensics/patoshi-pattern.md`](forensics/patoshi-pattern.md) write-up |
| C18 | Patoshi timezone analysis is inconclusive (Pacific vs GMT vs Eastern claims compete) | `[VF]` | See [`forensics/patoshi-pattern.md`](forensics/patoshi-pattern.md) — cites Lerner 2020 (no biological signal in extraNonce), Lopp's Pacific claim, Chain Bulletin's GMT/London claim |

## Common-knowledge claims I have NOT independently sourced

These are widely cited in the Bitcoin community and trade press, but I have not located primary sources in our search. They are marked `[UV]` wherever they appear in the README and forensics write-ups:

- Hal Finney's biographical dates and place of death (community-knowledge level)
- The specific block number 170 for the first peer-to-peer transaction (we have the date but not the block)
- Aston University 2014 forensic-linguistic study by Jack Grieve et al. naming Szabo (cited in trade press; original report not located in our search)
- Adam Back's first email contact with Satoshi: August 2008 (widely cited; primary source not located)
- HBO "Money Electric" documentary 2024 naming Peter Todd as Satoshi (trade-press level)
- Wright v Hodlonaut UK court ruling 2024 (court records exist but not pulled in our search)

If you have primary sources for any of these, please open a PR.

## Sources we explicitly do NOT cite

- Wikipedia (any language edition)
- Fandom wikis, encyclopedic aggregators
- Quora, Stack Exchange answers (for factual claims)
- Reddit / forum threads (unless thread is itself a primary source — see HN policy above)
- AI-generated content as a source (LLM outputs, ChatGPT, etc.)
