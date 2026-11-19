number = [2, 5, 8, 11, 14, 17, 20, 23]

#list comprehension technique
sqr_num = [(num * num) for num in number]
print(sqr_num)

# Using for loop with + operator
def sqr_number_01(number):
    sqr_num_1 = []
    for num in number:
        sqr_num_1 = sqr_num_1 + [num * num]
    return sqr_num_1
sn_01 = sqr_number_01(number)
print(sn_01)

# Using for loop with append()
def sqr_number_02(number):
    sqr_num_2 = []
    for num in number:
        sqr_num_2.append(num * num)
    return sqr_num_2
sn_02 = sqr_number_02(number)
print(sn_02)

# Using index
def sqr_number_03(number):
    #create an empty list with the same size of given list
    sqr_num_3 = [0] * len(number)
    for i in range(len(number)):
        sqr_num_3[i] = number[i] * number[i]
    return sqr_num_3
sn_03 = sqr_number_03(number)
print(sn_03)

# Using lambda expression
def sqr_number_04(number):
    sqr_num_04 = list(map(lambda num: num * num, number))
    return sqr_num_04
sn_04 = sqr_number_04(number)
print(sn_04)

# Use list comprehension to get only even numbers
def get_even_number(number):
    even_num = [num for num in number if num % 2 == 0]
    return even_num
print(get_even_number(number))

# Use a normal for loop and append() to get only odd numbers.
def get_odd_number(number):
    odd_num = []
    for num in number:
        if num % 2 != 0:
            odd_num.append(num)
    return odd_num
print(get_odd_number(number))

# Create a function get_even_squares(numbers) that returns the squares of only the even numbers.
def get_even_squares(number):
    even_sqr_num = [(num * num) for num in number if num % 2 == 0]
    return even_sqr_num
even_sqr = get_even_squares(number)
print(even_sqr)