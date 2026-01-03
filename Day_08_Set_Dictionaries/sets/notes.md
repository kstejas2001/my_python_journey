# sets

A `set` is an `unordered` collection of `unique, hashable elements` meaning do not allow duplicate values(mutable). It is built-in data type. It is one of 4 built-in data types in python. They also support mathematical operations such as union, intersection, and difference.

**What is set? (Simple Definition)**

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
- **Mutable (mostly):** While the elements within a set must be immutable (e.g., numbers, strings, tuples), the set itself is mutable. We can add or remove elements from a set after its creation.
- **Mathematical set operations:** Sets support common mathematical set operations like union, intersection, difference, and symmetric difference.
- **Heterogeneous:** Sets can store elements of different data types (e.g., integers, strings, booleans).

---

## Creating Sets:

- Sets can be created using: curly braces `{}` or the `set()` constructor. Curly braces are used for non-empty sets, ignoring duplicate values. For instance:

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
```

- **The `set()` constructor:** This can take an iterable (like a list or tuple) as an argument.

```python
my_list = [1, 2, 2, 3]
my_set = set(my_list) # {1, 2, 3}
```

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

---

## Common Set Operations:

- **1. Adding elements:** Use `add()` for single element or `update()` for multiple elements (from an iterable).

```python
my_set = {1, 2, 3}
my_set.add(4) # It will be {1, 2, 3, 4}
my_set.update([5, 6])
print(my_set) # {1, 2, 3, 4, 5, 6}
```

Add elements from another set into current set.

```python
thisset = {"apple", "banana", "cherry"}
another = {"pineapple", "mango", "papaya"}
thisset.update(another)
print(thisset) # {'apple', 'banana', 'papaya', 'pineapple', 'mango', 'cherry'}
```

Add elements of a list to at set

```python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # {'cherry', 'orange', 'apple', 'kiwi', 'banana'}
```

- **2. Removing elements:** Use `remove()` (raises `KeyError` is element not found) or `discard()`(does nothing if element not found). `pop()` removes and returns an arbitrary element.

```python
my_set = {1, 2, 3, 4, 5}
my_set.remove(1)
print(my_set) # {2, 3, 4, 5}

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # {'apple', 'cherry'}

my_set.remove(7)
print(my_set) # KeyError (because, element '7' is not found)

my_set.discard(7)
print(my_set) # No error (because, element '7' is not found) If the element is found, it will just removed.
```

Remove a random item by using `pop()` method:

```python
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) # (remove randomly)
print(thisset) # expect removed item

# clear() method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set() empty set

# del() keyword will delete complete set
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) # error: not defined
```

- **3. Membership testing:** Use the `in` keyword for efficient checks.

```python
my_set = {"apple", "banana", "mango"}
if "apple" in my_set:
    print("Apple is in the set.") # Apple is in the set.

# Using Boolean values
s = {1, 2, 3}
print(1 in s) # True
print(5 in s) # False
```

- `add()` --> add only single elements
- `update()` --> adds multiple elements
- `remove()` --> removes element or error if the element not found
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
