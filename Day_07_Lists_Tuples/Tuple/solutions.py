# Solution 1: Create tuple and indexing
t = (10, 20, 30, 40)
print(t[1], t[-1]) # 20 40


# Solution 2: Single element tuple
single_tuple = (99,)
print(type(single_tuple)) # <class 'tuple'>


# Solution 3: Unpacking

# Step 1: Unpack the tuple
person = ("Tejas", 23, "ECE")
name, age, dept = person

# Step 2: Print the variables
print(f"Name: {name}") # Name: Tejas
print(f"Age: {age}") # Age: 23
print(f"Department: {dept}") # Department: ECE


# Solution 4: Swap variables using tuple unpacking
a, b = 1, 2
print(f"Before swap a = {a}, b = {b}") # Before swap a = 1, b = 2
a, b = b, a
print(f"After swap a = {a}, b = {b}") # After swap a = 2, b = 1


# Solution 5: Tuple immutability
try:
    t = (1, 2, 3)
    print(f"Original tuple: {t}")
    t[0] = 9
except TypeError as e:
    print(f"Error: {e}")
mylist = list(t)
mylist[0] = 9
t = tuple(mylist)
print(f"Modified tuple: {t}")

# Solution 6: Tuple as dict key
d = {}
d[(2, 3)] = "point"
print(d)