# Paket Bab 7 — Explainability dan interpretabilitas

> Letak berkas: notebook di [`notebooks/bab07/`](../../notebooks/bab07/), ilustrasi SVG di [`gambar/bab07/`](../../gambar/bab07/); workflow Orange dan data berada di folder ini.

## Isi paket
- `P07_explainability.ipynb` — analisis Python untuk menjelaskan model prediksi stabilitas Marshall.
- `Orange_Bab7_Explainability.ows` — alur Orange 3.41.0: File → Select Columns → Rank dan Tree → Tree Viewer.
- `../../gambar/bab07/Gambar_7_1_Global_dan_Lokal.svg` — ilustrasi penjelasan global dan lokal.

## Cara menjalankan
1. Jalankan generator `notebooks/bab06/P06A_generator_data_sintesis.ipynb` untuk menghasilkan `data_bab6/marshall_regression.csv`.
2. Buka workflow OWS di Orange 3.41.0. Pilih CSV tersebut pada widget File; pastikan `stability_kN` menjadi target dan `mix_id` menjadi metadata pada Select Columns.
3. Periksa Rank sebagai skor keterkaitan fitur dengan target, lalu telusuri pohon intrinsik melalui Tree Viewer. Rank bukan SHAP dan bukan importance dari Random Forest.
4. Jalankan P07 di Jupyter/Colab. Notebook mencoba folder kerja lokal dan folder Bab 6. Jika CSV belum tersedia, unggah file di Colab atau salin CSV generator ke `data_bab6` di Jupyter lokal. Notebook menampilkan permutation importance, PDP/ICE, pohon dangkal, dan penjelasan satu observasi. SHAP/LIME opsional dan akan dilewati bila paket belum tersedia.

## Batas penggunaan
Data sepenuhnya sintetis; fungsi generator bukan hasil uji laboratorium atau hukum material. Semua penjelasan menggambarkan model pada data sintesis. Penjelasan fitur bukan bukti kausal, mekanisme material, rekomendasi desain, atau sertifikasi emisi.

## Hasil acuan
- P07 dijalankan seluruh selnya pada runtime Orange 3.41.0; permutation importance, PDP/ICE, pohon dangkal, dan contoh lokal berjalan. SHAP/LIME tidak tersedia dalam runtime tersebut dan bagian opsional dilewati.
- OWS dijalankan melalui runtime Orange 3.41.0 dengan salinan uji sementara yang diarahkan ke CSV Marshall. Workflow selesai tanpa error; peringatan deprecation pada widget Tree tidak mengganggu hasil.
- Jalur CSV tidak disimpan di OWS terbitan sehingga tetap portabel. Saat membuka OWS, pilih CSV dari generator Bab 6. Jika Orange tidak memulihkan peran target secara otomatis, tetapkan `stability_kN` sebagai target dan `mix_id` sebagai metadata pada Select Columns.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
