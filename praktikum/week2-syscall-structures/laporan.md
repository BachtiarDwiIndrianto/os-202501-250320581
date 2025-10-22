
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
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Sistem Operasi (Operating System)
Sistem operasi adalah perangkat lunak sistem yang berfungsi sebagai penghubung antara pengguna dan perangkat keras komputer. Sistem operasi mengelola sumber daya seperti prosesor, memori, penyimpanan, dan perangkat input/output agar dapat digunakan secara efisien oleh berbagai program.

Kernel
Kernel merupakan inti dari sistem operasi yang berjalan di mode istimewa (privileged mode). Kernel bertanggung jawab atas manajemen proses, manajemen memori, pengaturan perangkat keras, serta penjadwalan tugas. Kernel juga menyediakan antarmuka bagi program pengguna melalui system call.

System Call
System call adalah mekanisme yang digunakan oleh program aplikasi untuk meminta layanan dari kernel. Dengan system call, aplikasi dapat melakukan operasi penting seperti membaca/menulis file, membuat proses baru, atau berkomunikasi dengan perangkat keras tanpa harus mengakses kernel secara langsung.

Arsitektur Sistem Operasi
Arsitektur sistem operasi umumnya terdiri dari beberapa lapisan: user space, system call interface, dan kernel space. Program aplikasi berjalan di user space dan tidak memiliki akses langsung ke perangkat keras. Semua permintaan terhadap perangkat keras harus melalui system call yang dijalankan di kernel space.

Modularitas Kernel (Kernel Modules)
Kernel modern seperti Linux mendukung modul yang dapat dimuat (loadable modules). Modul ini memungkinkan fungsionalitas kernel (seperti driver perangkat keras) ditambahkan atau dilepaskan secara dinamis tanpa perlu me-restart sistem. Hal ini meningkatkan fleksibilitas dan efisiensi sistem operasi.

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
<img width="1898" height="950" alt="Screenshot 2025-10-22 162516" src="https://github.com/user-attachments/assets/bb204a99-3f41-42ed-9e41-f77970280f55" />
---<img width="1913" height="964" alt="Screenshot 2025-10-22 162353" src="https://github.com/user-attachments/assets/a37ffb18-ae8a-4fdf-a1ca-98711c66cfaa" />
<img width="887" height="210" alt="Screenshot 2025-10-22 162425" src="https://github.com/user-attachments/assets/c97cd7a2-075c-4562-b6ca-c32dcf1a6e42" />

## Analisis
- Jelaskan makna hasil percobaan.
 Makna hasil percobaan
Dari hasil eksekusi perintah:

uname -a menampilkan informasi detail mengenai sistem operasi yang digunakan, termasuk versi kernel dan arsitektur mesin. Hal ini menunjukkan bahwa kernel merupakan inti dari sistem operasi yang menentukan kompatibilitas perangkat keras dan fitur sistem.

lsmod | head menampilkan daftar modul kernel yang sedang aktif. Modul ini berfungsi sebagai komponen tambahan yang dapat dimuat atau dilepas tanpa perlu mem-boot ulang sistem, menunjukkan sifat kernel yang modular dan fleksibel.

