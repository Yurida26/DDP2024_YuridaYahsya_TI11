from Animal import Animal

class Cat(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, warna_mata ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.warna_mata = warna_mata

    # Method
    def info_cat(self):
        super().info_animal()
        print(f"Jenis Bulu\t\t: ", self.jenis_bulu, "\nWarna Mata\t\t: ", self.warna_mata)

#Objek
print()
cat = Cat("Kucing Anggora", "Ikan", "Di Rumah", "Melahirkan", "Lembut dan Tebal", "Biru")
print(" ## Info Cat 1 ##")
cat.info_cat()

print()
cat = Cat("Kucing Siamese", "Daging Segar", "Di Rumah", "Melahirkan", "Pendek dan Halus", "Hijau")
print(" ## Info Cat 2 ##")
cat.info_cat()

print()
cat = Cat("Kucing Persia", "Daging Segar", "Di Rumah", "Melahirkan", "Panjang dan Lembut", "Biru")
print(" ## Info Cat 3 ##")
cat.info_cat()