
# Laporan Praktikum Minggu [X]
Topik: [Sinkronisasi Proses dan Masalah Deadlock]

---

## Identitas
- **Nama**  : [Bachtiar Dwi Indrianto]  
- **NIM**   : [250320581]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengidentifikasi empat kondisi penyebab deadlock (*mutual exclusion, hold and wait, no preemption, circular wait*).  
2. Menjelaskan mekanisme sinkronisasi menggunakan *semaphore* atau *monitor*.  
3. Menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Menyajikan hasil studi kasus secara sistematis.
   
---

## Dasar Teori
Pada praktikum minggu ini, kami mempelajari mekanisme sinkronisasi proses dan penanganan deadlock dalam sistem operasi. Tujuan utamanya adalah memahami bagaimana beberapa proses dapat berjalan secara bersamaan (concurrent) tanpa menyebabkan konflik data atau kebuntuan sumber daya (deadlock).
Kami melakukan studi kasus berbasis Dining Philosophers Problem, yaitu permasalahan klasik sinkronisasi yang menggambarkan bagaimana proses harus berbagi sumber daya terbatas (garpu/mutex/semaphore) tanpa menimbulkan deadlock
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1919" height="1079" alt="Screenshot 2025-11-26 194111" src="https://github.com/user-attachments/assets/a11c5552-306e-471f-a235-fd6321661f9f" />
<img width="1919" height="1078" alt="Screenshot 2025-11-26 194413" src="https://github.com/user-attachments/assets/cf2cde05-675f-4ebd-9990-35bcf85e561e" />
<img width="1919" height="1079" alt="Screenshot 2025-11-26 194518" src="https://github.com/user-attachments/assets/83154c6e-a622-4bb4-a1d1-304b7d8a99ec" />
<img width="1914" height="1076" alt="Screenshot 2025-11-26 194619" src="https://github.com/user-attachments/assets/97799517-b2ae-4067-88ce-b18f70cb87ce" />

---
## Eksperimen 1

Simulasi Dining Philosophers (Deadlock Version)
```
import threading
import time
import random

# jumlah filsuf
N = 5

# setiap garpu = 1 lock
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        print(f"Filsuf {i} sedang berpikir...")
        time.sleep(random.uniform(0.5, 1.5))

        print(f"Filsuf {i} mencoba mengambil garpu kiri {left}")
        forks[left].acquire()
        print(f"Filsuf {i} mengambil garpu kiri {left}")

        print(f"Filsuf {i} mencoba mengambil garpu kanan {right}")
        forks[right].acquire()  # <-- DI SINI DEADLOCK TERJADI
        print(f"Filsuf {i} mengambil garpu kanan {right}")

        print(f"Filsuf {i} sedang makan...")
        time.sleep(random.uniform(0.5, 1.5))

        forks[left].release()
        forks[right].release()
        print(f"Filsuf {i} selesai makan dan meletakkan garpu\n")

# Membuat thread
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
```


## Eksperimen 2
Versi Fixed (Menggunakan Semaphore / Monitor)
FIXED VERSION — Semaphore (Mutex Global)
```
import threading
import time
import random

N = 5
forks = [threading.Lock() for _ in range(N)]
mutex = threading.Semaphore(1)  # mencegah deadlock

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        print(f"Filsuf {i} sedang berpikir...")
        time.sleep(random.uniform(0.2, 0.6))

        mutex.acquire()  # hanya 1 filsuf yang boleh ambil garpu
        forks[left].acquire()
        forks[right].acquire()
        mutex.release()

        print(f"Filsuf {i} mulai makan...")
        time.sleep(random.uniform(0.3, 0.7))

        forks[left].release()
        forks[right].release()
        print(f"Filsuf {i} selesai makan.\n")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.start()
```

FIXED VERSION Batasi Maksimal 4 Filsuf

```
import threading
import time
import random

N = 5
forks = [threading.Lock() for _ in range(N)]
room = threading.Semaphore(4)   # hanya 4 boleh mencoba makan

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        print(f"Filsuf {i} sedang berpikir...")
        time.sleep(random.uniform(0.2, 0.6))

        room.acquire()
        forks[left].acquire()
        forks[right].acquire()

        print(f"Filsuf {i} makan...")
        time.sleep(random.uniform(0.3, 0.7))

        forks[left].release()
        forks[right].release()
        room.release()
        print(f"Filsuf {i} selesai makan.\n")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.start()
```

