# MENGHITUNG RATA-RATA DARI N BUAH DATA

# 2. TANYA N (Banyaknya Data)
# 3. Meminta pengguna menentukan berapa banyak data yang akan dihitung
try:
    jumlah_data = int(input("Masukkan banyaknya data (N): "))
except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat.")
    exit()

# Memastikan input data positif
if jumlah_data <= 0:
    print("Banyaknya data harus lebih dari nol.")
    exit()

# 3. INISIALISASI List kosong untuk menyimpan data
data_list = []

print("--- Memasukkan Data ---")
# 4. ULANGI Sebanyak N kali
for i in range(jumlah_data):
    while True:
        try:
            # 4a. BACA Data_ke_i
            nilai = float(input(f"Masukkan data ke-{i+1}: "))
            # 4b. Tambahkan data ke list
            data_list.append(nilai)
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

# 5. HITUNG RataRata = Jumlah / N
# Menggunakan fungsi bawaan Python: sum() untuk menjumlahkan semua elemen dalam list
jumlah = sum(data_list)

# Menggunakan fungsi bawaan Python: len() untuk mendapatkan banyaknya data
rata_rata = jumlah / len(data_list)

# 6. TAMPILKAN RataRata
print("\n--- Hasil Perhitungan ---")
print(f"Total data yang dimasukkan (N): {len(data_list)}")
print(f"Jumlah Total (Sum): {jumlah}")
print(f"Rata-Rata (Average): {rata_rata}")

# 7. SELESAI