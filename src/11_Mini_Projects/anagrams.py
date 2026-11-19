'''
Check whether two strings are anagrams
Two strings are anagrams if they contain exactly the same characters with the same frequencies, but in a different order.
'''

text1 = "listen"
text2 = "silent"

#Interview Oriented Approach using loop only
def check_anagrams(text1, text2):
    # Step 1: Check whether both strings have equal length
    if len(text1) != len(text2):
        return False

    # Step 2: Create an empty dictionary
    char_count = {}

    # Step 3: Count characters in the first string
    for char in text1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Step 4: Check characters in the second string
    for char in text2:

        if char not in char_count:
            return False

        # This prevents a character from being used more times than it appears in the original string
        if char_count[char] == 0:
            return False

        char_count[char] -= 1

    # Step 5: Both strings are anagrams
    return True

print(check_anagrams(text1, text2))
print(check_anagrams("race", "care"))
print(check_anagrams("Debit Card", "Bad Credit"))
print(check_anagrams("aabbcc", "abcabc"))
