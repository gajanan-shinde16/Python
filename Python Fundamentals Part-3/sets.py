# Set: Unordered collection of unique elements.
# Sets are mutable, do not allow duplicates, and are useful for fast membership testing.
# can hve only mutable things like tuple,string

s = {10, 20, 30, 40, 20}

print(s)
# {10, 20, 30, 40}  (duplicate removed)

# Add element
s.add(50)
print(s)

# Add multiple elements
s.update([60, 70])
print(s)

# Remove element (error if not found)
s.remove(20)
print(s)

# Remove element safely (no error if not found)
s.discard(100)

# Remove and return random element
item = s.pop()
print(item)

# Check membership
print(30 in s)     # True

# Length
print(len(s))      # Number of elements

# Clear set
s.clear()
print(s)           # set()


# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all unique elements)
print(a | b)
print(a.union(b))
# {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(a & b)
print(a.intersection(b))
# {3, 4}

# Difference
print(a - b)
print(a.difference(b))
# {1, 2}

# Symmetric Difference
print(a ^ b)
print(a.symmetric_difference(b))
# {1, 2, 5, 6}

# Return New Sets (don't modify original)
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)

# Example:

print(a.union(b))
# {1, 2, 3, 4, 5}

'''
# Modify Current Set
add()
update()
remove()
discard()
pop()
clear()

intersection_update()
difference_update()
symmetric_difference_update()

'''
# Example:

a.intersection_update(b)
print(a)
# {3}


# Subset & Superset
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
# True

print(b.issuperset(a))
# True


# Frozen Set (Immutable Set)
fs = frozenset([1, 2, 3])

print(fs)

# Not allowed
# fs.add(4)