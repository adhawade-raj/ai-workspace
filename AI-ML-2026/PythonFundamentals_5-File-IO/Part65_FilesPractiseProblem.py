from pathlib import Path


data = True
line = 1
word = "Python"

sample_file = Path(__file__).resolve().parent / "Sample5.txt"
with open(sample_file, "r") as f:

    while data:
        data = f.readline()

        if(word in data):
            print(f"Word '{word}' found in line {line}")
            break

        print(data)
        line+=1