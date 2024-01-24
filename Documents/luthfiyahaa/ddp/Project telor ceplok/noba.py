bensin = {
    "Pertalite": {"harga": 10000, "jarak": 12},
    "Pertamax": {"harga": 14000, "jarak": 13},
    "Pertamax Turbo": {"harga": 17000, "jarak": 13.5}
}

jarak_kota = {
    "Jakarta": 20,
    "Bekasi": 35.7,
    "Depok": 5,
    "Tangerang": 99,
    "Bogor": 120.6
}

nama_kendaraan = input("Nama Kendaraan: ")
jenis_bensin = input("Jenis Bensin (Pertalite, Pertamax, Pertamax Turbo):")
kota_tujuan = input("Kota Tujuan (Jakarta, Bekasi, Depok, Tangerang, Bogor): ")

match nama_kendaraan:
    case "Motor"|"Mobil"|"motor"|"mobil":
        sisi = (input("Masukan nilai sisi: "))
        luas = sisi*sisi
        print(luas)
    case "2"|"Lingkaran"|"lingkaran":
        jarijari = int(input("Masukan nilai jarijari: "))
        luas = 3.14*jarijari*2
        print(luas)
    case "3"|"Segitiga"|"segitiga":
        alas = int(input("Masukan nilai alas: "))
        tinggi = int(input("Masukan nilai tinggi: "))
        luas = alas*tinggi/2
        print(luas)
    case _:
        print("coba lagi")