# A while loop is used when you don't know in advance how many times the loop should execute.
# It continues until a condition becomes False.

# ATM PIN Verification -> The user gets only 3 attempts to enter the correct PIN.
correct_pin = "54321"
attempts = 3
while attempts > 0:
    entered_pin = input("Enter the PIN: ")
    if entered_pin == correct_pin:
        print("Login Successful")
        break
    print(f"Wrong PIN Entered. Attempts left: {attempts}")
    attempts -= 1
if attempts == 0:
    print("You account has been blocked")

# Login Until Correct Credentials
username = "admin"
password = "admin@123"
while True:
    user = input("Username: ")
    pwd = input("Password is: ")
    if user == username and pwd == password:
        print("Welcome!")
        break
    else:
        print("Invalid credentials. Try again.")

# Menu-Driven Application
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Money Deposit")
    elif choice == "2":
        print("Money Withdraw")
    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")