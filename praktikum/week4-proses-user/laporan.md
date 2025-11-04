
# Laporan Praktikum Minggu [X]
Topik: [Manajemen Proses dan User di Linux]

---

## Identitas
- **Nama**  : [Bachtiar Dwi Indrianto]  
- **NIM**   : [250320581]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:  
1.Menjelaskan konsep proses dan user dalam sistem operasi Linux. 
2.Menampilkan daftar proses yang sedang berjalan dan statusnya. 
3.Menggunakan perintah untuk membuat dan mengelola user. 
4.Menghentikan atau mengontrol proses tertentu menggunakan PID. 
5.Menjelaskan kaitan antara manajemen user dan keamanan sistem.

## Dasar Teori
1. **Proses di Linux**
   Proses adalah program yang sedang berjalan. Setiap proses punya nomor sendiri (PID) dan diatur oleh sistem agar semua bisa jalan dengan lancar.

2. **User dan Hak Akses**
   Ada dua jenis user di Linux: user biasa dan user root.
   User root punya hak penuh untuk mengatur sistem, sedangkan user biasa hanya bisa menjalankan program.

3. **Systemd dan Kernel**
   `systemd` adalah proses pertama yang aktif saat Linux dinyalakan, sedangkan **kernel** adalah inti sistem yang menghubungkan pengguna dengan perangkat keras.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="935" height="601" alt="Screenshot 2025-11-03 214842" src="https://github.com/user-attachments/assets/b17fdccd-914f-4305-9426-32e86960112e" />
<img width="1919" height="1077" alt="Screenshot 2025-11-03 215054" src="https://github.com/user-attachments/assets/98b86f5d-3e72-4511-93d2-36181881acbe" />
 Penjelasan Kolom Penting di Linux

- **PID** → Nomor unik buat setiap proses yang sedang jalan.  
  (Ibarat nomor identitas tiap program.)

- **USER** → Nama orang (user) yang menjalankan proses itu.  
  Misalnya `root`, `ubuntu`, atau nama akun kamu sendiri.

- **%CPU** → Menunjukkan seberapa banyak CPU yang dipakai proses itu.  
  Kalau angkanya tinggi, berarti prosesnya lagi berat kerja.

- **%MEM** → Menunjukkan seberapa banyak RAM yang dipakai.  
  Kalau tinggi, proses itu makan banyak memori.

- **COMMAND** → Nama program atau perintah yang lagi dijalankan.  
  Misalnya `firefox`, `bash`, `code`, dan lainnya.

<img width="954" height="203" alt="Screenshot 2025-11-04 222936" src="https://github.com/user-attachments/assets/f15941dd-5c07-4485-ab38-9f71f727f23d" />
<img width="954" height="592" alt="Screenshot 2025-11-03 235937" src="https://github.com/user-attachments/assets/153def59-3a4f-4156-8ccf-8e0901b228ca" />

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Dari praktikum ini, saya jadi paham kalau **setiap kegiatan di Linux itu dijalankan lewat proses** dan setiap proses dikendalikan oleh user tertentu.
2. Saya belajar cara **melihat, mengatur, dan menghentikan proses** dengan perintah seperti `ps`, `kill`, dan `killall`.
3. Saya juga tahu kalau **user root** adalah pengguna utama yang punya hak penuh untuk mengatur sistem, dan **systemd/init** adalah proses pertama yang mengatur jalannya semua layanan di Linux.
4. Secara keseluruhan, praktikum ini membuat saya lebih mengerti bagaimana **Linux bekerja dari dalam**, mulai dari proses dijalankan sampai sistem bisa digunakan dengan aman.

---

## Quiz
1. [Apa fungsi dari proses init atau systemd dalam sistem Linux?]  
   Fungsi init dan systemd dalam linux
- Menjalankan proses pertama setelah sistem dinyalakan  
- Menyiapkan lingkungan sistem (mount disk, aktifkan jaringan, dll)  
- Mengatur dan mengawasi semua proses dan layanan  
- Menentukan mode kerja sistem (teks, GUI, atau pemeliharaan)  
- Mengelola proses shutdown dan reboot agar aman  
- Menjadi induk dari semua proses di sistem

2. [Apa perbedaan antara kill dan killall?]  
Perbedaan `kill` dan `killall`

- **`kill`** → menghentikan **satu proses** berdasarkan **PID (nomor proses)**  
 Contoh: `kill 1234`

- **`killall`** → menghentikan **semua proses** dengan **nama yang sama**  
 Contoh: `killall firefox`

**Intinya:**  
`kill` = pakai nomor proses  
`killall` = pakai nama program

3. [Mengapa user root memiliki hak istimewa di sistem Linux?]  
User **root** di Linux itu seperti **bos besar** dari sistem.  
Dia punya **hak penuh** untuk melakukan apa saja, misalnya:
- Mengedit atau menghapus file apa pun  
- Menambah atau menghapus pengguna  
- Menginstal atau menghapus program  
- Mengubah pengaturan sistem
Akun ini dibuat supaya ada satu pengguna yang bisa **mengatur dan memperbaiki seluruh sistem** tanpa batasan.

`root` adalah pengguna tertinggi yang **mengontrol semua hal di Linux.**


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
 Bagian yang paling susah itu waktu cari dan matiin proses, karena harus teliti lihat PID-nya.
- Bagaimana cara Anda mengatasinya?
  Coba coba terus menerus sambil berdiskusi bersama teman teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
