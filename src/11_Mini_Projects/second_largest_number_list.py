'''
Find the second-largest number in a list without using sort() or sorted().
'''
numbers = [10, 5, 20, 8, 20, 15, 12]
#numbers = [-10, -15, -5, -8]
def second_largest_number(numbers):

    first_largest = None
    second_largest = None

    for num in numbers:

        if first_largest is None or num > first_largest:
            second_largest = first_largest
            first_largest = num

        elif (second_largest is None or num > second_largest) and num != first_largest:
            second_largest = num

    return second_largest

print(second_largest_number(numbers))