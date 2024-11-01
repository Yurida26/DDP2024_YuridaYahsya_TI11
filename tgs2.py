# 2. Buat program python dengan match case untuk 
# mengitung luas bangun datar :
penampung = '''
Tugas Nomer : 2
Selamat Datang di Program Perhitungan Menghitung Luas Bangun Datar Sederhana - Yuri_TI11
Syarat Menggunakan - Masukan Pilihan Perhitungan Telebih Dahulu!!  :

1. Luas Persegi
2. Luas Lingkaran
3. Luas Segitiga

Masukkan pilihan (1/2/3):  '''

pilihan = input(penampung)

# Match Case - Perhitungan Luas - Luas Persegi, Luas Lingkaran, Luas Segitiga
match pilihan:
    # jika pilih 1, maka menghitung Luas Persegi  
    #  Diketahui Rumus Persegi : L = sisi x sisi.
    case "1":
        print ("Kamu Memilih - Perhitungan Luas Persegi : ")
        sisi = int(input("Masukan sisi?"))
        luasP = sisi * sisi
        print("Luas Persegi Yang Sisi = ", sisi, ",adalah", luasP)
        
    # jika pilih 2, maka menghitung Luas Lingkaran   
    #  Diketahui Rumus Lingkaran : L  = π x r²
    case "2":
        print ("Kamu Memilih - Perhitungan Luas Lingkaran : ")
        phi = 22/7
        jari_jari = float(input("Masukan Jari - Jari? "))
        luasLingkaran = phi * jari_jari * jari_jari
        print("Luas Lingkaran Yang Jari = ", jari_jari, ",adalah ", luasLingkaran)
    
    # jika pilih 3, maka menghitung Luas Segitiga  
    #  Diketahui Rumus Segitiga :L = 1/2 x a x t
    case "3":
        print ("Kamu Memilih - Perhitungan Luas Segitiga : ")
        alas = float(input("Masukan Alas? "))
        tinggi = float(input("Masukan Tinggi? "))
        luasSegitiga = 1/2 * alas * tinggi
        print("Luas Segitiga Yang Alas = ", alas, " dan Tinggi ", tinggi, ",adalah ", luasSegitiga)
     
    # selain pilihan di atas, maka keterangan : salah pilih angka   
    case _:
        print ("Pilih Pilihan Sesuai Dengan Pilihan Yang Ada !! : ")