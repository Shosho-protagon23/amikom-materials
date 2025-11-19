tinggi = int(input("Tinggi puncak piramida: ..."))  # Tinggi piramida

# Loop utama untuk setiap baris (i)
for i in range(1, tinggi + 1):
    # 1. Menghitung dan mencetak spasi (untuk memusatkan piramida)
    # Spasi yang dibutuhkan: tinggi - i
    spasi = " " * (tinggi - i)

    # 2. Menghitung dan mencetak bintang
    # Bintang yang dibutuhkan: 2 * i - 1
    bintang = "*" * (2 * i - 1)

    # 3. Menggabungkan dan mencetak baris
    print(spasi + bintang)