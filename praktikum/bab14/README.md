# Paket Bab 14 — Studio Riset Terintegrasi I

> Letak berkas: notebook di [`notebooks/bab14/`](../../notebooks/bab14/), ilustrasi SVG di [`gambar/bab14/`](../../gambar/bab14/); workflow Orange dan data berada di folder ini.

Data sintetis pedagogis: seed 14014, 72 lereng virtual × 18 kampanye = 1.296 baris. Persamaan respons hanya menguji rancangan dan kode; bukan simulator geoteknik tervalidasi, data lapangan, faktor keamanan, prediksi longsor atau sistem evakuasi.

## Urutan penggunaan
1. Jalankan `P14A_generator_lereng_sintetis.ipynb` di Google Colab/Python.
2. Buka `Orange_Bab14_Desain_Riset.ows`; di File, pilih `praktikum/bab14/slope_campaign_orange.tab`. Eksplorasi dengan Data Table, Distributions, Scatter Plot.
3. Jalankan `P14B_protokol_baseline_sintetis.ipynb`. Random split dan group holdout menjawab sasaran generalisasi yang berbeda.
4. Gunakan DOCX dan SVG untuk menyusun protokol penelitian. Jangan mengutip angka simulasi sebagai temuan empiris.

Group holdout memisahkan lereng utuh. Skor hanya menunjukkan seberapa baik model memulihkan pola generator, yang memiliki variasi laten per lereng. Tidak ada ambang keselamatan ataupun rekomendasi operasional.
## Catatan hasil simulasi Bab 14

Dengan seed baku, random row split menghasilkan MAE 0,090 dan R² 0,976; group holdout (18 lereng baru) menghasilkan MAE 0,705 dan R² −0,832. Baseline rata-rata pada group holdout memiliki MAE 0,703. Ini menunjukkan keterbatasan generalisasi pada generator yang memiliki efek laten per lereng. Seluruh angka hanya hasil data sintetis dan bukan metrik kinerja lapangan.

## Audit ulang (16 November 2026)
- DOCX berisi 4.879 kata dan 13 tabel. Notebook P14A/P14B berhasil dijalankan ulang tanpa exception; data sintesis berisi 1.296 pengamatan dari 72 lereng dan 18 kampanye.
- Orange 3.41.0 memuat 1.296 baris, target `deformation_response_synth_mm`, serta metadata identitas lereng dan status data sintesis. Workflow 4 node/3 koneksi meneruskan data ke Distributions dan Scatter Plot.
- Hasil teregenerasi selaras dengan README: split acak MAE 0,090/R² 0,976; group holdout 18 lereng MAE 0,705/R² −0,832; baseline holdout MAE 0,703. Ini menunjukkan efek laten per lereng pada generator, bukan performa geoteknik.
- SVG/OWS lolos parsing XML. Render halaman DOCX belum diverifikasi.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