dmesg | head menampilkan log pesan kernel, terutama terkait proses booting dan deteksi perangkat keras. Ini membuktikan bahwa kernel secara aktif berinteraksi dengan perangkat keras dan mencatat setiap aktivitas penting untuk tujuan debugging dan pemantauan.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
Hasil praktikum sesuai dengan teori bahwa kernel berperan sebagai penghubung utama antara perangkat keras dan perangkat lunak. Semua interaksi antara program pengguna dan perangkat keras dilakukan melalui system call, bukan secara langsung. System call memberikan mekanisme terkontrol agar proses dapat berjalan aman tanpa mengganggu stabilitas sistem operasi. 
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Pada Linux, sebagian besar system call dan kernel bersifat terbuka (open source) dan dapat diinspeksi langsung oleh pengguna melalui terminal, sedangkan pada Windows, proses tersebut lebih tertutup dan diatur melalui API tingkat tinggi seperti Win32 API. Hal ini membuat Linux lebih transparan untuk pembelajaran sistem operasi, sementara Windows lebih berorientasi pada kenyamanan pengguna.
## Hasil Observasi
**Tabel Observasi Hasil Eksperimen strace**
| No | System Call | Deskripsi Fungsi                                                                               | Keterangan / Hasil Observasi                                                 |
| -- | ----------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 1  | `execve()`  | Menjalankan program baru (dalam hal ini `/usr/bin/ls`) dengan argumen dan variabel lingkungan. | Proses dimulai, sistem menjalankan perintah `ls`.                            |
| 2  | `brk()`     | Mengatur batas ruang memori proses untuk alokasi dinamis (heap).                               | Kernel menyesuaikan memori yang dibutuhkan program.                          |
| 3  | `mmap()`    | Memetakan file atau perangkat ke memori virtual proses.                                        | Digunakan untuk mengalokasikan ruang memori tambahan.                        |
| 4  | `access()`  | Mengecek izin akses terhadap file tertentu.                                                    | Mengecek file konfigurasi `/etc/ld.so.preload`, hasilnya tidak ada (ENOENT). |
| 5  | `openat()`  | Membuka file pada direktori tertentu.                                                          | Membuka file cache library `/etc/ld.so.cache` untuk mencari dependensi.      |
| 6  | `fstat()`   | Mengambil informasi status file yang dibuka.                                                   | Mengecek ukuran dan tipe file cache library.                                 |
| 7  | `mmap()`    | Memetakan isi file yang dibuka ke memori.                                                      | Agar lebih efisien dalam membaca data library.                               |
| 8  | `close()`   | Menutup file descriptor setelah digunakan.                                                     | File cache ditutup setelah selesai dibaca.                                   |
| 9  | `read()`    | Membaca data dari file descriptor.                                                             | Membaca header ELF library yang dibuka.                                      |
| 10 | `openat()`  | Membuka library lain seperti `libselinux.so.1`.                                                | Program mulai memuat dependensi yang dibutuhkan untuk eksekusi.              |



**Tabel Observasi Hasil Eksperimen dmesg**
| No | Waktu (s) | Pesan Kernel                                                              | Deskripsi / Interpretasi                                                  |
| -- | --------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1  | 2.80      | `systemd-journald[42]: Collecting audit messages is disabled.`            | Kernel mencatat bahwa proses logging audit tidak diaktifkan.              |
| 2  | 2.91      | `systemd-journald[42]: Received client request to flush runtime journal.` | Sistem logging menerima permintaan untuk membersihkan log sementara.      |
| 3  | 2.91      | `File /var/log/journal/... corrupted or uncleanly shut down`              | Kernel mendeteksi log sebelumnya rusak dan menggantinya dengan yang baru. |
| 4  | 3.13      | `ACPI: battery: Slot [BAT1] (battery present)`                            | Kernel mendeteksi keberadaan baterai pada perangkat.                      |
| 5  | 3.14      | `ACPI: AC Adapter [AC1] (off-line)`                                       | Adaptor daya sedang tidak tersambung.                                     |
| 6  | 3.48      | `kvm_intel: Using Hyper-V Enlightened VMCS`                               | Kernel mendeteksi sistem berjalan di lingkungan virtual (WSL/Hyper-V).    |
| 7  | 6.00      | `systemd-journald: user-1000.journal rotating`                            | Kernel melakukan rotasi file log pengguna.                                |
| 8  | 6.01      | `TCP: eth0: Driver has suspect GRO implementation`                        | Kernel memberi peringatan terkait performa jaringan.                      |
| 9  | 6.34      | `WSL (214) ERROR: CheckConnection: getaddrinfo() failed`                  | Kernel WSL gagal melakukan resolve jaringan.                              |
| 10 | 48.47     | `hv_balloon: Max. dynamic memory size: 4024 MB`                           | Kernel melaporkan batas maksimum memori dinamis yang dialokasikan di WSL. |


---

