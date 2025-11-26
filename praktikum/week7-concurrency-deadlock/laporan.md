
# Laporan Praktikum Minggu [X]
Topik: [Sinkronisasi Proses dan Masalah Deadlock]

---

## Identitas
- **Nama**  : [Bachtiar Dwi Indrianto]  
- **NIM**   : [250320581]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengidentifikasi empat kondisi penyebab deadlock (*mutual exclusion, hold and wait, no preemption, circular wait*).  
2. Menjelaskan mekanisme sinkronisasi menggunakan *semaphore* atau *monitor*.  
3. Menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Menyajikan hasil studi kasus secara sistematis.
   
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Sebutkan empat kondisi utama penyebab deadlock.]  
   **Jawaban:** 
   Mutual Exclusion (Saling Mengunci)
   Resource hanya bisa digunakan oleh satu proses pada satu waktu.

   Hold and Wait (Menahan dan Menunggu)
   Proses sudah memegang satu resource, lalu menunggu resource lain yang sedang dipakai proses lain.

   No Preemption (Tidak Dapat Diambil Paksa)
   Resource yang sedang digunakan proses tidak bisa diambil secara paksa oleh sistem; harus dilepas secara sukarela.

   Circular Wait (Menunggu Secara Melingkar)
   Terjadi rantai proses yang saling menunggu resource satu sama lain dalam bentuk lingkaran.

Jika keempat kondisi ini terjadi secara bersamaan, maka deadlock dapat muncul.

2. [Mengapa sinkronisasi diperlukan dalam sistem operasi?]  
   **Jawaban:**  

Mencegah Race Condition
Ketika dua atau lebih proses/threads mengakses dan mengubah data yang sama secara bersamaan, hasil akhirnya bisa menjadi tidak benar atau tidak dapat diprediksi. Sinkronisasi memastikan hanya satu proses yang mengubah data pada satu waktu.

Menjaga Konsistensi Data
Tanpa sinkronisasi, data bersama (shared data) bisa rusak karena akses yang tak teratur. Mekanisme seperti mutex, semaphore, atau monitor memastikan data tetap konsisten.

Mengatur Akses ke Resource Bersama
Banyak resource bersifat terbatas (file, printer, memory buffer). Sinkronisasi mengatur giliran sehingga semua proses dapat memakai resource dengan aman dan teratur.

Menghindari Deadlock dan Livelock
Dengan sinkronisasi yang tepat (misalnya aturan penguncian), sistem dapat mencegah situasi di mana proses saling menunggu tanpa akhir.

Mendukung Kerja Paralel yang Efisien
Pada sistem multiprosesor/multicore, sinkronisasi membantu proses berjalan bersamaan tanpa saling mengganggu dan memastikan performa tetap optimal.

Singkatnya: Sinkronisasi diperlukan untuk **keamanan data, keteraturan akses resource, dan stabilitas sistem** dalam menjalankan banyak proses secara bersamaan.

3. [Jelaskan perbedaan antara semaphore dan monitor.]  
   **Jawaban:**
   
| Aspek | Semaphore | Monitor |
|-------|-----------|---------|
| Level | Low-level | High-level |
| Mekanisme | Counter + operasi P/V | Lock otomatis + function |
| Kemudahan | Rawan error | Lebih aman |
| Penggunaan | Sinkronisasi sederhana | Program kompleks berbasis OOP |

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
