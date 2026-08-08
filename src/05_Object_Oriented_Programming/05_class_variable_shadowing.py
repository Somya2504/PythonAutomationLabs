class Employee:
    # Class Variable
    company_name = "CGI"

    def __init__(self, employee_id, employee_name, department, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("-" * 50)
        print(f"Company Name : {self.company_name}")
        print(f"Employee ID  : {self.employee_id}")
        print(f"Name         : {self.employee_name}")
        print(f"Department   : {self.department}")
        print(f"Salary       : ₹{self.salary:,}")
        print("-" * 50)


# Create Employee Objects
employee_1 = Employee(501, "Alok Das", "Finance", 75000)
employee_2 = Employee(502, "Prem Chopra", "Law", 62500)
employee_3 = Employee(503, "Tarun Nair", "Marketing", 72500)

print("\n========== INITIAL VALUE ==========")
print("Employee.company_name  :", Employee.company_name)
print("employee_1.company_name:", employee_1.company_name)
print("employee_2.company_name:", employee_2.company_name)
print("employee_3.company_name:", employee_3.company_name)

# Change the Class Variable
Employee.company_name = "NTT DATA"

print("\n========== AFTER CHANGING CLASS VARIABLE ==========")
print("Employee.company_name  :", Employee.company_name)
print("employee_1.company_name:", employee_1.company_name)
print("employee_2.company_name:", employee_2.company_name)
print("employee_3.company_name:", employee_3.company_name)

# Create an Instance Variable with the same name
employee_1.company_name = "Google"

print("\n========== AFTER CREATING INSTANCE VARIABLE ==========")
print("Employee.company_name  :", Employee.company_name)
print("employee_1.company_name:", employee_1.company_name)
print("employee_2.company_name:", employee_2.company_name)
print("employee_3.company_name:", employee_3.company_name)

print("\n========== DISPLAY DETAILS ==========")
employee_1.display_details()
employee_2.display_details()
employee_3.display_details()

print("\n========== INTERNAL DICTIONARIES ==========")

print("Employee Class Dictionary:")
print(Employee.__dict__)

print("\nEmployee 1 Dictionary:")
print(employee_1.__dict__)

print("\nEmployee 2 Dictionary:")
print(employee_2.__dict__)

print("\nEmployee 3 Dictionary:")
print(employee_3.__dict__)