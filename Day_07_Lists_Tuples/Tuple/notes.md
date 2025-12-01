# What is tuple?

A tuple is an **ordered**, **immutable** collection of items. Meaning its contents cannot be changed after it is created. Tuples are written with parentheses `()` and commas, such as `(1, 2, 3)`. They are used for storing fixed collections of data and are particularly useful for returning multiple values from a function, as they allow for a specific number and sequence of values.

### Syntax

```python
t = (1, 2, 3)
# or without parentheses
t = 1, 2, 3
```

### Creating Tuples:

```python
# Empty tuple
empty_tuple = ()
```

---

## Key characteristics

- **Ordered:** The order of elements in a tuple is maintained and does not change.
- **Finite:** A tuple has a fixed number of elements.
- **Immutable:** Once a tuple is created, its elements cannot be modified, added, or removed. We can, however, create a new tuple based on the old one. Attempting to do so will result in a `TypeError`
- **Heterogeneous:** Tuples can contain elements of different data types, such as strings, integers, and booleans, within the same tuple.
- **Indexed:** Each element in a tuple is assigned an index, starting from zero, which can be used to access the element.

---

### Single-element tuple (common pitfall)

```python
t = (5,) # correct single-element tuple
not_a_tuple = (5) # this is just the number 5
```

### type()

tuples are defined as objects with data type 'tuple':
`<class 'tuple'>`

```python
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # <class 'tuple'>
```

### Allow Duplicates

Since tuples are indexed, they can have items with same value:

```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry") # ("apple", "banana", "cherry", "apple", "cherry")
```

### Tuple Length

To determine how many items a tuple has, use the `len()` function:

```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # 3
```

---

## Why use tuples?

