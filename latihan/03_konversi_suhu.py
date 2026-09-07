print("=== KONVERSI SUHU ===")

celsius = float(input("Masukkan suhu Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("\n=== HASIL KONVERSI ===")
print(f"Fahrenheit: {fahrenheit:.2f}")
print(f"Kelvin: {kelvin:.2f}")