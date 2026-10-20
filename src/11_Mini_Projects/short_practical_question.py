#Exception handling
try:
    number = int("ABC")
    print("Success")
except ValueError:
    print("Invalid number")
finally:
    print("Execution completed")

#OOP and inheritance
class Employee:
    def work(self):
        print("Employee working")


class Tester(Employee):
    def work(self):
        print("Tester testing")

tester = Tester()
tester.work()

#List comprehension
test_results = [
    {"test": "Login", "status": "PASS"},
    {"test": "Payment", "status": "FAIL"},
    {"test": "Refund", "status": "FAIL"}
]

failed_tests = [
    result["test"]
    for result in test_results
    if result["status"] == "FAIL"
]

print(failed_tests)