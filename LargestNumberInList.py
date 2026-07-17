#Largest Number in List

numbers = [10, 23, 54, 99, 29, 64, 79, 91]
largest_num = numbers[0]
for n in numbers:
    if n > largest_num:
        largest_num = n
print(largest_num)