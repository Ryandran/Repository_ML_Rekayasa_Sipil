# Catatan Perubahan

## 2026-11-18 — Sinkronisasi Bab 3 (notebook, README, naskah)
- P03B ditulis ulang agar sesuai panduan Bab 3: grafik (histogram, scatter plot berwarna menurut umur, box plot menurut umur), pencarian berkas CSV otomatis (akar repositori, folder Colab lama, folder kerja), toleransi pembulatan rasio air-semen, mutual information (`random_state=30303`), dan latihan diagnosis pada salinan rusak (baris terdampak, ID ganda, penanda IQR, ilustrasi pemulihan nilai air). Keluaran dalam bahasa Indonesia. CSV sumber tidak diubah dan hasil P03A tetap identik.
- P03A: kode tidak berubah; ditambah penjelasan cara menjalankan.
- README Bab 3: folder `Data/` yang sudah tidak ada diganti `praktikum/bab03/`; berkas Orange `.tab` atau `.csv` dijelaskan.
- Naskah (Tahap2): jalur kode, langkah Orange, toleransi pembulatan, mutual information, dan catatan salinan rusak disesuaikan dengan notebook.

## 2026-11-18 — Penataan ulang folder mengikuti `ml-rekayasa-sipil`
- `BabN_Paket/` dipecah menurut jenis berkas: notebook ke `notebooks/babNN/`, workflow Orange dan data ke `praktikum/babNN/`, ilustrasi SVG ke `gambar/babNN/`, README bab ke `praktikum/babNN/` (bab tanpa notebook ke `gambar/babNN/`). Nomor bab ditulis dua digit. Riwayat berkas dipertahankan (`git mv`).
- Notebook Bab 3 dan 8–15: jalur keluaran `BabN_Paket/Data` diganti `praktikum/babNN`. Notebook P07: jalur CSV Bab 6 diganti `../../praktikum/bab06/data_bab6/`. Kode dan data tidak berubah.
- README bab: nama berkas Orange diperbaiki (`Orange_BabN_Paket_*.ows` → `Orange_BabN_*.ows`), jalur `BabN_Paket_Paket/Data/` diperbaiki, jalur relatif disesuaikan, dan ditambah catatan letak berkas.
- `requirements-optional.txt` digabung ke `requirements.txt` (shap dan lime, untuk Bab 7).
- `README.md` ditulis ulang mengikuti format `ml-rekayasa-sipil`; `.gitignore` ditambah aturan CSV dan log.