FIXED VERSION Odd–Even Fork Picking Rule

```
import threading
import time
import random

N = 5
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    left = i
    right = (i + 1) % N

    # odd = right-first, even = left-first
    first = left if i % 2 == 0 else right
    second = right if i % 2 == 0 else left

    while True:
        print(f"Filsuf {i} sedang berpikir...")
        time.sleep(random.uniform(0.2, 0.6))

        forks[first].acquire()
        forks[second].acquire()

        print(f"Filsuf {i} makan (urutan garpu dibalik)...")
        time.sleep(random.uniform(0.3, 0.7))

        forks[first].release()
        forks[second].release()
        print(f"Filsuf {i} selesai makan.\n")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.start()
```

## Eksperimen 3

| **Kondisi Deadlock** | **Terjadi di Versi Deadlock?**                                 | **Solusi di Versi Fixed**                                                                                                                                                                                                                                 |
| -------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mutual Exclusion** | Ya setiap garpu hanya bisa digunakan 1 filsuf                | Tetap ada (karena perlu), tetapi *akses garpu dikontrol* menggunakan **mutex atau semaphore** agar tidak menyebabkan hold-and-wait serentak                                                                                                               |
| **Hold and Wait**    | Ya  semua filsuf memegang garpu kiri dan menunggu garpu kanan | **Semaphore(1)**: filsuf hanya boleh mengambil kedua garpu sekaligus (menghilangkan hold-and-wait) <br> **Max 4**: tidak semua filsuf bisa menahan garpu kiri <br> **Odd-Even**: menghindari menunggu dalam kondisi simetris                              |
| **No Preemption**    | Ya  garpu tidak bisa direbut paksa                            | Tetap ada (karena garpu tidak bisa direbut), tetapi **deadlock hilang karena circular wait dihilangkan**                                                                                                                                                  |
| **Circular Wait**    | Ya  P0 menunggu P1 → P1 menunggu P2 → … → P4 menunggu P0      | **Max 4 philosophers**: siklus tidak bisa terbentuk <br> **Odd-Even Rule**: urutan pengambilan garpu diubah sehingga tidak ada lingkaran menunggu <br> **Semaphore mutex**: hanya satu yang boleh mengambil garpu, sehingga siklus tidak pernah terbentuk |




## Analisis
Berikut **Analisis Eksperimen 1 dan Eksperimen 2 BESERTA Kesimpulannya**, sudah ditulis rapi dan siap ditempel ke laporan kamu.

---

# **Analisis Eksperimen 1 dan Eksperimen 2**

## **Analisis Eksperimen 1 – *Dining Philosophers Deadlock Version***

Pada eksperimen pertama, setiap filsuf mengambil **garpu kiri terlebih dahulu**, kemudian mencoba mengambil **garpu kanan**. Pola ini terlihat sederhana, namun menciptakan kondisi yang sangat rentan terhadap *deadlock*.

Dari hasil eksekusi terlihat bahwa:

* Semua filsuf **berhasil mengambil garpu kiri secara bersamaan**.
* Setelah itu, semua filsuf **mencoba mengambil garpu kanan**, tetapi garpu tersebut sedang digunakan oleh filsuf lain.
* Akibatnya, **semua filsuf menunggu secara bersamaan**, tidak ada yang bisa melanjutkan, dan tidak ada garpu yang dilepas.
* Kondisi ini menyebabkan **deadlock total**: tidak ada filsuf yang dapat makan maupun melanjutkan proses.

Empat kondisi Coffman yang menyebabkan deadlock semuanya muncul pada eksperimen ini:

1. **Mutual Exclusion** – Garpu hanya bisa digunakan oleh satu filsuf.
2. **Hold and Wait** – Filsuf memegang garpu kiri sambil menunggu garpu kanan.
3. **No Preemption** – Garpu tidak bisa direbut atau dipaksa dilepas.
4. **Circular Wait** – Siklus menunggu terbentuk:
   P0 → P1 → P2 → P3 → P4 → kembali ke P0.

