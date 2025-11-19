tinggi = int(input("Tinggi puncak piramida: "))

for i in range(1, tinggi + 1):
    bintang = "*" * i
    print(bintang)

for i in range(tinggi - 1, 0, -1):
    bintang = "*" * i
    print(bintang)