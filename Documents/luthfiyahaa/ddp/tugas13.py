# Parent class
class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

# Child classes
class Rhinoceros(Animal):
    def __init__(self, name, food, habitat, reproduction, horn_length, endangered):
        super().__init__(name, food, habitat, reproduction)
        self.horn_length = horn_length
        self.endangered = endangered

    def charge(self):
        print(f"{self.name} is charging!")

    def display_info(self):
        print(f"{self.name} is a rhinoceros with a horn length of {self.horn_length} meters.")

class Fish(Animal):
    def __init__(self, name, food, habitat, reproduction, fin_color, scale_pattern):
        super().__init__(name, food, habitat, reproduction)
        self.fin_color = fin_color
        self.scale_pattern = scale_pattern

    def swim(self):
        print(f"{self.name} is swimming!")

    def display_info(self):
        print(f"{self.name} is a fish with {self.fin_color} fins.")

class Snake(Animal):
    def __init__(self, name, food, habitat, reproduction, venomous, length):
        super().__init__(name, food, habitat, reproduction)
        self.venomous = venomous
        self.length = length

    def slither(self):
        print(f"{self.name} is slithering!")

    def display_info(self):
        venom_status = "venomous" if self.venomous else "non-venomous"
        print(f"{self.name} is a {venom_status} snake with a length of {self.length} meters.")

# Contoh penggunaan
rhino = Rhinoceros("Rhino", "Grass", "Savannah", "Viviparous", 1.5, True)
rhino.charge()
rhino.display_info()

fish = Fish("Nemo", "Plankton", "Ocean", "Oviparous", "orange", "striped")
fish.swim()
fish.display_info()

snake = Snake("Cobra", "Rodents", "Jungle", "Oviparous", True, 2)
snake.slither()
snake.display_info()
