# instance methods

# self is compulsory

'''
class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage
    
    def get_info(self): # instance method
        print(f"laptop has {self.RAM} and {self.storage} {self.storage_type}") # self.storage_type self is needed here 0r we can use Laptop.storage_type self is needed because inside an instance method, Python looks for variables in the method's local scope first. The class attribute storage_type is not a local variable, so you must access it through either: the instance: self.storage_type, the class: Laptop.storage_type

l1 = Laptop("16gb","512gb")
l1.get_info()

'''

# Class Methods
# decorator @classmethod
# Can access:
   # 1. Class attributes
   # 2. Other class methods
   
   # Cannot directly access instance attributes
   # because no object is available here

'''
class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage
    
    def get_info(self): # instance method
        print(f"laptop has {self.RAM} and {self.storage} {self.storage_type}") 
    @classmethod # decorators -> takes fun and changes its behavour
    def get_storage_type(self,cls):
        print(f"storage type is: {cls.storage_type}")
        # we cannot access instance attributes or methds here

l1 = Laptop("16gb","512gb")
l1.get_info()
Laptop.get_storage_type() # can be accessed by instance or just class name
l1.get_storage_type()

'''



#Static methods

#Cannot directly access:
    # 1. Instance attributes
    # 2. Class attributes
    
    # Used for utility/helper functions
    # that are logically related to the class

class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage
    
    def get_info(self): # instance method
        print(f"laptop has {self.RAM} and {self.storage} {self.storage_type}") 

    @classmethod # decorators -> takes fun and changes its behavour
    def get_storage_type(cls): # Class Method
        print(f"storage type is: {cls.storage_type}")
        # we cannot access instance attributes or methds here

    @staticmethod # logically tied to class  no compulsory parameters
    def calc_disc(price,discount):
        print(price - price*discount/100)


l1 = Laptop("16gb","512gb")

Laptop.calc_disc(1000,10)
l1.calc_disc(1000,10)


# val = 10_000 = 10000 -> ignores _