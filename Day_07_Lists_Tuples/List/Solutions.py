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
# Solution 1:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"The Nested list are: {matrix}")

# Solution 2:
print(f"row 2 lists elements are: {matrix[1]}")
print(f"column 3 lists elements are: [{matrix[0][2]}], [{matrix[2][2]}]")

# Solution 3:
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()