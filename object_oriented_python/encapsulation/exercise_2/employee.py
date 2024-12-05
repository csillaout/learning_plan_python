class Employee:
    def __init__(self, name, position, salary):
        self.__name = name #private attribute
        self.__position = position #private attribute 
        self.__salary = salary #private attribute

    #getter for employee's name
    def get_name(self):
        return self.__name
    
    #setter for employee's name
    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            print(f"Employee's name updated to: {self.__name}")
        else:
            print("Invalid name!")

    #getter for employee's position
    def get_position(self):
        return self.__position
    
    #setter for employee's position
    def set_position(self, new_position):
        if new_position:
            self.__position = new_position
            print(f"Employee's position updated to: {self.__position}")
        else:
            print("Invalid position!")

    #getter for employee's salary
    def get_salary(self):
        return self.__salary

    #method to promote
    def promote(self, new_position, raise_percentage):
        if new_position:
            self.__position = new_position 
            self.__salary += self.__salary *(raise_percentage/100)
            print(f"Employee's position updated to: {self.__position}")
            print(f"new salary: {self.__salary:.2f}")
        else:
            print("Invalid promotion details!")

#create employee object
employee = Employee("Csilla", "Apprentice", 24000)
employee.set_name("Csilla Travis")
employee.set_position("VicePresident")
employee.get_name()
employee.get_position()
employee.get_salary
employee.promote("VicePresident", 100)

