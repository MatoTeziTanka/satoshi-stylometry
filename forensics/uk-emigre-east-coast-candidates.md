# Candidate-set expansion: UK descent + US East Coast

> **Headline finding:** primary-source sweep finds **zero candidates** who satisfy all four axes of the UK-emigré-East-Coast hypothesis with traceable evidence. The hypothesis (if correct) points outside the publicly-traceable cypherpunk community, or to someone who used a non-UK email address on the cypherpunks list (and is therefore invisible to a domain-based archive filter). This is a negative finding, reported because it tightens the search space.

The hypothesis is documented in [`uk-descent-eastern-resident-hypothesis.md`](uk-descent-eastern-resident-hypothesis.md). It requires a candidate fitting:

1. **UK origin or UK education.** Born in UK, or educated at UK universities/schools.
2. **US East Coast residence 2008–2010.** DC, NYC, Boston, Princeton, RTP, or anywhere in the EST corridor during Bitcoin's launch window.
3. **C++ MFC Windows enterprise background.** The Bitcoin codebase shows MFC Hungarian C-prefix naming (`CTransaction`, `CBlock`, `CScript`) — a 1990s-2000s Windows enterprise pattern.
4. **Cypherpunk activity.** Active on the cypherpunks list (~1992–2001), the metzdowd cryptography list (~2001+), or had published writings citing Hashcash, b-money, Haber/Stornetta, Merkle.

## Search method

We sweeped the cypherpunk-era archives for UK contributors by email domain and tried to trace their post-2001 trajectories. Sources:

