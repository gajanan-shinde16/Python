# Loops in Python

# For Loop
# Used to iterate over a sequence (list, string, tuple, etc.)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# While Loop
# Runs as long as the condition is True

count = 0

while count < 5:
    print(count)
    count += 1


# Nested Loops
# A loop inside another loop

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# f-string:
# f makes the string a formatted string.
# Values inside {} are evaluated and inserted into the string.


# Loop with Else
# else executes when the loop finishes normally

for num in range(5):
    print(num)
else:
    print("Loop completed successfully.")


# Break Statement
# Stops the loop immediately

for i in range(10):
    print(i)

    if i == 6:
        break


# Continue Statement
# Skips the current iteration

for i in range(10):

    if i % 2 == 0:
        continue

    print(i)


# Membership Operator (in)
# Checks whether an element is present

text = "Hello"

if 'l' in text:
    print("l is present in Hello")


# Range Function
# Generates a sequence of numbers

# Syntax:
# range(start, stop, step)

# start -> starting value (default 0)
# stop  -> ending value (not included)
# step  -> increment/decrement value (default 1)

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)