import json
from pathlib import Path

lesson_dir = Path(__file__).resolve().parent

with open(lesson_dir / "data.json", "r") as file:
    data = json.load(file)
    print("---- Reading JSON data from file ----")
    print(data, type(data))


    data_dict = {"name": "Bob", "age": 28, "city": "Chicago"}
    with open(lesson_dir / "data2.json", "w") as file_write:
        json.dump(data_dict, file_write, indent=4, sort_keys=True)