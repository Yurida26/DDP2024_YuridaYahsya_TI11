from Animal import Animal

class Bird(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    # Method
    def info_bird(self):
        super().info_animal()
        print(f"Warna\t\t\t: ", self.warna, "\nJenis Paruh \t\t: ", self.paruh)

#Objek
print()
bird = Bird("Burung Elang", "Daging", "Di tebing", "Menghasilkan telur", "Coklat", "Bengkok dan Lancip")
print(" ## Info Bird 1 ##")
bird.info_bird()

print()
bird = Bird("Burung Cendrawasih", "Biji Bijian", "Di Pohon", "Menghasilkan telur", "Kuning", "Bengkok dan Lancip")
print(" ## Info Bird 2 ##")
bird.info_bird()

print()
bird = Bird("Burung Gagak", "Daging", "Di Hutan", "Menghasilkan telur", "Hitam", "Bengkok dan Lancip")
print(" ## Info Bird 3 ##")
bird.info_bird()
