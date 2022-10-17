base=int(input("Enter base value")) #Accept Base value
exponent= int(input("Enter exponent value")) #ACcept Exponent Value
result = 1
for exponent in range(exponent, 0, -1): #calculation
    result=result*base;

print("Answer = ")
print(result)
