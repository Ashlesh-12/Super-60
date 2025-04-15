# class Address:
#     def __init__(self, street, city, zip_code):
#         self.street = street
#         self.city = city
#         self.zip_code = zip_code

# class Employee:
#     def __init__(self, name, emp_id, address,role,basic_salary,HRA):
#         self.name = name
#         self.emp_id = emp_id
#         self.address = address
#         self.role=role
#         self.basic_salary=basic_salary
#         self.HRA=HRA

# def store_data(employee):
#     employee.name = input("Enter the name of the employee: ")
#     employee.emp_id = input("Enter the Employee ID: ")
#     street = input("Enter the street name: ")
#     city = input("Enter the city name: ")
#     zip_code = input("Enter the zip code: ")
#     role=int(input("Enter the role: "))
#     basic_salary=float(input("Enter the basic salary: "))
#     HRA=float(input("Enter the HRA: "))
#     employee.address = Address(street, city, zip_code)
    
# class Employee_report:
#         def __init__(self,report_date):
#                 self.report_date=report_date
                
#         def display_employees(self,employee_list):
#                 print(f"Employee Report- ",self.report_date)
                
# class Role_builder:
#         def get_role_description(self,role_id):
#                 roles={1: 'Manager', 2: 'Developer', 3: 'Analyst', 4: 'Tester'}
#                 return 
        
# class Salary_calculator:
#         def get_allowance(self,basic,percentage):
#                 return (basic*percentage)/100

# def show_data(employee):
#     print(f"Employee Name: {employee.name}")
#     print(f"Employee ID: {employee.emp_id}")
#     print("Address:")
#     print(f"Street: {employee.address.street}")
#     print(f"City: {employee.address.city}")
#     print(f"Zip Code: {employee.address.zip_code}")

# def main():
#     employee=[]
#     for i in range(4):
#         emp = Employee(None,None,None,None,None,None)  
#         store_data(emp)
#         employee.append(emp)
#         show_data(emp)

# main()

import numpy as np