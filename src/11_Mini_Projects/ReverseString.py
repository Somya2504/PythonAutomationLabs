# Reverse String

# Using String Slicing (Shortest Method)
text = 'I am learning Python'
print(text[::-1])

# Using Loop
def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result
print(reverse_string(text))