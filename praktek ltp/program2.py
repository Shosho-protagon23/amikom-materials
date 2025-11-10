total_belanja = input("Totaal belanja: Rp ")
bayar = int(total_belanja)

if int(total_belanja) > 100000:
    print("lebih dari Rp 100.000??!! Nigga, you got Bonus voucher & diskon 5%")
    
    # diskon 5%
    diskon = int(total_belanja) * 5/100
    bayar = int(total_belanja) - diskon

print("Total anda: Rp %s" % bayar)
print("Terima kasih")
print("Datang kembali")