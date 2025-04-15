class InvalidExperienceException(Exception):
    pass

class Employee:
    def __init__(self, name: str, age: int, experience: str, address,salary,employment):
        self._name = None
        self._age = None
        self._experience = None
        self._address = address  # "Has-a" relationship with Address class
        self._salary=salary
        self._employment=employment
        
        self.set_name(name)
        self.set_age(age)
        self.set_experience(experience)
    
    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age: int):
        self._age = age
    
    def get_experience(self):
        return self._experience
    
    def set_experience(self, experience: str):
        if not self._is_valid_experience(experience):
            raise InvalidExperienceException("Invalid experience format")
        self._experience = experience
    
    def compute_years(self):
        int_part, frac_part = map(int, self._experience.split('.'))
        if frac_part == 10 or frac_part == 11:
            return int_part + 1
        return int_part
    
    def _is_valid_experience(self, experience: str):
        parts = experience.split('.')
        if not parts[0].isdigit() or not parts[1].isdigit():
            return False
        int_part, frac_part = int(parts[0]), int(parts[1])
        return 0 <= frac_part <= 11
    
    def __str__(self):
        return (f"Employee Details:\n"
            f"Name      : {self._name}\n"
            f"Age       : {self._age}\n"
            f"Experience: {self.compute_years()} years\n"
            f"Address   : {self._address}\n"
            f"Salary    : {self._salary}\n"
            f"Employment: {self._employment}")

class Address:
    def __init__(self, line1, line2, city, state, pin):
        self._line1 = line1
        self._line2 = line2
        self._city = city
        self._state = state
        self._pin = pin

    def __str__(self):
        return f"{self._line1}, {self._line2}, {self._city}, {self._state} - {self._pin}"

class Salary:
    def __init__(self,basic=0.0,hra=0.0,allowance=0.0):
        self.basic=basic
        self.hra=hra
        self.allowance=allowance
    def compute_total_salary(self):
        return self.basic+self.hra+self.allowance
    def __str__(self):
        return (f"Basic: {self.basic}, HRA: {self.hra}, Allowance: {self.allowance}, Total Salary: {self.compute_total_salary()}")
    
    
class Employment:
    def __init__(self,date_of_joining,notice_period:int=90):
        self.date_of_joining=date_of_joining
        self.notice_period=notice_period
    def __str__(self):
        return (f"Date of joining: {self.date_of_joining}, Notice period: {self.notice_period} days")
    
class Hiring:
    def __init__(self):
        self.technical_round = 20
        self.manager_round = 5
        self.hr_round = 5
        self.offer_rollout = 10
    def __str__(self):
        return (f"Technical Rounds: {self.technical_round} days, Manager Round: {self.manager_round} days, "
                f"HR Round: {self.hr_round} days, Offer Rollout: {self.offer_rollout} days")

class Console:
    @staticmethod
    def print_details(employee,hiring):
        print(employee)
        print("Hiring Details:")
        print(hiring)

try:
    address = Address("123 Street", "Apt 4B", "New Delhi", "ND", "10001")
    salary=Salary(70000,5000,3000)
    employment=Employment("2025-03-12")
    hiring=Hiring()
    emp = Employee("Jai Hind", 30, "5.10", address,salary,employment)
    Console.print_details(emp,hiring)
except InvalidExperienceException as e:
    print(e)
    
    
class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.__account_number = account_number  
        self.__balance = initial_balance  

  
    def get_account_number(self):
        return self.__account_number

  
    def get_balance(self):
        return self.__balance

  
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

 
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")


def main():
     
    account = BankAccount("12345", 100.0)
    
    account.deposit(50.0)
    
    account.withdraw(30.0)
    
    account.withdraw(150.0)
    
    print("Account Number:", account.get_account_number())
    print("Final Balance:", account.get_balance())

if __name__ == "__main__":
    main()


class Calculator:
    def __init__(self):
        pass  

    def add(self, a, b):
        return a + b

   
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

def main():
    
    calc = Calculator()

    print(calc.add(5, 3))
    print(calc.subtract(10, 4))
    print(calc.multiply(6, 2))
    print(calc.divide(8, 2))

    try:
        print("10 / 0 =", calc.divide(10, 0))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
    
    
class Temperature:
    def __init__(self, initial_celsius=0.0):
        self.__celsius = initial_celsius  

   
    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    
    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__celsius = (value - 32) * 5 / 9


def main():
  
    temp = Temperature(25)

    
    print("Temperature in Celsius:", temp.celsius)
    print("Temperature in Fahrenheit:", temp.fahrenheit)

   
    temp.fahrenheit = 98.6
    print("New Temperature in Celsius:", temp.celsius)
    print("New Temperature in Fahrenheit:", temp.fahrenheit)


if __name__ == "__main__":
    main()

