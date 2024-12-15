from Animal import Animal

class Dog(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_ras, kemampuan_melacak):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_ras = jenis_ras
        self.kemampuan_melacak = kemampuan_melacak

    # Method
    def info_dog(self):
        super().info_animal()
        print(f"Jenis Ras\t\t: ", self.jenis_ras, "\nKemampuan Melacak\t: ", self.kemampuan_melacak)

#Objek
print()
dog = Dog("Anjing Labrador", "Daging", "Di Rumah", "Melahirkan", "Labrador Retriever", "Sangat Baik")
print(" ## Info Dog 1 ##")
dog.info_dog()

print()
dog = Dog("Anjing Herder", "Daging", "Di Rumah", "Melahirkan", "German Shepherd", "Sangat Baik")
print(" ## Info Dog 2 ##")
dog.info_dog()

print()
dog = Dog("Anjing Beagle", "Daging", "Di Rumah", "Melahirkan", "Beagle", "Sangat Baik")
print(" ## Info Dog 3 ##")
dog.info_dog()