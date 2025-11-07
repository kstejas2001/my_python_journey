# Python Lists

A **list** in Python is a built-in data structure that holds an ordered, changeable (mutable) collection of items. Lists are defined by having elements inside square brackets `[ ]`, separated by commas.

---

## Key Characteristics

- **Ordered:** Elements maintain a specific sequence and can be accessed by their index.
- **Mutable:** Change, add, and remove items after creation.
- **Allow Duplicates:** Lists can contain duplicate values.
- **Heterogeneous:** Elements of different data types allowed (integers, strings, booleans, even other lists).
- **Dynamic:** Lists can grow or shrink in size.

---

## Creating Lists

### Using Square Brackets

```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = ["hello", 123, True, 3.14]
matrix = [[1, 2], [3, 4]] # Nested list
```

### With the `list()` Constructor

```python
my_list = list(("apple", "banana", "cherry")) # note the double round-brackets
string_to_list = list("python") # ['p', 'y', 't', 'h', 'o', 'n']
```

---

## Accessing List Items

Items are accessed by index. Indexing starts at **0**.

### Positive Indexing

Access items from the beginning.

```python
my_list = ["a", "b", "c", "d"]
print(my_list[0]) # Output: a
print(my_list[1]) # Output: b
print(my_list[2]) # Output: c
print(my_list[3]) # Output: d
```

### Negative Indexing

Access from the end of the list. Last item is at index **-1**.

```python
print(my_list[-1]) # Output: d
print(my_list[-2]) # Output: c
print(my_list[-3]) # Output: b
print(my_list[-4]) # Output: a
```

---

## List Comprehensions

### What is a List Comprehension ?

It's a **shortcut** way to create a list using a **single line**, instead of writing a full loop.

Think of it as:

`For each item in something, do something, and collect result into a new list.`

### Normal way (using a loop)

```python
squares = []
for x in range(1, 6):
  squares.append(x * x)
  print(squares)
  # Output: [1, 4, 9, 16, 25]
```

### Using list comprehension (short form)

```python
squares = [x * x for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]
```

Both do the **same thing**, but the comprehension is more compact.

### We can even add a condition

for example, only even squares:

```python
even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)
# Output: [4, 16, 36, 64, 100]
```

#### Syntax pattern:

```python
[ expression for item in iterable if condition ]
```

---

## Common List Operations & Methods

- **Adding elements:** `append()`, `insert()`, `extend()`
- **Remove elements:** `remove()`, `pop()`, `clear()`
- **Modify elements:** Assign new values with indexing
- **Slicing:** Extract sub-lists with `[start:end:step]`
- **Sorting:** `sort()` method or `sorted()` function
- **Reversing:** `reverse()` method
- **Finding elements:** `index()`, `count()`
- **Concatenation:** Use `+` operator
- **Repetition:** Use `*` operator

---

## Examples of List Operations

### 1. Accessing Items

List items are indexed and we can access them by referring to the index number.

- **Access items in Positive Indexing:**
  ```python
  fruits = ["apple", "banana", "cherry"]
  print(fruits[0]) # Output: apple
  print(fruits[1]) # Output: banana
  ```

We can also access items in Negative Indexing. It means start from the end. -1 refers to the last items, -2 refers to the second last item and so on.. For example,

- **Access items in Negative Indexing:**
  ```python
  print(fruits[-1]) # Output: cherry
  print(fruits[-2]) # Output: banana
  ```

### 2. Adding Elements

- **Append to end:**
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits.append("mango")
  print(fruits) # ["apple", "banana", "cherry", "mango"]
  ```
- **Insert at index:**

  ```python
  fruits.insert(2, "watermelon")
  print(fruits) # ["apple", "banana", "watermelon", "cherry", "mango"]
  ```

- **Extend with another list:**
  ```python
  fruit1 = ["apple", "banana", "cherry"]
  fruit2 = ["mango", "orange", "papaya"]
  fruit1.extend(fruit2)
  print(fruit1) # ["apple", "banana", "cherry", "mango", "orange", "papaya"]
  ```

### 3. Removing Elements

- **Remove Specified Item:**

  ```python
  fruits = ["apple", "kiwi", "orange", "cherry", "grapes", "kiwi"]
  fruits.remove("kiwi") # Output: ["apple", "orange", "cherry", "grapes", "kiwi"] Removes the first occurrence (if present)
  ```

- **Remove Specified Index:**

  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits.pop() # Remove the last item
  print(fruits) # Output: ["apple", "banana"]

  fruits = ["mango", "orange", "papaya"]
  fruits.pop(1) # Remove the second item
  print(fruits) # Output: ["mango", "papaya"]
  ```

