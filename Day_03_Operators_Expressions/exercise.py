# Exercise 1: Arithmatic and precendence
# - Compute: result = 3 + 4 * 2 ** 3 - (6 / 3)
# - Print the result and explain (in a comment) with operation happened first
# Solution Hint: Evalute step by step using precedence: power first, then multiplication, then addition/subtraction, then division inside parentheses


# Exercise 2: Modulo use-case
# - Given a number n from input, print whether it is even or odd using %
# Solution HINT: if n % 2 == 0: print('even') else: print('odd')

# Exercise 3: Logical conditions
# - Ask the user for age and has_id (y/n)
# - Convert has_id to boolean (True if 'y' else False)
# - Print if the user can enter (age >= 18 and has_id is True)
# Solution HINT: 
# has_id = input('Have ID? (y/n): ').lower() == 'y'
# can_enter = age >= 18 and has_id

# Exercise 4: Compound assignment
# - Start with points = 0
# - Read 3 integer scores from user, after each score add to points using +=
# - At the end, print total points
# Solution HINT:
# points = 0
# for _ in range(3):
# points += int(input('score: '))
# print(points)