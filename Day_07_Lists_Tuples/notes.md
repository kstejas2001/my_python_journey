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

empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = ["hello", 123, True, 3.14]
matrix = [[1, 2], [3, 4]] # Nested list

### With the `list()` Constructor

my_list = list(("apple", "banana", "cherry")) # note the double round-brackets
string_to_list = list("python") # ['p', 'y', 't', 'h', 'o', 'n']

---

## Accessing List Items

Items are accessed by index. Indexing starts at **0**.

### Positive Indexing

Access items from the beginning.

my_list = ["a", "b", "c", "d"]
print(my_list[0]) # Output: a
print(my_list[1]) # Output: b
print(my_list[2]) # Output: c
print(my_list[3]) # Output: d

### Negative Indexing

Access from the end of the list. Last item is at index **-1**.

print(my_list[-1]) # Output: d
print(my_list[-2]) # Output: c
print(my_list[-3]) # Output: b
print(my_list[-4]) # Output: a

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

# Examples for Common List Operations:

1. Accessing List Items: List items are indexed and we can access them by referring to the index number.

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # Output: apple
print(fruits[1]) # Output: banana

We can also access items in Negative Indexing. It means start from the end.
-1 refers to the last items, -2 refers to the second last item and so on..

Example:
print(fruits[-1]) # Output: cherry
print(fruits[-2]) # Output: banana

2. Adding Elements.

- append items: To add an item to the end

  fruits = ["apple", "banana", "cherry"]
  fruits.append("mango")
  print(fruits) # Output: ["apple", "banana", "cherry", "mango"] adds to the end

- Insert items: To insert a list item at a specified index

  fruits = ["apple", "banana", "cherry"]
  fruits.insert(2, watermelon)
  print(fruits) # Output: ["apple", "banana", "watermelon"]

- Extend List: To append elements from another list to the current list

  fruit1 = ["apple", "banana", "cherry"]
  fruit2 = ["mango", "orange", "papaya"]
  fruit1.extend(fruit2)
  print(fruit1) # ["apple", "banana", "cherry", "mango", "orange", "papaya"]

3. Removing Elements.

- remove items: removes the specified item

fruits.remove("apple") # Output: ["kiwi", "orange", "cherry", "grapes"] Removes the first occurrence of the value

4. Modifying Elements.

- Change the Items Value
  fruits[1] = "orange" # Change the second item
  print(fruits) # Output: ["apple", "orange", "cherry"]

- Change the range of items
  fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
  fruits[1:3] = ["blackcurrant", "watermelon"] change the value of items within a specific range
  print(fruits)

5. Slicing method: We can specify where to start and where to end the range.

Example:
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4]) # Output: [2, 3, 4] (Return the second, third, and fourth item.)

Note: The search will start at index 1(included) and end at index 4(not included). The first item has index 0.

print(numbers[:4]) # Output: [1, 2, 3, 4]
This example returns the items from the beginning to, but NOT including, "5". By leaving out the start value.

print(numbers[2:]) # Output: [3, 4, 5]
By leaving out the end value

print(numbers[-4:-1]) # Output: [2, 3, 4]
This example returns the items from "2" (-4) to, but NOT including "5" (-1)
