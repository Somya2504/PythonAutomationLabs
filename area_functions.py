# Python Code for finding the area of Circle, Rectangle, Square and Triangle

import math


class AreaCalculator:

    def circle_area(self, radius):
        area = math.pi * radius ** 2
        return area

    def rectangle_area(self, length, width):
        area = length * width
        return area

    def square_are(self, side):
        area = side ** 2
        return area

    def triangle_area(self, base, height):
        area = 0.5 * base * height
        return area

def main():
# For Object creation, we have to come out of the class.
# Create an object and assign it to an object variable to call the class.
    calc = AreaCalculator()

    print("Choose a shape")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")

    choice = int(input("Enter your choice (1-4): "))  # Type Casting

    if choice == 1:
        r = flot(input("Enter Radius: "))
        print(f"Area of Circle: {calc.circle_area(r):.2f}")

    elif choice == 2:
        len = flot(input("Enter length: "))
        wid = flot(input("Enter Width: "))
        print(f"Area of Rectangle: {calc.rectangle_area(len, wid):.2f}")

    elif choice == 3:
        s = flot(input("Enter Side: "))
        print(f"Area of Square: {calc.square_are(s):.2f}")

    elif choice == 4:
        b = float(input("Enter Base: "))
        h = float(input("Enter Height: "))
        print(f"Area of Triangle: {calc.triangle_area(b, h):.2f}")

    else:
        print("Invalid Choice !!!!")


# Program starts here
if __name__ == "__main__":
    main()