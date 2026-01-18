
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

Penelitian ini bertujuan untuk:
1. Mengimplementasikan simulasi algoritma FCFS dan SJF menggunakan bahasa pemrograman Python
2. Membandingkan kinerja kedua algoritma berdasarkan metrik *waiting time* dan *turnaround time*
3. Memvalidasi hasil simulasi dengan perhitungan manual
4. Menganalisis kelebihan dan keterbatasan masing-masing algoritma
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
  - Microsoft Excel
  
- **Bahasa Pemograman**
  - Phyton

## 2.2.Langkah Eksperimen
1. **Menyiapkan Dataset**

| Proses | Arrival Time | Burst Time |
|:------:|:------------:|:----------:|
| P1     | 0            | 6          |
| P2     | 1            | 8          |
| P3     | 2            | 7          |
| P4     | 3            | 3          |

2. **Persiapan Lingkungan**
   - Alat Pendukungnya : `Visual Studio Code`
   - Bahasa Pemrograman : `Python`
   - Perhitungan Manual : `Microsoft Excel`

3. **Implementasi FCFS**
4. 
   - Menghitung waiting time dan turnaround time.
   - Menghitung rata rata.
   - Catat hasil waiting time,turnaround time,dan rata rata.

5. **Implementasi SJF**
   
   - Menghitung waiting time dan turnaround time.
   - Menghitung rata rata.
   - Catat hasil waiting time,turnaround time,dan rata rata.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FCFS dan SJF.


## 2.3.Data Set

Dataset yang digunakan terdiri dari 4 proses dengan spesifikasi sebagai berikut:

| Proses | Arrival Time | Burst Time |
|:------:|:------------:|:----------:|
| P1     | 0            | 6          |
| P2     | 1            | 8          |
| P3     | 2            | 7          |
| P4     | 3            | 3          |

**Tabel 1.** Dataset proses untuk simulasi penjadwalan CPU

## 2.4.Program dalam bentuk PHYTON
### PROGRAM SIMULASI FCFS
```
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
### PROGRAM SIMULASI SJF
``` phyton

# PROGRAM SIMULASI SJF (Non-Preemptive)

# Data proses
proses = [
    {"nama": "P1", "arrival": 0, "burst": 6},
    {"nama": "P2", "arrival": 1, "burst": 8},
    {"nama": "P3", "arrival": 2, "burst": 7},
    {"nama": "P4", "arrival": 3, "burst": 3},
]

waktu_sekarang = 0
total_waiting = 0
total_turnaround = 0
selesai = []

print("SJF (Shortest Job First - Non Preemptive)")
print("-" * 80)
print(f"{'Proses':<8}{'Burst':<8}{'Arrival':<10}{'Start':<8}{'Waiting':<10}{'Turnaround':<12}{'Finish':<8}")
print("-" * 80)

while proses:
    # Ambil proses yang sudah datang
    tersedia = [p for p in proses if p["arrival"] <= waktu_sekarang]

    # Jika belum ada proses yang datang
    if not tersedia:
        waktu_sekarang += 1
        continue

    # Pilih proses dengan burst time terkecil
    proses_terpendek = min(tersedia, key=lambda x: x["burst"])
    proses.remove(proses_terpendek)

    start = waktu_sekarang
    waiting = start - proses_terpendek["arrival"]
    turnaround = waiting + proses_terpendek["burst"]
    finish = start + proses_terpendek["burst"]

    waktu_sekarang = finish
    total_waiting += waiting
    total_turnaround += turnaround

    print(f"{proses_terpendek['nama']:<8}{proses_terpendek['burst']:<8}{proses_terpendek['arrival']:<10}"
          f"{start:<8}{waiting:<10}{turnaround:<12}{finish:<8}")

    selesai.append(proses_terpendek)

rata_waiting = total_waiting / len(selesai)
rata_turnaround = total_turnaround / len(selesai)