Karena keempat kondisi ini aktif secara bersamaan, deadlock **pasti terjadi**.

---

## **Analisis Eksperimen 2 – *Fixed Version (Semaphore / Monitor)*

Eksperimen kedua menggunakan tiga solusi berbeda untuk mencegah deadlock. Ketiganya berhasil menghilangkan setidaknya satu dari empat kondisi Coffman, sehingga deadlock tidak bisa terbentuk.

### **1. Global Mutex (Semaphore = 1)**

Dalam solusi ini, hanya **satu filsuf** yang boleh mengambil garpu pada satu waktu.

Hasil pengamatan:

* Tidak pernah terjadi deadlock.
* Hold-and-wait dihilangkan karena filsuf langsung mengambil **dua garpu sekaligus**.
* Kekurangannya: tingkat paralelisme rendah, karena hanya satu filsuf bisa makan dalam satu periode waktu.

### **2. Room Semaphore (maksimal 4 filsuf mencoba makan)**

Dengan membatasi hanya 4 filsuf yang boleh mencoba mengambil garpu:

* Siklus circular wait **tidak dapat terbentuk**, karena tidak semua filsuf bisa masuk ke fase “mengambil garpu”.
* Deadlock hilang.
* Paralelisme lebih baik dibanding mutex global.
* Pendekatan ini banyak digunakan dalam implementasi Dining Philosophers modern.

### **3. Odd–Even Fork Picking Rule**

Filsuf genap mengambil garpu kiri dahulu, filsuf ganjil mengambil garpu kanan dahulu.

* Urutan pengambilan garpu **tidak lagi simetris**, sehingga circular wait otomatis hilang.
* Deadlock tidak terjadi.
* Paralelisme bagus, beberapa filsuf dapat makan secara bersamaan.

> **Kesimpulan eksperimen 2:**
> Semua versi perbaikan sukses menghilangkan deadlock dengan memutus "hold-and-wait" atau "circular wait" yang muncul pada eksperimen pertama.

---

**Kesimpulan Umum Eksperimen**

1. **Eksperimen 1 membuktikan bahwa deadlock terjadi ketika seluruh kondisi Coffman terpenuhi.**
   Dining Philosophers versi klasik tanpa mekanisme pencegah memang rawan mengalami kebuntuan total.

2. **Eksperimen 2 menunjukkan bahwa deadlock dapat dicegah dengan mengubah aturan pengambilan sumber daya.**
   Pendekatan seperti mutex global, room semaphore, dan odd–even rule efektif dalam menghilangkan hold-and-wait atau circular wait.

3. **Setiap solusi memiliki trade-off:**

   * *Mutex Global*: paling aman tetapi mengurangi paralelisme.
   * *Room Semaphore*: seimbang antara keamanan dan performa.
   * *Odd–Even*: paling efisien dan tetap aman.

4. **Pemahaman pola deadlock dan strategi sinkronisasi sangat penting dalam sistem operasi**, terutama pada lingkungan multi-threaded dan multi-prosesor.


---

## Kesimpulan
Dari rangkaian praktikum mengenai Dining Philosophers Problem dan mekanisme sinkronisasi proses, dapat disimpulkan bahwa:

1.Deadlock dapat terjadi ketika seluruh kondisi Coffman terpenuhi, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait. Hal ini terbukti pada Eksperimen 1, di mana seluruh filsuf mengambil garpu kiri terlebih dahulu sehingga terjadi antrian melingkar dan tidak ada filsuf yang dapat melanjutkan ke proses makan.

2.Eksperimen 2 membuktikan bahwa deadlock dapat dicegah dengan menerapkan mekanisme sinkronisasi yang tepat. Tiga teknik—global mutex, pembatasan maksimal filsuf yang mencoba makan (room semaphore), dan odd–even rule—berhasil mencegah deadlock dengan memutus kondisi hold-and-wait atau circular wait.

3.Setiap metode pencegahan deadlock memiliki kelebihan dan kekurangan masing-masing.
Global mutex sangat aman namun mengurangi paralelisme.
Room semaphore meningkatkan efisiensi karena beberapa filsuf tetap bisa makan secara bersamaan.
Odd–even rule adalah solusi paling ringan dan efisien karena tidak membutuhkan semaphore tambahan.

