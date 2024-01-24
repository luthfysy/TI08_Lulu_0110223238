#bensin
bensin = {
    'pertalite': {
        'hargaPerLiter': 10000,
        'jarakTempuh': 12,
    },
    'pertamax': {
        'hargaPerLiter': 14000,
        'jarakTempuh': 13,
    },
    'pertamax turbo': {
        'hargaPerLiter': 17000,
        'jarakTempuh': 13.5,
    }
}

#kota
jarakKota = {
    'jakarta': 20,
    'bekasi': 35.7,
    'depok': 5,
    'tangerang': 99,
    'bogor': 120.6
}


def gatau_mau_namain_apaan():
    kendaraan = input('jenis kendaraan? (mobil, motor): ')
    jenisBensin = input(f'jenis bensin? ({", ".join(list(bensin.keys()))}): ')
    kota = input(f'kota yang dituju? ({", ".join(list(kota.keys()))}): ')

    pemakaianBensin = round(jarakKota[kota] / bensin[jenisBensin]['jarakTempuh'], 2)
    total_harga_bensin = used_fuel * fuel[fuel_type]['hargaPerLiter']

    print(f'jenis kendaraan: {kendaraan}')
    print(f'jenis bensin: {jenisBensin}')
    print(f'kota yang dituju: {kota}')
    print(f'pemakaian bensin: {used_fuel}')
    print(f'total harga dari bensin: {total_fuel_price}')


gatau_mau_namain_apaan()