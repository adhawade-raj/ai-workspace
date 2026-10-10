nums = [1, 2, 3]

print("# Adding an element to the end of the list")
nums.append(4)  # Adding an element to the end of the list
print(nums)

print("# Inserting an element at a specific index")
nums.insert(1, 5)  # Inserting an element at index 1
print(nums)

print("# Removing an element from the list")
nums.remove(2)  # Removing the element with value 2 
print(nums)

print("# Sorting the list in ascending order")
nums.sort()  # Sorting the list in ascending order
print(nums)

print("# Reversing the list")
nums.reverse()  # Reversing the list
print(nums)

print("# Sorting the list in descending order")
nums2 = [4, 5, 6,9, 10]

nums2.sort(reverse=True)  # Sorting the list in descending order
print(nums2)