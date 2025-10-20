# Solution 1: Defining a function greet_user() that prints a welcome message.
def greet_user():
    print("Hello buddies, Welcome to Python functions!")

greet_user() # Calling it by its name:


# Solution 2: Writing a function add_numbers(a, b) that returns their sum.
def add_numbers(a, b): # This line defines a function named add_numbers that accepts two parameters, a and b.
    return a + b # This line calculates the sum of a and b and returns the result.

print(add_numbers(5, 10))
print(add_numbers(45, 15))


# Solution 3: Writing a function is_even(num) that returns True if even, False otherwise.
def is_even(num):
    return num % 2 == 0

print(is_even(5))
print(is_even(4))


# Solution 4: Creating a function power(base, exponent=2) that returns base ** exponent.
def power(base, exponent=2):
    return base ** exponent

print(power(6))
print(power(2, 3))
# The function power(base, exponent=2) would returns the value of 'base' raised to power of 'exponent'. The 'exponent=2' part of the function definition seta default value for the exponent, so if the user calls the function with only one argument, it will default to squaring the base.


# Solution 5: Writing a function calculate_area(width, height) with return.
def calculate_area(width, height):
    return width * height

print(calculate_area(5, 10))
'''
Calculates the area of a rectangle,

Args:
    width (float or int): The width of the rectangle,
    height (float or int): The height of the rectangle.

Returns:
    float or int: The area of the rectangle.
'''


# Solution 6: Using a global variable counter and increment it inside a function.
'''
Step 1: Define the global variable, initialize it to 0.
Step 2: Define the function
Step 3: Call the function and print the result
'''
counter = 0

def increment():
    global counter # Using the 'global' keyword to indicate that we are using the global variable 'counter' and not a local one
    counter += 1

increment()
print(counter)
