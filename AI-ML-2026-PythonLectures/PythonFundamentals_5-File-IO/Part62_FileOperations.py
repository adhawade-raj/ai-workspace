f = open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\sample.txt", "r")

data = f.read()
print("---- This will read all file data at once ----")
print(data)


# -------------------------------------------------------------
print("----- Append Operation -----")
f2 = open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\sample.txt", "a+")
f2.write("This is a new line added to the file.\n")
f2.seek(0)
data2 = f2.read()
print("---- PRINT File DATA after APPEND ----")
print(data2)

f2.close()

# -------------------------------------------------------------
print("----- x Operation -----")
print("---- x creates a file only if it does not already exist ----")
new_file_path = "AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\Sample2.txt"

f3 = open(new_file_path, "x")
f3.write("This content was written to a newly created file.\n")
f3.close()






