import os
os.system('cls' if os.name == 'nt' else 'clear')

#define a variable and make new variables with the changs required and print

single_string="The!quick!brown!fox!jumps!over!the!lazy!dog."
single_string_replace=single_string.replace("!"," ")
single_string_upper=single_string_replace.upper()
print(single_string_replace)
print(single_string_upper)
print(single_string_upper[::-1])