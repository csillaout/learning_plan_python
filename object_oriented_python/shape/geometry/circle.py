import math

class Circle:
    def __init__(self, radius):
        """Initialize the Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the Circle."""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Calculate the circumference of the Circle."""
        return 2 * math.pi * self.radius
