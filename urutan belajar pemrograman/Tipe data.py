#Nama   : Ika ramadanai
#NIM    : D0425325
#Kelas  : B Sistem Informasi

#Tipe data  :

# 1. Tipe Data Character (di Python menggunakan String/str)
print("--- 1. Tipe Data Character (str) ---")
karakter_tunggal = 'A'
kata_lengkap = "python"

# Operasi pada String
karakter_kedua = kata_lengkap[1] # Mengambil karakter pada indeks ke-1 (huruf 'y')
panjang_kata = len(kata_lengkap)

print(f"Karakter Tunggal: {karakter_tunggal}, Tipe: {type(karakter_tunggal)}")
print(f"Karakter Kedua dari 'Python': {karakter_kedua}, Tipe: {type(karakter_kedua)}")
print(f"Panjang kata 'Python': {panjang_kata}")

print("-" * 30)

# 2. Tipe Data Integer (int)
print("--- 2. Tipe Data Integer (int) ---")
bilangan_bulat_positif = 42
bilangan_bulat_negatif = -100
bilangan_besar = 9876543210123456789 # Python mendukung Integer yang sangat besar

# Operasi pada Integer
penjumlahan = bilangan_bulat_positif + 8
pembagian_bulat = 10 // 3 # Menggunakan // untuk pembagian yang menghasilkan Integer

print(f"Nilai Positif: {bilangan_bulat_positif}, Tipe: {type(bilangan_bulat_positif)}")
print(f"Hasil Penjumlahan: {penjumlahan}")
print(f"Hasil Pembagian Bulat (10 // 3): {pembagian_bulat}")

print("-" * 30)

# 3. Tipe Data Floating Point (float)
print("--- 3. Tipe Data Floating Point (float) ---")
bilangan_desimal = 3.14159
bilangan_scientific = 2.5e3 # Sama dengan 2.5 * 10^3 = 2500.0

# Operasi pada Floating Point
perkalian = bilangan_desimal * 2
pembagian_biasa = 10 / 3 # Menggunakan / untuk pembagian yang menghasilkan Float

print(f"Nilai Desimal: {bilangan_desimal}, Tipe: {type(bilangan_desimal)}")
print(f"Nilai Scientific: {bilangan_scientific}")
print(f"Hasil Perkalian (PI * 2): {perkalian}")
print(f"Hasil Pembagian Biasa (10 / 3): {pembagian_biasa}")

print("-" * 30)