from geometry.circle import Circle

if __name__ == "__main__":
    # Create a Circle with a radius of 5
    circle = Circle(5)

    # Print the area and circumference
    print(f"Circle with radius {circle.radius}")
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}")
