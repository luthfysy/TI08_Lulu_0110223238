# soal 1 
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40},
]

def lulus_aja(data):
    list_baru = []

    for item in data:
        if item['nilai'] > 65:
            list_baru.append(item['nama'])

    return list_baru
print(lulus_aja(hasil_akhir))

# soal 2
buah_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def reverse(data):
    new_list = []

    for item in range(len(data)):
        identity = item + 1
        new_list.append(data[-(identity)])

    return new_list
print(reverse(buah_buah))

# soal 3

def duplicate(data):
    new_list = []

    for item in data:
        new_list.append(item)
        new_list.append(item)

    return new_list
print(duplicate(buah_buah))

# soal 4
nama = 'Nurul Fikri'
vocal = ['a', 'i', 'u', 'e', 'o', ' ']

def konsonan(data):
    new_nama = ''

    for item in data:
        if item not in vocal:
            new_nama += item
    return new_nama
print(konsonan(nama))