
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Bachtiar Dwi Indrianto 
- **NIM**   : 250320581
- **Kelas** : 1DSRA

---
## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa mempelajari konsep **containerization** menggunakan Docker, serta bagaimana sistem operasi membatasi pemakaian sumber daya proses melalui mekanisme isolasi dan kontrol resource (mis. *cgroups* pada Linux).

Fokus praktikum adalah:
1. Membuat **Dockerfile sederhana** untuk menjalankan aplikasi/skrip.
2. Menjalankan container dengan **pembatasan resource** (CPU dan memori).
3. Mengamati dampak pembatasan resource melalui output program dan monitoring sederhana.
---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.
---

## Dasar Teori
Docker adalah platform untuk menjalankan aplikasi di dalam container yang bersifat ringan dan terisolasi dari sistem utama. Container memungkinkan aplikasi berjalan secara konsisten karena sudah dilengkapi dengan dependensi yang dibutuhkan. Docker menyediakan fitur pembatasan resource seperti CPU dan memori menggunakan parameter tertentu saat menjalankan container. Pembatasan CPU berpengaruh pada kecepatan eksekusi program, sedangkan pembatasan memori menentukan jumlah maksimum RAM yang dapat digunakan. Jika penggunaan memori melebihi batas yang ditentukan, container akan dihentikan otomatis oleh sistem. Monitoring penggunaan resource dapat dilakukan menggunakan perintah `docker stats` untuk melihat kinerja container secara real-time.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```


---

## Kode / Perintah
- PROGRAM SEDERHANA PHYTON
```
import time

data = []
iterasi = 0

print("Program uji CPU dan Memori dimulai...", flush=True)

while True:
    total = 0
    for i in range(1_000_000):
        total += i * i

    data.append("X" * 10_000_000)
    iterasi += 1

    print(f"Iterasi ke-{iterasi} | Memori terpakai: {iterasi * 10} MB", flush=True)
    time.sleep(1)
```
- Isi Dockerfile
```
FROM python:3.12-slim

WORKDIR /app

COPY code/ .

CMD ["python", "test_resource.py"]
```
---


## Analisis Dan Hasil Eksekusi
### Persiapan Lingkungan
<img width="1919" height="1079" alt="Screenshot 2026-01-10 001612" src="https://github.com/user-attachments/assets/da87df70-d2fe-4149-8c75-5de472ff5942" />


```
docker version
```

Menampilkan docker version yang terpasang

```
docker ps
```
Jika Docker berjalan normal, hasilnya:Tabel kosong (jika belum ada container aktif), atau Daftar container yang sedang berjalan

### Membuat Aplikasi/Skrip Uji
<img width="1919" height="1072" alt="Screenshot 2026-01-10 004154" src="https://github.com/user-attachments/assets/fc85b613-a294-4543-862c-55c974b24260" />

- PROGRAM SEDERHANA PHYTON
```
import time

data = []
iterasi = 0

print("Program uji CPU dan Memori dimulai...", flush=True)

while True:
    total = 0
    for i in range(1_000_000):
        total += i * i

    data.append("X" * 10_000_000)
    iterasi += 1

    print(f"Iterasi ke-{iterasi} | Memori terpakai: {iterasi * 10} MB", flush=True)
    time.sleep(1)

```
### Membuat Dockerfile
<img width="1919" height="988" alt="Screenshot 2026-01-10 005745" src="https://github.com/user-attachments/assets/cd440fe2-b373-48d0-9375-b9ca4daa0dd0" />


- Isi Dockerfile
```
FROM python:3.12-slim

WORKDIR /app

COPY code/ .

CMD ["python", "test_resource.py"]

```
FROM python:3.12-slim

- Image dasar Python ringan

WORKDIR /app

- Direktori kerja di dalam container COPY code/ .

- Menyalin program uji dari host ke container

CMD ["python", "test_resource.py"]

-  Menjalankan program uji saat container dijalankan

### Menjalankan Container Dengan Limit Resource

```
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
<img width="918" height="919" alt="Screenshot 2026-01-10 011644" src="https://github.com/user-attachments/assets/6d7ee084-dda0-4b93-8327-232afb09856c" />


- Container boleh melewati limit sebentar
- Kernel Linux memonitor RSS (real memory)
- Saat benar-benar kehabisan memori, barulah:
  - Kernel menjalankan OOM Killer
  - Container dihentikan

- Jadi wajar jika:
  - Output masih muncul sampai “520 MB”
  - Tapi docker stats tetap menunjukkan mendekati 256 MB
  - Container mati sedikit terlambat
 
- Nilai memori yang ditampilkan oleh program merupakan estimasi berdasarkan jumlah iterasi, bukan penggunaan memori aktual. Walaupun output program menunjukkan penggunaan memori melebihi 256 MB, Docker tetap membatasi penggunaan memori container. Container dihentikan secara otomatis oleh sistem (OOMKilled) ketika penggunaan memori aktual mencapai batas yang ditentukan.

### Monitoring Sederhana
<img width="1919" height="1079" alt="Screenshot 2026-01-10 014836" src="https://github.com/user-attachments/assets/ebe6b845-4621-4a7b-a62d-3ed9197d9382" />

- Parameter yang diamati:
  - CPU % → Terlihat dibatasi, tidak pernah mencapai 100%
  - MEM USAGE / LIMIT → Penggunaan memori meningkat bertahap hingga mendekati 256 MB
  - MEM % → Persentase memori naik seiring iterasi program
  - PIDS → Jumlah proses stabil (1 proses utama)

