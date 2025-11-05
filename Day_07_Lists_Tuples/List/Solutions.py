# Solution 1: Create the initial list 'nums' containing numbers 5, 2, 9, 1, 5.
nums = [5, 2, 9, 1, 5]
print(f"The list are: {nums}")

# Solution 2: Print its length of the list
print(f"The length of list is: {len(nums)}")

# Solution 3: Add the number '7' to the end.
nums.append(7)
print(f"After adding the new element(7) at the end: {nums}")

# Solution 4: Remove the first occurrence '5' from the list.
nums.remove(5) # or pop(0)
print(f"After remove the first '5' item: {nums}")

# Solution 5: Sort the list in ascending order and print the result.
nums.sort()
print(f"Sorted list: {nums}")