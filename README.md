# Machine Learning untuk Rekayasa Sipil — Materi Pendamping

Notebook, data sintetis, alur kerja Orange, dan ilustrasi pendamping buku ajar *Machine Learning untuk Rekayasa Sipil* (Program Magister Teknik Sipil).

> **Status: draf, belum dirilis.** Isi repositori masih bisa berubah mengikuti penyusunan buku. Naskah kerja saat ini (Tahap 16) 209 halaman; sasaran 250–300 halaman akan dicapai dengan Bab 17, Kata Pengantar, Lampiran, dan Glosarium. Verifikasi seluruh sumber dan klaim belum selesai.

## Isi

| Folder | Isi |
|---|---|
| `book/` | Satu berkas naskah versi terbaru (`Buku_Ajar_ML_Rekayasa_Sipil_Suntingan_Bahasa_TahapNN.docx`); versi sebelumnya tidak disimpan di folder ini (riwayat ada di git) |
| `notebooks/babNN/` | Notebook Python per bab. Notebook berawalan `PxxA` adalah pembangkit data sintetis; `PxxB` dan seterusnya adalah analisisnya |
| `praktikum/babNN/` | Alur kerja Orange (`.ows`), data latihan (`.csv`, `.tab`), dan `README.md` bab berisi urutan langkah serta catatan interpretasi |
| `gambar/babNN/` | Ilustrasi vektor (SVG) pendamping naskah |

### Peta bab

| Bab | Topik | `notebooks/` | `praktikum/` | `gambar/` |
|---|---|:-:|:-:|:-:|
| 1 | Machine learning dalam cara berpikir rekayasa | | | ✔ |
| 2 | Dari masalah rekayasa ke pertanyaan ML | | | ✔ |
| 3 | Data dan statistik | ✔ | ✔ | ✔ |
| 4 | Algoritma machine learning | ✔ | ✔ | ✔ |
| 5 | Indikator kinerja dan metrik kesalahan | ✔ | ✔ | ✔ |
| 6 | Coding-free dan coding-based | ✔ | ✔ | ✔ |
| 7 | Explainability dan interpretabilitas | ✔ | ✔ | ✔ |
| 8 | Discovery dan inferensi kausal | ✔ | ✔ | ✔ |
| 9 | Topik lanjutan machine learning | ✔ | ✔ | ✔ |
| 10 | Praktik audit penelitian ML | ✔ | ✔ | ✔ |
| 11 | Arah masa depan ML untuk rekayasa sipil | | | ✔ |
| 12 | Data spasial, temporal, dan multimodal | ✔ | ✔ | ✔ |
| 13 | Implementasi, pemantauan, dan tata kelola | ✔ | ✔ | ✔ |
| 14 | Studio riset I: pertanyaan, data, dan desain | ✔ | ✔ | ✔ |
| 15 | Studio riset II: validasi, pelaporan, dan klaim | ✔ | ✔ | ✔ |
| 16 | Pengantar deep learning | ✔ | ✔ | ✔ |
| 17 | Computer vision *(direncanakan; sesudah Bab 16)* | | | |

## Cara memakai

1. Buka `praktikum/babNN/README.md` untuk bab yang dipilih dan ikuti urutan langkahnya.
2. Jalankan notebook pembangkit (`PxxA`) lebih dulu bila ada. Notebook menghasilkan data latihan sintetis dengan *seed* dan asumsi yang dicatat.
3. Jalankan notebook analisis di Google Colab atau Python lokal.
4. Untuk Orange, buka berkas `.ows` di `praktikum/babNN/`. Setelah repositori dipindahkan atau alur dibuka di komputer lain, pilih ulang dataset pada widget **File**.

**Direktori kerja.** Semua bab: jalankan notebook dari akar repositori; data ditulis ke `praktikum/babNN/` (Bab 4–6: `praktikum/babNN/data_babN`). Di Colab atau folder lain, generator Bab 4–6 membuat `data_babN` di direktori kerja dan notebook analisisnya membacanya dari sana. Notebook Bab 7 mencari CSV Bab 6 di `praktikum/bab06/data_bab6/` dan di `data_bab6/`.

```bash
pip install -r requirements.txt
```

Orange Data Mining yang dipakai menyiapkan contoh adalah versi 3.41.0. Versi pustaka Python di Colab dapat berubah; periksa README bab bila hasil berbeda. Angka model Bab 12, 14, dan 15 dibuat dengan scikit-learn ≤ 1.8; scikit-learn 1.9 memberi hasil Random Forest yang sedikit berbeda (hingga sekitar 0,06 pada R² per pembagian), sehingga `requirements.txt` membatasi versi di bawah 1.9.

## Data dan batas penggunaan

Dataset latihan dibuat secara sintetis untuk menjelaskan alur analisis dan menguji kode. Data ini bukan hasil pengukuran lapangan, pengujian material, inspeksi aset, atau dasar keputusan keselamatan. Jalankan ulang pembangkit untuk mereproduksi keluaran; jangan menggeneralisasi skor simulasi ke infrastruktur nyata.

## Sitasi dan lisensi

Rujukan akademik dicantumkan pada naskah dan/atau README bab terkait. PDF sumber buku Wiley yang menjadi bahan telaah tidak disertakan.

| Bagian | Lisensi |
|---|---|
| Kode (notebook `.ipynb`, skrip `skrip/`) | MIT, lihat `LICENSE` |
| Data sintetis, alur kerja Orange, README bab, dan ilustrasi | CC BY 4.0, lihat `LICENSE-DATA.md` |
| Naskah buku (`book/`) | Hak cipta penulis, seluruh hak dilindungi (direncanakan terbit melalui penerbit) |

Perubahan dicatat di `CHANGELOG.md`.
