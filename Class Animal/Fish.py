from Animal import Animal

class Fish(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat

    # Method
    def info_fish(self):
        super().info_animal()
        print(f"Bernapas Menggunakan\t: ", self.bernapas, "\nHabitat\t\t\t: ", self.habitat)

#Objek
print()
fish = Fish("Ikan Hiu", "Daging", "Di laut", "Bertelur", "Menggunakan Insang", "Air Asin")
print(" ## Info Fish 1 ##")
fish.info_fish()

print()
fish = Fish("Ikan Koi", "Cacing Sutra", "Di Kolam", "Bertelur", "Menggunakan Insang", "Kolam")
print(" ## Info Fish 2 ##")
fish.info_fish()

print()
fish = Fish("Ikan Cupang", "Jentik Nyamuk", "Di Akuarium", "Bertelur", "Menggunakan Insang", "Akuarium")
print(" ## Info Fish 3 ##")
fish.info_fish()