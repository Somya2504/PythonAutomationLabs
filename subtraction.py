# Add subtraction functionality

import math

class Subtraction:

    def subtrac(self, C, D):
        sub = C - D
        return sub

def main():
    obj_sub = Subtraction()        # Create object for the Class

    entered_C = float(input("Value of C= "))
    entered_D = float(input("Value of D= "))

    if entered_C < 0 and entered_D < 0:
        print("Enter positive values")
    else:
        print(f"Subtraction of C & D is {obj_sub.subtrac(entered_C, entered_D)}")


# Program starts here
if __name__ == "__main__":
    main()