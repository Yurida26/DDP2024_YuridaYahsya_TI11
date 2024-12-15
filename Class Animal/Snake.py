from Animal import Animal

class Snake(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, habitat ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.habitat = habitat

    # Method
    def info_snake(self):
        super().info_animal()
        print(f"Apakah Berbisa\t\t: ", self.berbisa, "\nHabitat\t\t\t: ", self.habitat)

#Objek
print()
snake = Snake("Ular Kobra", "Tikus", "Di Hutan", "Bertelur", "Berbisa", "Di Hutan Tropis")
print(" ## Info Snake 1 ##")
snake.info_snake()

print()
snake = Snake("Ular Sanca", "Tikus", "Di Pepohonan", "Bertelur", "Tidak Berbisa", "Di Rawa-Rawa")
print(" ## Info Snake 2 ##")
snake.info_snake()

print()
snake = Snake("Ular Piton", "Tikus", "Di Pohon", "Bertelur", "Tidak Berbisa", "Di Hutan Tropis")
print(" ## Info Snake 3 ##")
snake.info_snake()