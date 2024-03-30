import os
os.system('cls' if os.name == 'nt' else 'clear')

#define a variable to input age
# use conditional if else statements

age=int(input("enter your age: "))

# using if and else to print relevant statement.
if age>100:
    print("Sorry,You are dead.")
elif age>=65:
    print("Enjoy your retirement.")
elif age>=40:
    print("You're over the hill.")
elif age<13:
    print("You qualify for kiddie discount.")
elif age==21:
    print("congrats on your 21st!")
else:
    print("Age is but a number.")
      
