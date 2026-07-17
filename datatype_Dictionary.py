# Dictionaries store data in key-value pairs.
# This makes them highly efficient for lookups and data retrieval.
# Mutable just like List and dynamic
# Keys must be unique
# Fast access to values using keys

dict = {"male": "Somyakanta", "female": "Sangeeta", "weds": 28022024}

print(dict)
print(dict['male'])       # output = Somyakanta ->> In Dictionary we need to provide the 'Key' to get the value not the index
print(dict['weds'])

# Add a key-value pair to the empty dictionary

std = {}        # empty dictionary
std['name'] = 'Ram'
std['rollnumb'] = 21
std['percentage'] = '81.5%'
std['grade'] = 'E'

print(std)

print(std['percentage'])