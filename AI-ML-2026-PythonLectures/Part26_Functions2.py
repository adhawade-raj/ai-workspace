def calc_avg(a,b,c):
    avg = (a + b + c) / 3
    return avg

# Example usage
result = calc_avg(4, 5, 6)
print("Average is:", result)

print("-------------Default values example-------------")
def sum_defaultValue(a,b,c=1):
    avg = (a + b + c)
    return avg

result = sum_defaultValue(4, 5)
print("Sum with default values is:", result)
print("Sum without default value is ", sum_defaultValue(4, 5, 6))