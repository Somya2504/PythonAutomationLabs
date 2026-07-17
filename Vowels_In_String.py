# Count Vowels in String
s = "automation"
vowels = "aeiou"
count = 0

for char in s:
    if char in vowels:
        count += 1

print(count)