- **Clear the Items:**
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits.clear() # Clears the entire list
  print(fruits) # Output: []
  ```

### 4. Modifying Elements

- **Change item by index:**

  ```python
  fruit = ["apple", "banana", "cherry"]
  fruits[1] = "orange"
  print(fruits) # ["apple", "orange", "cherry"]
  ```

- **Change a range:**
  ```python
  fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
  fruits[1:3] = ["blackcurrant", "watermelon"]
  print(fruits) # Output: ["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"] Updates the 2nd and 3rd items.
  ```

### 5. Slicing

We can specify where to start and where to end the range separated by a colon. For example,

- **Slicing in range:**

  ```python
  numbers = [1, 2, 3, 4, 5]
  print(numbers[1:4]) # Output: [2, 3, 4] (start at index 1, end before index 4)
  ```

- **Slice From the Start:**

  ```python
  print(numbers[:4]) # Output: [1, 2, 3, 4] (from start to index 3)
  ```

- **Slice From the End:**

  ```python
  print(numbers[2:]) # Output: [3, 4, 5] (from index 2 to end)
  ```

- **Negative Slicing:**
  ```python
  print(numbers[-4:-1]) # Output: [2, 3, 4] (from index -4 up to, not including, index -1)
  ```

### 6. Sorting Items

The sort() method sort the list ascending by default. For example

- **Sorting in ascending order:**

  ```python
  my_list = [3, 1, 4, 1, 5, 9, 2, 6]
  my_list.sort()
  print(f"Sorted in ascending order: {my_list}") # Output: [1, 1, 2, 3, 4, 5, 6, 9]

  ```

- **Sorting in descending order directly:**
  We can sort a list in descending order using sort() method with the reverse=True argument, or the sorted() function with reverse=True.

  ```python
  my_list = [3, 1, 4, 1, 5, 9, 2, 6]
  my_list.sort(reverse=True)
  print(f"Sorted in descending order (using sort()): {my_list}") # Output: [9, 6, 5, 4, 3, 2, 1, 1]

  my_list_2 = [3, 1, 4, 1, 5, 9, 2, 6]
  new_list = sorted(my_list_2, reverse=True)
  print(f"Sorted in descending order (using sorted()): {new_list}") # Output: [9, 6, 5, 4, 3, 2, 1, 1]

  nolan = ["inception", "interstellar", "tenet", "oppenheimer"]
  nolan.sort() # Sort the list alphabetically
  print(nolan) # Output: ['inception', 'interstellar', 'oppenheimer', 'tenet']
  ```

### 7. Reversing the List Items

If we only need to reverse the order of elements in a list without sorting it first, you can use the 'reverse()' method or list slicing.

- **Reverse without Sorting:**

  ```python
  my_list = [1, 2, 3, 4, 5]
  my_list.reverse()
  print(f"Reversed using reverse(): {my_list}")

  ```

- **Using Slicing:**
  ```python
  my_list_2 = [6, 7, 8, 9, 10]
  reversed_list = my_list_2[::-1]
  print(f"Reversed using slicing:{reversed_list}")
  ```

### 8. Finding elements

To find an element within a list in Python, several method are available, depending on whether we need to check for its presence, find its index, or retrieve all occurrences.

- **Using 'in' operator:**

  ```python
  my_list = ["apple", "banana", "cherry"]
  if "banana" in my_list:
  print("banana is in the list.")
  else:
  print("Not found.")

  ```

- **Using list.index():**
  ```python
  my_list = ["apple", "banana", "cherry", "banana"]
  try:
  index = my_list.index("banana")
  print(f"Banana found at index: {index}")
  except ValueError:
  print("Banana not found in the list.")
  ```

# 8. Quick notes (lists -- essentials)

- **What:** A list stores multiple items in ordered, is mutable. Example: nums = [1, 2, 3, 4]
- **Indexing:** num[0] --> first item, num[-1] --> last item.
- **Slicing:** num[1:3] --> items at indexes 1 and 2.
- **Common methods:** append(x) -- add to end, insert(i, x) -- insert at index i, remove(x) -- remove first occurrence of x, pop() / pop(i) -- remove and return last or at i, extend(iterable) -- add all items from another list, sort() / reverse() -- in place sorting/reversing, len(list) - length, x in list -- membership test

---

**Tip:**
Lists are among the most versatile Python data structures, allowing you to efficiently store, organize, and manipulate groups of data.
