# THE MILLSTREAM — Final 6 (@agusproblem) · NI22 Wave 7

One-page newspaper for Sunday 22 November 2026: 15 cards + 21 briefs = 36
stories, 7 regions. Lead order Hong Kong → COP31 → Ukraine; lumut / zaitun.
Duel winner is the alternate Layout A (three leads in a row) — the matrix
wide-lead layout lost the duel (its wide strip reads empty, page tallest).

## Build

- `compose.py` — PIL renderer (W=3900; fonts x1.45 vs G6, structure x~1.3).
  Renders `variant_A.png` (matrix layout B, matrix palette), `variant_B.png`
  (alternate layout A, same palette), `variant_C.png` (layout B, rust accent).
  Duel in `duel.md`: winner **B (35/40)**.
- `ni22v7-finish.sh final6 B` — fits winner to `entry.png` (1024×1024),
  runs margin check with `--fresh ni22-fresh-g7.txt`, writes `preview-300.png`.
- `main.py` — stdlib-only copy-only carrier with the 1024×1024 dimension gate.

## Gates (verified)

- entry.png 1024×1024, 213.363 bytes, sha256
  `6267589b617b1fdfb32dad4d07d94f2420795fe17703efdbe3bbac19dbba085a`
- margin check 13/13 (fresh G7 pool)
- render aspect 0,905 (3900×4311)
- main.py 2× run byte-identical (see verification below)

## Verify

```
MAKEFUN_OUTPUT_DIR=/tmp/ni22v7-verify-final6 python3 main.py
```

Izin Brian (chat utama, 23 Nov 2026): "Ya — bangun G7, bedah Top 1 dulu".
