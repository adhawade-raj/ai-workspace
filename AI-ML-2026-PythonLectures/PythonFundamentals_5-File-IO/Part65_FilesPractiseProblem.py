data = True
line = 1
word = "Python"

with open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\sample5.txt", "r") as f:

    while data:
        data = f.readline()

        if(word in data):
            print(f"Word '{word}' found in line {line}")
            break

        print(data)
        line+=1