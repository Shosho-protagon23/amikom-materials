# 1. luas kubus
# 2. volume balok
# 3. rumus energi potensial
# 4. USD --> IDR

## Kasus 1 ##

print("Kasus 1 -- 'Luas Kubus'")

sskubus = float(input("Sisi kubus: "))
luasKubus = (sskubus ** 2) * 6

print(f"Luas kubusmu adalah {luasKubus} cm^2.\n")


## Kasus 2 ##

print("Kasus 2 -- 'Volume Balok'")

panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))
tinggi = float(input("Tinggi: "))
volbal = panjang * lebar * tinggi

print(f"Volume balok mu adalah {volbal} cm^3.\n")


## Kasus 3 ##

print("Kasus 3 -- 'Rumus Energi Potensial'")

m = float(input("Massa: ")) # ---> kg
g = float(input("Percepatan Gravitasi: ")) # ---> m/s^2
h = float(input("Tinggi benda dari titik acuan: ")) # ---> meter
Ep = m * g * h

print(f"Besar energi potensial ini adalah {Ep} Joule.\n")


## Kasus 4 ##

print("Kasus 4 -- USD & IDR")
cash = int(input("Masukkan nominal: "))
option = input("USD atau IDR?? ")

# USD --> IDR
if option == "USD":
    cash = cash * 16623
    print(f"Nominal IDR mu adalah: {cash} Rupiah.")

# IDR --> USD
elif option == "IDR":
    cash = cash / 16623
    print(f"Nominal USD mu adalah: {round(cash, 2)} Dollar.")
else:
    print("INVALID! USD atau IDR saja!!")