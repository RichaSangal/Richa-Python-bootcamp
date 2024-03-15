import os
os.system('cls' if os.name == 'nt' else 'clear')

import math
# this program is to calculate interest on earnings or interest on payment loans
# this program takes inputs from user on what they need to calculate and outputs the calculated interest amount
# it uses if , nested if and elseif looping to get to the right calculation 

print("investment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount youll have to pay on home loan\n")

type_of_cal=input("Enter either 'investment' or 'bond' from the menu above to proceed:")

type_of_cal=type_of_cal.lower()

if type_of_cal=="investment":
    p=float(input("Enter the amount you would like to deposit: "))
    t=float(input("Enter the number of years that the money is being invested: "))
    r=float(input("Enter the interest rate as a number and not percentage: "))
    interest=input("Enter the type of interest rate: 'Simple' or 'compounded': ")
    r=r/100
    interest=interest.lower()
    if interest=="simple":
        amount=round(p*(1+r*t),3)
        print (f"The total amount earned is {amount}.")
    elif interest=="compounded":
        amount=round(p*math.pow((1+r),t),3)
        print(f"The total amount earned is {amount}.")
elif type_of_cal=="bond":
    v=float(input("Enter the present value of the house: "))
    i=float(input("Enter the interest rate: "))
    n=float(input("Enter the numbers of months they plan to take to repay the bond: "))
    i=(i/100)/12
    repayment=round((i*v)/(1-((1+i)**(-n))),3)
    print(f"The total monthly payment is {repayment}.")
else:
    print("Invalid entry, try again")
 





