# Machine Learning untuk Rekayasa Sipil

Repository pendamping bahan ajar Program Magister Teknik Sipil. Isinya mencakup naskah induk, notebook Python, dataset sintetis, workflow Orange, dan ilustrasi vektor per bab.

> **Status naskah:** PDF kerja saat ini 174 halaman. Sasaran 250–300 halaman belum tercapai; naskah masih perlu pengayaan materi secara substantif. Metadata bibliografi inti sudah diperiksa, tetapi verifikasi seluruh sumber dan klaim belum selesai.

## Isi repository

- [`book/`](book/) — naskah induk terbaru dalam DOCX dan PDF.
- [`Bab1_Paket/`–`Bab15_Paket/`](#paket-per-bab) — paket bab yang berisi notebook, data, workflow Orange, README, dan/atau ilustrasi.
- [`requirements.txt`](requirements.txt) — pustaka Python untuk notebook.
- [`requirements-optional.txt`](requirements-optional.txt) — pustaka tambahan untuk latihan explainability Bab 7.

## Paket per bab

| Bab | Topik | Materi pendamping |
|---|---|---|
| 1 | Machine learning dalam cara berpikir rekayasa | Ilustrasi SVG |
| 2 | Dari masalah rekayasa ke pertanyaan ML | Ilustrasi SVG |
| 3 | Data dan statistik | Generator data, audit eksplorasi, Orange |
| 4 | Algoritma machine learning | Generator, analisis Python, Orange |
| 5 | Indikator kinerja dan metrik kesalahan | Generator, evaluasi Python, Orange |
| 6 | Coding-free dan coding-based | Generator, praktikum Orange dan Python |
| 7 | Explainability dan interpretabilitas | Notebook, Orange |
| 8 | Discovery dan inferensi kausal | Generator, analisis Python, Orange |
| 9 | Topik lanjutan machine learning | Generator, augmentasi/ensemble, symbolic regression |
| 10 | Praktik audit penelitian ML | Generator, audit data dan validasi, Orange |
| 11 | Arah masa depan ML untuk rekayasa sipil | Ilustrasi SVG |
| 12 | Data spasial, temporal, dan multimodal | Generator panel, analisis dan validasi, Orange |
| 13 | Implementasi, pemantauan, dan tata kelola | Generator stream, monitoring, Orange |
| 14 | Studio riset I: pertanyaan, data, dan desain | Generator lereng, protokol dan baseline, Orange |
| 15 | Studio riset II: validasi, pelaporan, dan klaim | Audit validasi dan sensitivitas, Orange |

## Memulai

1. Buka README pada folder bab yang dipilih dan ikuti urutan notebook di sana.
2. Jalankan notebook generator lebih dahulu bila tersedia. Notebook menghasilkan data latihan sintetis dengan seed dan asumsi yang dicatat.
3. Jalankan notebook analisis menggunakan Google Colab atau lingkungan Python lokal.
4. Untuk Orange, buka file `.ows` di folder bab. Setelah repository dipindahkan atau workflow dibuka di komputer lain, pilih ulang dataset pada widget **File**.

Notebook disimpan di folder paket masing-masing bab. Jalankan dari direktori kerja yang disebutkan pada README bab karena sebagian notebook mengharapkan root repository, sedangkan yang lain membuat keluaran di folder kerja. Orange Data Mining yang dipakai saat menyiapkan contoh adalah versi 3.41.0. Versi pustaka Python yang tersedia di Colab dapat berubah; periksa README bab bila hasil berbeda.

## Data dan batas penggunaan

Dataset latihan dibuat secara sintetis untuk menjelaskan alur analisis dan menguji kode. Data tersebut bukan hasil pengukuran lapangan, pengujian material, inspeksi aset, atau dasar keputusan keselamatan. Jalankan ulang generator untuk mereproduksi keluaran; jangan menggeneralisasi skor simulasi ke infrastruktur nyata.

## Sitasi dan lisensi

Rujukan akademik dicantumkan pada naskah induk dan/atau README terkait. PDF sumber buku Wiley yang menjadi bahan telaah tidak disertakan dalam repository.

Lisensi repository belum ditetapkan. Sebelum repository dipublikasikan, tentukan izin penggunaan untuk naskah, notebook, ilustrasi, dan dataset. Tanpa berkas lisensi, pengguna tidak seharusnya menganggap ada izin untuk menggunakan ulang atau mendistribusikan materi.
