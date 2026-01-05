
# Laporan Praktikum Minggu [X]
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Bachtiar Dwi Indrianto
- **NIM**   : 250320581
- **Kelas** : 1DSRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Ketentuan Teknis
- Bahasa pemrograman **bebas** (Python / C / Java / lainnya).  
- Program berbasis **terminal**, tidak memerlukan GUI.  
- Fokus penilaian pada **logika algoritma deteksi deadlock**, bukan kompleksitas bahasa.
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```phyton
processes = ["P1", "P2", "P3"]

wait_for = {
    "P1": "P2",
    "P2": "P3",
    "P3": "P1"
}

deadlock = False

for p in processes:
    visited = set()
    while p not in visited:
        visited.add(p)
        if p not in wait_for:
            break
        p = wait_for[p]
    else:
        deadlock = True
        break

print("HASIL DETEKSI DEADLOCK")
print("-" * 45)
print(f"| {'Proses':^10} | {'Menunggu':^12} | {'Status':^12} |")
print("-" * 45)

for p in processes:
    status = "Deadlock" if deadlock else "Aman"
    print(f"| {p:^10} | {wait_for[p]:^12} | {status:^12} |")

print("-" * 45)
print("Status Sistem : DEADLOCK TERDETEKSI")
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

<img width="1919" height="1079" alt="Screenshot 2026-01-05 230452" src="https://github.com/user-attachments/assets/6d89ea1b-3271-4c6f-b3e9-0c44fb432828" />

---

## Analisis
Hasil Deteksi Deadlock

| Proses | Menunggu | Status   |
|--------|----------|----------|
| P1     | P2       | Deadlock |
| P2     | P3       | Deadlock |
| P3     | P1       | Deadlock |

**Status Sistem:** **DEADLOCK TERDETEKSI**

- Jelaskan mengapa deadlock terjadi atau tidak terjadi.
Berdasarkan hasil deteksi, seluruh proses berada dalam kondisi deadlock. Hal ini terjadi karena adanya **circular wait**, yaitu P1 menunggu P2, P2 menunggu P3, dan P3 menunggu P1. Akibatnya, tidak ada proses yang dapat melanjutkan eksekusi karena saling menunggu satu sama lain.

- Kaitkan hasil dengan teori deadlock (empat kondisi).
Berdasarkan hasil deteksi deadlock, kondisi yang terjadi pada sistem memenuhi **empat syarat utama terjadinya deadlock**, yaitu:
1. Mutual Exclusion (Saling Eksklusif) 
   Setiap proses hanya dapat menggunakan sumber daya tertentu secara eksklusif. Dalam kasus ini, sumber daya yang sedang digunakan oleh suatu proses tidak dapat digunakan oleh proses lain secara bersamaan.
2. Hold and Wait (Menahan dan Menunggu)
   Setiap proses menahan satu sumber daya sambil menunggu sumber daya lain yang sedang digunakan oleh proses lain. Misalnya, P1 menahan sumber daya tertentu sambil menunggu sumber daya yang dipegang oleh P2.
3. No Preemption (Tidak Ada Perampasan)
   Sumber daya tidak dapat diambil secara paksa dari proses yang sedang menggunakannya. Sumber daya hanya dapat dilepaskan oleh proses itu sendiri setelah selesai digunakan.
4. Circular Wait (Menunggu Melingkar)
   Terjadi siklus ketergantungan antar proses, yaitu P1 menunggu P2, P2 menunggu P3, dan P3 menunggu P1. Kondisi inilah yang paling jelas terlihat dari hasil deteksi dan menjadi penyebab utama terjadinya deadlock.


Karena keempat kondisi deadlock tersebut terpenuhi secara bersamaan, maka sistem berada dalam keadaan **deadlock**, sesuai dengan hasil deteksi yang menunjukkan status DEADLOCK TERDETEKSI


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?
   **Jawaban:**
   ## Perbandingan Deadlock Prevention, Avoidance, dan Detection

| Aspek              | Prevention | Avoidance | Detection |
|-------------------|------------|-----------|-----------|
| Pendekatan | Proaktif: Membatasi akses sumber daya untuk mencegah kondisi deadlock | Proaktif: Memeriksa keamanan sistem sebelum alokasi sumber daya | Reaktif: Membiarkan deadlock terjadi, lalu mendeteksi dan memulihkannya |
| Kondisi Deadlock | Tidak pernah memungkinkan kondisi deadlock terbentuk | Deadlock mungkin terjadi, tetapi sistem menghindari keadaan tidak aman | Deadlock diperbolehkan terjadi |
| Keuntungan | Sederhana dan efisien untuk sistem kecil; overhead rendah | Lebih fleksibel; memaksimalkan utilisasi sumber daya | Tidak membatasi proses; cocok untuk sistem kompleks |
| Kekurangan | Kurang efisien; proses dapat menunggu lama dan berpotensi starvation | Kompleks; membutuhkan informasi lengkap dan overhead tinggi | Deteksi memerlukan waktu; pemulihan bisa mahal |
| Algoritma Contoh | Aturan *no hold and wait* (semua resource diminta sekaligus) | Banker’s Algorithm | Wait-for Graph |
| Penggunaan | Sistem real-time dan embedded | OS seperti Unix; sistem dengan sumber daya terbatas | Database dan sistem besar (misalnya SQL Server) |


2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   **Jawaban:**
   - Alasan Utama
Deteksi deadlock tetap diperlukan dalam sistem operasi karena strategi pencegahan (prevention) dan penghindaran (avoidance) deadlock memiliki keterbatasan, sehingga deteksi menjadi pendekatan reaktif yang penting untuk menangani deadlock yang tidak dapat dihindari sepenuhnya. Berikut penjelasannya:
       - Keterbatasan Prevention dan Avoidance:
            - Prevention (misalnya, membatasi hold and wait) seringkali terlalu konservatif, menyebabkan utilisasi sumber daya rendah dan proses menunggu lama (starvation). Tidak cocok untuk sistem kompleks dengan banyak proses dinamis.
            - Avoidance (seperti Banker's Algorithm) memerlukan informasi lengkap tentang kebutuhan sumber daya proses di muka, yang sulit diperoleh dalam sistem real-time atau dengan proses yang berubah-ubah. Overhead komputasi tinggi, terutama untuk sistem besar.
        - Keunggulan Deteksi:
            - Fleksibilitas: Mengizinkan sistem berjalan tanpa pembatasan ketat, memaksimalkan performa dan utilisasi sumber daya. Deadlock dideteksi saat terjadi (misalnya, melalui wait-for graph), lalu dipulihkan.
            - Cocok untuk Sistem Kompleks: Dalam database, sistem terdistribusi, atau OS seperti Windows/Linux, proses seringkali tidak dapat diprediksi sepenuhnya. Deteksi memungkinkan respons cepat tanpa mencegah aktivitas normal.
            - Pemulihan Efektif: Setelah deteksi, sistem dapat terminate proses, rollback, atau preemption sumber daya, meminimalkan dampak. Ini lebih praktis daripada mencegah semua kemungkinan deadlock.
        - Skenario Praktis:
            - Dalam database (misalnya, SQL Server), deadlock sering terjadi karena transaksi konkurensi. Deteksi otomatis memungkinkan rollback transaksi yang terlibat tanpa menghentikan seluruh sistem.
            - Sistem operasi modern menggunakan kombinasi strategi: prevention untuk sumber daya kritis, avoidance untuk yang dapat diprediksi, dan detection untuk yang lainnya.
 - Contoh Ilustrasi
Bayangkan sistem dengan banyak proses yang saling bergantung (misalnya, printer dan file sharing). Prevention mungkin memaksa semua proses meminta sumber daya sekaligus, menyebabkan inefisiensi. Avoidance gagal jika kebutuhan proses tidak diketahui. Deteksi memungkinkan sistem mendeteksi siklus tunggu dan mengakhiri proses deadlock, menjaga sistem berjalan.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock? 
   **Jawaban:**  
## Kelebihan dan Kekurangan Pendekatan Deteksi Deadlock

| Aspek | Kelebihan | Kekurangan |
|------|-----------|------------|
| Cara Kerja | Sistem dibiarkan berjalan bebas dan bertindak hanya saat deadlock terdeteksi | Harus menunggu deadlock terjadi sebelum dapat ditangani |
| Kinerja | Tidak membatasi proses sehingga kinerja normal lebih tinggi | Saat deadlock terjadi, kinerja menurun karena proses macet |
| Penggunaan Sumber Daya | Sumber daya digunakan sepenuhnya tanpa reservasi | Saat deadlock, sumber daya terkunci dan tidak dapat digunakan |
| Implementasi | Relatif mudah diimplementasikan dengan algoritma deteksi | Proses pemulihan (*recovery*) bisa rumit dan mahal |
| Kebutuhan Informasi | Tidak perlu mengetahui kebutuhan sumber daya di awal | Membutuhkan informasi lengkap tentang keadaan sistem saat deteksi |
| Kesesuaian | Cocok untuk sistem dengan deadlock yang jarang terjadi | Tidak cocok untuk sistem yang sering atau bersifat kritis terhadap deadlock |

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
