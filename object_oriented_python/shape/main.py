from geometry.circle import Circle
from geometry.rectangle import Rectangle

if __name__ == "__main__":
    # Create a Circle with a radius of 5
    circle = Circle(5)
    rectangel = Rectangle(5,6)

    # Print the area and circumference
    print(f"Circle with radius {circle.radius}")
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}")

    print(f"Rectange with lengtht {rectangel.length} and width {rectangel.width}")
    print(f"Area:{rectangel.area():.2f}")
    print(f"Circumference of a rectangle is {rectangel.circumference():.2f}")