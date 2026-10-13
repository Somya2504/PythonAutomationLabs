# __init__.py is the conventional file used to mark and initialize a regular Python package.

from .employee_utils import calculate_salary, get_employee_details
# It means import from a module in the current package.
# Here, it refers to employee_utils.py inside the employee package.

from .salary_utils import (
    calculate_annual_salary,
    calculate_total_salary,
)

from .employee_validation import (validate_salary, validate_employee_name)