n = int(input("Masukkan tinggi bintang: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

for j in range(n, 1, -1):
    for i in range(i):
        print("*", end="")
    print()