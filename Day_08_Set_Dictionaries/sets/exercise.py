# Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset) # Output: {'banana', 'cherry', 'apple'} because sets are unordered

# Duplicate values will be ignored 
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # Output: {'banana', 'cherry', 'apple'}

# True and False are considered as 1 and 0. True is 1 and False is 0
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

# create a set using the 'set()' constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset) # Output: {'banana', 'cherry', 'apple'}

# access set items
thisset = {"apple", "banana", "cherry"}
for item in thisset:
    print(item) # Output: apple banana cherry (order may vary)

# check if item exists in set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # Output: True
print("orange" in thisset) # Output: False

# check if item is not exists in set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) # Output: False
print("orange" not in thisset) # Output: True

# add items to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # Output: {'banana', 'cherry', 'orange', 'apple'}

# add set
thisset = {"apple", "banana", "cherry"}
tropical = {"mango", "pineapple", "papaya"}
thisset.update(tropical)
print(thisset) # Output: {'banana', 'cherry', 'papaya', 'mango', 'apple', 'pineapple'}

# add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # Output: {'banana', 'cherry', 'orange', 'kiwi', 'apple'}

# remove item from set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # Output: {'cherry', 'apple'}.
# thisset.remove("mango")
# print(thisset) # If item not found, raises KeyError

# remove item using discard method (no error if item not found)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # Output: {'cherry', 'apple'}
thisset.discard("mango")
print(thisset) # No error, Output: {'cherry', 'apple'}

# using pop() method to remove an item
thisset = {"apple", "banana", "cherry"}
item = thisset.pop()
print(f"Item removed: {item}") # Output: Item removed: 'apple' (or any other item, since sets are unordered)
print(f"Remaining items: {thisset}") # Output: remaining items in the set

# clear the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # Output: set()

# delete the set
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # This will raise an error as "NameError: name 'thisset' is not defined", because the set no longer exists

# Loop through a set
thisset = {"apple", "banana", "cherry"}
for item in thisset:
    print(f"Items from set: {item}") # Output: apple banana cherry (order may vary)

# Loop though items
for x in {'apple', 'banana', 'cherry'}:
  print(f"Items are: {x}")


# Core operations on sets

# 1. Union
A = {"a", "b", "c"}
B = {1, 2, 3}
set1 = A | B
print(set1) # {'a', 'b', 'c', 1, 2, 3}
C = {"d", "e", "f"}
D = {"f", "g", "h"}
set2 = C | D # using '|' operator
print(set2) # {'d', 'e', 'f', 'g', 'h'}
set3 = C.union(D) # using 'union()' method
print(set3) # {'d', 'e', 'f', 'g', 'h'}

# join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {True, False}
myset1 = set1.union(set2, set3) # using union() method
print(f"using union method: {myset1}") # {'a', 'b', 'c', 1, 2, 3, False}
myset2 = set1 | set2 | set3 # using '|' operator
print(f"using | operator: {myset2}") # {'a', 'b', 'c', 1, 2, 3, False}
set1.update(set2)
print(f"using update method: {set1}") # {'a', 'b', 'c', 1, 2, 3}

# 2. Intersection
mobile = {"apple", "redmi", "sony"}
computer = {"hp", "microsoft", "apple"}
set3 = mobile & computer # using '&' operator
print(f"using & operator: {set3}") # {'apple'}
set4 = mobile.intersection(computer) # using 'intersection()' method
print(f"using intersection method: {set4}") # {'apple'}

# The values 'True' and '1' are considered the same value. The same goes for 'False' and '0'
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1 & set2
print(set3) # Output: {False, 1, 'apple'}

# 3. Difference
my_brand = {"apple", "vivo", "nothing"}
new_brand = {"iq", "realmi", "nothing"}

diff1 = my_brand - new_brand
print(f"using - operator: {diff1}") # {'vivo', 'apple'}

diff2 = my_brand.difference(new_brand)
print(f"using difference method: {diff2}") # {'vivo', 'apple'}

# 4. Symmetric Difference
setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple"}

setC = setA ^ setB
print(f"using ^ operator: {setC}") # {'banana', 'cherry', 'google', 'microsoft'}

setD = setA.symmetric_difference(setB)
print(f"using symmetric_difference method: {setD}") # {'banana', 'cherry', 'google', 'microsoft'}


# =========== Exercise 1: Basic Operations
# Create a set: {10, 20, 30, 40, 20, 10}
# Print the set
# Add the number 50
# Remove the number 20
# Check if 30 is in the set
# Print the final set