#superclass
class Animal:
    def speak(self):
        return "I make a sound"

#sublclass
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())