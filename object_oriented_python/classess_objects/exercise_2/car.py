class Car:
    def __init__(self, make, model, year, fuel=50):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel
    
    def drive(self, distance):
       fuel_needed = distance // 10
       if fuel_needed > self.fuel:
           print(f"Not enough fuel to drive {distance} km. Refuel first!")
       else:
            self.fuel -=fuel_needed
            print(f"Driving {distance} km ... fuel left: {self.fuel} units")
    
    def refuel(self, amount):
        self.fuel += amount
        print(f"Refueling {amount} units ... Fuel now: {self.fuel} units")
    
   
car = Car("toyota", "corolla", 2020)
car.drive(120)
car.refuel(20)


