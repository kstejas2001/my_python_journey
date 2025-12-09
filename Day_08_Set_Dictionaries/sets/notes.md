# sets

<<<<<<< HEAD
A `set` is an `unordered` collection of `unique` elements meaning do not allow duplicate values. It is built-in data type. It is one of 4 built-in data types in python

**What is set? (Simple Definition)**

=======
A `set` is an `unordered` collection of `unique` elements. It is built-in data type.

**What is set? (Simple Definition)**
>>>>>>> 8f2e1c6f6ebb0a0b83eb9d8fb807855ac874f10e
A **set** in python is:

- Unordered
- No duplicate values
- Mutable (we can add/remove items)

Look like this:

```python
s = {1, 2, 3}
```

---

## key characteristics:

- **Unordered:** Elements in a set do not have a defined order and cannot be accessed by index.
- **Unique Elements:** Sets automatically handle and remove duplicate values, ensuring each element within the set is distinct.
<<<<<<< HEAD
- **Mutable (mostly):** While the elements within a set must be immutable (e.g., numbers, strings, tuples), the set itself is mutable. We can add or remove elements from a set after its creation.
- **Mathematical set operations:** Sets support common mathematical set operations like union, intersection, difference, and symmetric difference.
=======
- **Mutable (mostly):** We can add or remove elements after a set has been created. However, the individual elements within the set are immutable.
>>>>>>> 8f2e1c6f6ebb0a0b83eb9d8fb807855ac874f10e
- **Heterogeneous:** Sets can store elements of different data types (e.g., integers, strings, booleans).

---

## Creating Sets:

<<<<<<< HEAD
- Sets can be created using: curly braces `{}` or the `set()` constructor.

```python
# 1. Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}

# 2. Creating a set set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))
print(thisset) # {'apple', 'banana', 'cherry'}

# 3. Creating a set from a list using the set() constructor
another_set = set([1, 2, 2, 3, 4, 4, 5])
print(another_set) # Output: {1, 2, 3, 4, 5} (duplicates removed)

# 4. Creating an empty set (empty curly braces create a dictionary)
empty_set = set()
print(empty_set) # set()
=======
Sets can be created using: curly braces `{}`.

```python
s = {1, 2, 3, 3, 2}
print(s) # {1, 2, 3}. Because duplicates are removed automatically.
my_set = {1, 2, 3, "apple", True}
>>>>>>> 8f2e1c6f6ebb0a0b83eb9d8fb807855ac874f10e
```

- **The `set()` constructor:** This can take an iterable (like a list or tuple) as an argument.

```python
my_list = [1, 2, 2, 3]
my_set = set(my_list) # {1, 2, 3}
```

<<<<<<< HEAD
### Duplicates Not Allowed

- 1. Set cannot have two items with same value.

Example: Duplicate value will be ignored.

```python
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # {'cherry', 'apple', 'banana'}
```

- 2. The values `True` and `1` are considered the same value in sets, and are treated as duplicates:

Example: `True` and `1` is considered the same value.

```python
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # {True, 2, 'apple', 'banana', 'cherry'}
```

- 3. The values `False` and `0` are considered the same value in sets, and are treated as duplicates:

Example: `False` and `0` is considered the same value.

```python
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) # {False, True, 'cherry', 'banana', 'apple'}
```

=======
>>>>>>> 8f2e1c6f6ebb0a0b83eb9d8fb807855ac874f10e
---

## Common Operations:

- **Adding elements:** Use `add()` for single element or `update()` for multiple elements (from an iterable).

```python
my_set = {1, 2, 3}
<<<<<<< HEAD
my_set.add(4) # It will be {1, 2, 3, 4}
my_set.update([5, 6])
print(my_set) # {1, 2, 3, 4, 5, 6}
=======
my_set.add(4)
my_set.update([5, 6]) # {1, 2, 3, 4, 5, 6}
>>>>>>> 8f2e1c6f6ebb0a0b83eb9d8fb807855ac874f10e
```

- **Removing elements:** Use `remove()` (raises `KeyError` is element not found) or `discard()`(does nothing if element not found). `pop()` removes and returns an arbitrary element.

```python
my_set = {1, 2, 3, 4, 5}
my_set.remove(1)
<<<<<<< HEAD
print(my_set) # {2, 3, 4, 5}

my_set.remove(7)
print(my_set) # KeyError (because, element '7' is not found)

my_set.discard(7)
print(my_set) # No error (because, element '7' is not found) If the element is found, it will just removed.
=======
my_set.remove(7) # KeyError (because, element '7' is not found)
my_set.discard(7) #
>>>>>>> 8f2e1c6f6ebb0a0b83eb9d8fb807855ac874f10e
```

- **Membership testing:** Use the `in` keyword for efficient checks.

```python
my_set = {"apple", "banana", "mango"}
if "apple" in my_set:
<<<<<<< HEAD
    print("Apple is in the set.") # Apple is in the set.

# Using Boolean values
s = {1, 2, 3}
print(1 in s) # True
print(5 in s) # False
```

- `add()` --> add only single elements
- `update()` --> adds multiple elements
- `remove()` --> error if the element not found
- `discard()` --> safe remove, no error

### Get the Length of a Set

```python
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # 3
```

### Set Item - Data Types

```python
# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set1 = {1, 3, 5, 7, 9}
set1 = {True, False, True}

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}
```

### type()

From Python, set are defined as objects with the data type 'set'.

```python
myset = {"apple", "banana", "cherry"}
print(type(myset)) # <class 'set'>
```

---

## Set Operations (VERY IMPORTANT)

These are **interview topics.**

Let:

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

- 1. **Union:** All unique items from both 'a' and 'b'

```python
print(a | b) # Output: {1, 2, 3, 4, 5} Unique
```

- 2. **Intersection:** Common items from both 'a' and 'b'

```python
print(a & b) # Output: {3} Common
```

- 3. **Difference:** Items in one set but not the other.

```python
print(a - b) # Output: {1, 2} In a but not in b
print(b - a) # Output: {4, 5} In b but not in a
```

- 4. **Symmetric Difference:** Items not common in both

```python
print(a ^ b) # Output: {1, 2, 4, 5} In a or b but not both
```

---

## Looping through a Set

```python
for item in {5, 10, 15}:
    print(item, end="") # 10 5 15.
```

**Note:** Order is random - because sets are unordered.

---

## Convert between list & set

```python
nums = [1, 2, 2, 3, 3, 3]
unique_nums = set(nums)
```

**Note:** Converts list --> removes duplicates.

---

## When to use Sets:

**Sets are particularly useful when we need to:**

- Store a collection of unique items.
- Efficiently check for membership of an element.
- Remove duplicate elements from a list ot other sequence.
- Perform mathematical set operation.
=======
    print("Apple is in the set.")
```
>>>>>>> 8f2e1c6f6ebb0a0b83eb9d8fb807855ac874f10e
