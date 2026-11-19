test_results = [
    {"name": "Login", "status": "PASS", "duration": 2.5},
    {"name": "Payment", "status": "FAIL", "duration": 8.2},
    {"name": "Refund", "status": "PASS", "duration": 6.5},
    {"name": "Checkout", "status": "FAIL", "duration": 9.1},
    {"name": "Search", "status": "PASS", "duration": 3.2}
]

# def count_passed_tests(test_results):
#     pass_count = 0
#     for pass_status in test_results:
#         if pass_status["status"] == "PASS":
#             pass_count = pass_count + 1
#     return pass_count
#
# pass_count_result = count_passed_tests(test_results)
# print(pass_count_result)
#
# #print(count_passed_tests(test_results))
# #count_passed_tests(test_results)
#
# def count_failed_tests(test_results):
#     fail_count = 0
#     for fail_status in test_results:
#         if fail_status["status"] == "FAIL":
#             fail_count += 1
#     return fail_count
# fail_count_result = count_failed_tests(test_results)
# print(fail_count_result)

def count_tests(test_results, status):
    count = 0
    for test_case in test_results:
        if test_case["status"] == status:
            count += 1
    return count


def calculate_test_percentage(test_results, status):

    if test_results == 0:
        return 0.0
    total_tests = len(test_results)
    test_percentage = (count_tests(test_results, status)/total_tests) * 100
    return test_percentage


def find_slow_tests(test_results, threshold):

    slow_tests = [test_case["name"] for test_case in test_results if test_case["duration"] > threshold]
    return slow_tests


def generate_test_summary(test_results):
    passed = count_tests(test_results, status="PASS")
    failed = count_tests(test_results, status="FAIL")

    print(f"Passed tests: {passed}")
    print(f"Failed tests: {failed}")

    total_tests = len(test_results)

    test_pass_percentage = calculate_test_percentage(test_results, status="PASS")
    test_fail_percentage = calculate_test_percentage(test_results, status="FAIL")

    print(f"Pass Percentage: {test_pass_percentage}")
    print(f"Fail Percentage: {test_fail_percentage}")

    slow_tests_result = find_slow_tests(test_results, 5)
    print(f"Slow Tests: {slow_tests_result}")

    summary = {
        "Total_Tests" : total_tests,
        "Passed_tests" : passed,
        "Failed_tests" : failed,
        "Pass_Percentage" : test_pass_percentage,
        "Fail_Percentage" : test_fail_percentage,
        "Slow_Tests" : slow_tests_result
    }
    return summary

test_summary = generate_test_summary(test_results)

print(test_summary)