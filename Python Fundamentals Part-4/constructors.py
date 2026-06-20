
# __init__ method (constructor)-->initializes object
# in python only one constructor(__init__) is allowed ( but there is case where it works --> later written will be called)

'''
# default constructor --> have only self parameter
class Student:
    def __init__(self):
        print("Constructor was called")


s1 = Student()
s2 = Student()

'''

'''

# parameterized
class Student:
    def __init__(self,name):
        self.name = name;


s1 = Student("Gemini")
s2 = Student("Gpt")

print(s1.name)
print(s2.name)

'''

class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
    
    def get_cgpa(self):
        return self.cgpa


s1 = Student("Gemini",9.8)
s2 = Student("Gpt",9.9)

print(s1.get_cgpa())
print(s2.get_cgpa())