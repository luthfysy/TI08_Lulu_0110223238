#soal 1
class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa tidak berasa")
        elif self.skala >= 2 and self.skala <= 4:
            print("Dampak gempa: bangunan retak-retak")
        elif self.skala > 4 and self.skala <= 6:
            print("Dampak gempa: bangunan roboh")
        else:
            print("Dampak gempa: bangunan roboh dan berpotensi tsunami")

gempa_jakarta = Gempa("Jakarta", 5.5)
gempa_jakarta.dampak()