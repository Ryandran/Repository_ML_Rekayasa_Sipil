# Paket Bab 16 — Pengantar deep learning

> Notebook di [`notebooks/bab16/`](../../notebooks/bab16/); gambar di [`gambar/bab16/`](../../gambar/bab16/).

## Isi
- `citra_retak_sintetis.npz`: 2.400 citra abu-abu 32 × 32 piksel dari 60 panel virtual (`X` uint8, `y` 1 = retak, `panel`, `seed`). Dibangkitkan oleh P16A dengan seed 16016; menjalankan ulang P16A menghasilkan berkas identik (md5 6e15b14e888ae494b6d72b408218c26e).

## Urutan
1. Jalankan `P16A_generator_citra_retak_sintetis.ipynb` (opsional; berkas data sudah disertakan).
2. Jalankan `P16B_pengantar_deep_learning.ipynb` dari root proyek. Data kuat tekan beton sintesis dibaca dari paket Bab 3.

## Kebutuhan
PyTorch versi CPU, hanya untuk notebook bab ini: `pip install torch --index-url https://download.pytorch.org/whl/cpu`. Keluaran tersimpan dibuat dengan PyTorch 2.15.0 dan scikit-learn 1.8.0; satu pelatihan CNN beberapa detik di CPU.

## Interpretasi wajib
Seluruh data sintesis. Hasil menguji alur kerja (MLP vs model klasik; CNN vs MLP piksel; pembagian per panel; variasi antarbenih), bukan kinerja deteksi retak lapangan.
