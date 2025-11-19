
# Laporan Praktikum Minggu [X]
Topik: [Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling"]

---

## Identitas
- **Nama**  : [Bachtiar Dwi Indrianto]  
- **NIM**   : [250320581]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
Menyusun tabel hasil perhitungan dengan benar dan sistematis.
Membandingkan performa algoritma RR dan Priority.
Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.
---

## Dasar Teori

1. **CPU Scheduling** adalah proses sistem operasi dalam menentukan urutan eksekusi proses agar CPU digunakan secara efisien dan adil.

2. **Round Robin (RR)** memberi waktu eksekusi sama rata (*time quantum*) untuk setiap proses. Jika waktu habis, proses akan diantrikan kembali. Cocok untuk sistem interaktif.

3. **Priority Scheduling** mengeksekusi proses berdasarkan tingkat prioritas. Proses dengan prioritas tertinggi dijalankan lebih dulu.

4. **Kelebihan & Kekurangan:**
   - RR: adil, tapi bisa boros waktu jika *quantum* terlalu kecil.  
   - Priority: efisien untuk proses penting, tapi bisa menyebabkan *starvation*.

5. **Kesimpulan:**  
   Round Robin menekankan keadilan waktu, sedangkan Priority Scheduling menekankan efisiensi sesuai tingkat kepentingan proses.
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

**ROUND ROBIN(RR)**

<img width="1911" height="1079" alt="Screenshot 2025-11-19 193730" src="https://github.com/user-attachments/assets/9970cf6c-7d72-4db7-890a-ab0c931edf48" />
Hitung Waiting dan Turnaround Time

|    Proses   | Burst Time | Arrival Time | Finish | Waiting Time | Turnaround Time |
| :---------: | :--------: | :----------: | :----: | :----------: | :-------------: |
|      P1     |      5     |       0      |   14   |       9      |        14       |
|      P2     |      3     |       1      |    6   |       2      |        5        |
|      P3     |      8     |       2      |   22   |      12      |        20       |
|      P4     |      6     |       3      |   20   |      11      |        17       |
|  **Total**  |            |              |        |    **34**    |      **56**     |
| **Average** |            |              |        |    **8,5**   |      **14**     |

   
Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).

       | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
    0    3    6    9   12    14   17   20   22

   Catat sisa burst time tiap putaran.
   | Putaran           | P1 | P2 | P3 | P4 |
| ----------------- | -- | -- | -- | -- |
| Awal              | 5  | 3  | 8  | 6  |
| Setelah Putaran 1 | 2  | 0  | 5  | 3  |
| Setelah Putaran 2 | 0  | 0  | 2  | 0  |
| Setelah Putaran 3 | 0  | 0  | 0  | 0  |

**PRIORITY SCHEDULING**

|    Proses   | Burst Time | Arrival Time | Priority | Start | Finish | Waiting Time | Turnaround Time |
| :---------: | :--------: | :----------: | :------: | :---: | :----: | :----------: | :-------------: |
|      P1     |      5     |       0      |     2    |   0   |    5   |       0      |        5        |
|      P2     |      3     |       1      |     1    |   5   |    8   |       4      |        7        |
|      P3     |      6     |       3      |     3    |   8   |   14   |       5      |        11       |
|      P4     |      8     |       2      |     4    |   14  |   22   |      12      |        20       |
|  **Total**  |            |              |          |       |        |    **21**    |      **43**     |
| **Average** |            |              |          |       |        |   **5,25**   |    **10,75**    |

 - Waitinng Time :
       - P1 : 0 - 0 = 0
       - P2 : 5 - 1 = 4
       - P3 : 8 - 3 = 5
       - P4 : 14 - 2 = 12
   - Turnaround Time :
       - P1 : 0 + 5 = 5
       - P2 : 4 + 3 = 7
       - P3 : 5 + 6 = 11
       - P4 : 12 + 8 = 20
    
    | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |


## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
1. Algoritma **Round Robin (RR)** memberikan keadilan waktu eksekusi bagi setiap proses karena semua mendapat jatah *time quantum* yang sama.  
   Namun, performanya sangat bergantung pada besar kecilnya nilai *quantum*.

2. Algoritma **Priority Scheduling** lebih efisien untuk proses penting dengan prioritas tinggi, tetapi bisa menyebabkan **starvation** bagi proses dengan prioritas rendah.

3. Nilai *time quantum* yang terlalu kecil membuat sistem sering melakukan **context switch**, sedangkan *quantum* yang terlalu besar membuat sistem kurang responsif.

4. Hasil perhitungan menunjukkan bahwa **RR lebih adil**, sedangkan **Priority lebih efisien** bila prioritas diatur dengan baik.

5. Secara keseluruhan, kedua algoritma memiliki kelebihan masing-masing dan pemilihannya harus disesuaikan dengan kebutuhan sistem:  
   - RR → cocok untuk sistem interaktif.  
   - Priority → cocok untuk sistem dengan tugas yang berbeda tingkat kepentingannya.
---

## Quiz
1. [Apa perbedaan utama antara Round Robin dan Priority Scheduling?]  
    Perbedaan Round Robin (RR) vs Priority Scheduling (PS)

| Aspek | **Round Robin (RR)** | **Priority Scheduling (PS)** |
|-------|----------------------|------------------------------|
| **Dasar Penjadwalan** | Berdasarkan **waktu** (time quantum) | Berdasarkan **prioritas** proses |
| **Cara Kerja** | Setiap proses mendapat jatah waktu yang sama secara bergantian (rotasi) | Proses dengan prioritas **lebih tinggi** dieksekusi lebih dulu |
| **Keadilan (Fairness)** | Adil, karena semua proses mendapat waktu eksekusi yang sama | Kurang adil, proses prioritas rendah bisa tertunda lama |
| **Cocok Untuk** | Sistem **time-sharing** (multitasking OS modern) | Sistem **real-time** atau tugas penting dengan prioritas tinggi |
| **Kelemahan Utama** | **Overhead** tinggi karena sering terjadi context switching | **Starvation**, proses prioritas rendah bisa tidak dieksekusi lama |

---

2. [Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?]  
   Pengaruh Time Quantum terhadap Performa Sistem
- **Kalau time quantum terlalu kecil:**  
  CPU sering ganti-ganti proses. Akibatnya banyak waktu terbuang untuk pindah tugas, jadi sistem jadi **lambat dan boros waktu**.
- **Kalau time quantum terlalu besar:**  
  Satu proses bisa jalan terlalu lama. Proses lain jadi **nunggu lama**, sistem terasa **kurang responsif**.
- **Kalau time quantum pas:**  
  Semua proses dapat giliran dengan lancar. Sistem jadi **lebih seimbang**, **efisien**, dan **responsif**.

Waktu quantum harus dipilih **tidak terlalu kecil dan tidak terlalu besar** supaya sistem berjalan **lancar dan adil** untuk semua proses.

3. [Mengapa algoritma Priority dapat menyebabkan starvation?]
    Dalam algoritma **Priority Scheduling**, proses yang punya **prioritas lebih tinggi** akan dijalankan dulu.
Nah, kalau terus-menerus ada proses baru dengan prioritas tinggi yang datang,  maka proses yang **prioritasnya rendah** akan terus **menunggu** dan **tidak pernah dijalankan**.Itulah yang disebut **starvation** — proses "kelaparan" karena **tidak kebagian waktu CPU**.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  Kesulitan utama adalah memahami alur pergantian proses pada Round Robin serta cara menentukan urutan eksekusi pada Priority Scheduling.  
Namun, setelah membuat Gantt Chart dan tabel perhitungan, konsepnya menjadi lebih mudah dipahami.
- Bagaimana cara Anda mengatasinya?
 Saya mencoba menghitung ulang secara manual, memeriksa contoh di referensi, dan mendiskusikannya dengan teman kelompok agar lebih paham alur eksekusi proses.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
