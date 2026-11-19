class Employee:
    # class variable
    company = "CGI"

    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Experience: {self.experience}")
        # Using Employee.company explicitly communicates that we're accessing a class-level attribute.
        print(f"Company: {Employee.company}")

        # When we access an attribute through an object,
        # Python first checks whether that attribute exists in the instance
        # Here 'self' represent the object, so it will print the value associated with the Object
        print(f"Company: {self.company}")

emp1 = Employee("Raghu Rajan", "CFO", "18 Years")
emp2 = Employee("Gyanesh Kumar", "CEC", "15 Years")

# Instance Variable
emp1.company = "NTT Data"

employees = [emp1, emp2]
for employee in employees:
    employee.display_details()
    print("**" * 20)

'''
Attribute Shadowing: an instance attribute/Variable with the same name takes 
precedence over the class attribute when accessed through that instance.
'''