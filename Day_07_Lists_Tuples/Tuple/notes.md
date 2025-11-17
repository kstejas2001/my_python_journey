# What is tuple?

A tuple is an **ordered**, **immutable** collection of items. Meaning its contents cannot be changed after it is created. Tuples are written with parentheses `()` and commas, such as `(1, 2, 3)`. They are used for storing fixed collections of data and are particularly useful for returning multiple values from a function, as they allow for a specific number and sequence of values.

### Syntax

```python
t = (1, 2, 3)
# or without parentheses
t = 1, 2, 3
```

### Single-element tuple (common pitfall)

```python
t = (5,) # correct single-element tuple
not_a_tuple = (5) # this is just the number 5
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

## Why use tuples?

- Immutability makes data safer (can't accidentally change).
- Tuples can be used as keys in dictionaries(list can't).
- Slightly faster and smaller than lists - useful for fixed collections.

---

## Key characteristics

- **Ordered:** The order of elements in a tuple is maintained and does not change.
- **Immutable:** Once a tuple is created, its elements cannot be modified, added, or removed. We can, however, create a new tuple based on the old one.
- **Heterogeneous:** Tuples can contain elements of different data types, such as strings, integers, and booleans, within the same tuple.
- **Indexed:** Each element in a tuple is assigned an index, starting from zero, which can be used to access the element.

---

## Accessing items

- Indexing and slicing works like lists:

```python
t = (10, 20, 30)
print (t[0]) # 10
print (t[-1]) # 30
print (t[0:2]) #(10, 20)
```

## Tuple methods

- `count(value)` - number of occurrences
- `index(value)` - first index of value

### Example:

```python
t = (1, 2, 2, 3)
print(t.count(2)) # 2
print(t.index(3)) # 3 -> index 3
```

---

## Tuple Items -Data Types

Tuple items can be any data type:

```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```

A tuple can contain different data types:

```python
tuple1 = ("abc", 34, True, 40, "male")
```

---

## Packing and Unpacking

- **Packing** packs values into tuple:

```python
person = "Thejas", 23, "ECE" # packed tuple
```

- **Unpacking** assigns tuple elements to variable.

```python
name, age, dept = person
```

- Use **`*rest`** to capture remaining items;

```python
a, b, *rest = (1, 2, 3, 4, 5) # a=1, b=2, rest=[3,4,5]
```

## Immutability - what we can still do

- Reassign the variable name to a new tuple: `t = (1, 2); t = (3, 4)` is allowed
- Convert to list to modify, then back: `lst = list(t); lst[0] = 9; t = tuple(lst)`

## Tuple as dictionary keys

```python
d = {}
d[(1, 2)] = "pair"
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

## When to choose tuple vs list

- Use tuple when collection is fixed and want immutability or dict-keys. Use list for frequent modification.

---

## Common uses

- **Function return values:** A function can return multiple values bundled together in a single tuple.
- **Data structures:** Tuples can represent a single record or row of data in a database table.
- **Storing fixed data:** They are ideal for situations where you need to ensure the data will not change, like the coordinates of a point (x, y).
- **Using as dictionary keys:** Since they are immutable, tuples can be used as keys in a dictionary, unlike lists.
