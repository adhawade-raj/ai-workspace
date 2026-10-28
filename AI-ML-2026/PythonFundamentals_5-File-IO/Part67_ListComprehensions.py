
print("----With Normal for loop----")
squares = []
for i in range(6):
    squares.append(i**i)
print(squares)


print("----With List Comprehension----")
squares = [i**i for i in range(6)]
print(squares)


words = ["Python", "is", "a", "great", "programming", "language"]
words = [val.upper() for val in words]
print(words)
