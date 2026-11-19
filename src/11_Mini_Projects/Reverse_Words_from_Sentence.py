'''
Reverse words in a sentence
'''

text = 'I am learning Python'

def reverse_words(text):
    words = text.split()        # split() to separate the words.
    result = ""
    for rev_words in words:
        result = rev_words + " " + result
    return result.strip()
    # Because the first iteration adds a space before the existing result,
    # leaving an unnecessary space at the end of the final string.
    # .strip() removes leading and trailing whitespace.

print(reverse_words(text))