test_results = [
    {"test": "Login", "status": "PASS", "time": 2},
    {"test": "Payment", "status": "FAIL", "time": 8},
    {"test": "Refund", "status": "FAIL", "time": 6}
]
def generate_test_summary(test_results, **details):
    failed_tests = [
        result["test"]
        for result in test_results
        if result["status"] == "FAIL"
    ]

    failed_tests_times = {
        result["test"]: result["time"] for result in test_results if result["status"] == "FAIL"
    }

    print("Failed Tests:", failed_tests)
    print("Failed Test Times:", failed_tests_times)
    print("Execution Details:", details)

generate_test_summary(
    test_results,
    project="Payments",
    environment="QA"
)