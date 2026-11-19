class BaseTest:
    def __init__(self, test_id, test_name):
        self.test_id = test_id
        self.test_name = test_name

    def display_basic_details(self):
        print(f"Test ID: {self.test_id}")
        print(f"Test Name: {self.test_name}")

class FunctionalTest(BaseTest):

    def __init__(self, test_id, test_name, module_name):
        super().__init__(test_id, test_name)
        self.module_name = module_name

    def display_functional_details(self):
        super().display_basic_details()
        print(f"Module Name: {self.module_name}")

test1 = FunctionalTest(
    "TC001",
    "Login Validation",
    "Authentication"
)

test1.display_basic_details()
test1.display_functional_details()