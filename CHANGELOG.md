# Catatan Perubahan

## 2026-11-18 — Audit Bab 4 (notebook P04B, README, naskah)
- P04B diperluas agar sesuai panduan Bab 4: baseline rerata, pipeline k-NN (dengan dan tanpa penskalaan), regresi linear/pohon/random forest/gradient boosting dengan MAE, RMSE, dan rerata residual, lima pembagian acak, regresi logistik dengan ambang peluang, perbandingan k-means dan clustering hierarkis, tumpang tindih flag anomali. Pencarian folder data otomatis; keluaran dijalankan ulang (jalur lokal Windows di keluaran lama hilang).
- Temuan: `P04_data_sintesis_algoritma.ipynb` bukan salinan P04A; aturan skor jembatannya berbeda (koefisien dan ambang) sehingga menimpa label `data_sintesis_prioritas_jembatan.csv` di 277 baris bila dijalankan. P04A mereproduksi keempat CSV di repositori secara identik. Berkas ganda belum dihapus; menunggu keputusan.
- `requirements.txt`: `scikit-learn>=1.4`.
- Naskah Tahap5 (`book/`): perbaikan teks Bab 4, hasil P04B dikutip, Latihan 3 dan 5 dihubungkan dengan notebook, istilah dibakukan.

## 2026-11-18 — Sinkronisasi Bab 3 (notebook, README, naskah)
- P03B ditulis ulang agar sesuai panduan Bab 3: grafik (histogram, scatter plot berwarna menurut umur, box plot menurut umur), pencarian berkas CSV otomatis (akar repositori, folder Colab lama, folder kerja), toleransi pembulatan rasio air-semen, mutual information (`random_state=30303`), dan latihan diagnosis pada salinan rusak (baris terdampak, ID ganda, penanda IQR, ilustrasi pemulihan nilai air). Keluaran dalam bahasa Indonesia. CSV sumber tidak diubah dan hasil P03A tetap identik.
- P03A: kode tidak berubah; ditambah penjelasan cara menjalankan.
- README Bab 3: folder `Data/` yang sudah tidak ada diganti `praktikum/bab03/`; berkas Orange `.tab` atau `.csv` dijelaskan.
- Naskah (Tahap2): jalur kode, langkah Orange, toleransi pembulatan, mutual information, dan catatan salinan rusak disesuaikan dengan notebook.
- Naskah Tahap4 (`book/`): audit Bab 3 — sitasi untuk MCAR/MAR/MNAR (Rubin, 1976; Little & Rubin, 2019), aturan IQR dan box plot (Tukey, 1977), mutual information (Kraskov dkk., 2004), kebocoran data (Kaufman dkk., 2012), dan Orange (Demšar dkk., 2013) beserta entri Referensi; Latihan 3 dan 6 disesuaikan dengan dataset; butir kebocoran ditambahkan ke Kesimpulan; istilah dibakukan; tanda backtick dibersihkan. Berkas Tahap1 tidak diubah.
- `catatan-tindak-lanjut.md` ditambahkan.

## 2026-11-18 — Penataan ulang folder mengikuti `ml-rekayasa-sipil`
- `BabN_Paket/` dipecah menurut jenis berkas: notebook ke `notebooks/babNN/`, workflow Orange dan data ke `praktikum/babNN/`, ilustrasi SVG ke `gambar/babNN/`, README bab ke `praktikum/babNN/` (bab tanpa notebook ke `gambar/babNN/`). Nomor bab ditulis dua digit. Riwayat berkas dipertahankan (`git mv`).
- Notebook Bab 3 dan 8–15: jalur keluaran `BabN_Paket/Data` diganti `praktikum/babNN`. Notebook P07: jalur CSV Bab 6 diganti `../../praktikum/bab06/data_bab6/`. Kode dan data tidak berubah.
- README bab: nama berkas Orange diperbaiki (`Orange_BabN_Paket_*.ows` → `Orange_BabN_*.ows`), jalur `BabN_Paket_Paket/Data/` diperbaiki, jalur relatif disesuaikan, dan ditambah catatan letak berkas.
- `requirements-optional.txt` digabung ke `requirements.txt` (shap dan lime, untuk Bab 7).
- `README.md` ditulis ulang mengikuti format `ml-rekayasa-sipil`; `.gitignore` ditambah aturan CSV dan log.
