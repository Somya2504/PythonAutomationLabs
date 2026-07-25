"""
In this code we are using 'Function', 'While loop' and 'Error Handling'.
"""

import math


# declaration of Function
def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius can't be negative.")
    return math.pi * (radius ** 2)


# # Simple & Happy Flow
# result = calculate_circle_area(5)
# print(f"The area of circle is: {result}")

# Use of While loop and Error Handling
while True:
    # System will take value from console
    entered_radius = input("Enter the radius of the circle: ")
    try:
        # Attempt to convert input and calculate area
        radius_value = float(entered_radius)
        result = calculate_circle_area(radius_value)

        # Display successful result and continue the loop
        print(f"The area of circle is: {result}")
        break
    except ValueError as error:
        # Catch text conversion failures and negative inputs
        print(f"Error: {error}")
        break
