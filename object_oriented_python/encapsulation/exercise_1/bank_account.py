class BankAccount:
    def __init__(self, account_number, account_holder):
        self.__account_number = account_number #private attribute
        self.__account_holder = account_holder #private attribute 
        self.__balance = 0 #private attribute

    #getter for balance
    def get_balance(self):
        return self.__balance

    #method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deeposited {amount}. New balance:{self.__balance}")
        else:
            print("Deposit amount must be positive!")

    #method to withdraw money
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -=amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount!")
    
    #getter for account holder details
    def get_account_holder(self):
        return self.__account_holder

    #Setter for account holder detials (allows updating the holder's name)
    def set_account_holder(self, new_name):
        if new_name:
            self.__account_holder = new_name
            print(f"Account holder updated to: {self.__account_holder}")
        else:
            print("Invalid name!")

#create a bank account
account = BankAccount("123456789", "Csilla Toth")

#deposit money
account.deposit(500)

#withdraw money
account.withdraw(200)

#access balance using getter
print(f"Current balance: {account.get_balance()}")

#update account holder name using setter
account.set_account_holder("Csilla Travis 500.000 winner!")
