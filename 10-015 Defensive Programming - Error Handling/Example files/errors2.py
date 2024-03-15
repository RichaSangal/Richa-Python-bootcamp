# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"         # runtime error: Lion is not defines variable, it should bein quotes
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  
# logical error: The entire line is being printed as string, need to add f in front
# logical errror: Giving wrong answer as variables number of teeth and animal type need to be switched

print (full_spec)   # syntax error: missing paranthesis

