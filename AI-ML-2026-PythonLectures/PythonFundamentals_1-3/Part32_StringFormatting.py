a=5
b=10
sum=a+b


print("----------without Formatting----------")
print("The sum of a and b is: ",sum)

#normal fomratting
print("----------With Formatting----------")
print("The sum of is {}".format(sum))
print("The sum of {} and {} is: {}".format(a,b,sum))

#index based formatting
print("----------With index based Formatting----------")
print("sum of {0} and {1} is: {2}".format(a,b,sum))
print("sum of {1} and {0} is: {2}".format(a,b,sum))

#variable based formatting
print("----------With variable based Formatting----------")
print("{a} values of vars {a} and {b}".format(a=5,b=10))

#F-String formatting
print("----------With F-String Formatting----------")
print(f"Sum of {a} and {b} is {a+b}")