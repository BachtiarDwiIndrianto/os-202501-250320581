``` phyton
# PROGRAM SIMULASI SJF (Non-Preemptive)

# Data proses
proses = [
    {"nama": "P1", "arrival": 0, "burst": 6},
    {"nama": "P2", "arrival": 1, "burst": 8},
    {"nama": "P3", "arrival": 2, "burst": 7},
    {"nama": "P4", "arrival": 3, "burst": 3},
]

waktu_sekarang = 0
total_waiting = 0
total_turnaround = 0
selesai = []

print("SJF (Shortest Job First - Non Preemptive)")
print("-" * 80)
print(f"{'Proses':<8}{'Burst':<8}{'Arrival':<10}{'Start':<8}{'Waiting':<10}{'Turnaround':<12}{'Finish':<8}")
print("-" * 80)

while proses:
    # Ambil proses yang sudah datang
    tersedia = [p for p in proses if p["arrival"] <= waktu_sekarang]

    # Jika belum ada proses yang datang
    if not tersedia:
        waktu_sekarang += 1
        continue

    # Pilih proses dengan burst time terkecil
    proses_terpendek = min(tersedia, key=lambda x: x["burst"])
    proses.remove(proses_terpendek)

    start = waktu_sekarang
    waiting = start - proses_terpendek["arrival"]
    turnaround = waiting + proses_terpendek["burst"]
    finish = start + proses_terpendek["burst"]

    waktu_sekarang = finish
    total_waiting += waiting
    total_turnaround += turnaround

    print(f"{proses_terpendek['nama']:<8}{proses_terpendek['burst']:<8}{proses_terpendek['arrival']:<10}"
          f"{start:<8}{waiting:<10}{turnaround:<12}{finish:<8}")

    selesai.append(proses_terpendek)

rata_waiting = total_waiting / len(selesai)
rata_turnaround = total_turnaround / len(selesai)

print("-" * 80)
print(f"{'Rata-rata':<36}{rata_waiting:<10.2f}{rata_turnaround:<12.2f}")
```
