What is a variable?
A variable is a name that refer to a value stored in a memory. Use the assignment operator = to give a name to a value.

Exapmles

age = 23 # integer
height = 5.9 # float
name = "Thejas" # string
is_student = True # boolean

Naming rules

- Start with a letter (a–z, A–Z) or underscore \_ (not a number).
- No spaces (use underscores): my_name not my name.
- Case-sensitiove: Age and age different.
- Avoid Python keywords (eg., class, for, if).
- Prefer snake_case for variable names.

Dynamic typing Python variables don’t require declaring a type. The same variable can be reassigned to a different type:

x = 5
x = "five" # allowed

Check type Use type() to find the data type:

age = 23
print(type(age)) # output: <class 'int'>

Type conversion Convert between types using int(), float(), str(), bool():

s = "123"
n = int(s) # 123
f = float("3.14")

Multiple assignment & swap

x, y = 3, 4

# swap

x, y = y, x

Input function input() returns a string. Convert if you need numbers:

n = input("Enter number: ") # string
n = int(input("Enter number: ")) # integer

String formatting (f-strings)

name = "Tejas"
age = 21
print(f"My name is {name} and I am {age} years old.")
