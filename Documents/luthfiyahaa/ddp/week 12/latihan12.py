#class
class orang:
    #properti
    name = ''
    age = ''

    def __init__(self, nama, umur) :
        self.name = nama
        self.age = umur

    def hello(self):
        print('hello',self.name)

#objek
mahasiswa = orang('bagus','19 tahun')
print(mahasiswa.name)
print(mahasiswa.age)

#objek 2
dosen = orang('dr. bagus','30 tahun')
print(dosen.name)
print(dosen.age)

class bank:
    norek = ""
    nama = ""
    saldo = 0
    BANK = 'Bank Syariah NF'

    def __init__(self,no,nama,saldo) :
        self.norek = no
        self.nama = nama
        self.saldo = saldo

    def nabung(self, uang):
        self.saldo += uang

    def tarik(self, uang):
        self.saldo -= uang

    def cetak(self):
        print(bank.BANK)
        print("Nomor Rekening")
        print()

agus = bank