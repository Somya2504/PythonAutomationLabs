import truststore

# Tell Python to use Windows trusted certificates
truststore.inject_into_ssl()

import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)
print(response.json())
