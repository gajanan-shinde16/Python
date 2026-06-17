# Taking User Input

# Taking input from the user using input() function
# The input() function always returns a string, so if you want to take numerical input, you need to convert it to the appropriate type using int() or float().

'''
# Taking string input
name = input("Enter your name: ")
print("Hello, ", name)

# Taking integer input
age = int(input("Enter your age: "))
print("You are ", age, " years old.")

# Taking float input
height = float(input("Enter your height in meters: "))
print("Your height is ", height, " meters.")

'''

# try

x = input("Enter a number: ")
y = input("Enter another number: ")

print("sum: ", x+y) # This will concatenate the two strings instead of adding them as numbers

