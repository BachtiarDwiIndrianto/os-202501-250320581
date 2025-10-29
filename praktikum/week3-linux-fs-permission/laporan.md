
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
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
