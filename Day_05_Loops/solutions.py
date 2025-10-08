# Solution 1: Print numbers 1 to 10 using a while loop.

count = 1
while count <= 10:
    print(count)
    count += 1


# Solution 2: Print squares of numbers from 1 to 5 using a for loop.

for i in range(1, 6):
    print(i ** 2)


# Solution 3: Write a loop that prints only odd numbers from 1 to 10.

for i in range(1, 11):
    if i % 2 == 1:
        print(i)


# Solution 4: Use a for loop with break — stop the loop when number == 7.
for i in range(1, 11):
    if i == 7:
        break
    print(i)



# Solution 5: Use a for loop with continue — skip number 5 but print others (1–7).

for i in range(1, 8):
    if i == 5:
        continue
    print(i)


# Solution 6: Nested loops pattern
for i in range(1, 6):
    print ("*" * i)