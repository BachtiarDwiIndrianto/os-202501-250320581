
# Laporan Praktikum Minggu [X]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)
---

## Identitas
- **Nama**  : Bachtiar Dwi Indrianto  
- **NIM**   : 250320581
- **Kelas** : 1DSRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

- 1 Mengimplementasikan algoritma page replacement FIFO dalam program.
- 2 Mengimplementasikan algoritma page replacement LRU dalam program.
- 3 Menjalankan simulasi page replacement dengan dataset tertentu.
- 4 Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
- 5 Menyajikan hasil simulasi dalam laporan yang sistematis.
  
C. Ketentuan Teknis
- Bahasa pemrograman **bebas** (Python / C / Java / lainnya).
- Program berbasis **terminal** (tidak wajib GUI).
- Fokus penilaian pada **logika algoritma dan keakuratan hasil simulasi**.
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```phyton
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3


def print_process_table(title, steps):
    print(f"\n{title}")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")
    print("| Page   | Frame 1  | Frame 2  | Frame 3  | Status   |")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")
    
    for page, mem, status in steps:
        print(f"| {page:<6} | {mem[0]:<8} | {mem[1]:<8} | {mem[2]:<8} | {status:<8} |")
    
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")


# ================= FIFO =================
def fifo_page_replacement(ref, frames):
    memory = ['-'] * frames
    fifo_index = 0
    steps = []
    page_fault = 0

    for page in ref:
        if page in memory:
            steps.append((page, memory.copy(), "HIT"))
        else:
            page_fault += 1
            memory[fifo_index] = page
            fifo_index = (fifo_index + 1) % frames
            steps.append((page, memory.copy(), "FAULT"))

    return page_fault, steps


# ================= LRU =================
def lru_page_replacement(ref, frames):
    memory = ['-'] * frames
    last_used = {}
    steps = []
    page_fault = 0

    for time, page in enumerate(ref):
        if page in memory:
            steps.append((page, memory.copy(), "HIT"))
        else:
            page_fault += 1
            if '-' in memory:
                index = memory.index('-')
            else:
                lru_page = min(last_used, key=last_used.get)
                index = memory.index(lru_page)
                del last_used[lru_page]

            memory[index] = page
            steps.append((page, memory.copy(), "FAULT"))

        last_used[page] = time

    return page_fault, steps


# ================= EKSEKUSI =================
fifo_fault, fifo_steps = fifo_page_replacement(reference_string, frames)
lru_fault, lru_steps = lru_page_replacement(reference_string, frames)

print_process_table("PROSES FIFO (First-In First-Out)", fifo_steps)
print_process_table("PROSES LRU (Least Recently Used)", lru_steps)

# ================= RINGKASAN =================
print("\nRINGKASAN HASIL AKHIR")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
print("| Algoritma | Jumlah Frame | Page Fault   |")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
print(f"| FIFO      | {frames:^12} | {fifo_fault:^12} |")
print(f"| LRU       | {frames:^12} | {lru_fault:^12} |")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
```

---

## Hasil Eksekusi

<img width="1664" height="3218" alt="FIFO DAN LRU" src="https://github.com/user-attachments/assets/51ad80d4-6d57-403d-9d8a-e8c910f7a3b7" />
<img width="896" height="990" alt="Screenshot 2026-01-05 223802" src="https://github.com/user-attachments/assets/d6d834fc-100f-41c6-bdc7-abea1de671e4" />

---

## Analisis

| Algoritma | Jumlah Frame | Page Fault |
|-----------|--------------|------------|
| FIFO      | 3            | 10         |
| LRU       | 3            | 9          |

Berdasarkan hasil simulasi dengan jumlah frame sebanyak **3**, algoritma **LRU** menghasilkan jumlah *page fault* yang lebih sedikit dibandingkan algoritma **FIFO**. Hal ini menunjukkan bahwa algoritma **LRU lebih efisien** dalam pengelolaan memori karena mempertimbangkan penggunaan halaman terbaru.

