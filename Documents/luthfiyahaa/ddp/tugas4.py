nama = "Lee Felix"
usia = 23

if(usia < 17):
    keterangan = "Anak anak"
elif(usia >= 18 and usia < 65):
    keterangan = "Dewasa"
else:
    keterangan = "Lanjut Usia"

print(nama,"kategori usia",keterangan)        


bill_1 = 7
bill_2 = 3

if(bill_1 > bill_2):
    pesan = "7 lebih besar dari 3"
elif(bill_1 < bill_2):
    pesan = "3 lebih kecil dari 7"
else:
    pesan = "bill 1 dan bill 2 memiliki nilai yang sama"

print(pesan)            