4.Pemahaman sinkronisasi dan pencegahan deadlock sangat penting dalam sistem operasi, terutama dalam sistem yang menjalankan banyak proses secara bersamaan. Praktikum ini memberikan gambaran nyata mengenai bagaimana kesalahan pengaturan resource dapat menyebabkan kebuntuan dan bagaimana mekanisme sinkronisasi dapat mengatasinya.

Secara keseluruhan, praktikum ini menegaskan bahwa pentingnya desain sinkronisasi yang benar bukan hanya untuk mencegah deadlock, tetapi juga untuk menjaga efisiensi, keadilan, dan stabilitas sistem.

---

## Quiz
1. [Sebutkan empat kondisi utama penyebab deadlock.]  
   **Jawaban:** 
   Mutual Exclusion (Saling Mengunci)
   Resource hanya bisa digunakan oleh satu proses pada satu waktu.

   Hold and Wait (Menahan dan Menunggu)
   Proses sudah memegang satu resource, lalu menunggu resource lain yang sedang dipakai proses lain.

   No Preemption (Tidak Dapat Diambil Paksa)
   Resource yang sedang digunakan proses tidak bisa diambil secara paksa oleh sistem; harus dilepas secara sukarela.

   Circular Wait (Menunggu Secara Melingkar)
   Terjadi rantai proses yang saling menunggu resource satu sama lain dalam bentuk lingkaran.

Jika keempat kondisi ini terjadi secara bersamaan, maka deadlock dapat muncul.

2. [Mengapa sinkronisasi diperlukan dalam sistem operasi?]  
   **Jawaban:**  

Mencegah Race Condition
Ketika dua atau lebih proses/threads mengakses dan mengubah data yang sama secara bersamaan, hasil akhirnya bisa menjadi tidak benar atau tidak dapat diprediksi. Sinkronisasi memastikan hanya satu proses yang mengubah data pada satu waktu.

Menjaga Konsistensi Data
Tanpa sinkronisasi, data bersama (shared data) bisa rusak karena akses yang tak teratur. Mekanisme seperti mutex, semaphore, atau monitor memastikan data tetap konsisten.

Mengatur Akses ke Resource Bersama
Banyak resource bersifat terbatas (file, printer, memory buffer). Sinkronisasi mengatur giliran sehingga semua proses dapat memakai resource dengan aman dan teratur.

Menghindari Deadlock dan Livelock
Dengan sinkronisasi yang tepat (misalnya aturan penguncian), sistem dapat mencegah situasi di mana proses saling menunggu tanpa akhir.

Mendukung Kerja Paralel yang Efisien
Pada sistem multiprosesor/multicore, sinkronisasi membantu proses berjalan bersamaan tanpa saling mengganggu dan memastikan performa tetap optimal.

Singkatnya: Sinkronisasi diperlukan untuk **keamanan data, keteraturan akses resource, dan stabilitas sistem** dalam menjalankan banyak proses secara bersamaan.

3. [Jelaskan perbedaan antara semaphore dan monitor.]  
   **Jawaban:**
   
| Aspek | Semaphore | Monitor |
|-------|-----------|---------|
| Level | Low-level | High-level |
| Mekanisme | Counter + operasi P/V | Lock otomatis + function |
| Kemudahan | Rawan error | Lebih aman |
| Penggunaan | Sinkronisasi sederhana | Program kompleks berbasis OOP |

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
Bagian paling menantang adalah memahami interaksi kompleks antara keempat kondisi deadlock dan menerapkan solusi yang tepat untuk Dining Philosophers Problem. Analisis mendalam tentang bagaimana setiap solusi mempengaruhi kondisi Coffman membutuhkan pemahaman konseptual yang kuat.
- Bagaimana cara Anda mengatasinya?
Studi Teori: Mempelajari ulang konsep dasar deadlock dan kondisi Coffman
Simulasi Manual: Melakukan tracing eksekusi untuk setiap skenario
Diskusi Kelompok: Berbagi pemahaman dan pendekatan solusi
Eksperimen Berulang: Menjalankan kode multiple times untuk verifikasi
Analisis Komparatif: Membuat tabel perbandingan antar solusi



---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
