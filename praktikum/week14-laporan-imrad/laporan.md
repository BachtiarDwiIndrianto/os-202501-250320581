
# Laporan Praktikum Minggu [14]
Topik: Penyusunan Laporan Praktikum Format IMRAD
---

## Identitas
- **Nama**  : Bachtiar Dwi Indrianto  
- **NIM**   : 250320581
- **Kelas** : 1DSRA

---

## JUDUL
Analisis Algoritma Penjadwalan CPU (FCFS dan SJF)

---
# 1.Pendahuluan

## 1.1.Latar Belakang
Penjadwalan CPU merupakan salah satu fungsi fundamental dalam sistem operasi yang menentukan urutan eksekusi proses pada CPU. Efisiensi penjadwalan CPU berpengaruh langsung terhadap kinerja sistem, termasuk *waiting time* (waktu tunggu) dan *turnaround time* (waktu penyelesaian total) proses. Dua algoritma penjadwalan dasar yang sering digunakan adalah **First Come First Served (FCFS)** dan **Shortest Job First (SJF)**.

FCFS merupakan algoritma paling sederhana yang menjalankan proses berdasarkan urutan kedatangan (*arrival time*). Meskipun mudah diimplementasikan, algoritma ini dapat menyebabkan *convoy effect* di mana proses pendek harus menunggu proses panjang selesai. Sebaliknya, SJF memilih proses dengan *burst time* terpendek untuk dieksekusi terlebih dahulu, yang secara teoritis menghasilkan *average waiting time* minimum.

## 1.2.Rumusan Masalah
1. Bagaimana kinerja algoritma FCFS dan SJF dalam hal *waiting time* dan *turnaround time*?
2. Apakah hasil simulasi program sesuai dengan perhitungan manual?
3. Apa kelebihan dan keterbatasan masing-masing algoritma dalam konteks praktis?


## 1.3.Tujuan Penulisan

---
# 2.Metode
## 2.1.Lingkungan Uji
- **Perangkat Keras**
  - Device name	LENOVO LOQ 15IRX9
  - Processor	13th Gen Intel(R) Core(TM) i7-13650HX (2.60 GHz)
  - Installed RAM	16,0 GB
  - System type	64-bit operating system, x64-based processor

- **Perangkat Lunak**
  - Edition	Windows 11 Home Single Language
  - Version	24H2

- **Tools**
  - Virtual Code
  
- **Bahasa Pemograman**
  - Phyton

## 2.2.Langkah Eksperimen

## 2.3.Data Set

Dataset yang digunakan terdiri dari 4 proses dengan spesifikasi sebagai berikut:

| Proses | Arrival Time | Burst Time |
|:------:|:------------:|:----------:|
| P1     | 0            | 6          |
| P2     | 1            | 8          |
| P3     | 2            | 7          |
| P4     | 3            | 3          |

**Tabel 1.** Dataset proses untuk simulasi penjadwalan CPU

## 2.4.Cara pengukuran
### Parameter Pengukuran
Untuk setiap algoritma, parameter yang diukur meliputi:
1. **Start Time**: Waktu mulai eksekusi proses
2. **Waiting Time**: Waktu proses menunggu di ready queue (Start Time - Arrival Time)
3. **Turnaround Time**: Total waktu proses di sistem (Waiting Time + Burst Time)
4. **Finish Time**: Waktu selesai eksekusi proses (Start Time + Burst Time)
5. **Average Waiting Time**: Rata-rata waktu tunggu semua proses
6. **Average Turnaround Time**: Rata-rata waktu penyelesaian semua proses

### Prosedur Eksperimen

#### Algoritma FCFS
1. Inisialisasi variabel `waktu_sekarang = 0`
2. Urutkan proses berdasarkan arrival time (sudah terurut dalam dataset)
3. Untuk setiap proses:
   - Tentukan start time: `max(waktu_sekarang, arrival_time)`
   - Hitung waiting time: `start_time - arrival_time`
   - Hitung turnaround time: `waiting_time + burst_time`
   - Update waktu CPU: `waktu_sekarang = start_time + burst_time`
4. Hitung rata-rata waiting time dan turnaround time

#### Algoritma SJF (Non-Preemptive)
1. Inisialisasi variabel `waktu_sekarang = 0`
2. Selama masih ada proses yang belum selesai:
   - Filter proses yang sudah datang: `arrival_time ≤ waktu_sekarang`
   - Jika tidak ada proses tersedia, increment waktu CPU
   - Pilih proses dengan burst time terkecil dari proses tersedia
   - Hitung parameter (start, waiting, turnaround, finish)
   - Update waktu CPU dan hapus proses dari daftar
3. Hitung rata-rata waiting time dan turnaround time

---
# 3.Hasil
## 3.1.Hasil Uji
## 3.2.Ringkasan Temuan

---
# 4.Pembahasan
## 4.1.Interpretasi hasil
## 4.2.Keterbatasan

1. **Dataset Terbatas**: Simulasi hanya menggunakan 4 proses. Dataset lebih besar diperlukan untuk analisis statistik yang lebih robust
2. **Asumsi Ideal**: Simulasi mengasumsikan tidak ada context switch overhead, I/O blocking, atau interrupt
3. **Burst Time Deterministik**: Dalam sistem nyata, burst time sulit diprediksi dengan akurat
4. **Non-Preemptive**: Implementasi SJF yang digunakan adalah versi non-preemptive; versi preemptive (SRTF) mungkin memberikan hasil berbeda

## 4.3.Perbandingan teori

---
# 5.Kesimpulan

Berdasarkan hasil simulasi dan analisis yang telah dilakukan, dapat disimpulkan bahwa:

1. **Validasi Implementasi**: Program simulasi yang dikembangkan menggunakan Python terbukti akurat dengan hasil identik terhadap perhitungan manual, memvalidasi kebenaran implementasi algoritma FCFS dan SJF.

2. **Perbandingan Kinerja**: Algoritma SJF menghasilkan kinerja yang superior dibandingkan FCFS dengan average waiting time 28.6% lebih rendah (6.25 vs 8.75) dan average turnaround time 16.9% lebih rendah (12.25 vs 14.75), membuktikan optimalisasi teoritis SJF dalam meminimalkan waktu tunggu.

3. **Trade-off Implementasi**: FCFS menawarkan kesederhanaan implementasi (kompleksitas O(n)) dan fairness tanpa starvation, sedangkan SJF memerlukan kompleksitas lebih tinggi (O(n²)) dan pengetahuan burst time namun menghasilkan efisiensi optimal. Pemilihan algoritma harus disesuaikan dengan karakteristik sistem dan ketersediaan informasi proses.

4. **Keterbatasan Praktis**: Kedua algoritma memiliki keterbatasan signifikan untuk sistem operasi modern: FCFS rentan convoy effect dan SJF menghadapi masalah prediksi burst time serta potensi starvation, sehingga sistem operasi kontemporer menggunakan algoritma hybrid yang lebih adaptif.


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
