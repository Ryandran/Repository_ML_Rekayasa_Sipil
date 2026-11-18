# Paket Bab 10 — Praktik audit penelitian ML

> Letak berkas: notebook di [`notebooks/bab10/`](../../notebooks/bab10/), ilustrasi SVG di [`gambar/bab10/`](../../gambar/bab10/); workflow Orange dan data berada di folder ini.

## Isi
- `P10A_generator_data_sintesis.ipynb` — membangkitkan dataset beton sintetis multi-batch dengan seed tetap.
- `P10B_audit_data_dan_validasi.ipynb` — statistik data, baseline, validasi acak dan held-out batches, diagnostik residual.
- `Orange_Bab10_Audit_Data.ows` — File → Data Table, Distributions, Scatter Plot.
- `Data/` — CSV dan `.tab` keluaran generator.
- `SVG/` — ilustrasi proses audit yang juga tertanam sebagai PNG di DOCX.

## Urutan
Jalankan P10A lebih dulu dari root repository; notebook menghasilkan CSV serta `.tab` untuk Orange, dengan `strength_MPa` sebagai target dan specimen/batch sebagai metadata. Buka workflow di Orange 3.41.0 dan pilih `concrete_strength_orange.tab` pada widget File untuk memeriksa tabel/distribusi. Jalankan P10B dari root repository. P10B menguji bahwa batch tidak tumpang tindih pada held-out split dan membandingkan baseline dengan model bertahap.

Data sintetis dibangkitkan dari persamaan ilustratif dan efek batch yang diketahui. Angka skor hanya menguji workflow, bukan validasi suatu campuran nyata atau dasar desain. Kelompok penggunaan harus dipilih dari rancangan penelitian aktual (misalnya batch, laboratorium, lokasi, atau waktu), bukan ditiru otomatis dari contoh ini.

## Status pemeriksaan (16 November 2026)
- P10A dan semua sel P10B dijalankan pada Python Orange 3.41.0. Generator menghasilkan 990 spesimen pada sembilan batch. Berkas `.tab` menetapkan `strength_MPa` sebagai target dan `specimen_id`/`batch_id` sebagai metadata.
- OWS memuat 990 baris; Distributions dan Scatter Plot menerima data. Workflow hanya untuk eksplorasi, sedangkan perbandingan baseline dan model dijalankan di P10B.
- Pada split acak, Ridge MAE 3,507 MPa, RMSE 4,264, R² 0,779; pada held-out batches MAE 3,956, RMSE 4,771, R² 0,728. Random Forest: MAE 3,840 dan 3,958 MPa; R² 0,738 dan 0,722. Perbedaan ini menggambarkan dua target generalisasi pada DGP sintesis, bukan validasi campuran beton nyata.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
