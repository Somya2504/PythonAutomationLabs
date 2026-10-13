def validate_salary(salary):
    return salary >= 0

def validate_employee_name(name):
    return bool(name and name.strip())