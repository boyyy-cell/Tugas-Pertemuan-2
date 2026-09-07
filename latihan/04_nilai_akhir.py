print("=== MENGHITUNG NILAI AKHIR ===")

nama = input("Nama: ")
tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

nilai_akhir = (tugas * 0.20) + (uts * 0.30) + (uas * 0.50)

print("\n=== HASIL ===")
print(f"Nama: {nama}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")