# Paket Bab 4 — Algoritma Machine Learning

> Letak berkas: notebook di [`notebooks/bab04/`](../../notebooks/bab04/), ilustrasi SVG di [`gambar/bab04/`](../../gambar/bab04/); workflow Orange dan data berada di folder ini.

## Berkas
- `P04A_generator_data_sintesis.ipynb` — generator empat dataset sintesis ber-seed tetap.
- `P04B_analisis_algoritma.ipynb` — pemeriksaan skema, contoh regresi, clustering, PCA dan deteksi anomali. Jalankan setelah P04A.
- `Orange_Bab4_Regresi.ows` — workflow perbandingan model regresi di Orange 3.41.0.
- `../../gambar/bab04/Gambar_4_1_Peta_Keluarga_Algoritma.svg` — ilustrasi peta keluarga algoritma.

## Menjalankan latihan
1. Buka P04A di Google Colab atau Jupyter lalu jalankan seluruh sel. Notebook membuat folder `data_bab4` di folder kerja dengan empat CSV. Data ini dibuat oleh aturan simulasi; bukan hasil uji material, inspeksi, atau pengukuran sensor lapangan.
2. Jalankan P04B pada folder kerja yang sama. Notebook memperlihatkan kandidat klasifikasi jembatan, regresi beton, clustering, PCA, serta penyaringan anomali. Hasilnya merupakan demonstrasi alur dan tidak menyatakan algoritma terbaik.
3. Untuk Orange, buka OWS lalu di widget **File** pilih `data_bab4/data_sintesis_kuat_tekan.csv`. Pada **Select Columns**, periksa `kuat_tekan_MPa` sebagai target, `id_spesimen` sebagai metadata dan delapan kolom lain sebagai fitur. Evaluasi beberapa learner melalui **Test and Score**; pembahasan indikator ada pada Bab 5.
4. Dataset perkerasan memiliki `label_pembangkit` untuk pemeriksaan sesudah clustering. Keluarkan label dan ID saat membentuk kelompok; label boleh ditinjau setelahnya untuk memahami generator. Dataset sensor memuat flag generator, bukan diagnosis.

Generator memakai seed 41804 agar dapat dijalankan ulang. Jika notebook dijalankan pada direktori yang berbeda, pilih lokasi folder kerja yang konsisten agar P04B dan Orange menemukan CSV. Data sintesis tidak boleh digunakan untuk perencanaan campuran, keputusan inspeksi, penilaian keselamatan atau klaim kinerja lapangan.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
