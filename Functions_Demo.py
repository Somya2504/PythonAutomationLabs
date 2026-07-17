# In Python, Function is a group of related statements which perform a specific task.

# Function Declaration
def GreetMe_1():
    print("Hello, Good Morning Branch A and Branch B")


# Call the Function
GreetMe_1()


# Parameterized Function Call
def GreetMe_2(name):
    print("Hello, Good Evening", name)
    print("Hello, Good Night " + name)
    print(f"Hello, Good Morning {name}")
    # The f before the string makes it an f-string (formatted string literal).
    # It allows you to insert variables or expressions directly into a string.
    # Faster than 1st 2 formatting methods
    # The recommended approach in modern Python (3.6+)


# Call the Function
GreetMe_2("Somya")

import math


def calculate_circle_area(radius: float) -> float:
    """Calculates the area of a circle.

    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)


def get_user_radius() -> float | None:
    """Prompts the user for a radius value via the console.

    Returns:
        float: The validated radius value.
        None: If the user requests to exit the program.
    """
    while True:
        raw_input = input("\nEnter the radius of the circle (or type 'exit' to quit): ")
        clean_input = raw_input.strip().lower()

        if clean_input == 'exit':
            return None

        try:
            return float(clean_input)
        except ValueError:
            print("Invalid input. Please enter a valid decimal number (e.g., 5 or 3.5).")


def main() -> None:
    """Main execution block managing the application lifecycle."""
    print("--- Circle Area Calculator Initialized ---")

    while True:
        try:
            radius = get_user_radius()

            # None indicates the user initiated an exit command
            if radius is None:
                print("Exiting application. Goodbye!")
                break

            area = calculate_circle_area(radius)
            print(f"Success: The area of the circle is {area:.2f}")
            break

        except ValueError as error:
            # Captures semantic errors raised by the math function
            print(f"Business Logic Error: {error}")


if __name__ == "__main__":
    main()
