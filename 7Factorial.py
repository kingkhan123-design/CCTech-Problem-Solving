num = int(input("Enter a number: "))   #Accept value
factorial = 1

if num < 0:     #Check if value is negative or not
   print(" Factorial does not exist for negative numbers")
   
elif num == 0:    
   print("The factorial of 0 is 1")    
else:
   
   for i in range(1,num+1 ):
      
       factorial = factorial*i  #Calculating of factorial   
   print("The factorial of",num,"is",factorial)
