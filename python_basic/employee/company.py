from employee import SalaryEmployee, HourlyEmployee, CommissionEmployee#employee is the file name, Employee is the class name

class Company:
    def __init__(self):
        self.employees = [] #initialise the properties as an empty list
    
    def add_employee(self, new_employee): #define a method to add new employee to the list
        self.employees.append(new_employee)

    def display_employees(self): #wirte a method to display the employee's name
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('------------------------')
    
    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount:, ${i.calculate_paycheck():,.2f}')
            print('----------------------------------')
    
def main():  #define the main program 
    my_company = Company() #call the company object and assign to the my_company constractor

    employee1 = SalaryEmployee('Sarah', 'Hess', 50000)  #add new employees to the comp
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Lee', 'Smith', 25, 50) 
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Bob', 'Brown', 30000, 5, 200) 
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()