# Type Conversion in Python

#implicit Type Conversion
a = 5  # integer
b = 2.0  # float
c = a + b  # implicit type conversion (integer to float)
print("Result: ", c)
print("Type of c: ", type(c))

#explicit Type Conversion(Type Casting)
d = int(c)  # explicit type conversion (float to integer)
print("Result: ", d)
print("Type of d: ", type(d))
