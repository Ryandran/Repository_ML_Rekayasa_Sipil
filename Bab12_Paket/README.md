# Bab 12 — paket data spasial-temporal multimodal

Semua tabel latihan pada paket ini adalah **data sintetis**, dibuat untuk mengajarkan struktur panel, penyelarasan sumber, missingness, dan validasi. Koordinat tidak mewakili lokasi nyata dan skor kondisi bukan hasil inspeksi aset nyata.

## Urutan penggunaan

1. Jalankan `P12A_generator_panel_sintetis.ipynb` dari root repository. Seed baku `12012`; notebook menulis CSV dan `.tab` ke `Bab12_Paket_Paket/Data/`.
2. Buka `Orange/Orange_Bab12_Paket_Data_Multimodal.ows` dengan Orange 3.41.0. Pada widget File, pilih `Data/bridge_panel_orange.tab`; lanjutkan ke Data Table, Distributions, dan Scatter Plot untuk inspeksi.
3. Jalankan `P12B_sinkronisasi_validasi_ruang_waktu.ipynb` dari root repository untuk audit, visualisasi, evaluasi split, dan ablation. Split yang digunakan: acak per baris, aset jembatan ditahan, serta bulan masa depan ditahan.
4. Buka DOCX dan ilustrasi SVG di folder masing-masing sebagai bahan ajar.

## Isi paket

- `P12A_generator_panel_sintetis.ipynb` — pembangkit data panel 18 jembatan × 36 bulan.
- `P12B_sinkronisasi_validasi_ruang_waktu.ipynb` — analisis Python.
- `Data/bridge_panel_synthetic.csv` — data portabel.
- `Data/bridge_panel_orange.tab` — data dengan definisi peran dan tipe kolom Orange.
- `Data/P12_split_metrics_synthetic.csv` — metrik tiga rancangan split.
- `Data/P12_modality_ablation_synthetic.csv` — perbandingan empat kelompok fitur pada split sama.
- `Orange/Orange_Bab12_Paket_Data_Multimodal.ows` — workflow eksplorasi Orange.
- `SVG/Gambar_12_1_Data_spasial_temporal_multimodal.svg` — ilustrasi vektor.

## Batas interpretasi

Random row split membagi pengamatan yang saling berulang dari aset yang sama sehingga cenderung memberi estimasi optimistis untuk generalisasi ke aset baru. Group holdout menguji aset yang tidak muncul pada latih; future-month split menguji masa berikutnya pada aset yang sudah dikenal. Hasil bergantung pada data sintesis dan split yang dipilih. Jangan gunakan angka untuk menyimpulkan kinerja teknik lapangan atau untuk keputusan keselamatan.

Untuk eksperimen multi-seed, ubah seed generator dan simpan hasil setiap replikasi; jangan memilih seed berdasarkan skor terbaik. Notebook menggunakan scikit-learn, pandas, NumPy dan matplotlib; Orange hanya digunakan pada eksplorasi visual.

## Audit ulang (16 November 2026)
- DOCX berisi 5.971 kata dan 12 tabel. Kedua notebook P12A/P12B dijalankan ulang sampai selesai tanpa exception; data menghasilkan 648 baris (18 jembatan sintetis × 36 bulan), dengan 54 baris sensor dan 73 baris modalitas visual yang hilang.
- Orange 3.41.0 memuat 648 baris; target `condition_next_3m_synth`, metadata `bridge_id` dan `observation_month`. Workflow 4 node/3 koneksi meneruskan data ke Distributions dan Scatter Plot.
- Hasil split yang diregenerasi: row-random MAE 4,149/R² 0,696; bridge holdout MAE 5,189/R² 0,275; future-month MAE 3,265/R² 0,787. Perbedaan ini menguatkan bahwa split menjawab klaim generalisasi yang berlainan. Hasil tetap demonstrasi data sintetis.
- SVG/OWS lolos parsing XML; naskah, dataset dan keluaran generator konsisten. Render halaman DOCX belum diverifikasi.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
