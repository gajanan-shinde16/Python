# Abstraction in Python

# Abstraction means:
# Hide implementation details and show only essential functionality.
#
# User knows WHAT to do,
# not HOW it is done internally.


# Why Abstraction?

# Without abstraction, every class may have different methods.

class CreditCard:
    def pay(self):
        print("Credit Card Payment")


class UPI:
    def send_money(self):
        print("UPI Payment")

# No common structure.


# With abstraction:

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

# Every payment class MUST implement pay().


# Abstract Class

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Animal()   Error
# Cannot create object of abstract class.


# Implementing Abstract Methods

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


# If Child Doesn't Implement It

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    pass

# Dog()  Error
# sound() must be implemented.


# Abstract Class Can Have Normal Methods

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle Stopped")


class Car(Vehicle):

    def start(self):
        print("Car Started")


c = Car()

c.start()
c.stop()

# Output:
# Car Started
# Vehicle Stopped


# Real Example

class Payment(ABC):

    @abstractmethod
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


# Key Difference

# Inheritance  -> Reuse Code
# Encapsulation -> Hide Data
# Abstraction -> Hide Complexity


# Quick Summary

# ABC              -> Abstract Base Class (module)
# @abstractmethod  -> Forces child classes to implement method
# Abstract Class   -> Cannot create object directly
# Main Purpose     -> Define a common contract for subclasses