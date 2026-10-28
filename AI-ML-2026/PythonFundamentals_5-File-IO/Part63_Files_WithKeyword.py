from pathlib import Path


sample_file = Path(__file__).resolve().parent / "Sample3.txt"
with open(sample_file, "r") as f:
    print("---- This will read all file data at once using 'with and no need to write close explicitly' ----")
    print(f.read())