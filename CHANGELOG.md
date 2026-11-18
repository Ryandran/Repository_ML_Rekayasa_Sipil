# Catatan Perubahan

## Bab 17 Computer vision (naskah Tahap 17)

- Bab baru setelah Bab 16 (11 subbab, 8 gambar, tabel, Definisi, Blueprint, 9 latihan, 12 referensi; naskah menjadi 220 halaman). Naskah dibagikan lewat Releases GitHub (bukan di repositori).
- Notebook P17A (detektor jendela geser, IoU, NMS, AP pada adegan sintesis), P17B (transfer learning: CNN kecil, ResNet-18 fitur beku/setel halus/dari nol pada 60/240/1.000 citra; uji ketahanan kontras, derau, blur), P17C (aturan kepatuhan APD di atas keluaran detektor simulasi) beserta `praktikum/bab17/README.md`. Gambar konseptual oleh `skrip/gambar_konseptual_bab17.py`.
- Hasil utama (semua sintesis): AP@IoU 0,5 = 0,271 pada P17A (0,314 ± 0,059 lintas 5 benih); fitur beku + regresi logistik 0,860 vs CNN kecil 0,540 pada 60 citra; augmentasi menaikkan akurasi pada kondisi terdegradasi namun menurunkannya pada citra bersih; ambang menurut rasio biaya 5:1 = 0,42.
- Catatan: P17B tidak sepenuhnya deterministik pada CPU (konvolusi multi-thread); angka dapat bergeser beberapa poin antarpelarian.
- `requirements.txt`: torchvision ditambahkan pada catatan opsional PyTorch.

## Folder book/ dikeluarkan dari repositori

- Atas keputusan penulis, `book/` dihapus; naskah versi akhir (DOCX dan PDF, Tahap 16; kini Tahap 17) dibagikan lewat Releases GitHub. Riwayat naskah lama tetap tersimpan di riwayat git.

## Bab 16 Pengantar deep learning (naskah Tahap 16)

- Bab baru setelah Bab 15 (11 subbab, 6 gambar, 3 tabel, Definisi, Blueprint, 9 latihan, 7 referensi; naskah menjadi 209 halaman). `book/` kini memuat Tahap 16 menggantikan Tahap 15.
- Notebook P16A (pembangkit 2.400 citra retak sintesis) dan P16B (MLP pada beton sintesis; CNN pada citra, pembagian per panel, variasi antarbenih) beserta `praktikum/bab16/`. Gambar konseptual dibuat oleh `skrip/gambar_konseptual_bab16.py`.
- Hasil utama (seed 16016): MLP R² 0,894 vs regresi linear 0,900 vs Random Forest 0,820; CNN akurasi 0,900 vs MLP piksel 0,673 pada jumlah parameter sebanding.
- Penomoran daftar Blueprint dan latihan Bab 16 dimulai dari 1 (penomoran bab lain masih berlanjut; dicatat sebagai tindak lanjut).
- `requirements.txt`: catatan opsional PyTorch CPU.

## Repositori: lisensi dan folder book/

