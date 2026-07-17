list = [1, 2, 3, 4, 5]
print(list)

# Print the values in the given list in a sequence manner -- Use 'for' loop
for i in list:
    print(i)
print('Task 1 done')

# write the square of each number present in the given list
for i in list:
    print(i**2)
print('Task 2 done')

# Code for find the square of a number
num = 5
sq_num = pow(num, 2)   #num**2   #num * num
print(sq_num)
print('Task 3 done')

# Find the sum of first natural number in the range of 10 in Python.
sum = 0
for i in range(1, 11):      # range(x, y) where x is the starting value and y is the index value
    sum += i
print('Total Sum=', sum)
print('Task 4 done')

# I want the output as 1, 3, 5... in a certain range.
for j in range(1, 15, 2):
    print(j)
print('Task 5 done')
