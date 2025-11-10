from art import *

nilai = int(input("Nilai mu: "))

if nilai > 100:
    print(text2art("Wait.. holdup.. Oh sh#t", font="small"))
elif nilai >= 90:
    print("rank = A")
elif nilai >= 80:
    print("rank = B+")
elif nilai >= 70:
    print("rank = B")
elif nilai >= 60:
    print("rank = C+")
elif nilai >= 50:
    print("rank = C")
elif nilai >= 40:
    print("rank = D")

else:
    print("rank = bro... :v")

print(f"Hasil: {nilai}")