
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine

---
## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari konsep **virtualisasi sistem operasi** dengan menggunakan **Virtual Machine (VM)**.  
Mahasiswa diarahkan untuk menginstal dan menjalankan sistem operasi guest di atas host OS menggunakan perangkat lunak virtualisasi seperti **VirtualBox** atau **VMware**.

Praktikum ini menekankan pemahaman hubungan antara **host OS**, **guest OS**, dan **hypervisor**, serta bagaimana konfigurasi resource (CPU, memori, dan storage) memengaruhi kinerja dan isolasi sistem.

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
Virtualisasi adalah teknik yang memungkinkan pembuatan beberapa mesin virtual di atas satu komputer fisik, sehingga sumber daya seperti CPU, RAM, dan penyimpanan dapat dibagi untuk menjalankan lebih dari satu sistem operasi secara bersamaan. Hypervisor berperan sebagai pengelola yang mengatur alokasi sumber daya dan mengisolasi setiap mesin virtual, meningkatkan keamanan karena masalah pada satu mesin tidak menyebar ke lainnya. Selain itu, virtualisasi memungkinkan pengaturan sumber daya secara fleksibel (seperti menambah core CPU atau RAM) serta memudahkan proses migrasi, cadangan, dan pemulihan sistem.


---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
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
- Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.

Virtual Machine (VM) membuat sistem operasi guest berjalan terpisah dari sistem operasi host. Pemisahan ini diatur oleh hypervisor, yang mengontrol penggunaan CPU, RAM, dan storage.Karena berjalan di lingkungan terisolasi, masalah atau error pada guest OS tidak langsung memengaruhi host OS. Dengan cara ini, VM membantu menjaga keamanan dan kestabilan sistem.

- Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

   - Sandboxing
     Virtual Machine menerapkan konsep sandboxing dengan menjalankan sistem operasi guest dalam lingkungan virtual yang terisolasi dari sistem operasi host. Isolasi ini dikendalikan oleh hypervisor yang membatasi akses guest OS terhadap sumber daya hardware, sehingga kesalahan sistem, kegagalan aplikasi, maupun serangan keamanan pada guest OS tidak berdampak langsung pada host OS.

   - Hardening OS
     Virtual Machine mendukung hardening sistem operasi dengan memisahkan layanan atau aplikasi ke dalam mesin virtual yang berbeda. Pemisahan ini bertujuan untuk mengurangi permukaan serangan (attack surface) dan membatasi dampak apabila terjadi kompromi pada salah satu sistem, sehingga keamanan dan stabilitas sistem secara keseluruhan dapat ditingkatkan.


---

## Kesimpulan
**Kesimpulan Praktikum Virtualisasi**

1. Berhasil menguasai instalasi dan konfigurasi VM – Praktikum ini berhasil membuktikan kemampuan dalam menginstal perangkat lunak virtualisasi (VirtualBox), membuat mesin virtual, serta menginstal dan menjalankan sistem operasi guest (Ubuntu) di dalam lingkungan virtual.

2. Mampu mengatur alokasi sumber daya secara dinamis – Pengaturan konfigurasi resource VM (seperti CPU, RAM, dan storage) dapat dilakukan dengan fleksibel sesuai kebutuhan, sekaligus memahami dampak perubahan konfigurasi terhadap performa host dan guest.

3. Memahami mekanisme isolasi dan keamanan melalui virtualisasi – Virtualisasi memberikan lapisan isolasi yang kuat antara host dan guest OS, sekaligus menjadi fondasi untuk penerapan prinsip sandboxing dan hardening dalam meningkatkan keamanan sistem.

4. Keterampilan dokumentasi dan analisis – Melalui penyusunan laporan praktikum yang sistematis beserta analisis hasil, kemampuan dalam mendokumentasikan proses teknis dan merefleksikan pembelajaran dapat semakin terasah.

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
 Proses instalasi sistem operasi guest pada Virtual Machine, terutama saat terjadi kegagalan instalasi akibat pengaturan virtualisasi dan konfigurasi resource yang belum sesuai.
- Bagaimana cara Anda mengatasinya?
  Memeriksa kembali pengaturan BIOS, memastikan fitur virtualisasi aktif, serta menyesuaikan konfigurasi RAM, CPU, dan storage pada mesin virtual hingga sistem dapat berjalan dengan normal.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
