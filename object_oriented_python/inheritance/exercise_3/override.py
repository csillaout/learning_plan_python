class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return " I amke a sound."

class Cat(Animal):
    def speak(self):
        return "Meow!"

cat = Cat("Shiskers")
print(cat.speak())