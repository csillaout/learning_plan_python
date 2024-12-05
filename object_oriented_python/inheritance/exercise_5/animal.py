from unicodedata import name


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__ (self, name, species, breed):
        super().__init__(name, species)
        self.breed =breed
