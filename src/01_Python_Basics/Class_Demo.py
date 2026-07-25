# Class is a user defined blueprint

class HelloWorld:
    country = 200  # class variable

    # default constructor
    def __init__(self, a, b):
        self.first_no = a
        self.second_no = b
        print("Constructor is called automatically when object is created")

    # a function inside a class called 'Method'
    def HelloWorldMethod(self):
        print("Welcome to the Earth !!!")

    def Summation(self):
        return self.first_no + self.second_no + HelloWorld.country


# For Object creation, we have to come out of the class.
# Create an object and assign it to an object variable to call the class.
obj = HelloWorld(2, 3)  # syntax to create object in Python
print(obj.country)
obj.HelloWorldMethod()
print(obj.Summation())