## Kesimpulan
1. Apa fungsi utama system call dalam sistem operasi?  
   **Jawaban:**
   **Fungsi utama system call adalah sebagai penghubung antara program pengguna (user space) dengan kernel (system space) agar aplikasi dapat meminta layanan dari sistem operasi seperti membaca atau menulis file, mengalokasikan memori, membuat proses baru, atau berkomunikasi dengan perangkat keras. System call memungkinkan interaksi ini dilakukan dengan aman dan terkontrol tanpa memberi akses langsung kepada user terhadap sumber daya kernel.**
     
2. Sebutkan 4 kategori system call yang umum digunakan.  
   **Jawaban:**
   **Empat kategori utama system call yang umum digunakan dalam sistem operasi adalah:**
**1.	Process Control – untuk membuat, menghentikan, dan mengatur proses (contoh: fork(), execve(), exit(), wait()).**
**2.	File Management – untuk operasi file seperti membuka, membaca, menulis, atau menutup file (contoh: open(), read(), write(), close()).**
**3.	Device Management – untuk mengontrol dan mengakses perangkat input/output (contoh: ioctl(), read(), write()).**
**4.	Information Maintenance – untuk mendapatkan atau mengatur informasi sistem (contoh: getpid(), uname(), gettimeofday()).**

3. Mengapa system call tidak bisa dipanggil langsung oleh user program? 
   **Jawaban:**
   **System call tidak dapat dipanggil langsung oleh program pengguna karena berjalan di tingkat kernel (privileged mode), sedangkan program biasa berjalan di user mode. Hal ini bertujuan untuk menjaga keamanan dan stabilitas sistem operasi, agar pengguna tidak bisa mengakses atau mengubah sumber daya kernel secara langsung yang dapat menyebabkan kerusakan sistem, kebocoran data, atau crash. Oleh karena itu, program hanya dapat memanggil system call melalui antarmuka API yang disediakan oleh sistem operasi (misalnya pustaka C glibc di Linux).**

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?  
   **Jawaban:**
   **Fungsi utama system call adalah sebagai penghubung antara program pengguna (user space) dengan kernel (system space) agar aplikasi dapat meminta layanan dari sistem operasi seperti membaca atau menulis file, mengalokasikan memori, membuat proses baru, atau berkomunikasi dengan perangkat keras. System call memungkinkan interaksi ini dilakukan dengan aman dan terkontrol tanpa memberi akses langsung kepada user terhadap sumber daya kernel.**
     
2. Sebutkan 4 kategori system call yang umum digunakan.  
   **Jawaban:**
   **Empat kategori utama system call yang umum digunakan dalam sistem operasi adalah:**
**1.	Process Control – untuk membuat, menghentikan, dan mengatur proses (contoh: fork(), execve(), exit(), wait()).**
**2.	File Management – untuk operasi file seperti membuka, membaca, menulis, atau menutup file (contoh: open(), read(), write(), close()).**
**3.	Device Management – untuk mengontrol dan mengakses perangkat input/output (contoh: ioctl(), read(), write()).**
**4.	Information Maintenance – untuk mendapatkan atau mengatur informasi sistem (contoh: getpid(), uname(), gettimeofday()).**

3. Mengapa system call tidak bisa dipanggil langsung oleh user program? 
   **Jawaban:**
   **System call tidak dapat dipanggil langsung oleh program pengguna karena berjalan di tingkat kernel (privileged mode), sedangkan program biasa berjalan di user mode. Hal ini bertujuan untuk menjaga keamanan dan stabilitas sistem operasi, agar pengguna tidak bisa mengakses atau mengubah sumber daya kernel secara langsung yang dapat menyebabkan kerusakan sistem, kebocoran data, atau crash. Oleh karena itu, program hanya dapat memanggil system call melalui antarmuka API yang disediakan oleh sistem operasi (misalnya pustaka C glibc di Linux).**


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  Tentu pada saat di ubuntu pada saat percobaan karena masih awam dan sering salah kode.
- Bagaimana cara Anda mengatasinya?  
Saya belajar dengan teman yang sudah bisa dan bertanya ke AI.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
