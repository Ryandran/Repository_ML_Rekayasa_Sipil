# Paket Bab 15 — Audit validasi dan klaim

> Letak berkas: notebook di [`notebooks/bab15/`](../../notebooks/bab15/), ilustrasi SVG di [`gambar/bab15/`](../../gambar/bab15/); workflow Orange dan data berada di folder ini.

Jalankan P14A generator terlebih dahulu bila ingin membangun ulang data; paket ini juga membawa salinan CSV sintesis Bab 14 (`slope_campaign_synthetic.csv`, byte-identik dengan keluaran P14A) untuk reproduksi mandiri. P15A mencari berkas itu di `praktikum/bab15/`, lalu `praktikum/bab14/`, lalu direktori kerja. P15A memakai Python/sklearn untuk audit kelompok dan menghasilkan keluaran prediksi/residual untuk Orange.

## Urutan
1. Buka `Orange_Bab15_Audit_Hasil.ows`, pilih `praktikum/bab15/P15_holdout_orange.tab` di File. Gunakan Data Table, Distributions, Scatter Plot untuk memeriksa aktual, prediksi, dan residual.
2. Jalankan `P15A_audit_validasi_sensitivitas_klaim.ipynb` dari root proyek.
3. Tinjau `P15_repeated_group_splits.csv`, bootstrap kondisional, permutation importance, dan prediksi.

## Interpretasi wajib
Dataset bersifat sintesis: 72 lereng virtual × 18 kampanye. Dua belas split kelompok berulang saling tumpang tindih dan dipakai sebagai sensitivitas, bukan replikasi independen. Bootstrap mengulang kelompok pada satu holdout dan bersifat kondisional. Permutation importance adalah perilaku prediktif pada model/split tersebut, bukan sebab. Hasil tidak mewakili lereng nyata atau keselamatan geoteknik.
Hasil utama notebook P15A pada seed 15015: dari 12 group holdout yang saling tumpang tindih, MAE model rata-rata 0,740 (SD 0,085; rentang 0,579–0,863), baseline mean rata-rata 0,768. Pada satu holdout, bootstrap 18 kelompok menghasilkan persentil 2,5–97,5 untuk baseline MAE dikurangi model MAE sebesar −0,194 hingga 0,243 (mencakup nol). Permutation importance tutupan vegetasi sintesis menaikkan MAE 0,045 pada holdout tersebut; ini bukan efek kausal. Semua angka merupakan hasil DGP sintetis, bukan bukti geoteknik.

## Audit ulang (16 November 2026)
- DOCX berisi 3.501 kata dan 7 tabel. Notebook P15A dijalankan ulang tanpa exception dan meregenerasi keluaran holdout, split berulang, bootstrap kelompok kondisional, serta permutation importance.
- Orange 3.41.0 memuat 324 baris; target `actual_synth`, metadata `slope_id` dan `campaign_index`. Workflow 4 node/3 koneksi meneruskan data ke Distributions dan Scatter Plot untuk inspeksi prediksi/residual.
- Angka README cocok dengan eksekusi: MAE model pada 12 split kelompok tumpang tindih 0,740 (SD 0,085), baseline 0,768; interval bootstrap kondisional untuk baseline−model −0,194 sampai 0,243; permutation importance tutupan vegetasi +0,045 MAE. Tidak ada bukti efek kausal atau generalisasi geoteknik nyata.
- SVG/OWS lolos parsing XML. Bab ini menjadi penutup audit bukti yang koheren dengan rancangan Bab 14. Naskah relatif ringkas (3.501 kata, 7 tabel); tinjau kecukupan contoh pelaporan, ketidakpastian, pertahanan klaim dan latihan sebelum pagination final. Render DOCX belum diverifikasi.

## Catatan penggunaan di repository

Ikuti direktori kerja yang tercantum pada langkah penggunaan di atas. Setelah membuka workflow `.ows` di Orange, pilih kembali dataset pada widget **File** bila lokasi berkas berubah. Dataset latihan bersifat sintetis.
