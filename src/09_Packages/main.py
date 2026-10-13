# A package helps us organize related Python modules into directories.

## Absolute imports -->Python follows the path from the package to the module, then accesses the requested function.
from employee.employee_utils import calculate_salary
from employee.employee_utils import validate_employee_id

salary = calculate_salary(50000, 25000)

print(f"Salary:{salary}")
print(validate_employee_id(501))
print(validate_employee_id(-1))

# Relative Imports
'''
Python executes employee/__init__.py when importing the regular package. Because that file imports and exposes the selected functions, main.py can access them directly through employee.
Industry benefit: __init__.py can define a clean public interface for your package, hiding some of the internal file structure from its users.
'''
from employee import calculate_salary, get_employee_details
from employee.employee_utils import validate_employee_id

salary = calculate_salary(50000, 5000)
employee = get_employee_details(510, 'Sudarshan')   #One important nuance: __init__.py doesn't automatically expose every function in the package. You choose what to import or define there.

print(f"Salary: {salary}")
print(validate_employee_id(420))
print(f"Employee details: {employee}")

from employee import calculate_annual_salary, calculate_total_salary

print(calculate_annual_salary(50000))
print(calculate_total_salary(50000, 5000))

from employee import validate_salary, validate_employee_name

print(validate_salary(50000))
print(validate_salary(-100))
print(validate_employee_name("Alok"))
print(validate_employee_name(" "))
