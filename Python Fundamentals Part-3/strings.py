'''
Python allows variable reassignment.

A variable can be assigned a value and then later assigned a different value:

x = 10
print(x)  # 10

x = 20
print(x)  # 20

Python variables are just names that reference objects, so reassignment makes the name point to a new object.

You can even reassign to a different type:

x = 10        # integer
x = "hello"   # string

'''

str = "hello"

print(str)

print(str[2])

# print(str[100]) # IndexError: string index out of range

print(str[-2])

# Strings are immutable in python
# str[0] = "a" # TypeError: 'str' object does not support item assignment

str3 = str + " " + "dear"

print(str3)





# Slicing in Strings

# Syntax [start=0 , stop = n , step=1] stop is excluded (0,n,1 are def values) if step=-1 reverses string

s = "Python"

print(s[:3])      # Pyt
print(s[2:5])     # tho
print(s[3:])      # hon

# Entire string
print(s[:])       # Python

# Last 3 characters
print(s[-3:])     # hon

# String except last 2 characters
print(s[:-2])     # Pyth

# Every second character
print(s[::2])     # Pto

# Every third character
print(s[::3])     # Ph

# Reverse string
print(s[::-1])    # nohtyP

# Reverse part of string
print(s[4:1:-1])  # oht

# First character
print(s[0])       # P

# Last character
print(s[-1])      # n

# Characters between index 1 and 4
print(s[1:5])     # ytho

# Skip first and last character
print(s[1:-1])    # ytho

# Empty slice
print(s[2:2])     # ''

# Slice beyond length (no error)
print(s[:20])     # Python




# Formatting

# using .format()

name = "Alice"
age = 25
city = "Mumbai"

# Insert variables
print("Name: {}, Age: {}".format(name, age))
# Name: Alice, Age: 25

# Multiple variables
print("{} is {} years old.".format(name, age))
# Alice is 25 years old.

# Positional indexing
print("{1} lives in {0}".format(city, name))
# Alice lives in Mumbai

# Named arguments
print("{n} is {a} years old".format(n=name, a=age))
# Alice is 25 years old

# Float formatting
pi = 3.14159265
print("{:.2f}".format(pi))
# 3.14

# Width formatting
print("{:10}".format(name))
# Alice      (padded to width 10)

# Right align
print("{:>10}".format(name))
#      Alice

# Left align
print("{:<10}".format(name))
# Alice

# Center align
print("{:^10}".format(name))
#   Alice

# Integer formatting
num = 1234
print("{:,}".format(num))
# 1,234

# Percentage
score = 0.875
print("{:.1%}".format(score))
# 87.5%




# using f-strings  
 
name = "Alice"
age = 25
city = "Mumbai"

# Insert variables
print(f"Name: {name}, Age: {age}")
# Name: Alice, Age: 25

# Multiple variables
print(f"{name} is {age} years old.")
# Alice is 25 years old.

# Any order you want
print(f"{name} lives in {city}")
# Alice lives in Mumbai

# Float formatting
pi = 3.14159265
print(f"{pi:.2f}")
# 3.14

# Width formatting
print(f"{name:10}")
# Alice

# Right align
print(f"{name:>10}")
#      Alice

# Left align
print(f"{name:<10}")
# Alice

# Center align
print(f"{name:^10}")
#   Alice

# Integer formatting
num = 1234
print(f"{num:,}")
# 1,234

# Percentage
score = 0.875
print(f"{score:.1%}")
# 87.5%

# Expressions inside f-strings
print(f"Next year age: {age + 1}")
# Next year age: 26

# Method calls
print(f"{name.upper()}")
# ALICE