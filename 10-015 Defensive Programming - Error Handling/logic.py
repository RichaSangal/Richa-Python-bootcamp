import os
os.system('cls' if os.name == 'nt' else 'clear')

# program generates comments based on your age.
# it gives you the incorrect result for age over 40years as it has a logical error.

age = int(input("Enter your age: "))

if age >= 40:
    print ("You are over the hill.")

elif age >= 60:
    print ("You are old.")

elif age >= 100:
    print ("You are dead.")

else:
    print ("You are young.")