class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        print(f"vehicle make: {self.make}")
        print(f"vehicle's model: {self.model}")
        print(f"vehicle's year: {self.year}")

#subclass
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__( make, model, year)
        self.doors = doors
    
    def info(self):
         print(f"vehicle make: {self.make}")
         print(f"vehicle's model: {self.model}")
         print(f"vehicle's year: {self.year}")
         print(f"vehicle's doors: {self.doors}")



class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def info(self):
         print(f"vehicle make: {self.make}")
         print(f"vehicle's model: {self.model}")
         print(f"vehicle's year: {self.year}")
         print(f"vehicle's type: {self.type}")



car = Car("Toyota", "Corolla", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")

car.info()  # Displays car details
motorcycle.info()  # Displays motorcycle details