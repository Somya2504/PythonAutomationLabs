# Tuples are similar to lists but are immutable, meaning their values cannot be changed once defined.
# They are useful when data should remain constant.
# Ordered collection
# Allows duplicate values
# Faster than lists in performance

tp = (1, 3, 'Sangeeta', 4.44, 5)

# the following actions are same as List
print(tp)
print(tp[1])
print(tp[-1])
print(tp[1:3])

# Test Tuple is Immutable
tp[3] = 'Pradhan'
print(tp)   # Throws an error as Tuple can't be modified