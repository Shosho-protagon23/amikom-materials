### MENGHITUNG RATA RATA DARI N BUAH DATA ###

try:
    jumlah_data = int(input("Masukkan jumlah data (n): "))
except ValueError:
    print("Input data tidak valid. Harap masukkan bilangan bulat.")
    exit()

# memastikan inputnya data (+)
if jumlah_data <= 0:
    print("Banyaknya data harus lebih dari 0.")
    exit()

# inisialisasi list kosong untuk tempat storing data
data_list = []
print("--- Memasukan data... ---")

# ulangi sebanyak n kali
for i in range(jumlah_data):
    while True:
        try:
            ## baca data ke-i
            nilai = float(input(f"masukkan data ke-{i+1}: "))
            ## tambah data ke list
            data_list.append(nilai)
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

## hitung rata-rata = jumlah / n
## menggunakan fungsi sum() untuk menjumlahkan elemen dalam list
jumlah = sum(data_list)

## menggunakan fungsi len() untuk mendapatkan banyaknya data
rata_rata = jumlah / len(data_list)

# tampilkan rata-rata
print("\n--- HASIL PERHITUNGAN ---")
print(f"Total data (n): {len(data_list)}")
print(f"Total jumlah (n) data: {jumlah}")
print(f"Total rata (n) data: {rata_rata}")

#### SELESAI ####