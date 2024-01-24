#parent class
class binatang:

    def __init__(self, fname, makanan, hidup, berkembangbiak):
        self.name = fname
        self.makanan = makanan
        self.hidup = hidup
        self.biak = berkembangbiak

#child classes
class cheetah(binatang):
    def __init__(self, fname, makanan, hidup, berkembangbiak):
        super().__init__(fname, makanan, hidup, berkembangbiak)

    def hya(self):
        print(f'Nama \t:  {self.name}  \nMakanan :  {self.makanan} \nHidup \t: {self.hidup} \nBerkembangbiak \t: {self.biak} ')

class kambing(binatang):
    def __init__(self, fname, makanan, hidup, berkembangbiak):
        super().__init__(fname, makanan, hidup, berkembangbiak)

    def mbe(self):
        print(f'Nama \t:  {self.name}  \nMakanan :  {self.makanan} \nHidup \t: {self.hidup} \nBerkembangbiak \t: {self.biak} ')

class burung(binatang):
    def __init__(self, fname, makanan, hidup, berkembangbiak):
        super().__init__(fname, makanan, hidup, berkembangbiak)

    def cukurukuk(self):
        print(f'Nama \t:  {self.name}  \nMakanan :  {self.makanan} \nHidup \t: {self.hidup} \nBerkembangbiak \t: {self.biak} ')
                       
#contoh penggunaan
h1 = cheetah("cheetah", "daging", "darat", "beranak")
h1.hya()
s1 = kambing("kambing", "rumput", "darat", "beranak")
s1.mbe()
a1 = burung("burung", "pakan", "darat", "bertelur")
a1.cukurukuk()