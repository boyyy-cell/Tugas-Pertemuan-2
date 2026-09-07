print("=== KALKULATOR KOORDINAT ===")

x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))

x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

dx = x2 - x1
dy = y2 - y1

jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

tengah_x = (x1 + x2) / 2
tengah_y = (y1 + y2) / 2

print("\n=== HASIL ===")
print(f"Perubahan koordinat: ({dx:.2f}, {dy:.2f})")
print(f"Jarak: {jarak:.2f}")
print(f"Titik tengah: ({tengah_x:.2f}, {tengah_y:.2f})")