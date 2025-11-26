
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
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
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

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
