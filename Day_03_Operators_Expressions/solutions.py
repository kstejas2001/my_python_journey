# Solution 1: Arithmetic and precedence

# Step 1: Understand Python's operator Precedence: 1. Parenthese (), 2. Exponentiation **, 3. Multiplication * and division / (evaluted from left to right), 4. Addition + and Subtraction - (evaluated from left to right)

# Step 2: Evaluate the Expression Step-by-Step.
# The given expression is:  # result = 3 + 4 * 2 ** 3 - (6 / 3)

# 1. Parentheses/Brackets:
par = 6 / 3 # (6 / 3) = 2. The expression becomes: result = 3 + 4 * 2 ** 3 - 2

# 2. Exponents:
exp = 2 ** 3 # 2 ** 3 = 8. The expression becomes: result = 3 + 4 * 8 - 2

# 3. Multiplication:
mul = 4 * 8 # 4 * 8 = 32. The expression becomes: result = 3 + 32 - 2

# 4. Addition (from left to right):
add = 3 + 32 # 3 + 32 = 35. The expression becomes: result = 35 - 2

# 5. Subtraction (from left to right):
sub = 35 - 2 # 35 - 2 = 33. The expression becomes: result = 33

# Print the result
print(sub)

# Explaination: The first operation to happen was the divisioninside the parentheses: (6 / 3).
# According to Python's operator precedence, oprations within parantheses are evaluted first, followed by exponentiation, then multiplication/division, and finally addition/subtraction.

# Short One
par = 6 / 3
power = 2 ** 3
mul = 4 * power
add = 3 + mul
sub = add - par
print(sub)


# Solution 2: Modulo use-case

# Step 1: # Understand the problem: The problem ask to determine is a given number n is even or odd using modulo (%).

# Step 2: Input the Number
n = int(input("Enter a number: "))

# Step 3: Apply the modulo operator and condition logic. We use if-else statement to check the condition n%2==0. If the condition is true, the number is even, and we print "even" else "odd"
if n % 2 == 0:
    print('even')
else:
    print('odd')


# Solution 3: Logical condition

# Step 1: Get user input for age and ID status(Prompt the user to enter their age and store it in a variable and also prompt the user to answer whether they have an ID (y/n) and store the response in a variable.)
age = int(input("Enter your age: "))
has_id = input("Have ID? (y/n): ").lower() == 'y'

# Step 2: Determine if the user can enter (This means the user can enter only if they are 18 or older AND they have an ID.)
can_enter = age >= 18 and has_id

# Step 3: Print the result (Print the value of can_enter to inform the user if they meet the entry requirements.)
print(can_enter)


# Solution 4: Compound assignment

# Step 1: Initialize points (Start by init the points variable to 0)
points = 0

# Step 2: Read the score and add to points (Use a for loop to iterate 3 times(range(3) in to read 3 integer scores form the user. Each iterate, convert the input score to integer and add it to points += operator.))
for _ in range(3):
    score = int(input('score: '))
    points += score

# Print the total points.
print(points)