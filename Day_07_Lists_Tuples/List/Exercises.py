# Tiny examples

# 1. Creating list elements
fruits = ["apple", "banana", "cherry", "mango", "orange", "kiwi"]

# Print the number of items in the list
print(len(fruits)) # 6

# Print the type of list
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
print(f"Before changing: {my_list}") # [1, 2, 0, 4, 5]
my_list[2] = 3
print(f"After change: {my_list}") # [1, 2, 3, 4, 5]

# b. Insert items
my_list.insert(0, 0)
print(f"Insert new item: {my_list}") # [0, 1, 2, 3, 4, 5]

# c. Append() Items
my_list.append(6)
print(f"After append: {my_list}") # [0, 1, 2, 3, 4, 5, 6]

# d. Remove Specified Item
my_list.remove(0)
print(f"Removing the first item {my_list}") # [1, 2, 3, 4, 5, 6]



# Implement the following:

# 1. Make a list 'nums' containing numbers 5, 2, 9, 1, 5.
# 2. Print its length.
# 3. Add the number '7' to the end.
# 4. Remove the first '5' from the list.
# 5. Sort the list in ascending order and print the final list.
