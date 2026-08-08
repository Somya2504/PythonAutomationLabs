class Employee:
    def __init__(self,employee_id,employee_name,department,salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("Employee Details:")
        print("-" * 40)
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print("-" * 40)

    def increment_salary(self, amount):
        self.salary += amount
        # print(f"Updated Employee Salary: {self.salary}")
        return self.salary

    def calculate_annual_salary(self):
        return self.salary * 12

employee = Employee(111,"Somyakanta","QA",100000)

employee.display_details()

new_salary = employee.increment_salary(25000)
print(f"New Salary: {new_salary}")
print("-" * 40)

employee.display_details()

annual_salary = employee.calculate_annual_salary()
print(f"Annual Salary: {annual_salary}")
print("-" * 40)