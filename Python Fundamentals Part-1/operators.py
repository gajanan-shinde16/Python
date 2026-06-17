# Operators in python

# Arithmetic Operators
'''
a = 10
b = 3
print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Modulus: ", a % b)
print("Exponentiation: ", a ** b) # power
print("Floor Division: ", a // b)   # Floor/integer Division

'''

#Relational Operators
'''
a = 10
b = 20
print("Equal: ", a == b)
print("Not Equal: ", a != b)
print("Greater Than: ", a > b)
print("Less Than: ", a < b)
print("Greater Than or Equal: ", a >= b)
print("Less Than or Equal: ", a <= b)

'''

#Assignment Operators
'''
a = 10
b = 20
print("Assignment: ", a)
a += 5  # a = a + 5
print("Addition Assignment: ", a)
a -= 5  # a = a - 5
print("Subtraction Assignment: ", a)
a *= 5  # a = a * 5
print("Multiplication Assignment: ", a)
a /= 5  # a = a / 5
print("Division Assignment: ", a)
a %= 5  # a = a % 5
print("Modulus Assignment: ", a)
a **= 5  # a = a ** 5
print("Exponentiation Assignment: ", a)
a //= 5  # a = a // 5
print("Floor Division Assignment: ", a)
'''

'''
#Logical Operators
a = True
b = False
print("AND: ", a and b)
print("OR: ", a or b)
print("NOT: ", not a)

'''

'''

# Bitwise Operators (similar to java bitwise operators)
a = 5  # 0101
b = 3  # 0011
print("AND: ", a & b)
print("OR: ", a | b)
print("XOR: ", a ^ b)
print("NOT: ", ~a)
print("Left Shift: ", a << 1)
print("Right Shift: ", a >> 1)


'''
# Membership Operators (used to check if a value is present in a sequence)
s = "Hello, World!"
print('Hello' in s)
print('Python' in s)
print('Hello' not in s)

# Operator Precedence 
# Parentheses
# Exponentiation
# Multiplication, Division, Modulus, Floor Division
# Addition, Subtraction
# Relational Operators
# Logical Operators
# Assignment Operators
# Bitwise Operators
# Membership Operators
# Identity Operators
# Operator precedence can be overridden using parentheses.
result = (10 + 5) * 2  # Parentheses will be evaluated first
print("Result: ", result)