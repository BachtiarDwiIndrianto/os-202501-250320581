
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Nama Mahasiswa]  
- **NIM**   : [NIM Mahasiswa]  
- **Kelas** : [Kelas]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

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
1. [Apa perbedaan utama antara FCFS dan SJF?]  
#  Perbandingan FCFS vs SJF

| Aspek | FCFS (First Come First Serve) | SJF (Shortest Job First) |
|-------|-------------------------------|--------------------------|
|  Urutan | Siapa datang duluan, dikerjakan duluan | Yang paling cepat selesai, dikerjakan duluan |
|  Waktu Tunggu | Bisa lama kalau proses awal panjang | Lebih cepat secara rata-rata |
|  Efisiensi | Kurang efisien | Lebih efisien |
|  Jenis | Non-preemptive | Bisa preemptive atau non-preemptive |
|  Contoh | Antre kasir: datang duluan dilayani duluan | Kasir pilih pelanggan dengan barang paling sedikit dulu |

- **FCFS**: Sederhana tapi bisa bikin nunggu lama.  
- **SJF**: Lebih cepat tapi butuh tahu lama tiap proses.
  
2. [Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?]  
    Kenapa SJF Waktu Tunggunya Paling Kecil
SJF itu efisien karena sistem ngerjain proses yang cepat dulu.  
Jadi proses kecil langsung selesai, nggak harus nunggu proses besar beres dulu.  
Akibatnya, rata-rata waktu tunggu semua proses jadi lebih singkat.

SJF bikin banyak proses cepat selesai,  
makanya waktu tunggunya paling kecil dibanding algoritma lain.

4. [Apa kelemahan SJF jika diterapkan pada sistem interaktif?]  
Kelemahan SJF di Sistem Interaktif

1.  **Susah tahu waktu proses**
   - Di sistem interaktif, kita nggak bisa tahu berapa lama tiap proses butuh waktu.

2.  **Proses panjang bisa nggak kebagian**
   - Proses kecil terus didahulukan, jadi proses besar bisa terus tertunda.

3.  **Kurang cocok buat sistem yang butuh respon cepat**
   - Sistem interaktif butuh cepat tanggap, sedangkan SJF kurang fleksibel.

SJF memang cepat dan efisien, tapi **nggak cocok untuk sistem interaktif** karena susah diprediksi dan bisa bikin proses besar nunggu lama.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
