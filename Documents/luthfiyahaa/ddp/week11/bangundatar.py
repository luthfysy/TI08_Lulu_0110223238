# luas dan keliling bangun datar 
def segitiga_luas(alas, tinggi):
    hasil = (alas * tinggi) * 1/2
    return hasil

def segitiga_kel(sisi1, sisi2, sisi3):
    hasil = (sisi1 + sisi2 + sisi3)
    return hasil

def persegi_luas(sisi1, sisi2):
    hasil = (sisi1 * sisi2)
    return hasil

def persegi_kel(sisi):
    hasil = (sisi) * 4
    return hasil

def persegi_panjang_luas(p, l):
    hasil = (p * l)
    return hasil

def persegi_panjang_kel(p, l):
    hasil = (p + l) * 2
    return hasil

def belah_ketupat_luas(d1, d2):
    hasil = (d1 * d2) * 1/2
    return hasil

def belah_ketupat_kel(sisi1, sisi2, sisi3, sisi4):
    hasil = (sisi1 + sisi2 + sisi3 + sisi4)
    return hasil

def jajar_genjang_luas (alas, tinggi):
    hasil = (alas * tinggi)
    return hasil

def jajar_genjang_kel(panjang, lebar):
    hasil = 2 * (panjang) + 2 * (lebar)
    return hasil