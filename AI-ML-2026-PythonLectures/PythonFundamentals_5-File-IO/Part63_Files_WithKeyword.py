with open("AI-ML-2026-PythonLectures\\PythonFundamentals_5-File-IO\\sample3.txt", "r") as f:
    print("---- This will read all file data at once using 'with and no need to write close explicitly' ----")
    print(f.read())