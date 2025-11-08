# Exercise 1 (simple)
# Solution 1: Create the initial list 'nums' containing numbers 5, 2, 9, 1, 5.
nums = [5, 2, 9, 1, 5]
print(f"The list are: {nums}") # [5, 2, 9, 1, 5]

# Solution 2: Print its length.
print(f"The length of list is: {len(nums)}") # 5

# Solution 3: Add the number '7' to the end.
nums.append(7)
print(f"After adding the new element(7) at the end: {nums}") # [5, 2, 9, 1, 5, 7]

# Solution 4: Remove the first occurrence '5' from the list.
nums.remove(5)
print(f"After remove the first '5' item: {nums}") # [2, 9, 1, 5, 7]

# Solution 5: Sort the list in ascending order and print the result.
nums.sort()
print(f"Sorted list: {nums}") # [1, 2, 5, 7, 9]


# Exercise 2 (Nested Lists)
# 1: Create the nested list.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"The Nested list are: {matrix}") # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2: Access and print the element at row 2, column 3.

# Access the element at row 2 (index 1), column 3 (index 2).
element = matrix[1][2]
print(f"The element at row 2, column 3 is: {element}") # expected output: 6

# 3: Use nested loops to print every element on a new line.
# Nested 'for' loops can be used to iterate through each sublist(row) and then each item within that sublist (column).

# Iterate though each row in the matrix.
for row in matrix:
    # Iterate through each element in the current row.
    for element in row:
        # Format the output string.
        print(f"Element: {element}")


# Exercise 3 — List Comprehension
# 1. Create the list from 1 to 100 using list comprehension.
squares = [x**2 for x in range(1, 11)]

# 2. Print the list.
print(squares)

# 3. For even numbers
even_squares = [x for x in squares if x % 2 == 0]
print(even_squares)