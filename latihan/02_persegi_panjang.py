print("=== MENGHITUNG PERSEGI PANJANG ===")

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print("\n=== HASIL ===")
print(f"Luas: {luas:.2f}")
print(f"Keliling: {keliling:.2f}")