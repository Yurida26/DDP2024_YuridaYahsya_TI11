my_list=[1,2,3,4,5,6,7,8,9]
my_list.append("Hello")
my_list.remove(5)
my_poplist = my_list.pop(4)
print(my_list) 
print(my_poplist) 

#Mengubah elemen dlm dictionary
kontak = {1: "budi", "ibu_budi" : "098765", "budi" : "09876" }
kontak["budi"] = "0839021348"
print(kontak)

#menambaha elemen kedalam dictionari
kontak["budi"] = "0398742"
print(kontak)

kendaraan = ["beat karbu", "motor", 200, "pink", 2]
print(kendaraan)

kendaraan.append("13jt")
kendaraan.append("matic")
print(kendaraan)

kendaraan.insert(2, "honda")
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))

hitung_luas =  int(input("""pilih salah satu
1. Hitung luas persegi
2. Hitung luas lingkaran
3. Hitung luas segitiga
"""))

match hitung_luas:
    case 1:
        print("Menghitung Luas Persegi")
        sisi = int(input("Masukkan nilai sisi: "))
        hitung_luas_persegi = sisi **2
        print(f"Jadi luas persegi dengan sisi {sisi} cm adalah {hitung_luas_persegi} cm^2")
    case _:
        print("pilihan tidak valid")


