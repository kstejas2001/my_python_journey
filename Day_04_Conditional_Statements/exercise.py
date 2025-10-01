# Exercise 1: Grade calculator
# - Ask user for a numeric score (0-100)
# - Print grade:
#    90-100: A
#    80-89: B
#    70-79: C
#    60-69: D
#    <60: F
# Hint: Use chained if/elif/else with comparisons, e.g. if score >= 90: grade = 'A'


# Exercise 2: Vowel or consonant
# - Ask user for a single letter
# - Print whether it's a vowel or consonant (handle uppercase and lowercase)
# - If user input length != 1 or not a letter, print an error message
# Hint: letter = input('Enter a letter: ').lower()
# if len(letter) != 1 or not letter.isalpha(): print('Invalid')
# elif letter in 'aeiou': print('vowel') else: print('consonant')


# Exercise 3: Nested if practice — Age group
# - Ask for age
# - If age < 0: print invalid
# - Else if age < 13: print 'child'
# - Else if age < 20: print 'teen'
# - Else if age < 60: print 'adult'
# - Else: print 'senior'
# Hint: Use nested if only if needed. Prefer sequential elif checks as described.


# Exercise 4: Use match-case (if your Python >= 3.10)
# - Ask the user for a weekday number (1-7)
# - Use match-case to print the weekday name (1 -> Monday, ... 7 -> Sunday)
# - Handle invalid numbers with default case
# Hint: match day:
#           case 1: print('Monday')
#           case 2: print('Tuesday')
#           ...
#           case _: print('Invalid day')