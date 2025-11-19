# Menerima input batas atas dari pengguna
while True:
    try:
        batas_atas = int(input("Masukkan Batas Atas (bilangan bulat positif): "))
        if batas_atas <= 1:
            print("Batas atas harus bilangan bulat yang lebih besar dari 1.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")

# Inisialisasi variabel
bilangan_genap = []
total_penjumlahan = 0

# Iterasi dari 1 hingga batas_atas untuk menemukan bilangan genap
for angka in range(1, batas_atas + 1):
    # Cek apakah angka adalah bilangan genap (angka % 2 == 0)
    if angka % 2 == 0:
        bilangan_genap.append(angka)
        total_penjumlahan += angka

# Menentukan jumlah bilangan genap yang ditemukan
banyaknya_bilangan_genap = len(bilangan_genap)

# Menghitung rata-rata
if banyaknya_bilangan_genap > 0:
    nilai_rata_rata = total_penjumlahan / banyaknya_bilangan_genap
else:
    # Kasus ini seharusnya hanya terjadi jika batas_atas < 2
    nilai_rata_rata = 0.0

# Menampilkan hasil
print("-" * 40)
print(f"Batas Atas yang dimasukkan: {batas_atas}")
print(f"Bilangan Genap yang ditemukan (hingga {batas_atas}): {bilangan_genap}")
print("-" * 40)
print(f"1. Banyaknya Jumlah Bilangan Genap: {banyaknya_bilangan_genap}")
print(f"2. Total Penjumlahan: {total_penjumlahan}")
print(f"3. Nilai Rata-rata dari Penjumlahan: {nilai_rata_rata}")