print("=== BIODATA ===")

nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

tahun_sekarang = 2026
umur = tahun_sekarang - tahun_lahir

print("\n=== HASIL BIODATA ===")
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"Kelas: {kelas}")
print(f"Tahun lahir: {tahun_lahir}")
print(f"Perkiraan umur: {umur} tahun")