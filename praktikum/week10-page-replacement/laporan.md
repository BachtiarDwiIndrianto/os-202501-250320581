
# Laporan Praktikum Minggu [X]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)
---

## Identitas
- **Nama**  : Bachtiar Dwi Indrianto  
- **NIM**   : 250320581
- **Kelas** : 1DSRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

- 1 Mengimplementasikan algoritma page replacement FIFO dalam program.
- 2 Mengimplementasikan algoritma page replacement LRU dalam program.
- 3 Menjalankan simulasi page replacement dengan dataset tertentu.
- 4 Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
- 5 Menyajikan hasil simulasi dalam laporan yang sistematis.
  
C. Ketentuan Teknis
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
1. Apa perbedaan utama FIFO dan LRU?  
   **Jawaban:**
   - Perbedaan FIFO dan LRU

| Aspek                  | FIFO (First In First Out)             | LRU (Least Recently Used)           |
|-----------------------|---------------------------------------|-------------------------------------|
| Prinsip Kerja         | Data yang pertama masuk dikeluarkan   | Data yang paling lama tidak digunakan dikeluarkan |
| Dasar Penggantian     | Urutan waktu masuk                    | Riwayat penggunaan terakhir         |
| Memperhatikan Pola Akses | Tidak                               | Ya                                  |
| Kompleksitas          | Sederhana                             | Lebih kompleks                      |
| Efisiensi             | Kurang efisien                       | Lebih efisien                       |
| Page Fault            | Cenderung lebih banyak               | Cenderung lebih sedikit             |
| Implementasi          | Mudah                                | Membutuhkan pencatatan akses        |
| Contoh Penggunaan     | Sistem sederhana                     | Sistem dengan performa tinggi       |

2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly? 
   **Jawaban:**
    - Belady’s Anomaly adalah fenomena di mana algoritma FIFO (First In, First Out) menghasilkan lebih banyak page fault saat jumlah frame memori ditingkatkan, yang bertentangan dengan intuisi bahwa lebih banyak memori seharusnya mengurangi fault.
    - Penyebab Utama
   FIFO mengganti halaman berdasarkan urutan masuknya ke memori, tanpa mempertimbangkan frekuensi penggunaan atau waktu akses terakhir. Dengan lebih banyak frame:
      - Halaman yang masuk lebih awal (meski masih relevan) tetap diprioritaskan untuk diganti jika memori penuh.
      - Ini bisa menyebabkan halaman yang sering digunakan atau akan segera dibutuhkan diganti lebih dini, sehingga meningkatkan fault saat pola akses berulang atau kompleks.
      - Algoritma lain seperti LRU tidak mengalami ini karena mempertimbangkan penggunaan terbaru, memanfaatkan prinsip lokalitas referensi.
        
     - Contoh Ilustrasi

       Misalkan urutan akses halaman: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5.
       Dengan 3 frame memori: Page fault = 9.
       Dengan 4 frame memori: Page fault = 10 (lebih banyak!).

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   **Jawaban:**
  - Alasan Utama Performa Lebih Baik
LRU umumnya lebih baik karena memanfaatkan prinsip lokalitas referensi (temporal dan spatial), yang menyatakan bahwa program cenderung mengakses halaman yang baru saja digunakan atau halaman berdekatan. Ini membuat LRU lebih adaptif terhadap pola akses dunia nyata:

    - Pengurangan Page Fault: LRU memprediksi halaman yang mungkin tidak segera dibutuhkan lagi, sehingga mengurangi kesalahan penggantian. FIFO bisa mengganti halaman yang masih relevan jika masuk lebih awal, terutama dalam pola berulang.
    - Hindari Anomali: FIFO rentan terhadap Belady’s Anomaly (page fault meningkat saat frame memori bertambah), sedangkan LRU menghindarinya karena fokus pada penggunaan terbaru, bukan urutan masuk.
    - Efisiensi dalam Pola Akses: Pada aplikasi dengan loop atau akses berulang (seperti database atau web browsing), LRU menjaga halaman "panas" di memori lebih lama, meningkatkan hit rate cache.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
