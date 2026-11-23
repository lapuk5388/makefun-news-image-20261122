"""THE MILLSTREAM dari @agusproblem (Akun Final 6) — NI22 Wave 7.

Seperti aliran penggilingan yang tidak boleh keruh di tengah jalan,
berkas gambar ini diperiksa di hulu (header dan ukuran), dialirkan
utuh ke keluaran, lalu dicek lagi di hilir sebelum dinyatakan bersih.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

CONCEPT = "THE MILLSTREAM"
ACCOUNT = "@agusproblem"
ACCOUNT_LABEL = "Akun Final 6"
BOUNTY = "news-image-20261122"
STORIES = 36
MAX_SIDE = 1024

SIGNATURE = b"\x89PNG\r\n\x1a\n"


def measure(path):
    """Ukur berkas sekali jalan: kembalikan (ukuran, sha256) dari isi penuhnya."""
    sha = hashlib.sha256()
    seen = 0
    data = path.read_bytes()
    sha.update(data)
    seen = len(data)
    return seen, sha.hexdigest()


def header_dimensions(path):
    """Baca lebar dan tinggi dari potongan 33 byte pertama PNG."""
    with path.open("rb") as fh:
        opening = fh.read(33)
    if len(opening) < 33:
        print("Pembuka berkas kurang dari 33 byte.", file=sys.stderr)
        sys.exit(1)
    if opening[:8] != SIGNATURE:
        print("Signature PNG tidak cocok.", file=sys.stderr)
        sys.exit(1)
    if opening[12:16] != b"IHDR":
        print("Chunk pertama bukan IHDR.", file=sys.stderr)
        sys.exit(1)
    lebar, tinggi = struct.unpack(">II", opening[16:24])
    return lebar, tinggi


def main():
    base = Path(__file__).resolve().parent
    origin = base / "entry.png"
    if not origin.is_file():
        print("entry.png hilang dari folder repo.", file=sys.stderr)
        return 1

    lebar, tinggi = header_dimensions(origin)
    if lebar > MAX_SIDE or tinggi > MAX_SIDE:
        print(f"Sisi {lebar}x{tinggi} melampaui pagu {MAX_SIDE}.", file=sys.stderr)
        return 1

    size_before, hash_before = measure(origin)

    out_root = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_root.mkdir(parents=True, exist_ok=True)
    replica = out_root / "entry.png"
    replica.write_bytes(origin.read_bytes())

    size_after, hash_after = measure(replica)
    if (size_after, hash_after) != (size_before, hash_before):
        print("Salinan di keluaran tidak identik.", file=sys.stderr)
        return 1

    print(f"Concept: {CONCEPT}")
    print(f"Account: {ACCOUNT} ({ACCOUNT_LABEL})")
    print(f"Bounty: {BOUNTY}")
    print("File: entry.png")
    print(f"Size: {size_before}")
    print(f"Dim: {lebar}x{tinggi}")
    print(f"SHA256: {hash_before}")
    print(f"Stories: {STORIES}")
    print("Copy verified byte-identical.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
