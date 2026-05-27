# Satoshi Code Corpus — Source Provenance

## Version

**Bitcoin v0.1.3 ALPHA** (released December 2009)

This is the earliest publicly-archived release of the Bitcoin reference
implementation with source code attached. Bitcoin 0.1.0 (January 2009) and
0.1.1/0.1.2 were Windows binary-only releases; 0.1.3 was the first source
release. All files in this corpus carry `Copyright (c) 2009 Satoshi Nakamoto`
headers and predate the first community contributor commits (Martti "Sirius"
Malmi began contributing in late 2009/early 2010, post-0.1.3).

## Source

- **Primary**: https://github.com/trottier/original-bitcoin
- **Commit**: `92ee8d9a994391d148733da77e2bbc2f4acc43cd`
- **Original upstream**: bitcointrading.com forum "Original Bitcoin Source
  Code Archives" thread (cited in trottier's commit message)
- **License**: MIT/X11 (per `license.txt` — Satoshi-authored)

The trottier/original-bitcoin repo is the curated historical archive of the
original Satoshi codebase as released on SourceForge before the project
migrated to GitHub. The main `bitcoin/bitcoin` GitHub repository started
later (mid-2010) and its earliest commits are already past 0.1.3.

## Files Included (22 files, 16,644 LOC)

All files are Satoshi-authored C++ source, copied verbatim from
`/tmp/original-bitcoin/src/` after `git clone --depth 1`.

### .cpp files (9,621 LOC)

| File         | LOC  |
|--------------|------|
| ui.cpp       | 3228 |
| main.cpp     | 2660 |
| script.cpp   | 1127 |
| net.cpp      | 1067 |
| db.cpp       |  608 |
| util.cpp     |  379 |
| irc.cpp      |  288 |
| market.cpp   |  264 |

### .h files (7,023 LOC)

| File         | LOC  |
|--------------|------|
| main.h       | 1317 |
| serialize.h  | 1151 |
| net.h        |  856 |
| uint256.h    |  750 |
| script.h     |  597 |
| bignum.h     |  498 |
| db.h         |  420 |
| ui.h         |  418 |
| util.h       |  399 |
| base58.h     |  201 |
| market.h     |  182 |
| key.h        |  156 |
| headers.h    |   71 |
| irc.h        |    7 |

## Files Excluded (NOT Satoshi-authored)

These files were present in the original tarball but deliberately omitted
from the stylometry corpus because they would contaminate the signal:

| File             | Why excluded                                              |
|------------------|-----------------------------------------------------------|
| `sha.cpp`        | Public domain, Wei Dai / Steve Reid (Crypto++ 5.5.2)      |
| `sha.h`          | Public domain, Wei Dai / Steve Reid (Crypto++ 5.5.2)      |
| `uibase.cpp`     | wxFormBuilder machine-generated (Satoshi copyright header but the code itself is auto-generated wxWidgets boilerplate — not Satoshi's hand-written style) |
| `uibase.h`       | wxFormBuilder machine-generated (same reason)             |
| `uiproject.fbp`  | wxFormBuilder project file (XML, not C++)                 |
| `ui.rc`          | Windows resource file (not C++)                           |
| `makefile`       | GNU make script (not C++)                                 |
| `makefile.vc`    | MSVC nmake script (not C++)                               |
| `src/rc/`        | Windows icon/manifest resources                           |
| `bitcoin.exe`    | Compiled binary                                           |
| `libeay32.dll`   | OpenSSL bundled binary                                    |
| `mingwm10.dll`   | MinGW runtime bundled binary                              |

No Boost headers were bundled in the original tarball — Boost is used via
system headers (`#include <boost/...>`) referenced in `headers.h`. The
project also depends on OpenSSL and wxWidgets, but those are external and
not present in source form.

## Attribution Notes

- Every `.cpp`/`.h` file in this corpus begins with
  `// Copyright (c) 2009 Satoshi Nakamoto`.
- The codebase is single-author per the headers; no other contributor
  attribution appears.
- Style markers visible at a glance: Hungarian notation (`pszBuffer`,
  `nValue`, `vchData`, `mapBlockIndex`), Allman braces, heavy use of
  `printf`-style debug logging via custom `printf()` wrapper, MFC-influenced
  patterns (`CCriticalSection`, `CDataStream`, `CScript`), Windows-first
  cross-platform conditionals.

## Verification Reproducibility

```bash
git clone --depth 1 https://github.com/trottier/original-bitcoin.git
cd original-bitcoin
git rev-parse HEAD  # expect: 92ee8d9a994391d148733da77e2bbc2f4acc43cd
grep -l "Satoshi" src/*.cpp src/*.h  # 20 files match
```
