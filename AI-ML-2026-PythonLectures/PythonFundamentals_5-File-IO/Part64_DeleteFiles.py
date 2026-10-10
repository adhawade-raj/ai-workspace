import os

f = open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\sample4.txt", "w")
f.write("This is a new line added to the file.\n")
f.close()

os.remove("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\sample4.txt")

