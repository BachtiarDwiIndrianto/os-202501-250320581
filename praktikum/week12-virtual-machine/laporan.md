
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine

---

## Identitas
- **Nama**  : Bachtiar Dwi Indrianto
- **NIM**   : 250320581
- **Kelas** : 1DSRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.
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

### **1.Instalasi Virtual Machine**
<img width="980" height="691" alt="Screenshot 2026-01-08 234736" src="https://github.com/user-attachments/assets/d5e4b811-9490-463d-8580-39015c028689" />


### **2.Proses konfigurasi virtual machine**
<img width="979" height="689" alt="Screenshot 2026-01-08 223141" src="https://github.com/user-attachments/assets/0aa3047e-20fe-4b12-837e-3a0bcb51dcbe" />

### **3.Instalasi Sistem Operasi OS Guest(UBUNTU)**
<img width="980" height="691" alt="Screenshot 2026-01-08 225030" src="https://github.com/user-attachments/assets/f6b34e66-e4de-4185-8998-5e4b2035563b" />

### **4.Instalasi Berhasil**
<img width="1919" height="1079" alt="Screenshot 2026-01-08 224528" src="https://github.com/user-attachments/assets/d5b0446c-2f1d-48ee-a8f0-144dd395cbab" />

### **5.Os Guest (CPU 1 CORE,RAM 2 GB,DISK SIZE 20 GB)**
<img width="1919" height="1079" alt="Screenshot 2026-01-08 231745" src="https://github.com/user-attachments/assets/2b620f88-7b5e-420d-8590-ed7e3d89d717" />

### **6.Os Guest (CPU 2 CORE,RAM 4 GB,DISK SIZE 20 GB)**
<img width="1919" height="1079" alt="Screenshot 2026-01-08 220027" src="https://github.com/user-attachments/assets/2d22577a-0263-4114-9da2-809b2585c1bc" />


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
1.  Apa perbedaan antara host OS dan guest OS? 
   **Jawaban:**
    ## Perbedaan Host OS dan Guest OS

| Aspek | Host OS (Sistem Operasi Induk) | Guest OS (Sistem Operasi Tamu) |
|------|-------------------------------|--------------------------------|
| Lokasi | Berjalan langsung di hardware fisik (laptop/server) | Berjalan di dalam Virtual Machine (VM) |
| Kontrol | Mengontrol seluruh hardware komputer | Mengontrol virtual hardware yang diberikan |
| Performa | Maksimal karena akses langsung ke hardware | Lebih lambat karena melalui lapisan virtualisasi |
| Contoh | Windows di laptop, Linux di server fisik | Ubuntu di VMware, Windows di VirtualBox |
| Fungsi | Menjalankan komputer dan software virtualisasi | Menjalankan OS seperti komputer terpisah di dalam VM |
| Instalasi | Diinstal langsung ke hardware | Diinstal ke dalam virtual machine |
| Akses Hardware | Akses langsung ke CPU, RAM, dan disk | Akses terbatas melalui virtual hardware |
| Tanggung Jawab | Mengelola semua VM dan aplikasi host | Mengelola sistem dan aplikasi di dalam VM |

2. Apa peran hypervisor dalam virtualisasi?   
   **Jawaban:**
     - Peran Hypervisor dalam Virtualisasi (Sederhana)

| Peran | Deskripsi Sederhana | Analogi |
|------|--------------------|---------|
| Pembagi Resource | Membagi CPU, RAM, dan disk fisik ke beberapa VM | Seperti bendahara yang membagi uang ke anak kos |
| Penerjemah | Menerjemahkan perintah dari VM ke bahasa hardware | Seperti penerjemah dalam meeting internasional |
| Penjaga Keamanan | Mengisolasi VM agar tidak saling mengganggu | Seperti tembok apartemen antar kamar |
| Pengatur Lalu Lintas | Mengatur giliran akses VM ke hardware | Seperti lampu lalu lintas di persimpangan |
| Administrator | Membuat, menghapus, memindahkan, dan membackup VM | Seperti manajer gedung yang mengatur penyewa |

3. Mengapa virtualisasi meningkatkan keamanan sistem?   
   **Jawaban:**  
- **Isolasi**
  - Setiap Virtual Machine (VM) berjalan terpisah.
  - Serangan pada satu VM tidak langsung memengaruhi VM lain atau host.

- **Kontainmen**
  - Insiden keamanan dapat dikarantina dalam satu VM.
  - Sistem lain tetap berjalan normal.

- **Snapshot dan Rollback**
  - VM dapat dikembalikan ke kondisi aman dengan cepat.
  - Mengurangi waktu pemulihan setelah serangan.

- **Pengujian dan Pembaruan**
  - Patch dan update dapat diuji di VM terpisah.
  - Tidak berisiko merusak sistem produksi.

- **Segregasi Jasa**
  - Setiap layanan dijalankan pada VM berbeda.
  - Mengurangi dampak jika satu layanan dikompromikan.

- **Keamanan Fisik dan Logis**
  - Konsolidasi server mengurangi jumlah perangkat fisik.
  - Kontrol akses antar VM lebih mudah diatur.

- **Keamanan Jaringan**
  - Mendukung kebijakan keamanan detail seperti mikro-segmentasi.
  - Membatasi pergerakan lateral ancaman.

- **Penggunaan Hypervisor yang Aman**
  - Hypervisor menambah lapisan keamanan tambahan.
  - Konfigurasi yang baik sangat penting untuk mencegah serangan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
