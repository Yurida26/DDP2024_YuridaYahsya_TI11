import math

# Rumus: π * jari_jari^2
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari**2

# Rumus: sisi * sisi
def luas_persegi(sisi):
    return sisi * sisi

# Rumus: 0.5 * alas * tinggi
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Rumus: panjang * lebar
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Rumus: alas * tinggi
def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi