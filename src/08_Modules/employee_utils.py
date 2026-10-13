# This file is our module. It contains reusable functions but doesn't execute them by itself.

def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus

def get_employee_details(employee_id, name):
    return {
        "employee_id": employee_id,
        "name": name
    }
def validate_employee_id(employee_id):
    if employee_id > 0:
        return True
    else:
        return False

print("Module loaded")

if __name__ == "__main__":
    print("Module executed directly")