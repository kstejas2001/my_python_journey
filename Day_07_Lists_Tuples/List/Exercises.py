# Tiny examples

# 1. Create list elements
fruits = ["apple", "banana", "cherry", "mango", "orange", "kiwi"]

# Print the number of items in the list
print(len(fruits)) # 6

# Print the type
print(type(fruits)) # <class 'list'>


# 2. Access Items
print(fruits[0]) # apple
print(fruits[-1]) # kiwi
print(fruits[0:3]) # ["apple", "banana", "cherry"]
print(fruits[:4]) # ["apple", "banana", "cherry", "mango"]
print(fruits[2:]) # ["cherry", "mango", "orange", "kiwi"]
print(fruits[-4:-1]) # ["cherry", "mango", "orange"]

# Check if Item Exists
if "apple" in fruits:
    print("Yes, 'apple' is exist in the fruits list")


# 3. Modification of items
# a. Change the value of a specific item
my_list = [1, 2, 0, 4, 5]
print(f"Before changing: {my_list}")
my_list[2] = 3
print(f"After change: {my_list}")

# b. Insert items
my_list.insert(4, 0)
print(f"Inserting new item: {my_list}")

# c. Append() Items
my_list.append(6)
print(f"After append: {my_list}")

# d. Remove Specified Item
my_list.remove(6)
print(f"Removing the specified item: {my_list}")

# e. Remove Specified Index
my_list.pop(4)
print(f"Remove specified index: {my_list}")


# 4. Loop Lists
# Loop Through a List
this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)

# From Index Numbers
this_list = ["apple", "banana", "cherry"]
for i in range(len(this_list)):
    print(this_list[i])

# While 
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1


# 5. List Comprehension
# Creating list of squares from range
square = [x * x for x in range(1, 6)]
print(square) # Output: [1, 4, 9, 16, 25]

# Using 'for' loop:
squares = []
for x in range(1, 6):
    squares.append(x * x)
    print(squares)

# list of only even numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers) # Output: [2, 4, 6, 8]

# With if-else (Conditional Expression):
numbers = [1, 2, 3, 4, 5]
result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(result) # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# Implement the following: 
# Exercise 1 — Simple

# 1. Make a list 'nums' containing numbers 5, 2, 9, 1, 5.
# 2. Print its length.
# 3. Add the number '7' to the end.
# 4. Remove the first '5' from the list.
# 5. Sort the list in ascending order and print the final list.

# Exercise 2 — Nested Lists

# 1. Create a nested list named 'matrix' with three lists: [ [1,2,3], [4,5,6], [7,8,9] ]
# 2. Print the number at row 2, column 3 (expected output → 6).
# 3. Use a nested 'for' loop to print every element on a new line.

# Exercise 3 — List Comprehension

# 1. Create a list of squares from 1 to 10 using list comprehension.
# 2. Print the list.
# 3. Then, create a new list containing only 'even squares'.