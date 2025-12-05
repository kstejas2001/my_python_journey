# sets

A `set` is an `unordered` collection of `unique` elements. It is built-in data type.

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
- **Mutable (mostly):** We can add or remove elements after a set has been created. However, the individual elements within the set are immutable.
- **Heterogeneous:** Sets can store elements of different data types (e.g., integers, strings, booleans).

---

## Creating Sets:

Sets can be created using: curly braces `{}`.

```python
s = {1, 2, 3, 3, 2}
print(s) # {1, 2, 3}. Because duplicates are removed automatically.
my_set = {1, 2, 3, "apple", True}
```

- **The `set()` constructor:** This can take an iterable (like a list or tuple) as an argument.

```python
my_list = [1, 2, 2, 3]
my_set = set(my_list) # {1, 2, 3}
```

---

## Common Operations:

- **Adding elements:** Use `add()` for single element or `update()` for multiple elements (from an iterable).

```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6]) # {1, 2, 3, 4, 5, 6}
```

- **Removing elements:** Use `remove()` (raises `KeyError` is element not found) or `discard()`(does nothing if element not found). `pop()` removes and returns an arbitrary element.

```python
my_set = {1, 2, 3, 4, 5}
my_set.remove(1)
my_set.remove(7) # KeyError (because, element '7' is not found)
my_set.discard(7) #
```

- **Membership testing:** Use the `in` keyword for efficient checks.

```python
my_set = {"apple", "banana", "mango"}
if "apple" in my_set:
    print("Apple is in the set.")
```
