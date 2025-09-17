Day 03 - operation & Expressions

Goal: Learn arithmetic, comparison, logical, and assignment operators; operator precedence; and practice with short exercises.

- Arithmetic operators: +, -, \*, /, // (floor division), % (modulo), \*\*(power)
- Comparison operators: ==, !=, >, <, >=, <= (return bool)
- Logical operators: and, or, not (work with boolean values)
  = Assignment operators: =, +=, -=, \*=, /=, %=
- Operator precedence: \*_ > _ / // % > + - > comparison > not > and > or

Examples (short):

# arithmetic

x = 7
y = 3
print(x + y) # 10
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
