# Tuple: Ordered, immutable collection of items.
# Tuples allow duplicates and support indexing/slicing like lists.

t = (10, 20, 30, 40, 20)

# Access elements
print(t[0])      # 10
print(t[-1])     # 20

# Slicing
print(t[1:4])    # (20, 30, 40)

# Length
print(len(t))    # 5

# Count occurrences
print(t.count(20))   # 2

# Find index of first occurrence
print(t.index(30))   # 2

# Membership check
print(40 in t)       # True

# Concatenation
t2 = (50, 60)
print(t + t2)
# (10, 20, 30, 40, 20, 50, 60)

# Repetition
print(t * 2)
# (10, 20, 30, 40, 20, 10, 20, 30, 40, 20)

# Unpacking we use when fun returns multiple values(tuple)
a, b, c = (1, 2, 3)
print(a, b, c)
# 1 2 3

# Single-element tuple
single = (10,)
print(type(single))
# <class 'tuple'>


t = (10, 20, 30)

print(len(t))    # 3
print(min(t))    # 10
print(max(t))    # 30
print(sum(t))    # 60
print(sorted(t)) # [10, 20, 30] returns a list, not a tuple.