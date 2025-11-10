import textColor

# Satu kondisi (if)
lulus = "tidak"
if lulus == "tidak":
    print("kamu harus ikut remidi")

# Dua kondisi (if & else)
lulus = input("ya atau tidak? ")
if lulus == "ya":
    print("selamat, anda bisa lanjut")
else:
    print("kamu harus ikut remidi")

# Lebih dari 2 kondisi (if, elif, & else)
nilai = int(input("Nilai mu kawan: "))

if nilai >= 90:
    print("Ranking ==> A")
elif nilai >= 80:
    print("Ranking ==> B")
elif nilai >= 70:
    print("Ranking ==> C")
else:
    print("Ranking ==> Nigga what?")