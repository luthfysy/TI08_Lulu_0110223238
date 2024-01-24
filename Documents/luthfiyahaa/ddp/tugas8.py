#soal 1
def data_diri(nama,alamat,gender,umur,hobby):
    
    print('Data Diri :')
    print('nama',nama)
    print('alamat',alamat)
    print('gender',gender)
    print('umur',umur)
    print('hobby',hobby)

data_diri("luthfiyah","kp sugutamu","perempuan",19,"main genshin")

#soal 2
def nilai_kelulusan(nilai):
    if(nilai < 60 ):
        print('Gagal')
    elif(nilai >= 61 and nilai < 70):
        print('Baik')
    elif(nilai >= 71 and nilai ):
        print('Sangat Baik')
    elif(nilai >= 81 and nilai < 100):   
        print('Istimewa')      

nilai_kelulusan(78)    

#soal 3
def nilai_ganjil(n):
    for i in range(1,n+1,2):
        print(i,end=" ")

nilai_ganjil(100)