# Some examples

# 1. Create Tuple elements
numbers = (1, 2, 3, 4, 5)

t1 = 1, 2, 3 # Without parentheses
print(t1) # (1, 2, 3)

t2 = (5,) # single-element not a (5)
print(t2) # (5,)

# allow duplicate:
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits) # ('apple', 'banana', 'cherry', 'apple', 'cherry')


# 2. Finding length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # 3


# 3. type
print(type(thistuple)) # <class 'tuple'>


# 4. Data Types
# Tuple can be any data type:
friends = ("sathisha", "vishwas", "sudeep", "manoj", "rohit")
age = (24, 21, 24, 22, 23)
is_freshers = (True, False, False)

# contain mixed/different types
mixed_tuple = ("Thejas", 24, "ECE", True, 5.8)
print(f"I'm {mixed_tuple[0]}, {mixed_tuple[1]} year. I'm from {mixed_tuple[2]} dept") # I'm Thejas, 24 year. I'm from ECE dept


# 5. Tuple Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple) # ('apple', 'banana', 'cherry')

# 6. Access
mytuple = ("apple", "banana", "cherry") # Note: The first item has index 0.
print(mytuple[0]) # apple

# negative Indexing
print(mytuple[-1]) # cherry

# Range of index
num = (1, 2, 3, 4 ,5, 6, 7, 8)
print(num[2:5]) # (3, 4, 5)
print(num[:4]) # (1, 2, 3, 4)
print(num[4:]) # (5, 6, 7, 8)
print(num[-4:-1]) # (5, 6, 7)

# Check if item exists
fruits = ("apple", "banana", "cherry")
if "apple" in friends:
    print("Yes, 'apple' is in the fruits tuple")


# 7. Updating the tuple elements

# insert new item
x = (1, 2, 3)
print(f"Before Update >> {x}") # Before Update >> (1, 2, 3)
y = list(x)
y.insert(0, 0)
x = tuple(y)
print(f"After Update >> {x}") # After Update >> (0, 1, 2, 3)

# Changing the existing item
fruits = ('apple', 'mango', 'cherry')
print(f"Before change >> {fruits}") # ('apple', 'mango', 'cherry')
mylist = list(fruits)
mylist[1] = 'banana'
fruits = tuple(mylist)
print(f"After change >> {fruits}") # ('apple', 'banana', 'cherry')

# append
thistuple = 1, 2, 3
y = list(thistuple)
y.append(4)
thistuple = tuple(y)
print(thistuple) # (1, 2, 3, 4)

# concatenation
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) # ('apple', 'banana', 'cherry', 'orange')

# remove the item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) # ('banana', 'cherry')

# delete the complete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) # error: because the tuple no longer exists


# 8. Packing and unpacking

# packing
fruits = ('apple', 'banana', 'cherry')

# unpacking
fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits
print(green) # apple
print(yellow) # banana
print(red) # cherry

# rest values
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green) # apple
print(yellow) # banana
print(red) # ['cherry', 'strawberry', 'raspberry']

# 9. Loops
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# ranging
thistuple = ("apple", "banana", "cherry", "grapes")
for i in range(len(thistuple)):
    print(thistuple[i])

# while loop
thistuple = (1, 2, 3, 4, 5)
i = 0
while i< len(thistuple):
    print(thistuple[i])
    i = i + 1


# Exercise
# Exercise 1: Create tuple and indexing
# - Create a tuple t = (10, 20, 30, 40)
# - Print t[1] and t[-1]


# Exercise 2: Single element tuple
# - Create a single-element tuple containing 99 and print its type


# Exercise 3: Unpacking
# - Given person = ("Tejas", 23, "ECE"), unpack into name, age, dept and print them


# Exercise 4: Swap variables using tuple unpacking
# - a = 1; b = 2; swap them in one line


# Exercise 5: Tuple immutability
# - Given t = (1,2,3), try to change t[0] = 9 and note the error. Then convert to list, change, and back to tuple.


# Exercise 6: Tuple as dict key
# - Create a dict that uses a coordinate tuple (2,3) as a key with value 'point'