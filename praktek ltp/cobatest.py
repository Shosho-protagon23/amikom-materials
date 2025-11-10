from art import *
import textColor

print(text2art("By DeadSec_Echof", font="small"))

nilai = int(input("Nilai kamu: "))

if nilai >= 70:
    print(textColor.blue(text2art("Lulus", font="small")))
    if nilai >= 90:
        print(textColor.green("Nilai == A"))
    elif nilai >= 80:
        print(textColor.yellow("Nilai == B"))
    else:
        print(textColor.red("Nilai == C"))

else:
    print(textColor.red(text2art("Tidak Lulus", font="small")))