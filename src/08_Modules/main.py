# Three ways to import modules
# Style 1 — Import the module
import employee_utils
salary_1 = employee_utils.calculate_salary(5000, 500)

employee = employee_utils.get_employee_details(501, 'Somya')

employee_id_status_1 = employee_utils.validate_employee_id(501)
employee_id_status_2 = employee_utils.validate_employee_id(-1)

print(f"Salary: {salary_1}")
print(f"Employee: {employee}")
print(employee_id_status_1)
print(employee_id_status_2)

# Style 2 — Import a specific function
from employee_utils import calculate_salary
salary_2 = calculate_salary(5000, 500)
print(f'Salary: {salary_2}')

# Style 3 — Import with an alias
import employee_utils as emp

salary_3 = emp.calculate_salary(4500, 200)
print(f'Salary: {salary_3}')

employee_3= emp.get_employee_details(502, 'Rakesh')
print(f'Employee: {employee_3}')