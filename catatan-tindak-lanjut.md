# Catatan tindak lanjut

Daftar hal yang belum selesai. Perbarui atau hapus butir yang sudah dikerjakan.

## Bab 3 (diaudit 2026-11-18)

| Butir | Status | Keterangan |
|---|---|---|
| Ambil ulang tangkapan layar Gambar 3.10 dan 3.11 | Menunggu (Ryan) | Tampilan lama memakai folder unggahan `Bab3_Paket/Data`. Ambil setelah struktur repositori final: jalankan P03A lalu P03B di Colab, tangkap sel yang memuat `pd.read_csv("praktikum/bab03/data_sintesis_beton.csv")` beserta panel Files (folder `praktikum/bab03`). Setelah itu hapus kalimat catatan tangkapan layar lama di paragraf pengantar kode (subbab 3.5.1). |
| Padatkan pengulangan pesan kebocoran (muncul 5 kali), "pencilan bukan berarti kesalahan" (2 kali), dan pengelompokan citra saat membagi data (3 kali) | Disetujui, ditunda | Kerjakan setelah Bab 6 selesai agar rujukan silang sudah final. |
| Uji workflow `Orange_Bab3.ows` di Orange 3.41 | Belum diuji | Hanya struktur XML yang diperiksa (5 widget, 4 tautan). Berkas tidak menyimpan jalur data. |
| Terapkan istilah baku (pengamatan, rerata, simpangan baku, pelatihan/data uji, prapemrosesan, antarkelompok) ke Bab 1–2 dan Bab 4–15 | Belum | Bab 3 sudah diseragamkan. Tambahkan ke `gaya-selingkung.md`. |
| Verifikasi akhir sitasi Bab 3 (DOI dan halaman) | Selesai 2026-11-18 | Rubin (1976), Little & Rubin (2019), Tukey (1977), Kraskov dkk. (2004), Demšar dkk. (2013), Kaufman dkk. (2012) dicocokkan dengan laman penerbit atau repositori resmi. Judul pada Referensi belum dicetak miring (mengikuti entri yang sudah ada). |

## Seluruh buku

- Selisih CSV saat dibangkitkan ulang: selesai diselidiki, lihat bagian "Reproduksibilitas CSV Bab 12/14/15" di bawah.
- Keluaran notebook P04B, P06A, dan P07 masih memuat jalur lokal Windows.
- Keputusan LICENSE dan LICENSE-DATA, serta apakah `book/` tetap di repositori.

## Bab 4 (diaudit 2026-11-18)

| Butir | Status | Keterangan |
|---|---|---|
| Hapus atau arsipkan `notebooks/bab04/P04_data_sintesis_algoritma.ipynb` | Selesai: dihapus (keputusan Ryan, 2026-11-18) | Tidak dirujuk naskah; aturan skor jembatannya berbeda dari P04A dan menimpa CSV jembatan. |
| Sitasi algoritma Bab 4 (ridge, lasso, random forest, gradient boosting, SVM, k-NN, k-means, Ward, DBSCAN, Isolation Forest, LOF, PCA, scikit-learn) | Selesai 2026-11-18 (Tahap6) | 13 sumber dicocokkan dengan laman penerbit atau repositori resmi. DOI Hoerl & Kennard (1970) dan Tibshirani (1996) belum terverifikasi sehingga tidak dicantumkan; nomor terbitan Cortes & Vapnik (1995) tidak dicantumkan karena tidak tertera pada sumber yang diperiksa. CART (Breiman dkk., 1984) tidak dikutip. Naive Bayes, jaringan saraf, ANFIS, LSTM, GNN, transformer, dan fuzzy c-means belum bersitasi. |
| Uji `Orange_Bab4_Regresi.ows` di Orange 3.41 | Belum diuji | Struktur: 8 widget, 7 tautan; berkas tidak menyimpan jalur data. |
| Bab 4–6 dijalankan dari `praktikum/babNN/`, bab lain dari akar repositori | Selesai: semua bab dijalankan dari akar repositori; Colab tetap memakai `data_babN` di direktori kerja |

## Audit asal-usul CSV (2026-11-18)
- 36 CSV/`.tab` di `praktikum/` dibandingkan dengan hasil menjalankan ulang seluruh notebook penulisnya pada salinan bersih (scikit-learn 1.8.0). 18 identik byte; 14 hanya beda digit terakhir (≤ 1e-13, versi numpy); 4 berkas metrik model (P12 dua berkas, P14, P15 `repeated_group_splits`) berbeda karena dihitung dari data hasil bangkitan ulang, sementara dari CSV data di repositori hasilnya identik (≤ 1,8e-15).
- `.tab` Bab 9 dan 10 keluar dengan akhir baris CRLF dari notebook (modul `csv`); di repositori berakhir LF. Isi sama; tidak diubah.
- `praktikum/bab15/slope_campaign_synthetic.csv` tidak ditulis notebook mana pun; salinan manual dari Bab 14. Ditangani dengan pencarian jalur di P15A.

## Reproduksibilitas CSV Bab 12/14/15 (diselidiki 2026-11-18)
- **Berkas data** (`bridge_panel_synthetic.csv`, `slope_campaign_synthetic.csv`, dan `.tab` turunannya): isi sama; hanya digit terakhir yang berbeda (≤1,1e-13) menurut versi numpy. Tidak perlu diubah.
- **Berkas metrik model** (P12, P14, P15): angka di repositori dan di naskah dibuat dengan scikit-learn ≤ 1.8. Dengan scikit-learn 1.5.2 (numpy 1.26.4, pandas 2.2.3) dan 1.8.0, P15 identik; P12 dan P14 identik hingga 1e-15 bila memakai CSV data yang ada. Dengan 1.6.1 dan 1.7.2 selisihnya ≤ 1,1e-5.
- **scikit-learn 1.9.1 mengubah hasil Random Forest** pada notebook ini (dengan numpy 2.2.6 maupun 2.4.6): selisih hingga 0,035 pada MAE/RMSE dan 0,06 pada R² per pembagian (peringkat dan kesimpulan kualitatif tetap). Penyebab internal perubahan belum ditelusuri.
- Bab 4 (P04B) tidak terpengaruh: keluaran identik pada 1.8.0 dan 1.9.1.
- Tindakan: `requirements.txt` dibatasi `scikit-learn>=1.4,<1.9`; CSV dan notebook di repositori tidak diubah. Usulan untuk naskah (menunggu persetujuan): satu kalimat pada Bab 12, 14, dan 15 bahwa angka dapat berbeda pada digit kedua bila memakai scikit-learn ≥ 1.9.
