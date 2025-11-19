# Definisi parameter dari permasalahan
batas_atas = 12
jumlah_bilangan_genap_dicari = 6

# Inisialisasi variabel
bilangan_genap = []
angka_saat_ini = 2  # Bilangan genap positif pertama adalah 2

# Mencari 6 bilangan genap pertama yang <= batas_atas
# Looping akan berhenti jika sudah mendapatkan 6 bilangan ATAU jika angka_saat_ini melebihi batas_atas
while len(bilangan_genap) < jumlah_bilangan_genap_dicari and angka_saat_ini <= batas_atas:
    bilangan_genap.append(angka_saat_ini)
    angka_saat_ini += 2 # Lompat ke bilangan genap berikutnya

# Menghitung jumlah (sum) dari bilangan genap yang ditemukan
total_penjumlahan = sum(bilangan_genap)

# Menghitung rata-rata (mean)
# Pastikan bilangan_genap tidak kosong untuk menghindari ZeroDivisionError
if bilangan_genap:
    nilai_rata_rata = total_penjumlahan / len(bilangan_genap)
else:
    nilai_rata_rata = 0.0

# Menampilkan hasil
print(f"Batas Atas yang Digunakan: {batas_atas}")
print(f"Jumlah Bilangan Genap yang Dicari: {jumlah_bilangan_genap_dicari}")
print("-" * 30)
print(f"Bilangan Genap yang Ditemukan: {bilangan_genap}")
print(f"Total Penjumlahan Bilangan Genap: {total_penjumlahan}")
print(f"Nilai Rata-rata: {nilai_rata_rata}")