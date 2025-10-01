Goal: Learn if, elif, else, nested conditionals, and the match statement.

# Conditional Statements:

    Conditional statements allow we to execute different block of code based on certain condition. In Python, the most commonly used conditional statements are if, elif, else stements.

1. if Statement: Use if to run code when a condition is true. It follows the syntax:

   if condition: # code to be executed if condition is true

   - For example, let's say we want to check if a number is positive:

   num = 10
   if num > 0:
   print("The number is positive)

   In this example, the code inside the if block will only be executed if the condition num > 0 is true

2. elif (else-if): The elif statement allow we to check for additional or multiple conditions. It follows the below syntax:

   if condition1: # code to be executed if condition1 is true
   elif condition2: # code to be executed if condition2 is true

   - For example, let's say we want to check if a number is positive or negative:

   num = -5
   if num > 0: print("The number is positive")
   elif num < 0: print("The number is negative")
   else: print("The number is zero")

   In the example, if the condition num>0 is true, the code inside the if block will be executed. Otherwise, the code inside the else block will be executed.

3. else: Code to be excuted if all conditions are false

- Example:
  x = 10
  if x > 10:
  print("Greater than 10")
  elif x == 10
  print("Equal to 10")
  else:
  print("Less than 10")

# Truthy and Falsy values

- Falsy: 0, 0.0, "" (empty string), [], {}, None, False.
- Truthy: most other non-empty values.

We can use values directly in conditionals:
Example:
if my_list:
print("list not empty")

# Nested if

- We can place if inside another if. Keep indentation clear and shallow where possible.

and / or / not: and requires both True. or requires at least one True. not negates.

match(structure pattern matching)--Python 3.10+: Useful for multiple discrete cases (like switch/case in other languages).

Example:
command = "start"
match command:
case "start": print("Starting")
case "stop": print("Stopping")
case \_: print("Unknown command")
