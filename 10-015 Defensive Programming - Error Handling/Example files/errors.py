# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")      # Syntax error: paranthesis missing
print ("\n")                                # syntax error: incorrect indentation, paranthesis missing

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old"                    # syntax error: incorrect indentation line 9-15 & runtime error: variable not defined
                                            # runtime error: there should be = instead of ==
age = age_Str[0:2]                          # runtime error: cannot convert string to integer, extracting age from string
print("I'm" + " "+ age + " " + "years old.")# syntax error: message does not have apropriate spacing

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = int(age) + int(years_from_now)  
# runtime error: needs to convert years_from_now into int 

print (f"The total number of years: {total_years}") 
# syntax errors: Paranthesis missing, incorrect variable name used 
# Runtime error: error of concatenating string and integer

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12              
# runtime error: incorrect variable name used/variable not defined
print (f"In 3 years and 6 months, I'll be {total_months+6} months old")  
# syntax error: paranthesis missing
# runtimeerror: error of concatenating string and integer
# logical error: Giving wrong age calculation, 6 months should be added to total months
#HINT, 330 months is the correct answer

