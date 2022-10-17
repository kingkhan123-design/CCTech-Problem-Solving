num = int (input ("Enter any number to test whether it is odd or not"))
if(num==0):
    print("Number must be positive or negative")
elif (num % 2) == 1:
    print("The number is odd ")
else:
    print("The provided number is not odd number")
