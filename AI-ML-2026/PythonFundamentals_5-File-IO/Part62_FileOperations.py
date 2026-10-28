from pathlib import Path


lesson_dir = Path(__file__).resolve().parent
sample_file = lesson_dir / "Sample.txt"
f = open(sample_file, "r")

data = f.read()
print("---- This will read all file data at once ----")
print(data)


# -------------------------------------------------------------
print("----- Append Operation -----")
f2 = open(sample_file, "a+")
f2.write("This is a new line added to the file.\n")
f2.seek(0)
data2 = f2.read()
print("---- PRINT File DATA after APPEND ----")
print(data2)

f2.close()

# -------------------------------------------------------------
print("----- x Operation -----")
print("---- x creates a file only if it does not already exist ----")
new_file_path = lesson_dir / "Sample2.txt"

f3 = open(new_file_path, "x")
f3.write("This content was written to a newly created file.\n")
f3.close()