print("-" * 80)
print(f"{'Rata-rata':<36}{rata_waiting:<10.2f}{rata_turnaround:<12.2f}")
```
## 2.5.Cara pengukuran
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

### Hasil Simulasi FCFS
- PROSES MANUAL MENGGUNKAN MICROSOFT EXCEL FCFS
  
  <img width="779" height="311" alt="FCFS_PerhitunganManual_excel" src="https://github.com/user-attachments/assets/54b6af68-ee7c-4602-8958-103b7f9143af" />
**Gambar 1.** Proses manual excel 
- HASIL SIMULASI ALGORITMA FCFS

| Proses | Burst | Arrival | Start | Waiting | Turnaround | Finish |
|:------:|:-----:|:-------:|:-----:|:-------:|:----------:|:------:|
| P1     | 6     | 0       | 0     | 0       | 6          | 6      |
| P2     | 8     | 1       | 6     | 5       | 13         | 14     |
| P3     | 7     | 2       | 14    | 12      | 19         | 21     |
| P4     | 3     | 3       | 21    | 18      | 21         | 24     |
| **Rata-rata** | - | - | - | **8.75** | **14.75** | - |

**Tabel 2.** Hasil simulasi algoritma FCFS

- OUTPUT HASIL PROGRAM SIMULASI FCFS
  <img width="793" height="266" alt="FCFS_Tabel_HasilPogram" src="https://github.com/user-attachments/assets/bbdc7de2-1f74-455d-9af1-96af6e1ae9e0" />

**Gambar 2.** Output program fcfs

### Hasil Simulasi SJF
- PROSES MANUAL MENGGUNAKAN MICROSOFT EXCEL SJF
  <img width="778" height="268" alt="SJF_PerhitunganManual_Excel" src="https://github.com/user-attachments/assets/aa3715fd-05ad-42f8-8242-58411f9a287f" />

**Gambar 3.** Proses manual excel sjf
  
- HASIL SIMULASI ALGORITMA SJF
  
| Proses | Burst | Arrival | Start | Waiting | Turnaround | Finish |
|:------:|:-----:|:-------:|:-----:|:-------:|:----------:|:------:|
| P1     | 6     | 0       | 0     | 0       | 6          | 6      |
| P4     | 3     | 3       | 6     | 3       | 6          | 9      |
| P3     | 7     | 2       | 9     | 7       | 14         | 16     |
| P2     | 8     | 1       | 16    | 15      | 23         | 24     |
| **Rata-rata** | - | - | - | **6.25** | **12.25** | - |

**Tabel 3.** Hasil simulasi algoritma SJF

- OUTPUT HASIL PROGRAM SIMULASI SJF
  <img width="796" height="290" alt="SJF_Tabel_HasilPogram" src="https://github.com/user-attachments/assets/e4b15184-9454-4797-a70d-bd6f2a221423" />

**Gambar 4.** Output program sjf

## 3.2.Ringkasan Temuan

Berdasarkan hasil simulasi yang telah dilakukan, berikut adalah temuan-temuan utama:

Akurasi Program: Implementasi program Python untuk kedua algoritma menghasilkan output yang 100% sesuai dengan perhitungan manual, menunjukkan validitas kode yang telah dibuat.
Keunggulan SJF dalam Efisiensi:

SJF menghasilkan average waiting time 28.6% lebih rendah (6.25 vs 8.75)
SJF menghasilkan average turnaround time 16.9% lebih rendah (12.25 vs 14.75)
Pengurangan 2.5 satuan waktu pada kedua metrik menunjukkan optimalisasi yang signifikan


Pola Urutan Eksekusi:

FCFS: P1 → P2 → P3 → P4 (mengikuti arrival time)
SJF: P1 → P4 → P3 → P2 (memprioritaskan burst time terpendek)

---
# 4.Pembahasan
## 4.1.Interpretasi hasil

#### Kinerja Algoritma FCFS

Hasil simulasi menunjukkan bahwa algoritma FCFS menghasilkan average waiting time sebesar 8.75 satuan waktu. Proses P4 yang memiliki burst time paling pendek (3 satuan) harus menunggu selama 18 satuan waktu karena tiba belakangan. Hal ini mendemonstrasikan , di mana proses pendek terjebak menunggu proses panjang yang datang lebih awal[2].

Urutan eksekusi FCFS mengikuti arrival time: P1 → P2 → P3 → P4. Meskipun sederhana dan adil  dalam hal pemberian kesempatan, algoritma ini tidak optimal dalam meminimalkan waiting time.

#### Kinerja Algoritma SJF
Algoritma SJF menghasilkan average waiting time sebesar 6.25 satuan waktu, **28.6% lebih baik** dibandingkan FCFS. Urutan eksekusi SJF adalah: P1 → P4 → P3 → P2. Dengan memprioritaskan P4 (burst time = 3) setelah P1 selesai, algoritma ini berhasil mengurangi total waiting time sistem.

Hasil ini sesuai dengan teori bahwa SJF menghasilkan minimum average waiting time untuk sekumpulan proses yang telah diketahui burst time-nya[1]. Namun, P2 yang datang paling awal (arrival time = 1) justru selesai paling akhir karena memiliki burst time terpanjang, menunjukkan potensi *starvation* pada SJF.

### Analisis Perbandingan

**Efisiensi Waktu Tunggu**  
SJF unggul dalam efisiensi dengan pengurangan 2.5 satuan waktu pada average waiting time dan average turnaround time. Perbedaan 28.6% ini signifikan untuk sistem dengan banyak proses pendek.

**Kompleksitas Implementasi**  
FCFS memiliki kompleksitas O(n) dengan logika linear sederhana. SJF memerlukan kompleksitas O(n²) karena harus melakukan pencarian minimum pada setiap iterasi, serta menambahkan logika pemilihan proses yang tersedia.

**Fairness dan Starvation**  
FCFS menjamin setiap proses akan dieksekusi sesuai urutan kedatangan (*first-come first-served fairness*). Sebaliknya, SJF dapat menyebabkan proses dengan burst time panjang menunggu sangat lama jika terus ada proses pendek yang datang, menimbulkan masalah *starvation*[2].

## 4.2.Keterbatasan

1. **Dataset Terbatas**: Simulasi hanya menggunakan 4 proses. Dataset lebih besar diperlukan untuk analisis statistik yang lebih robust
2. **Asumsi Ideal**: Simulasi mengasumsikan tidak ada context switch overhead, I/O blocking, atau interrupt
3. **Burst Time Deterministik**: Dalam sistem nyata, burst time sulit diprediksi dengan akurat
4. **Non-Preemptive**: Implementasi SJF yang digunakan adalah versi non-preemptive; versi preemptive (SRTF) mungkin memberikan hasil berbeda

## 4.3.Perbandingan teori

#### FCFS
**Kelebihan:**
- Implementasi sangat sederhana dan mudah dipahami
- Tidak memerlukan informasi burst time sebelumnya
- Fair terhadap semua proses (no starvation)
- Overhead minimal

**Keterbatasan:**
- Average waiting time tinggi, terutama dengan variasi burst time besar
- Rentan terhadap convoy effect
- Tidak optimal untuk sistem interaktif atau real-time

#### SJF
**Kelebihan:**
- Menghasilkan minimum average waiting time (optimal secara teoritis)
- Efisien untuk batch sistem dengan proses pendek dominan
- Meningkatkan throughput sistem

**Keterbatasan:**
- Memerlukan pengetahuan burst time sebelumnya (sulit diprediksi dalam praktik)
- Potensi starvation untuk proses panjang
- Kompleksitas implementasi lebih tinggi
- Tidak cocok untuk sistem time-sharing atau interaktif

---
# 5.Kesimpulan

Berdasarkan hasil simulasi dan analisis yang telah dilakukan, dapat disimpulkan bahwa:

1. **Validasi Implementasi**: Program simulasi yang dikembangkan menggunakan Python terbukti akurat dengan hasil identik terhadap perhitungan manual, memvalidasi kebenaran implementasi algoritma FCFS dan SJF.

2. **Perbandingan Kinerja**: Algoritma SJF menghasilkan kinerja yang superior dibandingkan FCFS dengan average waiting time 28.6% lebih rendah (6.25 vs 8.75) dan average turnaround time 16.9% lebih rendah (12.25 vs 14.75), membuktikan optimalisasi teoritis SJF dalam meminimalkan waktu tunggu.

3. **Trade-off Implementasi**: FCFS menawarkan kesederhanaan implementasi (kompleksitas O(n)) dan fairness tanpa starvation, sedangkan SJF memerlukan kompleksitas lebih tinggi (O(n²)) dan pengetahuan burst time namun menghasilkan efisiensi optimal. Pemilihan algoritma harus disesuaikan dengan karakteristik sistem dan ketersediaan informasi proses.

4. **Keterbatasan Praktis**: Kedua algoritma memiliki keterbatasan signifikan untuk sistem operasi modern: FCFS rentan convoy effect dan SJF menghadapi masalah prediksi burst time serta potensi starvation, sehingga sistem operasi kontemporer menggunakan algoritma hybrid yang lebih adaptif.


---

## Quiz

### 1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?

**Jawaban:**

Format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi karena beberapa alasan:

**A. Struktur Sistematis dan Terstandarisasi**  
IMRAD menyediakan kerangka yang konsisten dan universal dalam penulisan ilmiah. Struktur ini memudahkan pembaca untuk menemukan informasi spesifik tanpa harus membaca keseluruhan laporan. Peneliti lain dapat langsung menuju bagian Methods untuk mereplikasi eksperimen, atau ke Results untuk melihat temuan.

**B. Alur Logis Penelitian Ilmiah**  
Format IMRAD mengikuti alur berpikir ilmiah: (1) *Introduction* menetapkan konteks dan pertanyaan penelitian, (2) *Methods* menjelaskan cara menjawab pertanyaan, (3) *Results* menyajikan temuan objektif, (4) *Discussion* menginterpretasi makna temuan. Alur ini mencerminkan metode ilmiah yang sistematis.

**C. Pemisahan Fakta dan Interpretasi**  
Bagian Results menyajikan data objektif tanpa bias interpretasi, sementara Discussion menganalisis dan menginterpretasi data tersebut. Pemisahan ini meningkatkan objektivitas dan memungkinkan pembaca membentuk interpretasi independen.

**D. Replikabilitas**  
Bagian Methods yang detail memungkinkan peneliti lain mereplikasi eksperimen dengan presisi tinggi, yang merupakan fondasi validitas ilmiah.

**E. Evaluasi Bertingkat**  
Evaluator dapat menilai aspek berbeda secara terpisah: kualitas desain eksperimen (Methods), validitas data (Results), dan kekuatan argumentasi (Discussion). Ini memudahkan identifikasi kekuatan dan kelemahan spesifik.

**Kesimpulan**: Format IMRAD meningkatkan kredibilitas ilmiah dengan menyediakan struktur yang jelas, logis, dan memfasilitasi verifikasi serta replikasi penelitian.

---

### 2. Apa perbedaan antara bagian **Hasil** dan **Pembahasan**?

**Jawaban:**

| Aspek | Hasil (Results) | Pembahasan (Discussion) |
|:------|:----------------|:------------------------|
| **Tujuan** | Menyajikan temuan objektif tanpa interpretasi | Menginterpretasi makna dan implikasi temuan |
| **Isi** | Data mentah, tabel, grafik, statistik deskriptif | Analisis, perbandingan teori vs praktik, penjelasan pola |
| **Gaya Penulisan** | Faktual, deskriptif, netral | Analitis, evaluatif, argumentatif |
| **Subjektivitas** | Minimal/tidak ada interpretasi | Interpretasi dan opini berdasarkan data |
| **Contoh Kalimat** | "Average waiting time FCFS adalah 8.75 dan SJF adalah 6.25" | "SJF lebih efisien karena memprioritaskan proses pendek, mengurangi convoy effect yang terjadi pada FCFS" |
| **Referensi Teori** | Jarang/tidak ada | Sering, untuk membandingkan hasil dengan literatur |
| **Keterbatasan** | Tidak dibahas | Diidentifikasi dan dijelaskan dampaknya |

**Analogi Sederhana:**  
- **Hasil**: Seperti termometer menunjukkan 38°C (fakta objektif)
- **Pembahasan**: "Suhu 38°C menunjukkan demam ringan, kemungkinan disebabkan infeksi virus, perlu istirahat dan monitoring" (interpretasi dan rekomendasi)

**Kesimpulan**: Results menyajikan "apa yang ditemukan" secara objektif, sedangkan Discussion menjelaskan "mengapa hal itu terjadi" dan "apa implikasinya" melalui interpretasi dan analisis kritis.

---

### 3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?

**Jawaban:**

Sitasi dan daftar pustaka penting dalam laporan praktikum karena beberapa alasan fundamental:

**A. Integritas Akademik**  
Sitasi mencegah plagiarisme dengan memberikan kredit kepada penulis asli ide, teori, atau data yang digunakan. Ini merupakan etika dasar dalam dunia akademik dan menghormati hak intelektual orang lain.

**B. Kredibilitas dan Validitas**  
Referensi ke sumber terpercaya (textbook, jurnal peer-reviewed, dokumentasi resmi) meningkatkan kredibilitas laporan. Pembaca dapat memverifikasi bahwa argumen didukung oleh literatur yang valid, bukan opini pribadi tanpa dasar.

**C. Konteks Teoretis**  
Sitasi menunjukkan bahwa praktikum tidak berdiri sendiri, tetapi merupakan bagian dari body of knowledge yang lebih besar. Misalnya, mengutip Silberschatz untuk definisi algoritma scheduling menunjukkan pemahaman konteks teoritis.

**D. Replikasi dan Verifikasi**  
Daftar pustaka memungkinkan pembaca mengakses sumber asli untuk pemahaman lebih dalam atau verifikasi informasi. Jika ada ketidaksesuaian hasil, pembaca dapat menelusuri sumber yang dikutip.

**E. Pembelajaran Berkelanjutan**  
Daftar pustaka berfungsi sebagai reading list bagi pembaca yang ingin memperdalam topik. Ini mendukung budaya pembelajaran dan riset yang berkelanjutan.

**F. Standar Profesional**  
Kebiasaan sitasi dalam praktikum mempersiapkan mahasiswa untuk penulisan ilmiah tingkat lanjut (skripsi, thesis, paper) dan praktik profesional di industri yang menghargai dokumentasi.

**Contoh Praktis dalam Laporan Ini:**
- [1] Silberschatz et al. memberikan fondasi teoritis algoritma scheduling
- [2] Tanenbaum menjelaskan konsep convoy effect yang diamati dalam hasil
- Tanpa sitasi, klaim "SJF optimal" hanya opini; dengan sitasi, menjadi fakta terverifikasi

**Kesimpulan**: Sitasi dan daftar pustaka bukan formalitas, tetapi elemen esensial yang memastikan integritas, kredibilitas, dan nilai edukatif laporan praktikum. Kebiasaan ini membangun fondasi untuk riset dan komunikasi ilmiah yang berkualitas.

---

## Daftar Pustaka

1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). John Wiley & Sons.

2. Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson Education.

3. Love, R. (2010). *Linux Kernel Development* (3rd ed.). Addison-Wesley Professional.

4. Stallings, W. (2018). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson Education.

---

## Refleksi Diri

### Apa bagian yang paling menantang minggu ini?
Bagian paling menantang adalah menyusun **Pembahasan (Discussion)** yang tidak hanya menjelaskan hasil, tetapi juga menganalisis secara kritis dengan menghubungkan temuan eksperimen ke teori, mengidentifikasi keterbatasan, dan memberikan implikasi praktis. Memisahkan fakta objektif di Results dari interpretasi analitis di Discussion membutuhkan pemahaman mendalam tentang perbedaan keduanya.

### Bagaimana cara Anda mengatasinya?
Saya mengatasinya dengan:
1. **Membaca contoh paper ilmiah** untuk memahami pola penulisan Discussion yang baik
2. **Membuat outline** terlebih dahulu dengan sub-bagian: interpretasi hasil → analisis perbandingan → kelebihan/keterbatasan → implikasi praktis
3. **Menambahkan sitasi** untuk mendukung argumen dengan teori dari textbook
4. **Review iteratif**: menulis draft, membaca ulang untuk memastikan tidak ada pengulangan dengan Results, lalu memperbaiki

Format IMRAD ini sangat membantu mengorganisir pemikiran secara sistematis dan melatih kemampuan analisis kritis yang akan berguna untuk penulisan ilmiah tingkat lanjut.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_ 
