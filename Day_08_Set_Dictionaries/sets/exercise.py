# Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset) # Output: {'banana', 'cherry', 'apple'}

# Duplicate values will be ignored 
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # Output: {'banana', 'cherry', 'apple'}

# True and False are considered as 1 and 0
thisset = {0, 1, 2, 3, True, False}
print(thisset) # Output: {0, 1, 2, 3}

# length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # Output: 3

# set can contain different data types
thisset = {"apple", 1, True, 3.14}
print(thisset) # Output: {1, 3.14, 'apple'}

# type of a set
thisset = {"apple", "banana", "cherry"}
print(type(thisset)) # Output: <class 'set'>

# create a set using the set() constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset) # Output: {'banana', 'cherry', 'apple'}

# access set items
thisset = {"apple", "banana", "cherry"}
for item in thisset:
    print(item) # Output: apple banana cherry (order may vary)

# check if item exists in set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # Output: True
print("orange" in thisset) # Output: False

