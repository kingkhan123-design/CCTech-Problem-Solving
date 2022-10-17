num = int(input("Enter a number: ")) #Accept Number

if(num==1 or num<=0):
    print("if input number is less than or equal to 1, it is not prime")  #Check Condtion for the if number is 1 or less than 1
     
if num > 1:   #If number is greater than 1
   for i in range(2,num):
       
       if (num % i) == 0:  #Check Condition for the Prime Number
           print(num,"is not a prime number")  
           break
        
   else:
       print(num,"is a prime number")
