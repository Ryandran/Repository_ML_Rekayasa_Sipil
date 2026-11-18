# Paket Bab 6 — Pendekatan coding-free dan coding-based

> Letak berkas: notebook di [`notebooks/bab06/`](../../notebooks/bab06/), ilustrasi SVG di [`gambar/bab06/`](../../gambar/bab06/); workflow Orange dan data berada di folder ini.

## Berkas
- `P06A_generator_data_sintesis.ipynb` — generator data; terpisah dari latihan analisis.
- `P06B_praktik_orange_python.ipynb` — analisis Python atas keluaran generator dan panduan pembandingan Orange.
- `Orange_Bab6_Regresi.ows` — workflow perbandingan learner regresi.
- `SVG/` — dua ilustrasi pendamping: alur praktik dan perbedaan tiga tugas ML.

Notebook pada bab ini disimpan di folder paket ini.

## Langkah penggunaan
1. Jalankan `P06A_generator_data_sintesis.ipynb` di Google Colab atau Jupyter. Notebook membuat tiga CSV di folder `data_bab6` (dari akar repositori: `praktikum/bab06/data_bab6`; di Colab: direktori kerja). Di Colab, jalankan sel unduh opsional sebelum menutup runtime.
2. Jika notebook analisis dijalankan di runtime Colab yang berbeda, unggah tiga CSV saat diminta pada sel awal P06B. Di Jupyter lokal, jalankan dari akar repositori atau salin CSV generator ke folder `data_bab6` di direktori kerja.
3. Buka `Orange_Bab6_Regresi.ows`. Pada widget **File**, pilih `data_bab6/marshall_regression.csv` atau lokasi berkas hasil unduhan. Workflow menyimpan `stability_kN` sebagai target dan `mix_id` sebagai metadata; periksa keduanya pada **Select Columns**.
4. Tiga learner sudah terhubung ke **Test and Score** dengan validasi silang lima lipatan. Gunakan alur ini untuk contoh rancangan campuran independen.
5. Jalankan P06B untuk latihan regresi, klasifikasi, clustering, dan spot analysis. Untuk clustering, `synthetic_reference` hanya boleh dipakai sebagai rujukan evaluasi eksternal setelah kelompok dibentuk.
6. Untuk data nyata yang berulang per batch, lokasi, atau waktu, pisahkan kelompok sesuai unit generalisasi. Validasi silang acak per baris tidak otomatis menguji generalisasi ke kelompok baru.

Dataset sepenuhnya sintetis. Rumus generator sengaja dibuat transparan dan tidak mewakili hasil uji Marshall atau kondisi jalan sesungguhnya. Notebook dan workflow perlu disesuaikan dengan versi Python, pustaka, dan Orange yang tersedia; widget File perlu diarahkan ulang setelah folder dipindahkan.

## Status pemeriksaan

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
