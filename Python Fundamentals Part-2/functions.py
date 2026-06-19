# Functions in Python
# function is a reusable block of code

def hello(): # fun definition
    print("hello")

hello() # fun call
# hello()
# hello()

# with parameters
def greet(name): # parameter name
    print("Hello Mr.", name);

greet("Alex") #argument Alex

# returns a value
def get_sum(a,b):
    return a+b

sum = get_sum(2,7)
print(sum)

# returns multiple values (tuple)

def sum_diff(a,b):
    return a+b , a-b

sum,diff = sum_diff(5,3)

print(sum)
print(diff)

print(sum_diff(6,4)) # we can see it returned a tuple


# Default values

def sum(a,b=0):
    print(a+b)

sum(6)


# def sum(a=0,b): # error --> Non-default argument follows default argument
#     print(a+b)

sum(6)
sum(4,6)