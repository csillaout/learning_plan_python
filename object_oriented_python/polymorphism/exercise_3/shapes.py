import math
#Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subcalsses must implement this method")

#Rectangle sublclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width*self.height

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Triangle subclass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

#Demonstrating polymorphism
shapes = [Rectangle(5,10),
Circle(7),
Triangle(6,8)]

for shape in shapes: 
    print(f"Area of {type(shape).__name__}:{shape.area():.2f}")