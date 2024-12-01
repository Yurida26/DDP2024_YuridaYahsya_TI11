import math

# Rumus: 6 * (sisi^2)
def luas_permukaan_kubus(sisi):
    return 6 * (sisi ** 2)

# Rumus: 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Rumus: 2 * π * r * (r + t)
def luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

# Rumus: luas alas + jumlah luas sisi tegak
def luas_permukaan_limas(luas_alas, luas_sisi_tegak):
    return luas_alas + luas_sisi_tegak

# Rumus: 2 * luas alas + keliling alas * tinggi
def luas_permukaan_prisma(luas_alas, keliling_alas, tinggi):
    return 2 * luas_alas + keliling_alas * tinggi
