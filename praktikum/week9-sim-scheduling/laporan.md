
# Laporan Praktikum Minggu [X]
Topik: [Simulasi Algoritma Penjadwalan CPU  ]

---

## Identitas
- **Nama**  : [Bachtiar Dwi Indrianto]  
- **NIM**   : [250320581]  
- **Kelas** : [1DSRA]

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).


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
1. [Mengapa simulasi diperlukan untuk menguji algoritma scheduling?]  
   **Jawaban:**
   
Simulasi digunakan dalam pengujian algoritma *CPU scheduling* karena memberikan lingkungan yang aman, terkontrol, dan efisien. Berikut alasan utamanya:
A. Aman untuk Sistem
Pengujian algoritma scheduling secara langsung pada sistem operasi nyata berisiko mengganggu kinerja sistem. Dengan simulasi, pengujian dapat dilakukan tanpa memengaruhi sistem yang sedang berjalan.

B. Memudahkan Perbandingan Algoritma
Simulasi memungkinkan pengujian beberapa algoritma seperti **FCFS**, **SJF**, **Priority**, dan **Round Robin** menggunakan data proses yang sama, sehingga hasil perbandingan menjadi lebih objektif.

C. Kondisi Pengujian Dapat Dikontrol
Parameter seperti *arrival time*, *burst time*, *priority*, dan *time quantum* dapat diatur sesuai kebutuhan, sesuatu yang sulit dilakukan pada sistem nyata.

D. Analisis Kinerja Lebih Mudah
Melalui simulasi, metrik kinerja seperti:
- Waiting Time
- Turnaround Time
- Response Time  
dapat dihitung dan dianalisis dengan jelas.

E. Efisien dari Segi Waktu dan Biaya
Simulasi tidak memerlukan perangkat keras tambahan dan dapat dijalankan berulang kali dengan cepat.

F. Membantu Pemahaman Konsep
Visualisasi seperti **Gantt Chart** memudahkan pemahaman alur eksekusi proses dan cara kerja algoritma scheduling.

Kesimpulan
Simulasi merupakan metode yang efektif untuk menguji dan membandingkan algoritma scheduling secara aman, efisien, dan terkontrol sebelum diterapkan pada sistem operasi nyata.


2. [Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?]  
   **Jawaban:**
Perbedaan Hasil Simulasi dan Perhitungan Manual pada Dataset Besar

| Aspek                     | Simulasi                                      | Perhitungan Manual                          |
|---------------------------|-----------------------------------------------|---------------------------------------------|
| Akurasi                   | Tinggi dan konsisten karena otomatis          | Rentan kesalahan manusia                    |
| Efisiensi Waktu           | Sangat cepat meskipun dataset besar           | Sangat lambat dan tidak efisien             |
| Kompleksitas Algoritma    | Mampu menangani algoritma kompleks            | Sulit menangani proses yang berulang        |
| Konsistensi Hasil         | Konsisten untuk input yang sama               | Kurang konsisten                            |
| Penanganan Dataset Besar  | Efektif untuk ratusan hingga ribuan data      | Tidak praktis untuk dataset besar           |
| Visualisasi Hasil         | Mudah menghasilkan tabel dan Gantt Chart      | Visualisasi dibuat manual dan rawan salah   |
| Kelayakan Penggunaan      | Cocok untuk analisis dan implementasi nyata   | Cocok untuk pembelajaran dasar (dataset kecil) |

Kesimpulan
Untuk dataset besar, simulasi lebih unggul dibandingkan perhitungan manual karena lebih akurat, efisien, dan konsisten.

4. [ Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
