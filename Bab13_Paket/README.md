# Paket Bab 13 — Implementasi, Pemantauan, dan Tata Kelola Model

Dataset di paket ini sepenuhnya sintetis. Skor risiko, aset, kejadian inspeksi, dan perubahan sensor dibuat untuk menguji alur monitor; bukan data kondisi aset atau rekomendasi operasional.

## Urutan penggunaan

1. Jalankan `P13A_generator_stream_sintetis.ipynb` dari root repository. Seed baku `13013`; notebook menghasilkan 576 baris untuk 24 aset × 24 bulan di `Bab13_Paket_Paket/Data/`.
2. Buka `Orange/Orange_Bab13_Paket_Monitoring.ows` di Orange 3.41.0. Pada File, pilih `Data/bridge_monitor_orange.tab`. Gunakan Data Table, Distributions, Scatter Plot, dan Line Plot untuk melihat struktur waktu serta perubahan sebaran.
3. Jalankan `P13B_monitor_drift_kinerja_sintetis.ipynb` dari root repository. Ia membandingkan distribusi skor terhadap baseline, memakai window enam bulan, dan menghitung kinerja hanya untuk label yang sudah matang setelah jeda dua bulan.
4. Baca DOCX dan ilustrasi SVG untuk penjelasan penggunaan terbatas, pemantauan, triase, fallback, rollback, serta latihan.

## Ambang latihan

PSI > 0,20, Brier di atas baseline + 0,04, minimal 72 label matang dalam window enam bulan, dan skor 0,10 adalah aturan demonstrasi, bukan threshold universal atau rekomendasi keselamatan. PSI memberi sinyal perubahan distribusi; ia tidak membuktikan penurunan kinerja. Metrik berlabel hanya mencakup outcome yang telah tersedia. Hasil harus dibaca bersama jumlah, periode, komposisi aset, coverage label, serta pola override.

## Berkas utama

- `P13A_generator_stream_sintetis.ipynb` — generator data latihan.
- `P13B_monitor_drift_kinerja_sintetis.ipynb` — monitor bulanan dan visualisasi.
- `Data/bridge_monitor_stream_synthetic.csv` dan `Data/bridge_monitor_orange.tab` — tabel sintesis.
- `Data/P13_monthly_monitor_synthetic.csv` — keluaran monitor.
- `Orange/Orange_Bab13_Paket_Monitoring.ows` — workflow eksplorasi Orange.
- `SVG/Gambar_13_1_Siklus_operasi_monitoring.svg` — ilustrasi siklus operasional.

Notebook membuat simulasi monitoring, bukan sistem alert atau retraining otomatis. Penerapan nyata memerlukan persetujuan pemilik aset, validasi lapangan, prosedur keselamatan dan tata kelola yang sesuai.


## Audit ulang (16 November 2026)
- DOCX berisi 3.830 kata dan 11 tabel. Notebook P13A/P13B berhasil dijalankan ulang tanpa exception; generator menghasilkan 576 observasi (24 aset × 24 bulan), 80 baris perubahan sensor, 144 perubahan kejadian, dan jeda label dua bulan.
- Orange 3.41.0 memuat 576 baris; target `observed_event_synth`, metadata `bridge_id` dan `month`. Workflow 5 node/4 koneksi meneruskan data ke Distributions, Scatter Plot, dan Line Plot.
- Notebook menguji perubahan distribusi dan kinerja berlabel matang dengan ambang latihan eksplisit; sinyal perubahan tidak otomatis dianggap penurunan kinerja atau memicu retraining. Data dan threshold adalah sintesis/pedagogis, bukan alarm operasional.
- SVG/OWS lolos parsing XML. Render halaman DOCX belum diverifikasi. Naskah relatif lebih ringkas daripada Bab 11, 12, dan 14; sebelum pagination akhir, cek kecukupan pembahasan kasus, prosedur tanggap, dan materi latihan agar target halaman buku tercapai tanpa pengulangan.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
