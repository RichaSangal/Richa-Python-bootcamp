import os
os.system('cls' if os.name == 'nt' else 'clear')

# define variables and input to get values of integers
# create new variables for calculations and print

integer1=int(input("Enter an integer: "))
integer2=int(input("Enter an integer: "))
integer3=int(input("Enter an integer: "))
sum_integer=integer1+integer2+integer3
subtract_integer=integer1-integer2
multiply_integer=integer1*integer3
cal_integer=sum_integer/integer3

print("The sum of the 3 integers is "+str(sum_integer))
print("The first number minus the second number is "+ str(subtract_integer))
print("The third number multiplied by the first number is "+str(multiply_integer))
print("The sum of the numbers divided by the third number is "+str(cal_integer))