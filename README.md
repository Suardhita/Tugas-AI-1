# 🧩 Water Jug Problem Solver (BFS)

> Program berbasis Python untuk menyelesaikan masalah klasik **Water Jug Problem** menggunakan algoritma pencarian cerdas **Breadth-First Search (BFS)**. Dirancang khusus untuk menentukan langkah paling optimal dalam mendapatkan tepat **4 Liter** air pada ember berkapasitas **5 Liter**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Algorithm-BFS-orange.svg?style=for-the-badge" alt="Algorithm">
  <img src="https://img.shields.io/badge/Status-Completed-success.svg?style=for-the-badge" alt="Status">
</p>

---

### 👥 Anggota Kelompok

| No. | Nama Lengkap | NIM |
| :-: | :--- | :--- |
| **1** | I Made Suardhita Kusuma | `2501010075` |
| **2** | Putri Rahmawati Ambarwangi | `2501010059` |
| **3** | Dewa Ngakan Made Rasta Baladika Ak | `2501010074` |

---

### ⚙️ Cara Kerja & Deskripsi Program
Program ini mengeksplorasi ruang status (*state space*) menggunakan antrean (*queue*) pada algoritma **BFS** guna menjamin bahwa solusi yang ditemukan adalah jalur terpendek (optimal) dengan total **6 langkah**.

---

### 🖥️ Hasil Output & Visualisasi Eksekusi

Berikut adalah tangkapan layar dari hasil eksekusi program dari tahap awal hingga tercapainya target:

#### 1️⃣ Inisialisasi & Proses Awal (Langkah ke-0 s.d. Langkah ke-3)
<p align="center">
  <img src="output-01" alt="Output Water Jug Bagian 1" width="450">
</p>

* **`Langkah ke-0 (0L, 0L)`** — Kedua ember (5L dan 3L) mulai dalam kondisi kosong.
* **`Langkah ke-1 (5L, 0L)`** — Ember 5 Liter diisi penuh hingga mencapai kapasitas maksimal 5L.
* **`Langkah ke-2 (2L, 3L)`** — Air dari ember 5L dituangkan ke ember 3L sampai penuh, menyisakan 2L di ember 5L.
* **`Langkah ke-3 (2L, 0L)`** — Air dalam ember 3L dikosongkan (*empty*), sedangkan ember 5L dibiarkan berisi 2L.

#### 2️⃣ Penyelesaian Menuju Target (Langkah ke-4 s.d. Langkah ke-6)
<p align="center">
  <img src="output-02" alt="Output Water Jug Bagian 2" width="450">
</p>

* **`Langkah ke-4 (0L, 2L)`** — Sisa 2L air dari ember 5L dipindahkan sepenuhnya ke ember 3L.
* **`Langkah ke-5 (5L, 2L)`** — Ember 5L kembali diisi penuh hingga mencapai 5L, sementara ember 3L tetap menampung 2L.
* **`Langkah ke-6 (4L, 3L)`** — Air dari ember 5L dituangkan ke ember 3L untuk mencukupi kekurangannya (1L). Hasil akhirnya, ember 5L berhasil menyisakan **tepat 4 Liter air**!

> ### 🎉 Status Eksekusi
> ```text
> ==================================================
>    SOLUSI SELESAI! BERHASIL DAPAT 4L!
> ==================================================
> ```
