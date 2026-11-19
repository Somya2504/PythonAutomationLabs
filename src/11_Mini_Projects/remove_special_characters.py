'''
Remove special characters from a string using for-loop.
'''

text = "Hello@123 #QA_Automation! 2026"

# 1. Interview Oriented solution
def remove_special_characters_1(text):
    # If a character is a letter, number or space, keep it. Otherwise, ignore it
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = letters + letters.upper()
    numbers = "0123456789"
    space = " "

    #so now the allowed characters are
    allowed_characters = letters + numbers + space

    #create an empty string
    result = ""

    for char in text:
        if char in allowed_characters:
            result = result + char
    return result
print(remove_special_characters_1(text))

# 2. Python provides a built-in function called string.ascii_lowercase that gives you all lowercase English letters (a to z).

import string
def remove_special_characters_2(text):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    space = " "

    allowed_characters = lowercase_letters + uppercase_letters + digits + space
    result = ""

    for char in text:
        if char in allowed_characters:
            result = result + char
    return result
print(remove_special_characters_2(text))

# 3. Using isalnum() -> isalnum() checks whether a character is a letter or a number.

def remove_special_characters_3(text):
    space = " "
    result = ""
    for char in text:
        if char.isalnum() or char == space:
            result = result + char

    return result
print(remove_special_characters_3(text))

# 4. Using list comprehension
def remove_special_characters_4(text):
    return "".join(char for char in text if char.isalnum() or char == " ")

print(remove_special_characters_4(text))

# Using Regular Expressions (Regex)
# Regex is particularly useful when you need more complex text-cleaning rules.
import re

def remove_special_characters_5(text):
    return re.sub(r"[^a-zA-Z0-9 ]","",text)
print(remove_special_characters_5(text))

# Using filter() - lambda expression
def remove_special_characters_6(text):
    return "".join(filter(lambda char: char.isalnum() or char == " ", text))

print(remove_special_characters_6(text))

#####################
text_1 = "My_Name@QA#Engineer_2026!"
import string

def remove_special_characters_7(text_1):
    lower_case_letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    digits = string.digits
    space = " "
    underscores = '_'
    allowed_characters = lower_case_letters + upper_case_letters + digits + space + underscores
    results = ""

    for char in text_1:
        if char in allowed_characters:
            results = results + char
    return results
print(remove_special_characters_7(text_1))



