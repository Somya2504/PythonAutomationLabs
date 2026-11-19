class TestCase:

    total_test_cases = 0

    def __init__(self, test_id, test_name, status, duration):
        self.test_id = test_id
        self.test_name = test_name
        self.status = status
        self.duration = duration
        TestCase.total_test_cases += 1

    def display_details(self):
        print(f"Test ID: {self.test_id}")
        print(f"Test Name: {self.test_name}")
        print(f"Status: {self.status}")
        print(f"Duration: {self.duration} seconds")
        print('*' * 40)

    def is_test_passed(self):
        return self.status == "PASS"

    @classmethod    # Works with class attributes
    def display_total_test_cases(cls):
        print("Total Test Cases:", cls.total_test_cases)

    @staticmethod       #Utility functionality independent of instance/class state
    def validate_test_id(test_id):
        return (
                test_id.startswith("TC")
                and test_id[2:].isdigit()
                and len(test_id) == 5
        )


test1 = TestCase("TC001", "Login Test", "PASS", 2.5)
test2 = TestCase("TC002", "Payment Test", "FAIL", 5.2)

test1.display_details()
test2.display_details()

print(test1.is_test_passed())
print(test2.is_test_passed())

TestCase.display_total_test_cases()

print(TestCase.validate_test_id("TC001"))
print(TestCase.validate_test_id("ABC001"))