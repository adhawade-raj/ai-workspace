import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
print(json_string, type(json_string))


print("----Converting JSON string to Python Dictionary----")    
py_obj = json.loads(json_string)
print(py_obj, type(py_obj))

print("----Converting Python Dictionary to JSON string----")
py_dict = {"name": "Alice", "age": 25, "city": "Los Angeles"}
json_str = json.dumps(py_dict)
print(json_str, type(json_str)) 