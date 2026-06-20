# Inheritance in Python

# Inheritance allows one class (child/subclass) to acquire the attributes and methods of another class (parent/superclass).
# Instead of rewriting common code, we reuse it.

# Parent Class
#       ↑
#       |
# Child Class


# Why Use Inheritance?

# Without inheritance:

class Dog:
    def eat(self):
        print("Eating")

class Cat:
    def eat(self):
        print("Eating")

# The eat() method is duplicated.

# With inheritance:

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Both Dog and Cat automatically get eat().

# Basic Inheritance
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


d = Dog()

d.eat()

# Python searches:

# Dog
# Animal
# object

# Since eat() is not in Dog, it finds it in Animal.


# Parent and Child Attributes
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


d = Dog("Tommy")

print(d.name)

# Output:
# Tommy

# The child inherits the parent's constructor.


# Using super()

# Sometimes we want to extend parent behavior instead of replacing it.

class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

# Output:

# Animal sound
# Bark

# super() refers to the parent class.


# Inheriting Constructors

# Parent:

class Animal:
    def __init__(self, name):
        self.name = name

# Child:

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# Usage:

d = Dog("Tommy", "Labrador")

print(d.name)
print(d.breed)

# Output:

# Tommy
# Labrador

# Without super().__init__(), name would never be created.






# Types of Inheritance

# 1. Single Inheritance

# One child inherits from one parent.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof")


d = Dog("Tommy") #Python looks for a constructor (__init__) in Dog.Dog does not define its own __init__, so Python automatically uses the one inherited from Animal.

d.eat()      # inherited
d.bark()     # own method

# Output:

# Tommy is eating
# Tommy says Woof


# Using super() in Single Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # calls Animal.__init__
        self.breed = breed
        print("Dog constructor")


d = Dog("Tommy", "Labrador")

# Output:
# Animal constructor
# Dog constructor

# Without super().__init__(name), self.name would not exist.



# 2. Multilevel Inheritance

# A chain of inheritance.

class Animal:
    def eat(self):
        print("Eating")


class Mammal(Animal):
    def walk(self):
        print("Walking")


class Dog(Mammal):
    def bark(self):
        print("Barking")


d = Dog()

d.eat()
d.walk()
d.bark()

# Output:

# Eating
# Walking
# Barking



# super() Through Multiple Levels

class Animal:
    def __init__(self):
        print("Animal")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal")


class Dog(Mammal):
    def __init__(self):
        super().__init__()
        print("Dog")


d = Dog()

# Output:

# Animal
# Mammal
# Dog

# Call flow:

# Dog
#  ↓
# Mammal
#  ↓
# Animal

# Then returns upward.




# Hierarchical Inheritance

# One parent, multiple children.

class Employee:
    def login(self):
        print("Logged in")


class Developer(Employee):
    def code(self):
        print("Writing code")


class Tester(Employee):
    def test(self):
        print("Testing software")

# Usage:

dev = Developer()
tester = Tester()

dev.login()
dev.code()

tester.login()
tester.test()

# Output:

# Logged in
# Writing code
# Logged in
# Testing software


# Constructor Example

class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


class Tester(Employee):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

# Usage:

d = Developer("Rahul", "Python")
t = Tester("Amit", "Selenium")

print(d.name, d.language)
print(t.name, t.tool)



# 4. Multiple Inheritance

# One child inherits from multiple parents.

class Father:
    def money(self):
        print("Father's money")


class Mother:
    def jewelry(self):
        print("Mother's jewelry")


class Child(Father, Mother):
    pass


c = Child()

c.money()
c.jewelry()

# Output:

# Father's money
# Mother's jewelry



# Multiple Inheritance + Constructors

# Wrong way
class Father:
    def __init__(self):
        print("Father")


class Mother:
    def __init__(self):
        print("Mother")


class Child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child")

# Output:

Father
Child

# Only Father runs.

# Why?

# Because MRO(Method Resolution Order) is:
# print(Child.mro())
# [Child, Father, Mother, object]

# super() follows MRO.




# Cooperative Multiple Inheritance

# Proper usage:
# super() in parents is used to pass control to the next class in the MRO, so every class in a multiple-inheritance chain gets a chance to run its method.
class Father:
    def __init__(self):
        print("Father")
        super().__init__()


class Mother:
    def __init__(self):
        print("Mother")
        super().__init__()


class Child(Father, Mother):
    def __init__(self):
        print("Child")
        super().__init__()

# Usage:

c = Child()

# Output:

# Child
# Father
# Mother

# MRO:

# Child → Father → Mother → object 

# Each class calls the next one using super().


# 5. Hybrid Inheritance

# Combination of inheritance types.

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Bark")


class Cat(Animal):
    def meow(self):
        print("Meow")


class Puppy(Dog, Cat):
    pass

# Usage:

p = Puppy()

p.eat()
p.bark()
p.meow()

# Output:

# Eating
# Bark
# Meow


# Diamond Problem

# Most important multiple inheritance case.
'''
        Animal
       /      \
    Dog       Cat
       \      /
        Puppy
'''

class Animal:
    def speak(self):
        print("Animal")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Puppy(Dog, Cat):
    pass

# MRO:

print(Puppy.mro())

# Output:

# [Puppy, Dog, Cat, Animal, object]

# Python resolves ambiguity using MRO.


# Diamond Problem with super()

class Animal:
    def __init__(self):
        print("Animal")
        super().__init__()


class Dog(Animal):
    def __init__(self):
        print("Dog")
        super().__init__()


class Cat(Animal):
    def __init__(self):
        print("Cat")
        super().__init__()


class Puppy(Dog, Cat):
    def __init__(self):
        print("Puppy")
        super().__init__()

# Usage:

p = Puppy()

# Output:

# Puppy
# Dog
# Cat
# Animal

# Notice:

# Animal runs only once

# This is the biggest advantage of Python's MRO.

# super() does NOT mean "parent"

# It means:

# "Call the next class in the MRO."