import os
from pathlib import Path

sample_file = Path(__file__).resolve().parent / "Sample4.txt"
f = open(sample_file, "w")
f.write("This is a new line added to the file.\n")
f.close()

os.remove(sample_file)
