class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound."

#subclasses
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

#Usage
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

print(dog.speak())
print(cat.speak())