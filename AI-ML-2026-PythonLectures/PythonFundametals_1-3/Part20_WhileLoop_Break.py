i = 1

while (i<=10) :
    if(i % 6 ==0) :
        break
    print (i)
    i += 1

print("exiting loop with break keyword")
print("--------------------------------")

i = 1

while (i<=10) :
    if(i % 3 ==0) :
        i += 1
        continue
    print (i)
    i += 1

print("exiting loop with continue keyword")

print("-----------Print Odd Numbers---------------------")

i = 1

while (i<=10) :
    if(i % 2 ==0) :
        i += 1
        continue
    print (i)
    i += 1

print("exiting loop with continue keyword")