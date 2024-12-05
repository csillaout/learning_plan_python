
#Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subcalsses must implement this method")

#Car sublclass
class Car(Vehicle):
    def move(self):
        print("Driving on the road.")

# Boat subclass
class Boat(Vehicle):
    
    def move(self):
        print("Sailing on water")

# Plane subclass
class Plane(Vehicle):
    
    def move(self):
       print("Flying in the air")

#create object
car = Car()
boat = Boat()
plane = Plane()

#Demonstrating polymorphism
vehicles = [car, boat, plane]

for vehicle in vehicles: 
    if isinstance(vehicle, Vehicle):
        print(f"{type(vehicle).__name__} is  a type of vehicle")
        vehicle.move()

   