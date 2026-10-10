import json

with open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\data.json", "r") as file:
    data = json.load(file)
    print("---- Reading JSON data from file ----")
    print(data, type(data))


    data_dict = {"name": "Bob", "age": 28, "city": "Chicago"}
    with open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\data2.json", "w") as file_write:
        json.dump(data_dict, file_write, indent=4, sort_keys=True)