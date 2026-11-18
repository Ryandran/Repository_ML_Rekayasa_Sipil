# Paket Bab 17 — Computer vision

> Notebook di [`notebooks/bab17/`](../../notebooks/bab17/); gambar di [`gambar/bab17/`](../../gambar/bab17/). Folder ini tidak memuat data: seluruh data dibangkitkan di dalam notebook (P17A, P17C) atau berasal dari paket Bab 16 (P17B).

## Isi notebook
- `P17A_deteksi_jendela_geser.ipynb`: adegan sintesis 128 × 128 (seed 17017), detektor jendela geser, IoU dan NMS buatan sendiri (diperiksa terhadap `torchvision.ops.nms`), kurva precision–recall, AP menurut ambang IoU.
- `P17B_transfer_learning_ketahanan.ipynb`: citra retak sintesis Bab 16 (seed 17018); CNN kecil, ResNet-18 pralatih (fitur beku dan setel halus), ResNet-18 dari nol pada 60/240/1.000 citra; uji ketahanan terhadap kontras, derau, dan blur dengan dan tanpa augmentasi.
- `P17C_aturan_kepatuhan_simulasi.ipynb`: aturan kepatuhan APD di atas keluaran detektor **simulasi** (seed 17019): ambang menurut biaya, ukuran pekerja, pelaporan per bingkai vs per orang.

## Kebutuhan
PyTorch dan torchvision versi CPU: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu`. P17B mengunduh bobot ResNet-18 (sekitar 45 MB) dari `download.pytorch.org` pada penggunaan pertama. Keluaran tersimpan dibuat dengan PyTorch 2.15.0, torchvision 0.29.2, scikit-learn 1.8.0. Waktu jalan: P17A sekitar 5 menit, P17B sekitar 8–10 menit, P17C beberapa detik (CPU 2 inti).

## Catatan reproduksibilitas
P17A dan P17C menghasilkan angka identik pada setiap pelarian. P17B tidak sepenuhnya deterministik pada CPU (konvolusi multi-thread): ukuran 60 dan 240 citra memakai tiga benih; angka dapat bergeser beberapa poin antarpelarian tanpa mengubah pola (tercatat di naskah Bab 17).

## Interpretasi wajib
Seluruh data dan simulasi bersifat sintesis. Angka menguji alur kerja (strategi transfer learning, ketahanan, IoU/AP, aturan kepatuhan), bukan kinerja pada foto lapangan. Dataset citra nyata yang berlisensi terbuka dan catatan lisensinya ada di subbab 17.9; citra pihak ketiga tidak disebarkan ulang di repositori ini.
