# Solution 1: Grade Calculator

# Step 1: Get user input
# Prompt the user to enter a numeric score.
# Convert the input string to an integer.
score = int(input("Enter a numeric score (0-100): "))

# Step 2: Determine the grade using if-elif-else
# Use chained if, elif, and else staements to check the score against the grade boundaries.
if score < 0 or score > 100:
    print("Invalid score: Please enter a score between 0 and 100.")
else:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

# Print the grade: Display the calculated letter grade to the user.
    print(f"Your grade is: {grade}")


# Solution 2: Vowel or consonant

# Step 1: Get user input and convert to lowercase(case-insensitive comparison).
letter = input('Enter a letter: ').lower()

# Step 2: Validate the input
# Check if the input is a single alphabetic character. If not, print an "Invalid" message.
if len(letter) != 1 or not letter.isalpha():
    print('Invalid')

# Step 3: Determine if it's a vowel or consonant
# If the input is valid, check if it's in the set of vowels('a', 'e', 'i', 'o', 'u'). If it is, print "vowel"; otherwise, print "consonant".
elif letter in 'aeiou':
    print('vowel')
else:
    print('consonant')


# Solution 3: Nested if practice - Age group

# Step 1: Get user input for age
# Prompt the user to enter their age and score it as an integer.
age = int(input('Enter your age: '))

# Step 2: Implement conditional checks for age group
if age <= 0:
    print('invalid')
elif age < 13:
    print('child')
elif age < 20:
    print('teen')
elif age < 60:
    print('adult')
else:
    print('senior')


# Solution 4: Use match-case for weekday names

# Step 1: Get user input
# Prompt the user to enter a number between 1 and 7 to represent a weekday. Convert the input to an integer.
day = int(input("Enter a weekday number (1-7): "))

# Step 2: Use match-case to determine the weekday
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")