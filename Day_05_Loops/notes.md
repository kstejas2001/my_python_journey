- Goal: Learn iteration using while, for, break, continue, and renge().

- Why loops?
  Loops let repeats the code multiple times without writing it again.
  Two main types in Python:

1. while loop - repeat while a condition is true
2. for loop - iterate over a sequence (string, list, range, ect.).

Example 1: while loop

count = 1
while count <= 5:
print("Count:", count)
count += 1

Example 2: for loop with range()

for i in range(5): # 0, 1, 2, 3, 4
print("i:",i)

- range(start, stop, step) -> generates numbers from start to stop-1.

Example 3: break and continue

for i in range(1, 6):
if i == 3:
break # exit loop
print(i)

for i in range(1, 6):
if i == 3:
continue # skip current iteration
print(i)

Example 4: Nested loops

for i in range(3):
for j in range(2):
print(i, j)
