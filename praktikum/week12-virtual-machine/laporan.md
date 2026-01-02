
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
