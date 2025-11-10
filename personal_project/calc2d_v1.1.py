from art import *
import textColor
import time

# Fungsi untuk menampilkan loading bar sederhana.
def loading_bar(duration=2):
    for i in range(11):
        print(f"Loading: [{'#' * i}{' ' * (10 - i)}] {i*10}%", end='\r')
        time.sleep(duration / 10)
    print()  # Pindah ke baris baru setelah loading selesai

while True:
    print(textColor.yellow(text2art("Bangunans2D Calc")))
    print(textColor.blue(text2art("By: EchoF", font="cybemedium")))

    print("==============================")
    print("0. Exit")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Jajar Genjang")
    print("4. Trapesium")
    print("5. Segitiga")
    print("6. Lingkaran")
    print("7. Belah Ketupat")
    print("==============================")
    opt = input("Pilih opsi (0-7): ... ")

    if opt == "0":
        print("Terima kasih telah menggunakan Bangunans2D Calc!")
        break

    elif opt == "1":
        try:
            print(textColor.yellow(text2art("Persegi", font="cybermedium")))
            sisi = float(input("Sisi: "))
            loading_bar()  # Tambahkan loading bar sebelum perhitungan
            luas = sisi ** 2
            print(textColor.green(f"Luas Persegi: {luas} square units."))
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

    elif opt == "2":
        try:
            print(textColor.yellow(text2art("Persegi Panjang", font="cybermedium")))
            panjang = float(input("Panjang: "))
            lebar = float(input("Lebar: "))
            loading_bar()  # Tambahkan loading bar sebelum perhitungan
            luas = panjang * lebar
            print(textColor.green(f"Luas Persegi Panjang: {luas} square units."))
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

    elif opt == "3":
        try:
            print(textColor.yellow(text2art("Jajar Genjang", font="cybermedium")))
            alas = float(input("Alas: "))
            tinggi = float(input("Tinggi: "))
            loading_bar()  # Tambahkan loading bar sebelum perhitungan
            luas = alas * tinggi
            print(textColor.green(f"Luas Jajar Genjang: {luas} square units."))
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

    elif opt == "4":
        try:
            print(textColor.yellow(text2art("Trapesium", font="cybermedium")))
            a_atas = float(input("Alas Atas: "))
            a_bawah = float(input("Alas Bawah: "))
            tinggi = float(input("Tinggi: "))
            loading_bar()  # Tambahkan loading bar sebelum perhitungan
            luas = (1/2) * (a_atas + a_bawah) * tinggi
            print(textColor.green(f"Luas Trapesium: {luas} square units."))
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

    elif opt == "5":
        try:
            print(textColor.yellow(text2art("Segitiga", font="cybermedium")))
            alas = float(input("Alas: "))
            tinggi = float(input("Tinggi: "))
            loading_bar()  # Tambahkan loading bar sebelum perhitungan
            luas = (1/2) * (alas * tinggi)
            print(textColor.green(f"Luas Segitiga: {luas} square units."))
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

    elif opt == "6":
        try:
            print(textColor.yellow(text2art("Lingkaran", font="cybermedium")))
            phi = 3.14
            r = float(input("Jari-jari: "))
            loading_bar()  # Tambahkan loading bar sebelum perhitungan
            luas = phi * (r ** 2)
            print(textColor.green(f"Luas Lingkaran: {luas} square units."))
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

    elif opt == "7":
        try:
            print(textColor.yellow(text2art("Belah Ketupat", font="cybermedium")))
            diagonal1 = float(input("Diagonal 1: "))
            diagonal2 = float(input("Diagonal 2: "))
            loading_bar()  # Tambahkan loading bar sebelum perhitungan
            luas = (1/2) * (diagonal1 * diagonal2)
            print(textColor.green(f"Luas Belah Ketupat: {luas} square units."))
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

    else:
        print("OPSI TIDAK TERSEDIA!! -- (0-7)")
