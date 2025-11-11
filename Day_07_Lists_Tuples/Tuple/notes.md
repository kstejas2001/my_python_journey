# What is tuple?

A tuple is an **ordered**, **immutable** collection of items. It is like a list, but we cannot change (mutate) its elements after creation.

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

## Why use tuples?

- Immutability makes data safer (can't accidentally change).
- Tuples can be used as keys in dictionaries(list can't).
- Slightly faster and smaller than lists - useful for fixed collections.

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
