# ============ Exercise 1: Basic Operations in Sets

# 1. Create a set: {10, 20, 30, 40, 20, 10}
my_set = {10, 20, 30, 40, 20, 10}

# 2. Print the my_set
print(f"Initial set: {my_set}") # Initial set: {40, 10, 20, 30}

# 3. Add the number 50 to my_set
my_set.add(50)
print(f"Set after adding 50: {my_set}") # Set after adding 50: {40, 10, 50, 20, 30}

# 4. Remove the number 20 from my_set
my_set.discard(20)
print(f"Set after removing 20: {my_set}") # Set after removing 20: {40, 10, 50, 30}

# 5. Check if 30 is in the my_set
if 30 in my_set:
    print("30 is present in the my_set") # 30 is present in the my_set
else:
    print("30 is not present in the my_set")

# 6. Final output
print(f"The final set is: {my_set}") # The final set is: {40, 10, 50, 30}


# ============ Exercise 2: Core Set Operations

# 1. Creating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"Set A:  {A}") # Set A:  {1, 2, 3, 4}
print(f"Set B:  {B}") # Set B:  {3, 4, 5, 6}

# 2. Print Math Operations
# Union
print(f"Union: {A | B}") # Union: {1, 2, 3, 4, 5, 6}
# or A.union(B)

# Intersection
print(f"Intersection: {A & B}") # Intersection: {3, 4}
# or A.intersection(B)

# Difference
print(f"Difference (A - B): {A - B}") # Difference (A - B): {1, 2}
# or A.difference(B)

# Symmetric Difference
print(f"Symmetric Difference: {A ^ B}") # Symmetric Difference: {1, 2, 5, 6}
# or A.symmetric_difference(B)


# ============ Exercise 3: Real-world Use Case

python_students = ["Alice", "Bob", "Charlie", "David"]
java_students = ["Charlie", "David", "Eve", "Frank"]

know_both = set(python_students).intersection(java_students)
print(f"Know both: {know_both}") # Know both: {'Charlie', 'David'}

only_python = set(python_students).difference(java_students)
print(f"Only Python: {only_python}") # Only Python: {'Alice', 'Bob'}

at_least_one = set(python_students).union(java_students)
print(f"At least one: {at_least_one}") # At least one: {'Alice', 'Bob', 'David', 'Eve', 'Charlie', 'Frank'}


# === another way to solve this
python_students = ["Alice", "Bob", "Charlie", "David"]
java_students = ["Charlie", "David", "Eve", "Frank"]

# Convert lists to set
set_python = set(python_students)
set_java = set(java_students)

# 1. Students who know both Python and Java (Intersection)
know_both = set_python & set_java
# know_both = set_python.intersection(set_java)
print(f"Know both: {know_both}") # Know both: {'Charlie', 'David'}

# 2. Students who know only Python (Difference)
only_python = set_python - set_java
# only_python = set_python.difference(set_java)
print(f"Only Python: {only_python}") # Only Python: {'Alice', 'Bob'}

# 3. Students who know both Python and Java (Union)
at_least_one = set_python | set_java
# at_least_one = set_python.union(set_java)
print(f"At least one: {at_least_one}") # At least one: {'Alice', 'Bob', 'David', 'Eve', 'Charlie', 'Frank'}