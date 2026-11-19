'''
Write a function that finds the first character that appears only once in a given string
'''

text = "automation"

#Interview Oriented approach using for-loop
def first_non_repeating_char(text):
    for char in text:
        count = 0
        for other_char in text:
            if char == other_char:
                count += 1
        if count == 1:
            return char
    return None

print(first_non_repeating_char(text))

# Using counter
def first_non_repeating_char_using_counter(text):
    result = ''
    for char in text:
        if text.count(char) == 1:
            result = result + char
            break
    return result
print(first_non_repeating_char_using_counter(text))
