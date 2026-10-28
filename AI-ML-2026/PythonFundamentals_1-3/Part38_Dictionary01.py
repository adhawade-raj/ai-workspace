info ={
    "name": "John Doe",
    "cgpa": 3.8,
    "university": "XYZ University",
    3.14:"PI"
}

print(type(info))  # This will print <class 'dict'>

print("----------Accessing the element of the dictionary----------")
print(info["name"])  # This will print the value associated with the key "name"
print(info["cgpa"])  # This will print the value associated with the key "cgpa"
print(info["university"])  # This will print the value associated with the key "university"
print(info[3.14])  # This will print the value associated with the key 3.14


print("----------Updating the element of the dictionary----------")
info["cgpa"] = 3.9  # Updating the value associated with the key "cgpa"
print(info["cgpa"])  # This will print the updated value associated with the key "cgpa"