num = int (input ("Enter any number to test whether it is even or not"))
if(num==0):
    print("Number must be positive or negative")
elif (num % 2) == 0:
    print("The number is even ")
else:
    print("The provided number is not even number")
