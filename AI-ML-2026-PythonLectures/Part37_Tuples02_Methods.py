tup = (1,2,5,2,3,3,4)

sum = 0
for val in tup:
    sum += val
print(f"sum of vals is {sum}")

print("----------Tuple Methods----------")

print("# This will print the index of the first occurrence of 3 in the tuple")
print(tup.index(3))  

print("# This will print the number of occurrences of 2 in the tuple")
print(tup.count(2))  