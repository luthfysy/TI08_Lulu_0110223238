pelanggan = "Budi Santoso"
totalBelanja = 50000

if(totalBelanja > 100000) :
    keterangan = "Selamat Anda Mendapat Hadiah"
else:
    keterangan = "Terimakasih sudah berbelanja"

print("Pelanggan",pelanggan,"\nTotal Belanja Anda Rp.",totalBelanja,
      "\n",keterangan)        

nama = "Budi Santoso"
nilai = 69.99

if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai < 85):
    grade = "B"
elif(nilai >= 60 and nilai < 75):
    grade = "C" 
elif(nilai >= 30 and nilai < 60):
    grade = "D"
else:
    grade ="E"         

print(nama,"Mendapatkan grade",grade)    