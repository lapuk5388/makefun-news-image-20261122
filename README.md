# THE MILLSTREAM — news-image-20261122 — Akun Final 6

Gambar berita kepunyaan @agusproblem (Akun Final 6) untuk bounty
news-image-20261122 di make.fun, hasil pengerjaan gelombang 7.

## Gelombang 7

Bahan bakunya pool segar Minggu 22 Nov 2026: 15 kartu dan 21 brief
yang kalau dijumlah pas 36 cerita, tersebar di 7 region. Di atas
kanvas ada strip angka 186 / 161 / 35% / $120bn / 720 / 9 / 50.
Semua bahan sudah lewat DATE CHECK — yang kedaluwarsa dicatat
sebagai buangan bernama dan disingkirkan sebelum perakitan.

## Entry

- Dimensi: 1024x1024 piksel (di dalam gerbang 1024x1024)
- Ukuran: 213363 byte
- SHA256: 6267589b617b1fdfb32dad4d07d94f2420795fe17703efdbe3bbac19dbba085a
- Margin checker: 13/13 lulus

`main.py` berjalan hanya dengan pustaka standar Python. Tugasnya
memeriksa signature PNG dan chunk IHDR, menolak dimensi di atas
1024, menyalin `entry.png` ke folder keluaran tanpa modifikasi,
dan membuktikan keidentikan salinan lewat sha256 serta ukuran.
