# Paket Bab 9 — Data, biaya komputasi, dan model lanjutan

> Letak berkas: notebook di [`notebooks/bab09/`](../../notebooks/bab09/), ilustrasi SVG di [`gambar/bab09/`](../../gambar/bab09/); workflow Orange dan data berada di folder ini.

## Isi paket
- `P09A_generator_data_sintesis.ipynb` — generator spalling RC dan kapasitas momen.
- `P09B_augmentasi_ensemble_greenml_automl.ipynb` — oversampling train-only, metrik kelas minoritas, voting ensemble, pencarian GridSearchCV, dan proksi Green ML.
- `P09C_symbolic_regression_mapping.ipynb` — kandidat persamaan, pemetaan mekanika, dan uji ekstrapolasi.
- `Orange_Bab9_Spalling_Ensemble.ows` — workflow klasifikasi: File, Data Table, Distributions, Scatter Plot. Model comparison is handled in Python so the train-only oversampling and held-out test design stay explicit.
- `Data/` — CSV keluaran Python dan berkas `.tab` untuk Orange dengan tipe serta peran target eksplisit.
- `../../gambar/bab09/Gambar_9_1_Pemisahan_data_dan_augmentasi.svg` — diagram pencegahan kebocoran.

## Urutan praktik
1. Jalankan P09A dari root repository.
2. Buka OWS di Orange 3.41.0, pilih `rc_spalling_orange.tab` pada File; tipe target spalling dan metadata ID sudah didefinisikan. Amati distribusi fitur serta kelas.
3. Jalankan P09B untuk membandingkan baseline, interpolasi minoritas yang hanya diterapkan pada train, ensemble voting, GridSearchCV pada data train, dan proksi waktu/energi.
4. Jalankan P09C untuk membandingkan kandidat ekspresi mekanika dan model black-box pada wilayah interpolasi serta kelas fy yang lebih tinggi.

Data seluruhnya sintetis dan bukan catatan uji, rekomendasi struktur, atau model keselamatan. Energi yang dicetak merupakan estimasi sensitivitas berdasarkan daya asumsi, bukan hasil pengukuran perangkat. Oversampling demonstratif adalah interpolasi antarpasangan kelas minoritas; ia bukan implementasi resmi SMOTE.

## Hasil acuan
- P09A, P09B, dan P09C dijalankan ulang seluruh sel kodenya pada runtime Python Orange 3.41.0. Ketiganya selesai; joblib mengeluarkan peringatan lingkungan saat memeriksa jumlah core fisik, tetapi seluruh fit dan pencarian selesai.
- Generator menghasilkan 1.800 kolom RC (prevalensi label spalling 0,141) dan 1.400 balok. P09B menghasilkan 190 positif pada train dan 63 pada test; interpolasi hanya menyeimbangkan train. Pada run audit, logistic regression berbobot kelas memberi F1 0,433, sedangkan GridSearchCV memilih F1 validasi 0,463 dan F1 test 0,403. Timing berubah antar-run; angka emisi tetap proksi dari daya asumsi.
- P09C mereproduksi DGP balok: kandidat produk memberi MAE 7,14 kN·m in-domain dan 9,28 pada subset fy tinggi; model aditif 32,32 dan 130,07; Random Forest 15,29 dan 159,88. Hasil ini hanya validasi pada data sintesis yang DGP-nya diketahui.
- OWS memuat 1.800 baris dari `.tab`; kelas target adalah `spalling`, metadata adalah `column_id`, dan Distributions/Scatter Plot menerima data. OWS hanya untuk eksplorasi; pembandingan model dan augmentasi berlangsung di Python.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
