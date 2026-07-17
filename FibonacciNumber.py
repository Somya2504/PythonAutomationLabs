# Fibonacci Number
n_term = int(input("How many terms: "))
n0, n1 = 0, 1
count = 0
if n_term <= 0:
    print("Please provide a positive integer")
elif n_term == 1:
    print("Fibonacci number up to n_term", n_term, ":",)
    print(n0)
else:
    print("Fibonacci number up to n_term", n_term, ":",)
    while count < n_term:
        nth = n0 + n1
        print(nth)
        n0 = n1
        n1 = nth
        count += 1