- Immutability makes data safer (can't accidentally change).
- Tuples can be used as keys in dictionaries(list can't).
- Slightly faster and smaller than lists - useful for fixed collections.

---

## Accessing items

Tuple items can be accessed using indexing, similar to how elements in a list are accessed.

```python
t = (10, 20, 30)
# 1. Positive indexing:
print (t[0]) # 10
print (t[1]) # 20

# 2. Negative Indexing:
print (t[-1]) # 30
print (t[-2]) # 20

# 3. Slicing (Range of Indexes):
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi")
print(my_tuple[1:4]) # ("banana", "cherry", "orange")
print(my_tuple[:3]) # ("apple", "banana", "cherry")
print(my_tuple[2:]) # ("cherry", "orange", "kiwi")
print(my_tuple[-4:-1]) # ("banana", "cherry", "orange")
```

### Check if Item Exists

To determine if a specified item is present in a tuple use the `in` keyword:

```python
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple is in the fruits tuple")
```

---

## Immutability - what we can still do

Tuples in Python are immutable, which means their elements **cannot be changed, added, or removed after the tuple's creation**. However, there are workarounds to achieve the effect of "updating" a tuple by creating a new tuple with the desired modifications.

### Common methods for "updating" tuple:

- **Convert to List, Modify, Covert Back to Tuple:** This is the most common and versatile method for making individual element changes.

```python
my_tuple = ("apple", "banana", "cherry")
temp_list = list(my_tuple) # Convert to a list
temp_list[1] = "kiwi" # Modify the list
my_tuple = tuple(temp_list) # Convert back to a tuple
print(my_tuple) # ("apple", "banana", "cherry", "kiwi")
```

- **Reassignment:** If the entire tuple needs to be replaced with a new set of values, simply reassign the variable to a new tuple.

```python
my_tuple = (10, 20, 30)
my_tuple = (100, 20, 30) # Reassigning the variable to a new tuple
print(my_tuple) # (100, 20, 30)
```

- **Tuple Concatenation:** This method is useful for adding elements to the end of a tuple or combining multiple tuples.

```python
my_tuple = (1, 2, 3)
new_elements = (4, 5)
updated_tuple = my_tuple + new_elements # Creates a new tuple
print(updated_tuple) # (1, 2, 3, 4, 5)

# To "change" an element using concatenation and slicing:
original_tuple = ("a", "b", "c")
index_to_change = 1
new_value = "x"
updated_tuple = original_tuple[:index_to_change] + (new_value,) + original_tuple[index_to_change+1:]
print(updated_tuple) # ("a", "x", "c")
```

- **Use Unpacking (Python 3.5+):** The unpacking operator (\*) provides a clean way to merge tuples or insert elements when creating a new tuple.

```python
# Original tuple
fruits = ("apple", "banana", "cherry")
# Unpack the original tuple and add new elements to create a new tuple
new_fruits = (*fruits[:1], "kiwi", *fruits[2:])
print(new_fruits) # ('apple', 'kiwi', 'cherry')
```

---

## Tuple methods

- `count(value)` - number of occurrences
- `index(value)` - first index of value and returns the position

### Example:

```python
t = (1, 2, 2, 3)
print(t.count(2)) # 2
print(t.index(3)) # 3 -> index 3
```

---

## Tuple Items - Data Types

Tuple items can be any data type:

```python
tuple1 = ("apple", "banana", "cherry") # String
tuple2 = (1, 5, 7, 9, 3) # Int
tuple3 = (True, False, False) #Boolean
```

A tuple can contain mixed data types:

```python
tuple1 = ("abc", 34, True, 40, "male")
```

### Returning multiple values from a function

```python
def get_user_info():
    return ("Bob", 30)

name, age = get_user_info()
print(name) # Output: Bob
print(age): # Output: 30
```

---

## The tuple() Constructor

The `tuple()` constructor in python is a built-in function used to crate tuple objects.

### How to use `tuple()` constructor:

Creating an empty tuple.

```python
my_empty_tuple = tuple()
print(my_empty_tuple) # ()
```

### Converting an iterable to a tuple:

The `tuple()` constructor can take an iterable (like a list, string, set, or range) as an argument and convert it into a tuple.

- **From a list**

```python
my_list = [1, 2, 3, 4]
my_tuple_from_list = tuple(my_list)
print(my_tuple_from_list) # (1, 2, 3, 4)
```

- **From a String**

```python
my_string = "hello"
my_tuple_from_string = tuple(my_string)
print(my_tuple_from_string) # ('h', 'e', 'l', 'l', 'o')
```

- **From a set**

```python
my_set = {10, 20, 30}
my_tuple_from_set = tuple(my_set)
print(my_tuple_from_set) # (10, 20, 30) # Order might vary as sets are unordered
```

- **From a range**

```python
my_range = range(5)
my_tuple_from_range = tuple(my_range)
print(my_tuple_from_range) # (0, 1, 2, 3, 4)
```

---

## Packing and Unpacking

- **Packing** packs values into tuple:

```python
person = "Thejas", 23, "ECE" # packed tuple
```

- **Unpacking** assigns tuple elements to variable.

Tuple unpacking, also known as multiple assignment or destructuring assignment, is a Python feature that allows you to assign the individual elements of a tuple (or any iterable) to multiple variables in a single line

```python
person = "Thejas", 23, "ECE"
name, age, dept = person
print(name) # Thejas
print(age) # 23
print(dept) # ECE
```

Use **`*rest`** to capture remaining items;

```python
a, b, *rest = (1, 2, 3, 4, 5) # a=1, b=2, rest=[3,4,5]

numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

---

## Tuple as dictionary keys

```python
d = {}
d[(1, 2)] = "pair"
```

---

## Loop Tuples

Looping through tuples in Python allows you to access and process each individual item within the tuple.

- 1. Using `for` loop

```python
my_tuple = ("apple", "banana", "cherry")
for item in my_tuple:
    print(item)
```

- 2. Using a `for` loop with `range()` and `len()`:

```python
my_tuple = ("apple", "banana", "cherry")
for i in range(len(my_tuple)):
    print(f"Item at index {i}: {my_tuple[i]}")
```

- 3. Using a `for` loop with `enumerate()`:

```python
my_tuple = ("apple", "banana", "cherry")
for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value: {value}")
```

- 3. Using a `while` loop

```python
my_tuple = ("apple", "banana", "cherry")
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1
```

---

## Common interview pitfalls & tips

- Remember the single-element tuple comma: `(5,)`.
- Known the `()` is an empty tuple.
- Tuples are immutable but can contain mutable objects (e.g., lists). The tuple can't be replaced but the inner list can be changed.

Example:

```python
t = ([1, 2], 3)
t[0].append(5) # allowed - inner list mutated
```

---

## When to choose tuple vs list

- Use tuple when collection is fixed and want immutability or dict-keys. Use list for frequent modification.

---

## Common uses

- **Function return values:** A function can return multiple values bundled together in a single tuple.
- **Data structures:** Tuples can represent a single record or row of data in a database table.
- **Storing fixed data:** They are ideal for situations where we need to ensure the data will not change, like the coordinates of a point (x, y).
- **Using as dictionary keys:** Since they are immutable, tuples can be used as keys in a dictionary, unlike lists.
