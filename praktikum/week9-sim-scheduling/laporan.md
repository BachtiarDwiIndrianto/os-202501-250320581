
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

```python

# PROGRAM SIMULASI FCFS

# Data proses (nama proses, waktu datang, dan burst time)
proses = [
    {"nama": "P1", "arrival": 0, "burst": 6},
    {"nama": "P2", "arrival": 1, "burst": 8},
    {"nama": "P3", "arrival": 2, "burst": 7},
    {"nama": "P4", "arrival": 3, "burst": 3},
]

# Variabel untuk menyimpan waktu CPU saat ini
waktu_sekarang = 0

# Variabel untuk menghitung total waiting dan turnaround
total_waiting = 0
total_turnaround = 0

# Menampilkan judul tabel
print("FCFS (First Come First Served)")
print("-" * 75)
print(f"{'Proses':<8}{'Burst':<8}{'Arrival':<10}{'Start':<8}{'Waiting':<10}{'Turnaround':<12}{'Finish':<8}")
print("-" * 75)

# Proses perhitungan FCFS
for p in proses:
    # Start time ditentukan oleh waktu CPU atau arrival time
    start = max(waktu_sekarang, p["arrival"])

    # Waiting time = start time - arrival time
    waiting = start - p["arrival"]

    # Turnaround time = waiting time + burst time
    turnaround = waiting + p["burst"]

    # Finish time = start time + burst time
    finish = start + p["burst"]

    # Update waktu CPU
    waktu_sekarang = finish

    # Menjumlahkan total waiting dan turnaround
    total_waiting += waiting
    total_turnaround += turnaround

    # Menampilkan hasil per proses
    print(f"{p['nama']:<8}{p['burst']:<8}{p['arrival']:<10}{start:<8}{waiting:<10}{turnaround:<12}{finish:<8}")

# Menghitung nilai rata-rata
rata_waiting = total_waiting / len(proses)
rata_turnaround = total_turnaround / len(proses)

# Menampilkan rata-rata
print("-" * 75)
print(f"{'Rata-rata':<34}{rata_waiting:<10.2f}{rata_turnaround:<12.2f}")
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1919" height="1079" alt="Screenshot 2026-01-01 145108" src="https://github.com/user-attachments/assets/1fd46194-ba90-48e9-bd88-8c3d0586ba0d" />


---

## Analisis
- Alur dalam program tersebut
```
1. Program dimulai dengan menyiapkan data proses yang terdiri dari nama proses, waktu kedatangan (*arrival time*), dan waktu eksekusi (*burst time*).
2. Waktu CPU diinisialisasi mulai dari 0 menggunakan variabel `waktu_sekarang`.
3. Program memproses setiap proses satu per satu sesuai urutan kedatangan, sesuai dengan prinsip algoritma FCFS (First Come First Served).
4. Untuk setiap proses, program menghitung:
   - **Start Time**, yaitu waktu mulai proses dieksekusi.
   - **Waiting Time**, yaitu selisih antara start time dan arrival time.
   - **Turnaround Time**, yaitu total waktu proses berada di sistem.
   - **Finish Time**, yaitu waktu proses selesai dieksekusi.
5. Setelah satu proses selesai, nilai `waktu_sekarang` diperbarui ke waktu selesai proses tersebut.
6. Hasil perhitungan setiap proses ditampilkan dalam bentuk tabel agar mudah dibaca.
7. Di akhir program, dihitung rata-rata waiting time dan turnaround time sebagai evaluasi kinerja algoritma FCFS.
```
- Bandingkan dengan perhitungan manual
  - Manual dengan excel
  <img width="779" height="311" alt="Screenshot 2026-01-01 142425" src="https://github.com/user-attachments/assets/506c58ef-c759-4394-9559-de5616dfc08a" />

  - Tabel Hasil Simulasi FCFS (First Come First Served)

| Proses | Burst Time | Arrival Time | Start | Waiting | Turnaround | Finish |
|:-----:|:----------:|:------------:|:-----:|:-------:|:----------:|:------:|
| P1    | 6          | 0            | 0     | 0       | 6          | 6      |
| P2    | 8          | 1            | 6     | 5       | 13         | 14     |
| P3    | 7          | 2            | 14    | 12      | 19         | 21     |
| P4    | 3          | 3            | 21    | 18      | 21         | 24     |
| **Rata-rata** | — | — | — | **8,75** | **14,75** | — |

   - Hasil Program(Phyton)

<img width="793" height="266" alt="Screenshot 2026-01-01 150633" src="https://github.com/user-attachments/assets/325e0633-dee3-441a-a492-1a2c5d17ae06" />

   
- Jelaskan Kelebihan dan Keterbatasan Simulasi
  - Kelebihan
    - Perhitungan dilakukan secara otomatis dan cepat.
    - Mengurangi kesalahan dalam perhitungan manual.
    - Memudahkan pemahaman cara kerja algoritma penjadwalan CPU.
      
  - Keterbatasan
    - Hanya mensimulasikan kondisi tertentu, bukan sistem nyata.
    - Hasil simulasi bergantung pada dataset yang digunakan.
    - Tidak memperhitungkan faktor lain seperti interupsi atau overhead sistem.
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
