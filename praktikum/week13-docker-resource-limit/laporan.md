
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Bachtiar Dwi Indrianto 
- **NIM**   : 250320581
- **Kelas** : 1DSRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.
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
1. Mengapa container perlu dibatasi CPU dan memori?  
   **Jawaban:**
   Pembatasan CPU dan memori pada container diperlukan untuk mencegah satu container menggunakan sumber daya secara berlebihan sehingga mengganggu container lain dan kestabilan sistem host. Dengan adanya batasan, setiap container mendapatkan alokasi sumber daya yang adil, performa aplikasi menjadi lebih stabil dan terprediksi, serta risiko kehabisan memori atau crash sistem dapat dikurangi. Selain itu, pembatasan ini meningkatkan keamanan dengan membatasi dampak kesalahan aplikasi atau serangan yang mencoba menghabiskan resource, sekaligus membantu efisiensi penggunaan sumber daya dan memudahkan pengelolaan serta penjadwalan container oleh sistem orkestrasi seperti Kubernetes.
2. Apa perbedaan VM dan container dalam konteks isolasi resource? 
   **Jawaban:**
   ## Perbedaan Isolasi Resource antara VM dan Container

| Aspek | Virtual Machine (VM) | Container |
|-------|--------------------|-----------|
| Isolasi Resource | Tinggi, setiap VM memiliki sistem operasi sendiri dan alokasi CPU, memori, storage terpisah | Lebih ringan, berbagi kernel host, isolasi melalui cgroups dan namespace |
| Sistem Operasi | Setiap VM menjalankan Guest OS lengkap | Berbagi Host OS, hanya aplikasi dan dependensi yang terisolasi |
| Efisiensi | Lebih berat, memerlukan lebih banyak resource | Lebih ringan, efisien, startup lebih cepat |
| Dampak Gangguan | Gangguan pada satu VM jarang memengaruhi VM lain | Gangguan pada satu container bisa berisiko ke host jika ada celah kernel |
| Fleksibilitas | Lebih rigid, resource dialokasikan statis | Lebih fleksibel, resource bisa dibatasi atau diubah secara dinamis |
| Keamanan | Tinggi karena isolasi lengkap | Sedang, bergantung pada keamanan kernel host |

3. Apa dampak limit memori terhadap aplikasi yang boros memori? 
   **Jawaban:**  
- Dampak Limit Memori terhadap Aplikasi yang Boros Memori

1. **Aplikasi Melambat Secara Bertahap**  
   - Saat penggunaan memori mendekati limit, sistem atau runtime (misal Java GC) melakukan pembersihan memori lebih sering.  
   - Garbage collection menjadi lebih lama dan mengonsumsi CPU, sehingga aplikasi lambat dan responsif menurun.

2. **Alokasi Memori Gagal**  
   - Permintaan memori baru (misal `malloc` atau `new`) gagal jika limit tercapai.  
   - Aplikasi bisa menampilkan error "Out of Memory" dan beberapa fungsi berhenti bekerja.

3. **Aplikasi Diberhentikan Paksa (OOM Kill)**  
   - Pada container (Docker/Kubernetes), jika melebihi limit, container dihentikan dengan status `OOMKilled`.  
   - Di Linux, OOM Killer memilih proses berdasarkan skor tertentu, menyebabkan aplikasi mati tiba-tiba dan downtime.

4. **Restart Loop (Siklus Restart Berulang)**  
   - Jika ada mekanisme auto-restart, aplikasi terus restart dan kembali boros memori hingga mati lagi.  
   - Mengakibatkan service tidak stabil dan uptime rendah.

5. **Data Loss atau Corruption**  
   - Termination paksa dapat menghilangkan data yang belum tersimpan.  
   - Transaksi, koneksi database, atau file handle bisa tidak tertutup dengan benar.

6. **Dampak pada Sistem Lain (Noisy Neighbor)**  
   - Aplikasi boros memori bisa memengaruhi performa aplikasi lain di host yang sama.  
   - Jika ada swapping, performa sistem secara keseluruhan menurun.

7. **Kesulitan Debugging**  
   - Crash akibat OOM sulit dideteksi karena memori sudah hilang.  
   - Log biasanya hanya menunjukkan "killed by OOM", memerlukan profiling untuk menemukan kebocoran.

- Solusi Umum
  - Atur limit memori sesuai kebutuhan aplikasi.  
  - Gunakan monitoring dan alerting untuk memantau penggunaan memori.  
  - Optimasi kode untuk mengurangi penggunaan memori (hindari memory leak, gunakan struktur data efisien).  
  - Lakukan stress testing untuk memahami perilaku aplikasi di bawah beban tinggi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
