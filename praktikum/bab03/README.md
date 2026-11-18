# Paket Bab 3 — Data dan Statistik

> Letak berkas: notebook di [`notebooks/bab03/`](../../notebooks/bab03/), ilustrasi SVG di [`gambar/bab03/`](../../gambar/bab03/); workflow Orange dan data berada di folder ini.

Dataset dibangkitkan oleh P03A dengan seed 30303, 1.200 campuran virtual, dan 10 kolom. Persamaan target hanya DGP pedagogis: bukan hasil uji, basis desain campuran, representasi mutu lapangan, atau bukti kausal.

## Urutan kerja
1. Jalankan `P03A_generator_data_sintesis_beton.ipynb` di Google Colab atau Python lokal. Hasilnya ditulis ke `Data/`.
2. Buka `Orange_Bab3.ows` pada Orange 3.41.0. Pilih `praktikum/bab03/data_sintesis_beton_orange.tab` di widget File. Hubungkan tersedia: Data Table, Distributions, Scatter Plot, Correlations.
3. Jalankan `P03B_audit_eksplorasi_data.ipynb` dari root proyek untuk audit skema, rentang, ringkasan, korelasi dan contoh diagnosis sementara.

## Peringatan interpretasi
ID spesimen adalah metadata, bukan fitur. Rasio air-semen diturunkan dari air dan semen; tiga kolom ini berkaitan secara matematis. Korelasi terhadap target hanya menggambarkan generator yang diketahui. Salinan rusak untuk latihan dibuat dalam memori dan tidak menimpa CSV sumber.
Keluaran P03B dengan seed 30303: target sintetis rata-rata 26,44 MPa (simpangan baku 9,17; rentang 5,00–53,10); Pearson rasio air-semen–target −0,655 dan Spearman −0,652. Hasil menggambarkan persamaan generator, bukan campuran atau kuat tekan beton lapangan. CSV bersih memiliki 1.200 baris, semua ID unik, tanpa missing cell dan duplikasi persis.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
