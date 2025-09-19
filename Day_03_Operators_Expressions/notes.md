Day 03 - Operation & Expressions

Goal: Learn arithmetic, comparison, logical, and assignment operators; operator precedence; and practice with short exercises.

# 01. Operators

- Arithmetic operators: Arithmetic operators are used to perform mathematical operations in Python. +, -, \*, /, // (floor division), % (modulo), \*\*(power)

- Comparison operators: Comparison operators are used to compare values and return a boolean result. ==, !=, >, <, >=, <= (return bool)

- Logical operators: Logical operators are used to combine boolean values and perform logical operations. and(returns True if both operands are True), or(: returns True if at least one operand is True), not (returns the opposite boolean value).

- Assignment operators: =, +=, -=, \*=, /=, %=

- Operator precedence: \*_ > _ / // % > + - > comparison > not > and > or

Examples (short):

# arithmetic

x = 7
y = 3
print(x + y) # 10
print(x - y) # 4
print(x \* y) # 21
print(x / y) # 2.333...
print(x // y) # 2
print(x % y) # 1
print(x \*\* 2) # 49

# comparison

print(5 > 3) # True
print(5 == 5) # True
print(3 < 2) # False
print(3 == 2) # False

# Logical

a = True
b = False
print(a and b) # False
print(a or b) # True
print(not a) # False

# assignment

n = 10
n += 5 # n = n + 5 -> 15

# mixing types and caution

print(5 + 3.2) # 8.2 (int + float -> float)

# 02. Expressions

- Expressions are combinations of values, variables, and operators that produce a result. They follow the order of operations, also known as PEMDAS/BODMAS (Parentheses/Brackets, Exponents/Orders, Multiplication and Division, Addition and Subtraction).

Examples (short):

x = (10 + 5) _ 2 # parentheses
y = 2 \*\* 3 + 4 _ 5 # exponentiation and multiplication
z = 10 / (2 + 3) # division and addition
