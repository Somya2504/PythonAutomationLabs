# Add addition function

import math

class Addition:

    def add(self, A, B):
        sum = A + B
        return sum

def main():
    obj_add = Addition()        # Create object for the Class

    entered_A = float(input("Value of A= "))
    entered_B = float(input("Value of B= "))

    if entered_A < 0 and entered_B < 0:
        print("Enter positive values")
    else:
        print(f"Addition of A & B is {obj_add.add(entered_A, entered_B)}")


# Program starts here
if __name__ == "__main__":
    main()