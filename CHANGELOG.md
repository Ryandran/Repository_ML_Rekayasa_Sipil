# Catatan Perubahan

## Naskah Tahap 9 (book/)

- Tahap 7: Gambar 3.10–3.11 (rendering netral gaya notebook dari kode di naskah, bukan tangkapan layar Colab asli) dan satu kalimat versi scikit-learn di Bab 12, 14, 15.
- Tahap 8: istilah baku Bab 5–6.
- Tahap 9: konsolidasi pesan kebocoran data yang berulang (Bab 3–6) menjadi satu penjelasan kanonik (subbab 3.4, 4.4, 6.4) dengan rujukan silang; 8 paragraf berubah.
- Istilah baku Bab 7–15 belum dikerjakan.

## 2026-11-18 — P15A: pencarian data Bab 14/15
- Audit asal-usul 36 CSV/`.tab`: semua berasal dari notebook penulisnya, kecuali `praktikum/bab15/slope_campaign_synthetic.csv` yang berupa salinan manual dari keluaran P14A (byte-identik).
- P15A kini mencari `slope_campaign_synthetic.csv` di `praktikum/bab15/`, `praktikum/bab14/`, lalu direktori kerja, dengan pesan galat berbahasa Indonesia. Logika dan keluaran notebook tidak berubah.

## 2026-11-18 — Penyelidikan CSV Bab 12/14/15
- Delapan CSV yang tidak identik ditelusuri: berkas data hanya berbeda pada digit terakhir (versi numpy); berkas metrik model berbeda karena scikit-learn 1.9 mengubah hasil Random Forest. Dengan scikit-learn 1.5.2–1.8.0 hasilnya sama dengan repositori dan naskah.
- `requirements.txt`: `scikit-learn>=1.4,<1.9`. Catatan di README akar dan `catatan-tindak-lanjut.md`. CSV dan notebook tidak diubah.

## 2026-11-18 — Lanjutan Bab 4: notebook ganda dihapus, direktori kerja Bab 4–7 diseragamkan
- `notebooks/bab04/P04_data_sintesis_algoritma.ipynb` dihapus (tidak dirujuk naskah; menimpa CSV jembatan).
- P04A, P05A, P06A menulis ke `praktikum/babNN/data_babN` bila dijalankan dari akar repositori, dan ke `data_babN` di direktori kerja bila folder `praktikum/babNN` tidak ada (Colab). P04B, P05B, P06B, P07 mencari kedua lokasi.
- Semua notebook Bab 4–7 dijalankan ulang dari akar repositori dan dari folder kosong (mode Colab) tanpa galat; keluaran tidak lagi memuat jalur lokal. CSV Bab 4 dan 5 identik; `pavement_priority.csv` (Bab 6) berbeda hingga 4,4e-16 pada beberapa nilai akibat versi numpy, label sama, sehingga berkas di repositori tidak diubah.
- README akar dan README Bab 4–6 disesuaikan.
- Naskah Tahap6 (`book/`): sitasi Bab 4 (13 sumber, Referensi diurutkan abjad), petunjuk jalur P04 disesuaikan, dan koreksi kode `from sklearn.preprocessing import StandardScaler` yang keliru terubah menjadi `sklearn.prapemrosesan` pada Tahap5 (akibat pembakuan istilah). Tahap6 menggantikan Tahap5.

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
