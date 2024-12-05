class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "I am an animal."
    
class Dog(Animal):
    def bark(self):
        return "Woof!"


dog = Dog("Buddy")
print(dog.name)
print(dog.speak())
print(dog.bark())