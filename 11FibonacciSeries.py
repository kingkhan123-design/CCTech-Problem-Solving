num = int(input("Please Enter any Number: ")) #Accept value
num1=0  #Declaration for first two numbers

num2=1

print(" The Fibonacci Series is", num1, num2, end=" ")   #Print Fibonacci Series

for i in range(2, num):
    num3 = num1 + num2  #Create Fibonacci Series.
    num1 = num2
    num2 = num3
    print(num3)
