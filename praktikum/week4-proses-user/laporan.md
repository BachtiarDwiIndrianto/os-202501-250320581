
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
Setelah menyelesaikan tugas ini, mahasiswa mampu:  
1.Menjelaskan konsep proses dan user dalam sistem operasi Linux. 
2.Menampilkan daftar proses yang sedang berjalan dan statusnya. 
3.Menggunakan perintah untuk membuat dan mengelola user. 
4.Menghentikan atau mengontrol proses tertentu menggunakan PID. 
5.Menjelaskan kaitan antara manajemen user dan keamanan sistem.

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
  Pada saat pengoprasian linux
- Bagaimana cara Anda mengatasinya?
  Coba coba terus menerus sambil berdiskusi bersama teman teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
