'''
Write a Python program to identify all duplicate numbers only once, regardless of how many times it appears
Rules for your first attempt
- Don't use set().
- Don't use Counter.
- Don't use external libraries.
- Use basic Python loops and conditions.
- Return a list containing unique duplicate numbers.
'''
numbers = [4, 2, 7, 2, 8, 4, 9, 4, 10]
def find_duplicate_using_loop(numbers):
    duplicates_1 = []
    for n in range(len(numbers)):
        for m in range(len(numbers)):
            if n != m:
                if numbers[n] == numbers[m]:
                    if numbers[n] not in duplicates_1:
                        duplicates_1.append(numbers[n])
    return duplicates_1
    # I place the return statement outside both loops to ensure that all elements are checked
    # and all unique duplicates are collected before returning the result.

duplicates_num_1 = find_duplicate_using_loop(numbers)
print(duplicates_num_1)
duplicates_num_1.sort()
print(duplicates_num_1)

print('*' * 40)

'''Use count() to get the duplicate integer'''
def find_duplicate_using_count(numbers):
    duplicates_2 = []
    for num in numbers:
        if numbers.count(num) > 1:
            if num not in duplicates_2:
                duplicates_2.append(num)
    return duplicates_2
duplicates_num_2 = find_duplicate_using_count(numbers)
print(duplicates_num_2)

print('*' * 40)

'''Use set to get the duplicate integer'''
def find_duplicate_using_set(numbers):
    #Create two empty 'sets'
    seen = set()            #seen stores numbers we've already encountered
    duplicates_3 = set()    #duplicates stores numbers that appear more than once.

    for num in numbers:
        # If the number is already in 'seen' then we've encountered it before. So we add it to duplicates.
        if num in seen:
            duplicates_3.add(num)

        #Otherwise, remember the number
        else:
            seen.add(num)

    return list(duplicates_3)

duplicates_num_3 = find_duplicate_using_set(numbers)
print(duplicates_num_3)

print('*' * 40)

