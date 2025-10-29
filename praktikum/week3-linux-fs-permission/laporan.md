
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Bachtiar Dwi Indrianto]  
- **NIM**   : [250320581]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
Menggunakan chmod dan chown untuk manajemen hak akses file.
Menjelaskan hasil output dari perintah Linux dasar.
Menyusun laporan praktikum dengan struktur yang benar.
Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
## 🧠 Dasar Teori

1. **Sistem File dan Hak Akses di Linux**  
   Linux menggunakan sistem file yang dilengkapi dengan pengaturan izin (permission) untuk menjaga keamanan dan privasi pengguna.  
   Setiap file dan direktori memiliki pemilik (user), grup, dan hak akses tertentu.

2. **Konsep Permission (r, w, x)**  
   Hak akses pada Linux terbagi menjadi tiga jenis utama:
   - **r (read)** → izin untuk membaca isi file atau melihat isi direktori.  
   - **w (write)** → izin untuk mengedit, menambah, atau menghapus isi file/direktori.  
   - **x (execute)** → izin untuk menjalankan file (jika executable) atau membuka direktori.

3. **Perintah `chmod` (Change Mode)**  
   Digunakan untuk **mengubah hak akses** file atau folder.  
   Contoh:
   ```bash
   chmod 755 file.sh
4.Perintah chown (Change Owner)
Digunakan untuk mengubah pemilik atau grup dari sebuah file atau direktori.
Contoh:

chown budi:staff laporan.txt


Maka file laporan.txt sekarang dimiliki oleh user budi dengan grup staff.

5.Tujuan Pengaturan Izin dan Kepemilikan
Pengaturan permission dan kepemilikan penting untuk:

Menjaga keamanan sistem.

Mencegah akses tidak sah dari pengguna lain.

Mengatur kontrol penuh terhadap file sesuai peran pengguna.
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
<img width="1917" height="984" alt="Screenshot 2025-10-22 171349" src="https://github.com/user-attachments/assets/d81d6adc-d0d2-414f-97aa-bd04f4ca4134" />

## Analisis
- Jelaskan makna hasil percobaan.
  ## 🔍 Makna Percobaan

Percobaan ini menunjukkan bagaimana sistem operasi Linux mengatur hak akses dan kepemilikan file agar setiap pengguna hanya bisa melakukan tindakan tertentu sesuai izin yang diberikan.

Dengan mencoba perintah **`chmod`**, kita belajar bahwa:
- Linux memiliki sistem izin yang sangat ketat dan terstruktur.
- Setiap file atau folder bisa diatur siapa yang boleh membaca (`r`), menulis (`w`), atau menjalankan (`x`).
- Kesalahan pengaturan izin bisa menyebabkan file tidak bisa dijalankan atau bahkan tidak bisa dibaca.

Sementara dari perintah **`chown`**, kita memahami bahwa:
- File di Linux selalu memiliki **pemilik (user)** dan **grup**.
- Kepemilikan ini bisa diubah untuk menyesuaikan kebutuhan sistem atau manajemen pengguna.
- Dengan mengatur kepemilikan dan izin dengan benar, administrator bisa menjaga keamanan dan kestabilan sistem.

Secara keseluruhan, percobaan ini menegaskan pentingnya **manajemen hak akses** dalam sistem operasi.  
Tujuannya bukan hanya untuk membatasi, tetapi juga untuk **melindungi data, mencegah kesalahan pengguna lain, dan menjaga integritas sistem Linux.**
 
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
  ## 🔗 Hubungan Hasil dengan Teori

Hasil percobaan penggunaan perintah `chmod` dan `chown` berkaitan erat dengan teori **fungsi kernel**, **system call**, dan **arsitektur sistem operasi**.

1. **Hubungan dengan Fungsi Kernel**  
   Kernel berperan sebagai pengatur utama sumber daya sistem, termasuk pengelolaan file dan keamanan.  
   Saat kita menjalankan `chmod` atau `chown`, kernel bertugas **memverifikasi hak akses** dan **mengubah metadata file** di sistem file.  
   Artinya, setiap perubahan izin atau kepemilikan sebenarnya adalah instruksi yang dikirim ke kernel untuk memodifikasi informasi file di tingkat sistem.

2. **Hubungan dengan System Call**  
   Kedua perintah ini (`chmod`, `chown`) bekerja melalui **system call** — yaitu mekanisme komunikasi antara program pengguna (user space) dan kernel (kernel space).  
   Contohnya:
   - `chmod` memanggil system call `chmod()` untuk mengubah mode akses file.  
   - `chown` memanggil system call `chown()` untuk mengganti pemilik dan grup file.  
   Dengan demikian, hasil yang terlihat di terminal sebenarnya adalah **hasil dari proses system call yang berhasil dijalankan oleh kernel.**

3. **Hubungan dengan Arsitektur Sistem Operasi**  
   Dalam arsitektur OS, perintah dari user dijalankan di **user space**, sedangkan kernel menangani tugas berat di **kernel space**.  
   Saat pengguna mengetik `chmod` atau `chown`, perintah tersebut dieksekusi oleh **shell**, kemudian diteruskan ke kernel melalui system call.  
   Proses ini menunjukkan bagaimana **lapisan-lapisan OS bekerja sama**:  
   - **User layer**: pengguna memberikan perintah  
   - **Shell layer**: menerjemahkan perintah menjadi instruksi sistem  
   - **Kernel layer**: mengeksekusi perubahan di sistem file  

Dengan demikian, percobaan ini memperlihatkan bagaimana teori arsitektur sistem operasi dan mekanisme system call **terwujud secara nyata** melalui pengaturan izin dan kepemilikan file menggunakan `chmod` dan `chown`.
 
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Di Linux, manajemen hak akses bersifat lebih terbuka dan fleksibel lewat terminal.

Di Windows, pengaturannya lebih terpusat dan berbasis antarmuka grafis (GUI), dengan struktur izin yang berbeda.

Perintah chmod dan chown tidak bisa digunakan langsung di Windows, kecuali lewat subsistem Linux seperti WSL (Windows Subsystem for Linux).
---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
## ✅ Kesimpulan

1. Perintah `chmod` digunakan untuk **mengatur izin akses** (read, write, execute) terhadap file atau folder agar hanya pengguna tertentu yang bisa membacanya, mengubahnya, atau menjalankannya.  
2. Perintah `chown` berfungsi untuk **mengubah kepemilikan** file atau direktori, baik pemilik utama (user) maupun grupnya.  
3. Melalui percobaan ini, dapat disimpulkan bahwa sistem operasi Linux memiliki mekanisme manajemen hak akses yang **lebih transparan dan terstruktur** dibandingkan sistem operasi lain seperti Windows.

---

## Quiz
1. [Apa fungsi dari perintah chmod?]  
   **Jawaban:**  chmod adalah perintah di Linux yang dipakai untuk mengatur izin akses file atau folder — siapa yang boleh melihat, mengubah, atau menjalankan file tersebut.
2. [Apa arti dari kode permission rwxr-xr--?]  
   **Jawaban:**  # 🔐 Arti Kode Permission: `rwxr-xr--`

Kode ini menunjukkan izin (permission) pada file atau folder di Linux.

## 🧩 Pembagian Kode
| Bagian | Untuk Siapa | Kode | Arti |
|:-------|:-------------|:------|:-------------------------------------------|
| 1️⃣ | **User (Pemilik)** | `rwx` | Bisa **baca (r)**, **ubah (w)**, dan **jalankan (x)** |
| 2️⃣ | **Group (Kelompok)** | `r-x` | Bisa **baca (r)** dan **jalankan (x)**, tapi **tidak bisa ubah (–)** |
| 3️⃣ | **Others (Orang lain)** | `r--` | Hanya bisa **baca (r)** saja |

---

## 🧠 Kesimpulan
- Pemilik: **bebas melakukan apa saja**
- Grup: **hanya bisa baca & jalankan**
- Orang lain: **hanya bisa baca**

---

## 💡 Nilai Angka (Oktal)
`rwxr-xr--` = **754**

3. [Jelaskan perbedaan antara chown dan chmod?]  
   **Jawaban:**  chmod	Mengatur izin akses file atau folder (siapa yang boleh baca, ubah, jalankan)
chown	Mengubah kepemilikan file atau folder (siapa pemiliknya dan grupnya)

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Pada saat bagian peng operasian ubuntu/linuxnya
- Bagaimana cara Anda mengatasinya?  belajar bersama teman teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
