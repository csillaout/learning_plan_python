class ParentClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

class ChildClass(ParentClass):  # Inheriting from ParentClass
    def __init__(self, name, age):
        super().__init__(name)  # Calling the __init__ method of the ParentClass
        self.age = age
    
    def greet(self):
        super().greet()  # Calling the greet method of the ParentClass
        print(f"I am {self.age} years old.")

# Using the child class
parent = ParentClass("Greta")
child = ChildClass("Alice", 25)
child.greet()
parent.greet()