- Jelaskan mengapa jumlah page fault bisa berbeda?
  perbedaan strategi  yang menyebabkan jumlah page fault antara FIFO dan LRU tidak sama, dan umumnya LRU lebih efisien dalam memanfaatkan memori
- Analisis algoritma mana yang lebih efisien dan alasannya?
  Menurut saya LRU lebih efisien karena algoritma ini mempertimbangkan pola penggunaan halaman, yaitu dengan mempertahankan halaman yang paling sering atau paling baru digunakan agar tetap berada di memori. Dengan demikian, kemungkinan terjadinya page fault dapat dikurangi.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?  
   **Jawaban:**
   - Perbedaan FIFO dan LRU

| Aspek                  | FIFO (First In First Out)             | LRU (Least Recently Used)           |
|-----------------------|---------------------------------------|-------------------------------------|
| Prinsip Kerja         | Data yang pertama masuk dikeluarkan   | Data yang paling lama tidak digunakan dikeluarkan |
| Dasar Penggantian     | Urutan waktu masuk                    | Riwayat penggunaan terakhir         |
| Memperhatikan Pola Akses | Tidak                               | Ya                                  |
| Kompleksitas          | Sederhana                             | Lebih kompleks                      |
| Efisiensi             | Kurang efisien                       | Lebih efisien                       |
| Page Fault            | Cenderung lebih banyak               | Cenderung lebih sedikit             |
| Implementasi          | Mudah                                | Membutuhkan pencatatan akses        |
| Contoh Penggunaan     | Sistem sederhana                     | Sistem dengan performa tinggi       |

2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly? 
   **Jawaban:**
    - Belady’s Anomaly adalah fenomena di mana algoritma FIFO (First In, First Out) menghasilkan lebih banyak page fault saat jumlah frame memori ditingkatkan, yang bertentangan dengan intuisi bahwa lebih banyak memori seharusnya mengurangi fault.
    - Penyebab Utama
   FIFO mengganti halaman berdasarkan urutan masuknya ke memori, tanpa mempertimbangkan frekuensi penggunaan atau waktu akses terakhir. Dengan lebih banyak frame:
      - Halaman yang masuk lebih awal (meski masih relevan) tetap diprioritaskan untuk diganti jika memori penuh.
      - Ini bisa menyebabkan halaman yang sering digunakan atau akan segera dibutuhkan diganti lebih dini, sehingga meningkatkan fault saat pola akses berulang atau kompleks.
      - Algoritma lain seperti LRU tidak mengalami ini karena mempertimbangkan penggunaan terbaru, memanfaatkan prinsip lokalitas referensi.
        
     - Contoh Ilustrasi

       Misalkan urutan akses halaman: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5.
       Dengan 3 frame memori: Page fault = 9.
       Dengan 4 frame memori: Page fault = 10 (lebih banyak!).

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   **Jawaban:**
  - Alasan Utama Performa Lebih Baik
LRU umumnya lebih baik karena memanfaatkan prinsip lokalitas referensi (temporal dan spatial), yang menyatakan bahwa program cenderung mengakses halaman yang baru saja digunakan atau halaman berdekatan. Ini membuat LRU lebih adaptif terhadap pola akses dunia nyata:

    - Pengurangan Page Fault: LRU memprediksi halaman yang mungkin tidak segera dibutuhkan lagi, sehingga mengurangi kesalahan penggantian. FIFO bisa mengganti halaman yang masih relevan jika masuk lebih awal, terutama dalam pola berulang.
    - Hindari Anomali: FIFO rentan terhadap Belady’s Anomaly (page fault meningkat saat frame memori bertambah), sedangkan LRU menghindarinya karena fokus pada penggunaan terbaru, bukan urutan masuk.
    - Efisiensi dalam Pola Akses: Pada aplikasi dengan loop atau akses berulang (seperti database atau web browsing), LRU menjaga halaman "panas" di memori lebih lama, meningkatkan hit rate cache.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
