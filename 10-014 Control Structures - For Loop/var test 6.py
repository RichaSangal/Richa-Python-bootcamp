
import os
os.system('cls' if os.name == 'nt' else 'clear')

numlist=[1,2,3,4,5]

num=int(input("enter a number of your choice between 1-10: "))

if num>10 or num<1:
    print( "The number is not in 1-10")


for i in range (1,5):
    if numlist[i]==num:
        print(" number in the list")
    
