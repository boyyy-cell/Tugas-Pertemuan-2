print("=== MENGHITUNG NILAI AKHIR ===")

tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

print("\n=== HASIL ===")
print("Nilai Akhir:", nilai_akhir)