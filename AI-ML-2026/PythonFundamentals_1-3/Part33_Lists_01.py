from numpy import rint


marks = [10,20,30,89,78]

print("# Accessing the element of the list")
print(marks[1])  # Accessing the second element of the list


print("# Modifying the third element of the list")
marks[2] = 100  # Modifying the third element of the list
print(marks)


print("# Accessing the last element of the list")
print(marks[-1])  # Accessing the last element of the list

print("# Accessing the elements of the list using slicing")
print(marks[0:3])  # Accessing elements from index 0 to 2
print(marks[2:5])  # Accessing elements from index 2 to 4
print(marks[2:])  # Accessing elements from index 2 to the end

