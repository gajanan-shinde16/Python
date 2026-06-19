# Dictionary: Stores data as key:value pairs.
# Dictionaries are mutable, unordered (in older Python), and keys must be unique.

student = {
    "name": "Alice",
    "age": 20,
    "city": "Mumbai"
}

# Access value using key
print(student["name"])      # error if not present

# Access using get()
print(student.get("age"))   # none if not present

# Get non-existing key safely
print(student.get("marks")) # None

# Add new key-value pair
student["marks"] = 95
print(student)

student.update({"marks" : 100});
print(student)

# Update existing value
student["age"] = 21
print(student)

# Remove key and return value
removed = student.pop("city")
print(removed)              # Mumbai

# Remove last inserted item and return it
item = student.popitem()
print(item)

# Delete key
del student["age"]

# Check if key exists
print("name" in student)    # True

# Dictionary length
print(len(student))


# Looping 

student = {
    "name": "Alice",
    "age": 20,
    "city": "Mumbai"
}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key-value pairs
for key, value in student.items():
    print(key, value)

    print(student.items()) # List of tuple(key,val)

'''
# methods to remember
d.get("a")       # 1
d.keys()         # dict_keys(['a', 'b'])
d.values()       # dict_values([1, 2])
d.items()        # dict_items([('a',1), ('b',2)])
d.copy()         # new dictionary


d = {"a":10, "b":20, "c":30}

print(len(d))      # 3

print(min(d))
# a (minimum key)

print(max(d))
# c (maximum key)

print(sum(d.values()))
# 60

'''