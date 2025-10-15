
# Laporan Praktikum Minggu [X]
Topik: ["Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [BACHTIAR DWI INDRIANTO]  
- **NIM**   : [250320581]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Sistem operasi adalah perangkat lunak yang mengontrol dan mengatur perangkat keras komputer serta menjalankan program aplikasi. Sistem ini bertindak sebagai penghubung antara pengguna dengan perangkat keras (system call), memungkinkan komputer berfungsi dan program dapat berjalan dengan baik, dengan bagian terpenting nya adalah kernel yang mengelolah sumber daya CPU,Memory,Storage (hardisk) dan I/O
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
hasil percobaan 
<img width="1184" height="665" alt="bachtiar" src="https://github.com/user-attachments/assets/8017a3a1-78e6-4b7f-b6df-46c072f1c7e5" />


---

## Analisis
- Jelaskan makna hasil percobaan.
  uname -a adalah perintah di Linux yang digunakan untuk menampilkan semua informasi detail tentang sistem, termasuk nama kernel, nama mesin.
Perintah 1smod digunakan untuk menampilkan daftar modul kernel yang saat ini sedang dimuat (loaded) di sistem.

Modul kernel ini bisa berupa driver perangkat keras atau modul fungsional lainnya yang digunakan oleh kernel Linux Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
  Hasil dapat dihubungkan dengan fungsi kernel sebagai inti sistem operasi yang menjembatani hardware dan software; panggilan sistem ((syscall)) sebagai jembatan antara aplikasi pengguna dan kernel untuk meminta layanan; dan arsitektur OS yang mendefinisikan struktur ini, di mana kernel menjadi komponen sentral yang mengelola sumber daya melalui panggilan sistem.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Perbedaan hasil antara Linux dan Windows terlihat dari struktur sistem file (garis miring / di Linux vs "C:\ di Windows), cara penamaan berkas (bisa ada dua berkas dengan nama sama di direktori berbeda di Linux, tidak bisa di Windows), sistem partisi (Linux lebih fleksibel, Windows mendukung partisi Linux namun Linux belum tentu mendukung partisi Windows), dan penggunaan baris perintah (terminal di Linux lebih ampuh, cmd di Windows lebih terbatas
---

## Kesimpulan
Monolithic kernel adalah arsitektur sistem operasi di mana semua layanan inti OS, seperti manajemen memori, penjadwalan proses, dan manajemen perangkat keras, berjalan dalam satu ruang alamat (satu program besar) bagian dapat menyebabkan crash seluruh. Mikrokernel adalah jenis kernel sistem operasi yang hanya berisi fungsionalitas inti minimal, seperti manajemen memori dan komunikasi antarproses (IPC), sementara layanan lainnya (seperti driver perangkat dan sistem berkas) berjalan di ruang pengguna Arsitektur berlapis (layered architecture) adalah pola desain perangkat lunak yang membagi aplikasi menjadi beberapa lapisan terpisah, di mana setiap lapisan memiliki tanggung jawab tertentu dan hanya berinteraksi dengan lapisan di bawahnya, sebagai server terpisah.

---

## Quiz
1. [Sebutkan tiga fungsi utama sistem operasi]  
   **Jawaban:**  FUNGSI UTAMA SISTEM OPERASI
1.	Manajemen Proses
•	Mengatur dan mengelola proses yang sedang berjalan.
•	Membagi tugas pada CPU agar proses dapat berjalan efisien.
2.	Manajemen Memori
•	Mengelola penggunaan memori secara optimal agar program dapat berjalan tanpa gangguan.
•	Menyediakan ruang memori untuk setiap aplikasi yang dijalankan.
3.	Manajemen Perangkat Keras
•	Sistem operasi mengontrol perangkat keras seperti printer, monitor, dan keyboard.
•	Menyediakan driver untuk setiap perangkat agar dapat digunakan oleh aplikasi.

3. [Jelaskan perbedaan antara kernel mode dan user mode]  
   **Jawaban:**  PERBEDAAN KERTEL MODE DAN USER MODE
1.	Akses ke Sumber Daya: Kernel mode memiliki akses langsung dan penuh, sementara user mode memiliki akses terbatas.
2.	Keamanan: User mode melindungi sistem dari aplikasi yang salah atau jahat dengan membatasi apa yang bisa mereka lakukan.
3.	Switching: Proses berpindah dari user mode ke kernel mode melalui interrupt atau system call, dan sebaliknya.
4.	Contoh: Kernel mode digunakan untuk driver perangkat, manajemen memori; user mode untuk aplikasi seperti browser web atau editor teks.

4. [Sebutkan contoh OS dengan arsitektur monolithic dan microkernel]  
   **Jawaban:**  Contoh OS dengan arsitektur monolithic dan microkernel.
1.Monolithic yaitu Linux,Unix,Windows,Mac OS
2.Microkernel yaitu Minix,QNX,L4,Mach


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  Yang cukup bagian linux ubuntu nya karena baru pertama kali dan cukup kaget sehingga kesulitan  
- Bagaimana cara Anda mengatasinya?  
  Menonton youtube dan melihat tutorial di berbagai vidio,serta menanya nanya keteman teman
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
