def konversi_bilangan():
    """
    Program sederhana untuk mengkonversi bilangan antar oktal, desimal,
    heksadesimal, dan biner.
    """
    print("Selamat datang di Program Konversi Bilangan!")
    print("===========================================")

    while True:
        try:
            print("\nPilih format bilangan sumber:")
            print("1: Desimal")
            print("2: Biner")
            print("3: Oktal")
            print("4: Heksadesimal")
            pilihan_sumber = input("Masukkan pilihan (1-4): ")

            if pilihan_sumber not in ['1', '2', '3', '4']:
                print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 4.")
                continue

            bilangan_input = input("Masukkan bilangan yang akan dikonversi: ")

            basis_sumber = None
            if pilihan_sumber == '1':
                basis_sumber = 10
            elif pilihan_sumber == '2':
                basis_sumber = 2
            elif pilihan_sumber == '3':
                basis_sumber = 8
            elif pilihan_sumber == '4':
                basis_sumber = 16

            # Konversi bilangan_input ke integer (basis 10) terlebih dahulu
            nilai_desimal = int(bilangan_input, basis_sumber)

            print("\nPilih format bilangan tujuan:")
            print("1: Desimal")
            print("2: Biner")
            print("3: Oktal")
            print("4: Heksadesimal")
            pilihan_tujuan = input("Masukkan pilihan (1-4): ")

            if pilihan_tujuan not in ['1', '2', '3', '4']:
                print("Pilihan tujuan tidak valid. Silakan masukkan angka 1 sampai 4.")
                continue

            hasil_konversi = ""
            if pilihan_tujuan == '1':
                hasil_konversi = str(nilai_desimal)  # Sudah desimal
                format_tujuan = "Desimal"
            elif pilihan_tujuan == '2':
                # bin() menghasilkan prefix '0b', kita hapus dengan [2:]
                hasil_konversi = bin(nilai_desimal)[2:]
                format_tujuan = "Biner"
            elif pilihan_tujuan == '3':
                # oct() menghasilkan prefix '0o', kita hapus dengan [2:]
                hasil_konversi = oct(nilai_desimal)[2:]
                format_tujuan = "Oktal"
            elif pilihan_tujuan == '4':
                # hex() menghasilkan prefix '0x', kita hapus dengan [2:]
                # .upper() agar huruf heksa menjadi kapital
                hasil_konversi = hex(nilai_desimal)[2:].upper()
                format_tujuan = "Heksadesimal"

            print(f"\n✅ Hasil Konversi:")
            print(f"Bilangan sumber: **{bilangan_input}**")
            print(f"Hasil konversi ke **{format_tujuan}**: **{hasil_konversi}**")

        except ValueError as e:
            # Menangkap kesalahan jika input bilangan tidak valid untuk basis yang dipilih
            print(f"\n❌ Error: Input bilangan '{bilangan_input}' tidak valid untuk basis {basis_sumber}.")
            print("Pastikan digit yang dimasukkan sesuai dengan basis yang dipilih.")
        except Exception as e:
            print(f"\n❌ Terjadi kesalahan: {e}")

        lanjut = input("\nIngin melakukan konversi lagi? (y/t): ").lower()
        if lanjut != 'y':
            print("Terima kasih. Sampai jumpa!")
            break


# Jalankan fungsi utama
if __name__ == "__main__":
    konversi_bilangan()