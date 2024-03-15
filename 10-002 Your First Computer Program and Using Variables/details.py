import os
os.system('cls' if os.name == 'nt' else 'clear')

# take input from user of all information needed 
# Use either f or format command to mix strings and variables.

name=input("Enter your name: ")
age=input("Enter your age: ")
house_number=input("Enter your house number: ")
street_name=input("Enter your street name: ")
print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name} street.")
