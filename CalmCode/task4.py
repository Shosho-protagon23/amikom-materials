## Menentukan umur tua atau muda

def umur_usia(umur):

    # menentukan muda atau tua
    # usia < 45 maka muda
    # usia > 45 maka tua
    if umur <= 45:
        return "Usia Muda"
    else:
        return "Usia Tua"

# Bagian uji muda atau tua

try:
    umur_input = int(input("Masukkan umur anda: "))

    # memastikan usia adalah angka positif
    if umur_input < 0:
        print("Usia tidak boleh angka negatif.")
    else:
        kategori = umur_usia(umur_input)
        print(f"Usia anda adalah {umur_input} tahun.")
        print(f"Kategori {kategori}")

except ValueError:
    print("Usia harus angka bulat.")
