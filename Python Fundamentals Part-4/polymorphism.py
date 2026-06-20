# Polymorphism in Python

# Polymorphism means:
# "One Interface, Many Forms"
#
# Same method name,
# different behavior depending on the object.


# Why Polymorphism?

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

# Both classes have the same method: sound()
# But each behaves differently.


# Basic Polymorphism

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

# Output:
# Bark
# Meow

# Same method call:
# animal.sound()
#
# Different outputs depending on object.


# Polymorphism with Inheritance

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()

# Output:
# Bark
# Meow

# Child classes override the parent's method.


# Method Overriding

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Dog provides its own implementation of sound().

d = Dog()
d.sound()

# Output:
# Bark


# Real World Example

class Payment:
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card")

payments = [UPI(), CreditCard()]

for p in payments:
    p.pay(1000)

# Output:
# Paid ₹1000 via UPI
# Paid ₹1000 via Credit Card

# Same method:
# pay()
#
# Different implementations.


# Built-in Polymorphism

print(len("Python"))

print(len([1, 2, 3, 4]))

print(len({"a": 1, "b": 2}))

# Output:
# 6
# 4
# 2

# Same function:
# len()
#
# Works differently for different objects.


# Duck Typing (Python's Polymorphism)

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())

# Output:
# Bark
# Meow

# Python doesn't care about the class.
# It only cares whether the object has speak().


# Quick Summary

# Polymorphism = One Interface, Many Forms
#
# Achieved by:
# 1. Method Overriding
# 2. Inheritance
# 3. Duck Typing
#
# Examples:
# sound()
# pay()
# len()
#
# Key Idea:
# Same method call,
# Different behavior depending on the object.