- Perilaku yang terlihat:
  - CPU usage relatif stabil dan terbatas akibat opsi --cpus="0.5"
  - Memori terus bertambah sesuai alokasi program
  - Saat mendekati batas memori, container berhenti secara otomatis
  - Tidak ada error Python, container dihentikan oleh sistem (OOM)
---

## Kesimpulan
Praktikum ini menunjukkan bahwa Docker mampu menjalankan aplikasi dalam container dengan pembatasan resource secara efektif. Pembatasan CPU mempengaruhi kecepatan eksekusi program, sedangkan pembatasan memori dapat menyebabkan container dihentikan otomatis ketika batas terlampaui. Monitoring dengan `docker stats` membantu memahami penggunaan resource dan perilaku container secara nyata.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?  
   **Jawaban:**
   Pembatasan CPU dan memori pada container diperlukan untuk mencegah satu container menggunakan sumber daya secara berlebihan sehingga mengganggu container lain dan kestabilan sistem host. Dengan adanya batasan, setiap container mendapatkan alokasi sumber daya yang adil, performa aplikasi menjadi lebih stabil dan terprediksi, serta risiko kehabisan memori atau crash sistem dapat dikurangi. Selain itu, pembatasan ini meningkatkan keamanan dengan membatasi dampak kesalahan aplikasi atau serangan yang mencoba menghabiskan resource, sekaligus membantu efisiensi penggunaan sumber daya dan memudahkan pengelolaan serta penjadwalan container oleh sistem orkestrasi seperti Kubernetes.
2. Apa perbedaan VM dan container dalam konteks isolasi resource? 
   **Jawaban:**
   ## Perbedaan Isolasi Resource antara VM dan Container

| Aspek | Virtual Machine (VM) | Container |
|-------|--------------------|-----------|
| Isolasi Resource | Tinggi, setiap VM memiliki sistem operasi sendiri dan alokasi CPU, memori, storage terpisah | Lebih ringan, berbagi kernel host, isolasi melalui cgroups dan namespace |
| Sistem Operasi | Setiap VM menjalankan Guest OS lengkap | Berbagi Host OS, hanya aplikasi dan dependensi yang terisolasi |
| Efisiensi | Lebih berat, memerlukan lebih banyak resource | Lebih ringan, efisien, startup lebih cepat |
| Dampak Gangguan | Gangguan pada satu VM jarang memengaruhi VM lain | Gangguan pada satu container bisa berisiko ke host jika ada celah kernel |
| Fleksibilitas | Lebih rigid, resource dialokasikan statis | Lebih fleksibel, resource bisa dibatasi atau diubah secara dinamis |
| Keamanan | Tinggi karena isolasi lengkap | Sedang, bergantung pada keamanan kernel host |

3. Apa dampak limit memori terhadap aplikasi yang boros memori? 
   **Jawaban:**  
- Dampak Limit Memori terhadap Aplikasi yang Boros Memori

1. **Aplikasi Melambat Secara Bertahap**  
   - Saat penggunaan memori mendekati limit, sistem atau runtime (misal Java GC) melakukan pembersihan memori lebih sering.  
   - Garbage collection menjadi lebih lama dan mengonsumsi CPU, sehingga aplikasi lambat dan responsif menurun.

2. **Alokasi Memori Gagal**  
   - Permintaan memori baru (misal `malloc` atau `new`) gagal jika limit tercapai.  
   - Aplikasi bisa menampilkan error "Out of Memory" dan beberapa fungsi berhenti bekerja.

3. **Aplikasi Diberhentikan Paksa (OOM Kill)**  
   - Pada container (Docker/Kubernetes), jika melebihi limit, container dihentikan dengan status `OOMKilled`.  
   - Di Linux, OOM Killer memilih proses berdasarkan skor tertentu, menyebabkan aplikasi mati tiba-tiba dan downtime.

4. **Restart Loop (Siklus Restart Berulang)**  
   - Jika ada mekanisme auto-restart, aplikasi terus restart dan kembali boros memori hingga mati lagi.  
   - Mengakibatkan service tidak stabil dan uptime rendah.

5. **Data Loss atau Corruption**  
   - Termination paksa dapat menghilangkan data yang belum tersimpan.  
   - Transaksi, koneksi database, atau file handle bisa tidak tertutup dengan benar.

6. **Dampak pada Sistem Lain (Noisy Neighbor)**  
   - Aplikasi boros memori bisa memengaruhi performa aplikasi lain di host yang sama.  
   - Jika ada swapping, performa sistem secara keseluruhan menurun.

7. **Kesulitan Debugging**  
   - Crash akibat OOM sulit dideteksi karena memori sudah hilang.  
   - Log biasanya hanya menunjukkan "killed by OOM", memerlukan profiling untuk menemukan kebocoran.

- Solusi Umum
  - Atur limit memori sesuai kebutuhan aplikasi.  
  - Gunakan monitoring dan alerting untuk memantau penggunaan memori.  
  - Optimasi kode untuk mengurangi penggunaan memori (hindari memory leak, gunakan struktur data efisien).  
  - Lakukan stress testing untuk memahami perilaku aplikasi di bawah beban tinggi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Bagian paling menantang dalam praktikum ini adalah mengatasi error saat pembuatan Dockerfile serta memahami perilaku container ketika dibatasi CPU dan memori, terutama saat container berhenti otomatis karena keterbatasan memori.

- Bagaimana cara Anda mengatasinya?  Cara mengatasi tantangan tersebut adalah dengan memastikan penulisan Dockerfile dan struktur folder sudah benar, melakukan build ulang image setelah setiap perubahan, serta menggunakan perintah `docker stats` untuk memantau penggunaan CPU dan memori sehingga penyebab masalah dapat diidentifikasi dengan jelas.


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
