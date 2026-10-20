def validate_salary(salary):
    return salary >= 0

def validate_employee_name(name):
    return bool(name and name.strip())

test_results = [
    {"test": "Login", "status": "PASS", "time": 2},
    {"test": "Payment", "status": "FAIL", "time": 8},
    {"test": "Logout", "status": "PASS", "time": 1},
    {"test": "Refund", "status": "FAIL", "time": 6}
]

failed_tests = [result["time"] for result in test_results if result["status"] == "FAIL"]
print(failed_tests)

failed_tests_time = {
    result["test"]: result["time"] for result in test_results if result["status"] == "FAIL"
}
print(failed_tests_time)

def show_details(**details):
    print(details)

show_details(project="Payments", environment="QA")