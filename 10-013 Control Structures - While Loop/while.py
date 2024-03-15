import os
os.system('cls' if os.name == 'nt' else 'clear')


# the program requests user to enter a number until the user enters -1
# the programs outputs the average of the numbers inputted by user excluding -1



num=int(input("Enter a number of your choice: "))
i=0
sum=0

# use while loop to sum and average the numbers entered until user enters -1

while num!=-1:
    i=i+1
    sum=sum+num
    average=round(sum/i,2)
    num=int(input("Enter a number of your choice: "))

print(f"The average of the  numbers printed excluding -1 is {average}")
