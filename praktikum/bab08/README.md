# Paket Bab 8 — Discovery dan inferensi kausal

> Letak berkas: notebook di [`notebooks/bab08/`](../../notebooks/bab08/), ilustrasi SVG di [`gambar/bab08/`](../../gambar/bab08/); workflow Orange dan data berada di folder ini.

## Isi paket
- `P08A_generator_data_sintesis.ipynb` — membuat CSV numerik untuk Python dan CSV berlabel treatment kategorikal untuk Orange.
- `P08B_analisis_kausal.ipynb` — skeleton discovery instruksional terbatas dan estimasi efek terstandardisasi.
- `maintenance_synthetic.csv` — data numerik untuk analisis Python.
- `maintenance_orange.csv` — salinan dengan label treatment kategorikal agar Orange menampilkannya sebagai kelompok.
- `Orange_Bab8_Eksplorasi.ows` — File → Data Table, Distributions, Scatter Plot. Workflow untuk eksplorasi, bukan inferensi kausal.
- `../../gambar/bab08/Gambar_8_1_DAG_pemeliharaan_perkerasan.svg` — DAG asumsi kerja; PNG tertanam dalam naskah.

## Urutan penggunaan
1. Jalankan P08A dari root repository; dua CSV terbentuk di `praktikum/bab08/`.
2. Buka OWS di Orange 3.41.0 dan pilih `maintenance_orange.csv` pada widget File.
3. Gunakan `maintenance` sebagai variabel warna/kelompok untuk membandingkan distribusi IRI baseline dan IRI enam bulan. Data Table membantu memeriksa baris dan kolom. Visualisasi menunjukkan pola/ketimpangan, bukan efek kausal.
4. Jalankan P08B untuk membandingkan selisih mentah dengan estimasi standardisasi-regresi dan interval bootstrap.
5. Diskusikan estimand, consistency, exchangeability, positivity, bentuk model, dan confounding tak terukur sebelum menyatakan kesimpulan.

Data sepenuhnya sintetis, bukan bukti lapangan atau rekomendasi kebijakan. Bootstrap mengukur variasi sampling dan tidak mengoreksi bias identifikasi.

## Hasil acuan
- P08A dan P08B dijalankan ulang dari root repository menggunakan Python Orange 3.41.0. Generator menghasilkan 2.400 baris dengan seed tetap; analisis mereproduksi perbedaan mentah +0,453, estimasi standardisasi −0,828, dan interval bootstrap 95% [−0,865; −0,783] terhadap efek DGP −0,80.
- Workflow Orange memuat 2.400 baris; Distributions dan Scatter Plot menerima data. OWS memuat empat node dan tiga koneksi. Grafik menunjukkan asosiasi dan distribusi, bukan identifikasi efek kausal.
- Orange dipakai untuk eksplorasi; inferensi di notebook Python. Data Table terhubung untuk inspeksi baris, tetapi smoke test headless tidak dapat memeriksa status inputnya melalui atribut publik.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
