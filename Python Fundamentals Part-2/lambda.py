# Lambda Function
# A lambda function is a small anonymous function.
# It can have any number of arguments but only one expression.

# Syntax:
# lambda arguments : expression


# Example 1
square = lambda x: x * x
print(square(5))      # 25


# Example 2
add = lambda a, b: a + b
print(add(10, 20))    # 30


# Example 3
# Using lambda with sorted()

students = [
    ("Ram", 85),
    ("Shyam", 92),
    ("Ravi", 78)
]

students.sort(key=lambda x: x[1])

print(students)


# Equivalent normal function

def square(x):
    return x * x

# lambda funs used in higher order functions(can take fun as a input and can return output as a function)