# Encapsulation in Python

# Encapsulation means bundling data (attributes) and methods together inside a class and controlling access to the data.

# The goal is to:

# Protect data from accidental modification.
# Hide implementation details.
# Provide controlled access through methods.

# 1. Public Members

# By default, all attributes and methods are public.

'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Rohit", 50000)

print(e1.name)
print(e1.salary)

'''

# 2. Protected Members (_attribute)

# A single underscore is a convention indicating:
# "This is for internal use. Don't access it directly unless necessary."

'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

        '''
# Usage:
'''
e1 = Employee("Rohit", 50000)

print(e1._salary)

'''

# This still works.
# Python does not enforce protection. It's just a warning to programmers.


# 3. Private Members (__attribute)
# Double underscore triggers name mangling.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

# Now:

e1 = Employee("Rohit", 50000)
# print(e1.__salary)

# Error:
# AttributeError

# Because Python internally changes the name to:
# _Employee__salary

# You can see it:
print(e1.__dict__)

# Technically you can still access it:

print(e1._Employee__salary)
# So Python's private attributes are not truly private. They are designed to prevent accidental access, not determined access.



# Instead of getters and setters like Java, Python often uses @property.
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter # A property can also control assignment.
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Salary must be positive")

e1 = Employee(50000)

print(e1.salary)

e1.salary = 60000
e1.salary = -1000 # Notice that we access salary like an attribute, but validation happens behind the scenes.

# @property is one of Python's most useful features. It lets you use a method like an attribute.

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary


e = Employee(50000)

print(e.salary) # looks like an attribute but Python actually calls: salary(self) behind the scenes.

# You can also control deletion.

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.deleter
    def salary(self):
        print("Deleting salary")
        del self.__salary

# Usage:
del e.salary

# Python calls:
# salary.deleter(e)


# property is "An attribute on the outside, a method on the inside."