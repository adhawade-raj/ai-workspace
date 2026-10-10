f = open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\sample.txt", "r")

data = f.read()
print("---- This will read all file data at once ----")
print(data)

f.seek(0)  # Return to the beginning of the file
print("---- This will read the file line by line in this case 1st line ----")
data = f.readline()
print(data)

print("---- This will read the file line by line in this case 2nd line ----")
data = f.readline()
print(data)


print("---- This will overwrite the file with new data ----")
f = open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\sample.txt", "w")
f.write("This is a new line added to the file.\n")
f.write("This is another new line added to the file.\n")

print("---- This will close the file after writing ----")
f.close()