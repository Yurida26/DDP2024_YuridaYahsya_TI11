# Keliling Tabung
# 2 * 3,14 * R
# K = 2πr
import math
tinggi = float(input("Masukan - Tinggi Tabung :"))
jari_jari = float(input("Masukan - Jari - Jari Tabung :"))
k_tabung = 2 * math.pi * jari_jari
print("5.1. Hasil Tabung Keliling : ", k_tabung)

# Luas Tabung
# L = 2 * 3,14 * R * (R+T)
import math
tinggi = float(input("5.1 Masukan - Tinggi Tabung :"))
jari_jari = float(input("5.2 Masukan - Jari - Jari Tabung :"))
l_tabung = 2 * math.pi * jari_jari * (jari_jari + tinggi)
print("5.2. Hasil Tabung Luas :", l_tabung)