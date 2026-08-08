class Employee:
    def __init__(self, emp_id, name,department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Employee Salary: {self.salary}")

employee_1 = Employee(1001,"Somyakanta", "QA",100000)
employee_2 = Employee(1002,"Sangeeta", "Devloper", 11000)

print("Employee ID:", employee_1.emp_id)
print("Employee Name:", employee_1.name)
print("Employee Department:", employee_1.department)
print("Employee Salary:", employee_1.salary)

print("************************************")

print(f"Employee ID: {employee_2.emp_id}")
print(f"Employee Name: {employee_2.name}")
print(f"Employee Department: {employee_2.department}")
print(f"Employee Salary: {employee_2.salary}")

print("************************************")

employee_1.display_details()
employee_2.display_details()