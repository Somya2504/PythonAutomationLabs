# Reverse String

# Using String Slicing (Shortest Method)
s = 'pradhan'
print(s[::-1])

# Using Loop
s = "automation"
rev = ""

for i in s:
    rev = i + rev

print(rev)