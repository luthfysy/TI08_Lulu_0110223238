#quizz 1
Kendaraan = input('jenis kendaraan (motor/mobil: )')
jenisBensin = input('jenis bensin (pertalite/pertamax/pertamax turbo: )')
kota = input('kota tujuan (jakarta, bekasi, depok, tanggerang, bogor: )') 

if jenisBensin == 'pertalite':
    harga = 10000
    jarakTempuh = 12

elif jenisBensin == 'pertamax':
    harga = 14000
    jarakTempuh = 13 

elif jenisBensin == 'pertamax turbo':
    harga =17000
    jarakTempuh = 13,5


# pengecekan kota 
if kota == 'jakarta':   
    jarakkota= 20

elif kota == 'bekasi':
    jarakkota = 35.7

elif kota == 'depok':
    jarakkota = 5

elif  kota == 'Tanggerang':
    jarakkota = 99

elif kota == 'bogor':
    jarakkota = 120.6

print("Kendaraan:", Kendaraan)
print("Jenis bensin:", jenisBensin)
print('Kota tujuan:', kota)
print('Pemakaian bensin:', jarakkota/jarakTempuh)
print('total harga dari bensin:', (jarakkota/jarakTempuh)*harga)

#quizz 2

makanan = input('jenis makanan (nasi goreng/mie goreng/ayam geprek: )')
