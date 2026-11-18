# Paket Bab 5 — Indikator Kinerja dan Metrik Kesalahan

> Letak berkas: notebook di [`notebooks/bab05/`](../../notebooks/bab05/), ilustrasi SVG di [`gambar/bab05/`](../../gambar/bab05/); workflow Orange dan data berada di folder ini.

## Isi paket
- `P05A_generator_data_sintesis.ipynb` — membuat data sintesis kurva balok, prioritas jembatan dan clustering perkerasan.
- `P05_evaluasi_metrik.ipynb` — analisis dan latihan metrik. Jalankan P05A terlebih dahulu.
- `Orange_Bab5_Evaluasi.ows` — evaluasi model regresi melalui Orange 3.41.0.
- `../../gambar/bab05/Gambar_5_1_Matriks_Kebingungan.svg` dan `../../gambar/bab05/Gambar_5_2_Global_dan_Lokal.svg` — ilustrasi pendamping.

## Menjalankan latihan
1. Jalankan P05A di Google Colab atau Jupyter. Ia membuat folder `data_bab5` dengan CSV sintetis di direktori kerja.
2. Jalankan `P05_evaluasi_metrik.ipynb` dari direktori kerja yang sama. Ia menahan seluruh balok pada pemisahan uji, menghitung ukuran regresi, memeriksa kasus/subset, bootstrap per kelompok, klasifikasi dan clustering.
3. Buka `Orange_Bab5_Evaluasi.ows`. Pada widget **File**, pilih `data_bab5/data_sintesis_lendutan_per_balok.csv`. Berkas ini berisi satu baris per balok pada beban terminal yang sama; tetapkan `deflection_mm` sebagai target, `beam_id` sebagai metadata, dan fitur geometri/lingkungan sebagai masukan. Sambungkan beberapa learner ke **Test and Score**. Untuk analisis kurva tahap demi tahap, gunakan P05B dengan pemisahan kelompok.
4. Pembagian acak per baris tidak sesuai bila klaimnya generalisasi ke balok baru. Bila Orange 3.41.0 tidak menyediakan evaluasi berbasis grup lewat widget, gunakan `GroupShuffleSplit` di P05B.

Semua data berasal dari generator seed 51505 dan bukan hasil eksperimen, inventaris jembatan atau survei jalan. Nilai metrik latihan tidak boleh ditafsirkan sebagai batas desain, keselamatan, atau kinerja lapangan.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
