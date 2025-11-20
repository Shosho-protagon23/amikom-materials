# Menerima input tinggi dari pengguna
while True:
    try:
        tinggi = int(input("Masukkan tinggi bintang: "))
        if tinggi <= 0:
            print("Tinggi harus bilangan bulat positif.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")

# 1: PIRAMIDA ATAS (dari 1 hingga tinggi)
for i in range(1, tinggi + 1):
    bintang = "*" * i
    print(bintang)

# 2: PIRAMIDA BAWAH (Terbalik, dari tinggi - 1 hingga 1)
for i in range(tinggi - 1, 0, -1):
    bintang = "*" * i
    print(bintang)