
# Laporan Praktikum Minggu [X]
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Bachtiar Dwi Indrianto
- **NIM**   : 250320581
- **Kelas** : 1DSRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

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
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?
   **Jawaban:**
   ## Perbandingan Deadlock Prevention, Avoidance, dan Detection

| Aspek              | Prevention | Avoidance | Detection |
|-------------------|------------|-----------|-----------|
| Pendekatan | Proaktif: Membatasi akses sumber daya untuk mencegah kondisi deadlock | Proaktif: Memeriksa keamanan sistem sebelum alokasi sumber daya | Reaktif: Membiarkan deadlock terjadi, lalu mendeteksi dan memulihkannya |
| Kondisi Deadlock | Tidak pernah memungkinkan kondisi deadlock terbentuk | Deadlock mungkin terjadi, tetapi sistem menghindari keadaan tidak aman | Deadlock diperbolehkan terjadi |
| Keuntungan | Sederhana dan efisien untuk sistem kecil; overhead rendah | Lebih fleksibel; memaksimalkan utilisasi sumber daya | Tidak membatasi proses; cocok untuk sistem kompleks |
| Kekurangan | Kurang efisien; proses dapat menunggu lama dan berpotensi starvation | Kompleks; membutuhkan informasi lengkap dan overhead tinggi | Deteksi memerlukan waktu; pemulihan bisa mahal |
| Algoritma Contoh | Aturan *no hold and wait* (semua resource diminta sekaligus) | Banker’s Algorithm | Wait-for Graph |
| Penggunaan | Sistem real-time dan embedded | OS seperti Unix; sistem dengan sumber daya terbatas | Database dan sistem besar (misalnya SQL Server) |


2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   **Jawaban:**
   - Alasan Utama
Deteksi deadlock tetap diperlukan dalam sistem operasi karena strategi pencegahan (prevention) dan penghindaran (avoidance) deadlock memiliki keterbatasan, sehingga deteksi menjadi pendekatan reaktif yang penting untuk menangani deadlock yang tidak dapat dihindari sepenuhnya. Berikut penjelasannya:
       - Keterbatasan Prevention dan Avoidance:
            - Prevention (misalnya, membatasi hold and wait) seringkali terlalu konservatif, menyebabkan utilisasi sumber daya rendah dan proses menunggu lama (starvation). Tidak cocok untuk sistem kompleks dengan banyak proses dinamis.
            - Avoidance (seperti Banker's Algorithm) memerlukan informasi lengkap tentang kebutuhan sumber daya proses di muka, yang sulit diperoleh dalam sistem real-time atau dengan proses yang berubah-ubah. Overhead komputasi tinggi, terutama untuk sistem besar.
        - Keunggulan Deteksi:
            - Fleksibilitas: Mengizinkan sistem berjalan tanpa pembatasan ketat, memaksimalkan performa dan utilisasi sumber daya. Deadlock dideteksi saat terjadi (misalnya, melalui wait-for graph), lalu dipulihkan.
            - Cocok untuk Sistem Kompleks: Dalam database, sistem terdistribusi, atau OS seperti Windows/Linux, proses seringkali tidak dapat diprediksi sepenuhnya. Deteksi memungkinkan respons cepat tanpa mencegah aktivitas normal.
            - Pemulihan Efektif: Setelah deteksi, sistem dapat terminate proses, rollback, atau preemption sumber daya, meminimalkan dampak. Ini lebih praktis daripada mencegah semua kemungkinan deadlock.
        - Skenario Praktis:
            - Dalam database (misalnya, SQL Server), deadlock sering terjadi karena transaksi konkurensi. Deteksi otomatis memungkinkan rollback transaksi yang terlibat tanpa menghentikan seluruh sistem.
            - Sistem operasi modern menggunakan kombinasi strategi: prevention untuk sumber daya kritis, avoidance untuk yang dapat diprediksi, dan detection untuk yang lainnya.
 - Contoh Ilustrasi
Bayangkan sistem dengan banyak proses yang saling bergantung (misalnya, printer dan file sharing). Prevention mungkin memaksa semua proses meminta sumber daya sekaligus, menyebabkan inefisiensi. Avoidance gagal jika kebutuhan proses tidak diketahui. Deteksi memungkinkan sistem mendeteksi siklus tunggu dan mengakhiri proses deadlock, menjaga sistem berjalan.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock? 
   **Jawaban:**  
## Kelebihan dan Kekurangan Pendekatan Deteksi Deadlock

| Aspek | Kelebihan | Kekurangan |
|------|-----------|------------|
| Cara Kerja | Sistem dibiarkan berjalan bebas dan bertindak hanya saat deadlock terdeteksi | Harus menunggu deadlock terjadi sebelum dapat ditangani |
| Kinerja | Tidak membatasi proses sehingga kinerja normal lebih tinggi | Saat deadlock terjadi, kinerja menurun karena proses macet |
| Penggunaan Sumber Daya | Sumber daya digunakan sepenuhnya tanpa reservasi | Saat deadlock, sumber daya terkunci dan tidak dapat digunakan |
| Implementasi | Relatif mudah diimplementasikan dengan algoritma deteksi | Proses pemulihan (*recovery*) bisa rumit dan mahal |
| Kebutuhan Informasi | Tidak perlu mengetahui kebutuhan sumber daya di awal | Membutuhkan informasi lengkap tentang keadaan sistem saat deteksi |
| Kesesuaian | Cocok untuk sistem dengan deadlock yang jarang terjadi | Tidak cocok untuk sistem yang sering atau bersifat kritis terhadap deadlock |

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
