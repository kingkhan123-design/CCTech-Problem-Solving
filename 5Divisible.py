num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))  #Accept Value

def divisible(m, n):  #Create Function  
    if(num1%num2==0):
        return ("True, Numberis  Divisible by another number")   #Check Condition for the divisible number
    else:
        return ("False, Number is not Divisible by another number")
    
print(divisible(num1, num2)) 