- Ditambahkan `LICENSE` (MIT, untuk kode) dan `LICENSE-DATA.md` (CC BY 4.0, untuk data sintetis, alur kerja Orange, README bab, dan ilustrasi). Naskah buku tidak tercakup; hak cipta penulis.
- `book/` kini hanya berisi satu naskah versi terbaru (Tahap 16, setelah PR #15); Tahap 4, 5, 6, 9, 12, 13, 14 dihapus dari folder (riwayat tetap di git).
- README: peta bab memuat Bab 16 (pengantar deep learning) dan Bab 17 (computer vision) sebagai rencana; status halaman dan bagian lisensi diperbarui.
- `catatan-tindak-lanjut.md`: keputusan lingkup dicatat.

## Notebook: keluaran tersimpan P08B, P09B, P09C

- Ketiga notebook dijalankan dengan scikit-learn 1.8.0 dan keluarannya disimpan (sebelumnya kosong). Kode dan metadata kernel tidak diubah; CSV di `praktikum/` dikembalikan ke versi repositori.
- Angka sama dengan teks naskah Bab 8 dan 9 (mis. P08B: selisih mentah 0,453 dan estimasi −0,828; P09B: recall 0,698 dan F1 0,433; P09C: MAE 7,14 dan 9,28).

## Naskah Tahap 15 (book/)

- 23 gambar lama yang belum dirujuk di teks (Gambar 1.1–1.3, 2.1–2.2, 3.1–3.9, 5.1–5.2, 7.1, 10.2, 11.1, 12.1, 13.1, 14.1, 15.1 menurut nomor Tahap 14) kini masing-masing memiliki satu kalimat rujukan sebelum gambar. Gambar 3.11 sudah dirujuk bersama Gambar 3.10 sehingga tidak ditambah.
- Gambar 10.2 dipindah dari bawah judul "Pertanyaan dan latihan" ke akhir Bab 10 sebelum judul itu agar tidak tersisip di antara soal.
- Dua belas gambar keluaran notebook baru: P03B (histogram, scatter, box plot), P04B (clustering/PCA; Isolation Forest), P05 (kurva beban–lendutan), P08B (estimasi efek), P09B (klasifikasi spalling), P09C (regresi simbolik), P12B (tiga split; pemeriksaan visual), P13B (monitor bulanan), P14B (random vs grup), P15A (sensitivitas). Setiap gambar memiliki kalimat rujukan. Bab 1, 2, 11 tidak memiliki notebook.
- Gambar P07 (PDP/ICE dan kasus lokal) dirender ulang dengan judul "Partial dependence: rerata model".
- Angka pada gambar sama dengan angka di teks naskah. P08B, P09B, P09C dijalankan di salinan sementara (notebook di repositori tidak diubah).
- Nomor gambar per bab diurutkan ulang; Daftar Gambar disusun ulang (64 gambar).

## Notebook: penyegaran keluaran (PR terpisah)

- Keluaran tersimpan dijalankan ulang dengan scikit-learn 1.8.0 untuk P03B, P04B, P05, P06B, P07, P10B, P12B, P13B, P14B, P15A; metadata kernel tidak diubah. Notebook generator (P06A dst.) tidak dijalankan ulang agar data tidak bergeser.
- P07: judul grafik PDP diubah menjadi "Partial dependence: rerata model"; istilah baku (pengamatan, nonlinear) disesuaikan; P03B memakai "rerata". Sel SHAP/LIME opsional (pustaka tidak terpasang) dipertahankan dengan keluaran lama.
- P12B dan P13B kini menyimpan gambar keluaran.
- CSV di `praktikum/` yang ditulis ulang oleh notebook dikembalikan ke versi repositori.

## Naskah Tahap 14 (book/)

- Dua belas gambar keluaran notebook (dirender netral dari sel yang dijalankan ulang dengan scikit-learn 1.8): Gambar 4.3; 5.4–5.5; 6.4–6.6; 7.2–7.5 (permutation importance, PDP/ICE, kasus lokal, pohon surrogate); 10.1 (P10B); 12.3 (P12B). Berkas di `gambar/babNN/`; perender di `skrip/render_keluaran_notebook.py`.
- Gambar augmentasi (dulu 9.2, di akhir bab sesudah Latihan) dipindah ke subbab 9.1.2 dan menjadi Gambar 9.1; Gambar Orange menjadi 9.2. Kalimat rujukan ditambahkan.
- Nomor gambar per bab diurutkan ulang menurut kemunculan; Daftar Gambar disusun ulang.
- Catatan: keluaran yang tersimpan di notebook P05 (sel 4) dan P07 (sel 11) sedikit berbeda dari hasil jalan ulang (mis. P07 fidelity R² 0,617 tersimpan vs 0,616 segar, sama dengan naskah). Gambar memakai hasil jalan ulang. Notebook di repositori disegarkan pada PR #10.
- Catatan: 24 gambar lama belum punya kalimat rujukan di teks; dilengkapi pada Tahap 15.

## Naskah Tahap 13 (book/)

- Sepuluh tangkapan layar Orange 3.41.0 disisipkan dengan data sintesis dari repositori: Gambar 4.2, 5.3, 6.3 (alur kerja + Test and Score), 7.2 (alur kerja + Rank), serta 8.2, 9.1, 12.2, 13.2, 14.2, 15.2 (Distributions + Scatter Plot). Berkas gambar ada di `gambar/babNN/`; skrip pengambilnya `skrip/tangkap_orange.py`.
- Bab 10 dan 11 tidak memuat langkah Orange di teks, sehingga tidak diberi gambar.
- Gambar 9.1 lama menjadi Gambar 9.2 (urutan gambar dalam Bab 9).
- Daftar Gambar dilengkapi (Gambar 3.4–3.11 dan gambar baru) dan tiga entri yang rusak (10.1, 11.1, 15.1) diperbaiki.
- Penanda (bookmark) ganda pada Gambar 3.4–3.11 dibuat unik.
- Setiap kalimat rujukan memberi tahu bahwa angka Orange tidak untuk dibandingkan langsung dengan notebook Python.

## Naskah Tahap 9 (book/)

- Tahap 7: Gambar 3.10–3.11 (rendering netral gaya notebook dari kode di naskah, bukan tangkapan layar Colab asli) dan satu kalimat versi scikit-learn di Bab 12, 14, 15.
- Tahap 8: istilah baku Bab 5–6.
- Tahap 9: konsolidasi pesan kebocoran data yang berulang (Bab 3–6) menjadi satu penjelasan kanonik (subbab 3.4, 4.4, 6.4) dengan rujukan silang; 8 paragraf berubah.
- Istilah baku Bab 7–15 belum dikerjakan (lihat Tahap 12).

## Naskah Tahap 12 (book/)

- Tahap 10–12: istilah baku (pengamatan, rerata, prapemrosesan, nonlinear, data latih/uji) diterapkan pada Bab 7–15; 87 paragraf berubah, kode dan daftar pustaka tidak disentuh.
- Gambar 3.10–3.11 memakai rendering netral bergaya notebook; bab lain hanya memuat gambar konseptual, sehingga aturan ini belum berlaku di tempat lain.

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
