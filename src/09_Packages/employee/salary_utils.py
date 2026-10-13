from .employee_utils import calculate_salary


def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12


def calculate_total_salary(basic_salary, bonus):
    return calculate_salary(basic_salary, bonus)