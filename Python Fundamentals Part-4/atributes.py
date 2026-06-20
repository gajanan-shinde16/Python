class Student:

    clg_name = "ABC clg" # this is claa attribute
    def __init__(self,name,gpa):
        self.name = name # these are instance attributes
        self.gpa = gpa


s1 = Student("Gemini",9.0)
s2 = Student("Gpt",9.4)

print(s1.name) #can be accessed using instance only
print(Student.clg_name) # accessed using class name and common to all instances