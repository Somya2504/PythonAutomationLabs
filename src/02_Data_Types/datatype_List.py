# Lists are ordered collections of items that can store multiple values of different data types.
# They are mutable, meaning their content can be changed after creation.
# Allows duplicate values.
# Supports indexing and slicing.

ls = [1, 2, "somya", 3.5, 4, 3, 2]

print(ls)
print(ls[0])    # output = 1
print(ls[-1])   # output = 2 ->> [-1] returns the last value in a list
print(ls[1:3])  # # output = [2, "somya"] ->> [n:m] returns list from the nth index (1 index) till 'm' position (3rd position)

# insert some value to a certain position.
ls.insert(3, "pradhan")
print(ls)       # output = [1, 2, 'somya', 'pradhan', 3.5, 4]

ls.insert(4, 5)

# 'append' some value to the List
ls.append(5)    # append() function will add the value at the End position of the List.
print(ls)       # output = [1, 2, 'somya', 'pradhan', 3.5, 4, 5]

ls.append(6.7)
print(ls)

# update the existing value in a List
ls[3] = "PRADHAN"
print(ls)       # output = [1, 2, 'somya', 'PRADHAN', 3.5, 4, 5]

# delete the existing value in a List
del ls[3]
print(ls)   # output = [1, 2, 'somya', 3.5, 4, 5]

# 'extend' --> add multiple items at the end of the List
ls.extend(['abc', 7.45])
print(ls)   # output = [1, 2, 'somya', 3.5, 4, 5, 'abc', 7.45]

# '+' operator = Returns a new combined list
more = ls + [11, 'dev']
print(more)     # output = [1, 2, 'somya', 3.5, 4, 5, 'abc', 7.45, 11, 'dev']

# hence Proved that Lists are mutable, meaning their content can be changed after creation.