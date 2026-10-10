try :
    x = int(0)
    ans = 10/x

except ZeroDivisionError as e:
    print("Error : ", e)
    print("You cannot divide by zero")

except ValueError as e:
    print("Error : ", e)
    print("Please enter a valid integer")


else :
    print("The answer is : ", ans) 


# print("----Finally will execute always---- ")   

finally:
    print("This is the finally block. It will execute regardless of whether an exception occurred or not.")
