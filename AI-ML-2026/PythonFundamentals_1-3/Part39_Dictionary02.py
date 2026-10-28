info ={
    "name": "John Doe",
    "cgpa": 3.8,
    "university": "XYZ University",
    3.14:"PI"
}

print("----------# This will print all the keys in the dictionary---------- ")
print(info.keys())  # This will print all the keys in the dictionary

print("----------This will print all the values in the dictionary---------- ")
print(info.values())  # This will print all the values in the dictionary

print("----------This will print all the key-value pairs in the dictionary---------- ")
print(info.items())  # This will print all the key-value pairs in the dictionary

print("----------This will print each key and its corresponding value in the dictionary---------- ")
for key in info:
    print(key, ":", info[key])  # This will print each key and its corresponding value in the dictionary    


print('----------This will print the value associated with the key "name"---------- ')
print(info.get("name"))  # This will print the value associated with the key "name"


print('--------------------------This will print the value associated with the key "cgpa"---------- ')
info.update({"cgpa": 3.9})  # Updating the value associated with the key "cgpa"
print(info["cgpa"])  # This will print the updated value associated with the key "cgpa" 


key = info.keys()
print('----------This will print all the keys in the dictionary---------- ')
print(key)  # This will print all the keys in the dictionary