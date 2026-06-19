# Conditional Statements in Python

# If statement
age = 18
if age >= 18:
    print("You are eligible to vote.")

# If-Else statement
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:   
    print("You are not eligible to vote.")

# Elif statement
age = 20
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Nested If statement
age = 25
if age >= 18:
    if age >= 65:
        print("You are eligible for senior citizen benefits.")
    else:
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Match statement (Python 3.10+)-- Like switch-case in other languages
day = "Monday"
match day:
    case "Monday":
        print("It's the start of the work week.")
    case "Friday":
        print("It's almost the weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("It's a regular weekday.")