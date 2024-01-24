#soal 1
motor=["B 1234 SZX","motor",1500,"putih"]
print(motor)

#soal 2
motor.append("18jt")
motor.append("2roda")
motor.insert(4,"beat")
motor.insert(1,"matic")
print(motor)

#soal 3
luas = input("hitung luas bangun datar berikut ini")
match luas:
    case "persegi":
        sisi=int(input("masukan nilai:"))
        luas=sisi*sisi
        print(luas)

    case "lingkaran":
        jarijari=int(input("masukan nilai:"))
        luas=3.14*jarijari*jarijari
        print(luas)

    case "segitiga":
        alas=int(input("masukan nilai:"))
        tinggi=int(input("masukan nilai:"))
        luas=alas*tinggi*1/2
        print(luas)