# 🧩 Water Jug Problem Solver (BFS)

Program ini dibuat untuk menyelesaikan masalah klasik *Water Jug Problem* menggunakan algoritma pencarian **Breadth-First Search (BFS)** dalam bahasa pemrograman Python. Program dirancang untuk mencari langkah paling optimal dalam mendapatkan tepat 4 Liter air pada ember berkapasitas 5 Liter.

---

### 👥 Anggota Kelompok

| No. | Nama Lengkap | NIM |
| :--: | :--- | :--- |
| 1 | I Made Suardhita Kusuma | 2501010075 |
| 2 | Putri Rahmawati Ambarwangi | 2501010059 |
| 3 | Dewa Ngakan Made Rasta Baladika Ak | 2501010074 |

---

### 🖥️ Hasil Output & Penjelasan Program

Berikut adalah tampilan visualisasi hasil eksekusi program dari awal hingga target tercapai dalam total **6 langkah optimal**:

#### 1. Inisialisasi (Langkah ke-0 s.d. Langkah ke-3)
<img src="path/ke/gambar-output-1.png" alt="Output Water Jug Bagian 1" width="400">

* **Langkah ke-0 (0L, 0L):** Kedua ember (5L dan 3L) awalnya dalam kondisi kosong.
* **Langkah ke-1 (5L, 0L):** Ember 5 Liter diisi penuh (*fill*) hingga mencapai kapasitas maksimal 5L.
* **Langkah ke-2 (2L, 3L):** Sebagian air dari ember 5L dituangkan ke ember 3L hingga ember 3L penuh, menyisakan 2L di ember 5L.
* **Langkah ke-3 (2L, 0L):** Air di dalam ember 3L dikosongkan (*empty*), sedangkan ember 5L tetap berisi 2L.

#### 2. Penyelesaian Target (Langkah ke-4 s.d. Langkah ke-6)
<img src="path/ke/gambar-output-2.png" alt="Output Water Jug Bagian 2" width="400">

* **Langkah ke-4 (0L, 2L):** Sisa 2L air dari ember 5L dipindahkan seluruhnya ke ember 3L, membuat ember 5L menjadi kosong.
* **Langkah ke-5 (5L, 2L):** Ember 5L kembali diisi penuh hingga mencapai 5L, sementara ember 3L tetap berisi 2L.
* **Langkah ke-6 (4L, 3L):** Air dari ember 5L dituangkan ke ember 3L untuk mengisi kekurangannya (1L). Hasil akhirnya, ember 5L berhasil menyisakan **tepat 4 Liter air** sesuai target yang diinginkan!

> **Status:** `SOLUSI SELESAI! BERHASIL DAPAT 4L!`
