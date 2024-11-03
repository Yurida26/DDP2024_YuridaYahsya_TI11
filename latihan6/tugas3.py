#Buat program untuk minta input jumlah baris dan buat
#rangkaian berikut ini
#*
#**
#***
#****
#Dan seterusnya sejumlah baris yang diinputkan
#Gunakan for loop dengan range

print("")
print("3. Buat program untuk minta input jumlah baris dan buat rangkaian sesuai soal di elena")
print("")

tanda_bintang = "*"
jumlah_bintang = int(input("Masukan Jumlah Bintang : "))

for i in range(1, jumlah_bintang + 1):
    print(tanda_bintang * i)
