# Solution 1: Create variables and print types
print("1. Variable creation and print their types")

# Create the variables as spesified in the problem, assigning appropriate values for each data type:
name = "Thejas"
age = 23
height = 5.8
is_student = True

# Print each variable and its type
print(f"I'm {name}, and type of name is: {type(name)}")
print(f"Age: {age}, type of Age: {type(age)}")
print(f"My height is: {height}, and type of height: {type(height)}")
print(f"Is student: {is_student}, Type: {type(is_student)}")


# Solution 2: Swap variables
print("2. Swaping a variables")

a = 5
b = 10
print(f"Before swap A = {a}, B = {b}")
a, b = b, a # swap
print(f"After swap A = {a}, B = {b}")


# Solution 3: Input and sum
print("Input and sum")

# Step 1: Ask the user to input two numbers
# Use the input() function to get two numbers from the user. Store them in seperate variables.
num1_str = input("Enter a first number: ")
num2_str = input("Enter a second number: ")

# Step 2: Conver them into integer
# The input() function returns strings, so convert these string to integers using int().
num1 = int(num1_str)
num2 = int(num2_str)

# Step 3: Calculate the sum and print using an f-string
# Calculate the sum of the two integers and then use an f-sring to display the result
sum = num1 + num2
print(f"Sum of {num1} and {num2} is: {sum}")


# Solution 4: Rectangle area (mini-challenge)
print("Mini challenge: rectangle area")

# Step 1: Get user input for width and height
# Ask the user to input the width and height of the rectangle. Since the input can be decimal, convert it to a float type.
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

# Step 2: Compute the area
# Calculate the aera of the rectangle using the formula: area = width * height.
area = width * height

# Step 3: Print the area formatted to two decimal places
# Print the calculated area, formatted to two decimal places, as specified in the problem.
print(f"The area of the rectangle is: {area:.2f}")