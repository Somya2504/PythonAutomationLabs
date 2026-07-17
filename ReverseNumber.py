# Reverse Number
# Using String Slicing (Shortest Method)
num = 123456
rev = int(str(num)[::-1])
print("Print the Reverse Number:", rev)

# Using While Loop
num = 54321
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Print the Reverse Number:", rev)


