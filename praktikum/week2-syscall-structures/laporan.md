
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
<img width="1898" height="950" alt="Screenshot 2025-10-22 162516" src="https://github.com/user-attachments/assets/bb204a99-3f41-42ed-9e41-f77970280f55" />
---<img width="1913" height="964" alt="Screenshot 2025-10-22 162353" src="https://github.com/user-attachments/assets/a37ffb18-ae8a-4fdf-a1ca-98711c66cfaa" />
<img width="887" height="210" alt="Screenshot 2025-10-22 162425" src="https://github.com/user-attachments/assets/c97cd7a2-075c-4562-b6ca-c32dcf1a6e42" />

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
