print('Halo, Welcome to CalcShape!')
print('1. Segitiga')
print('2. Persegi')
print('3. Lingkaran')
print('4. Persegi Panjang')

opt = input("Pilih option: ")

if opt == '1':
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luasSG = (alas * tinggi) / 2
    print(f"Luas segitiga mu adalah: {luasSG} cm^2.")

elif opt == '2':
    sisi = float(input("Masukkan sisi: "))
    luasP = sisi * sisi
    print(f"Luas persegi mu adalah: {luasP} cm^2.")

elif opt == '3':
    r = float(input("Masukkan jari jari: "))
    Pi = 3.14
    luasO = Pi * (r * r)
    print(f"Luas lingkaran mu adalah: {luasO} cm^2.")

elif opt == '4':
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luasPP = panjang * lebar
    print(f"Luas persegi panjang mu adalah: {luasPP} cm^2.")

else:
    print("INVALID OPTION!")