# List: Ordered, mutable collection that can store different data types.
# Lists allow indexing, slicing, duplicates, and many built-in methods.

nums = [10, 20, 30, 40, 50]

# Access elements
print(nums[0])      # 10
print(nums[-1])     # 50

# Slicing
print(nums[1:4])    # [20, 30, 40]

# Update element
nums[0] = 100
print(nums)         # [100, 20, 30, 40, 50]

# Add single element (modifies list)
nums.append(60)
print(nums)

# Add multiple elements (modifies list)
nums.extend([70, 80])
print(nums)

# Insert at index (modifies list)
nums.insert(1, 999)
print(nums)

# Remove first matching value (modifies list)
nums.remove(999)
print(nums)

# Remove and return element (modifies list)
# removes and returns the last item
removed = nums.pop()
print(removed)      # 80
print(nums)

# Remove and return element at index (modifies list)
removed = nums.pop(0)
print(removed)      # 100
print(nums)

# Delete using del (modifies list)
del nums[1]
print(nums)

# Count occurrences (returns value)
print(nums.count(40))

# Find index (returns value)
print(nums.index(40))

# Check membership
print(30 in nums)

# Reverse in-place (modifies list)
nums.reverse()
print(nums)

# Sort in-place (modifies list)
nums.sort()
print(nums)

# Sort descending (modifies list)
nums.sort(reverse=True)
print(nums)

# Copy list (returns new list)
copy_list = nums.copy()
print(copy_list)

# Clear all elements (modifies list)
nums.clear()
print(nums)



# Loops with lists

#Linear Search

list = [5,6,3,8,12,90,878]
key = 90
for num in list:
    if num==key:
        print("found")
        break # after break else won't run
else : print("not found.")