- [Cypherpunks mailing list author index at cryptoanarchy.wiki](https://mailing-list-archive.cryptoanarchy.wiki/authors/by-posts/) — filtered for UK domains (`.ac.uk`, `demon.co.uk`, etc.) ranked by post count.
- [Metzdowd November 2008 archive](https://www.metzdowd.com/pipermail/cryptography/2008-November/) — the month Bitcoin was announced; all respondents enumerated.
- Personal academic homepages and self-published CV pages of named cryptographers (no Wikipedia — see [CITATIONS.md](../CITATIONS.md) discipline).

## Candidate-by-candidate (those reaching primary-source bar)

### Adam Back

Strongest match on axes 1, 3 (partial), and 4. **Directly fails axis 2.**

- UK origin: Born London 1970, PhD University of Exeter ([cypherspace.org/adam](http://www.cypherspace.org/adam/)). [VF]
- East Coast residence: NO. UK-resident through 2008, moved to Malta in 2009. No US East Coast residence trace.
- C++/MFC: Hashcash codebase is C, not C++; no MFC pattern in his published code. [Incomplete match]
- Cypherpunk activity: 732 posts under `aba@dcs.exeter.ac.uk`, longest-posting UK cypherpunk by volume. [VF]

**Stance:** Adam Back belongs in the existing candidate set as a "UK resident" candidate, not the UK-emigré-East-Coast branch. His geography directly contradicts axis 2. (The NYT April 2026 investigation implicating Back as Satoshi rests on stylometry that the paper's own linguist called "inconclusive"; see [CITATIONS.md "Common-knowledge claims I have NOT independently sourced"](../CITATIONS.md) for the discipline-compliant framing of that material.)

### Antonomasia (`ant@notatla.demon.co.uk`)

A pseudonymous UK cypherpunks-list contributor with hashcash-relevant posts. The four-axis profile is *possible* but entirely unverifiable.

- UK origin: demon.co.uk was a UK-only ISP — establishes UK location during posting period (~1997–2001). [VF for posting-period UK location]
- East Coast residence: no evidence. Identity unknown; no way to trace later location. [N/A]
- C++/MFC: posts discuss remailers, PGP, TEA cipher, hashcash. Technically sophisticated. No specific C++/MFC signal located. [N/A]
- Cypherpunk activity: 43 posts including hashcash discussions. [VF]

**Stance:** worth pursuing only if someone can de-anonymize the identity through other means (remailer server registration, UK company records for "notatla"). Not worth pulling into stylometric corpus without knowing who the writer is; 43 posts is also too thin for reliable stylometry against Satoshi's 582+ timestamped events.

### Paul Bradley (`paul@fatmans.demon.co.uk`)

High-volume UK cypherpunks list contributor (501 combined posts).

- UK origin: demon.co.uk during posting period. [VF for posting-period]
- East Coast residence: no professional profile or corporate affiliation found. [N/A — no evidence]
- C++/MFC: posts discussed cryptographic implementation, no specific C++/MFC signal. [N/A]
- Cypherpunk activity: ~501 posts over 1997–2000. [VF]

**Stance:** insufficient evidence on the non-UK-list axes. Personal-ISP subdomain gives no career signal. Untraceable post-list.

### Nicko van Someren

Cambridge PhD, ran nCipher (UK HSM company), moved to Juniper Networks (Sunnyvale CA) in 2010.

- UK origin: Cambridge undergraduate and PhD. [VF via multiple sources, including ResearchGate]
- East Coast residence: NO. Juniper Networks is California (West Coast). [VF — negative]
- C++/MFC: nCipher produced Windows-integrated HSM software; plausible MFC exposure, but no primary code reference found. [Suggestive but unverified]
- Cypherpunk activity: no cypherpunks list posts located, no metzdowd posts located. [No evidence]

**Stance:** fails the East Coast axis (West Coast), and the cypherpunk-activity gap is significant given that the hypothesis requires someone steeped in hashcash / b-money literature.

### Ian Grigg

Financial-cryptography theorist; Australian undergraduate, UK MBA.

- UK origin: NO. BSc UNSW (Sydney), MBA London Business School. Australian-educated, not UK-born or UK-undergraduate. [VF — partial / negative]
- East Coast residence: no US East Coast residence trace. LISA 2008 conference appearance is travel, not residence. Affiliations are UK and Caribbean. [No evidence]
- C++/MFC: papers emphasize architectural and protocol-level work, not implementation. No C++/MFC signal. [N/A]
- Cypherpunk activity: published financial-cryptography papers cited in pre-Bitcoin digital-cash discussion; archived at [nakamotoinstitute.org/authors/ian-grigg/](https://nakamotoinstitute.org/authors/ian-grigg/). [VF]

**Stance:** fails the UK-origin axis (Australian-educated) and the East Coast axis. Existing trade-press "Ian Grigg is Satoshi" speculation is excluded per the repo's citation discipline.

## Negative finding

No candidate satisfies all four axes with primary-source evidence. The closest single-axis matches are:

| Axis | Best primary-source match |
|------|---------------------------|
| UK origin | Adam Back, Paul Bradley, Antonomasia, Nicko van Someren — all UK-traceable to the posting period |
| East Coast 2008–2010 residence | NONE in our shortlist |
| MFC C++ Windows enterprise | NONE in our shortlist with direct evidence |
| Cypherpunk activity | Adam Back (732 posts) — highest-volume UK cypherpunk |

The four-axis intersection is empty in our search.

## Why the search may have missed the true candidate

If Satoshi was UK-emigré-East-Coast, our primary-source sweep would miss them under any of these conditions:

1. **Email domain camouflage.** A UK national using a US-based email provider on the cypherpunks list (yahoo.com, hotmail.com, gmail.com after 2004) is invisible to our domain-based filter. The list has thousands of such posters; we cannot enumerate them.
2. **Late-cypherpunk arrival via metzdowd.** Someone who joined the cryptography conversation only after the metzdowd list took over (~2001+) would have a thinner archive trail. We checked metzdowd 2008 respondents; we did not exhaustively search 2001–2007.
3. **Non-public corporate cryptographer.** UK-trained cryptographers at US East Coast financial firms (Goldman, Morgan Stanley, JPM, hedge funds, NSA contractors at BBN/Raytheon) often have no public cypherpunk trail. They show up in IETF working-group records or DEF CON talks but not on the open list archives.
4. **Pseudonymous identity not yet linked.** Antonomasia, "Cypherpunks 1995–2000 era handles" — many are pseudonyms whose real-world identities have never been linked. If Satoshi was one of these, no domain-based filter helps.

## What this means for the hypothesis

The hypothesis (UK descent + US East Coast residence 2008–2010) **survives** the candidate-search test, in the technical sense that no surfaced candidate contradicts it. But it is not *confirmed* either — the four-axis filter found no positive match because the public-record trail thins out for exactly the kind of person the hypothesis describes (mid-career UK-emigré at a non-academic US institution).

The honest framing: **this hypothesis points outside the publicly-traceable cypherpunk archive sweep.** A future researcher wanting to test it further would need to:

1. Cross-reference IETF working-group attendance lists (UK affiliations + US East Coast subsequent affiliations) from 2002–2010.
2. Pull Financial Cryptography conference attendance records (1997–2010) for UK-trained East Coast US participants.
3. Pull UK Companies House records for cryptography-or-fintech-related UK→US migrations 2000–2008.
4. Attempt to de-anonymize the higher-volume pseudonymous cypherpunks (Antonomasia and similar) via remailer server registration records or other forensic methods.

None of these is impossible; none is in scope for this repo's current sweep.

## What we will NOT do

- We will not name a specific person on the basis of "fits the type" without primary-source evidence for all four axes. The four-axis bar is the test; absence of a name passing the bar is the result.
- We will not promote any of the partial-fit candidates above (Back, Antonomasia, Bradley, van Someren, Grigg) to "likely Satoshi." Each has at least one disqualifying axis or one missing-evidence axis.
- We will not lean on the NYT April 2026 trade-press investigation, the HBO "Money Electric" Peter Todd theory, or any other secondary-source nominations. Per [CITATIONS.md](../CITATIONS.md) issue #1 discipline.

## Methodology caveats

- The cryptoanarchy.wiki archive favors high-volume posters. Someone who lurked or posted rarely is invisible here.
- UK `demon.co.uk` participants are legible because the ISP domain is UK-specific. A UK national using a US-based email provider in 2000–2008 is invisible to a domain-based sweep.
- The metzdowd 2008 Bitcoin thread shows only public respondents. Anyone who received the whitepaper privately or was an existing contact of Satoshi's would not appear.
- "No East Coast trace found" is NOT the same as "not East Coast" — it reflects the limits of public-record searchability for pseudonymous 1990s list participants.

## What candidate-type the hypothesis still points to

The original [`uk-descent-eastern-resident-hypothesis.md`](uk-descent-eastern-resident-hypothesis.md) profile is unchanged:

- UK-born or UK-educated
- US East Coast resident in 2008–2010
- Technical role with C++ exposure (likely Windows-MFC)
- Active in cypherpunk circles (read Hashcash, b-money, Haber/Stornetta)

The most likely candidate-type missing from our sweep is "UK national working at a US East Coast bank or financial-cryptography firm in 2008–2010, who participated in cypherpunk discussions under a US-based email address." That profile is structurally invisible to our search method.
