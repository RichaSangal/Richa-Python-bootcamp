import os
os.system('cls' if os.name == 'nt' else 'clear')

# program to print chocolate in a tier form. Printing the first letter and appending one more letter as well.

word = "chocolate"        # syntax error: missing paranthesis

for i in range (0,15):  # runtime error:range given is too big and will not produce desired result
    print ( word[0:i+1:2]) # logical error: we do not want to skip the letters



word = "chocolate"        # syntax error: missing paranthesis

for i in range ( 0 , len(word) ):  # runtime error:range given is too big and will not produce desired result
    print ( word[ 0 : i+1 ] ) # logical error: we do not want to skip the letters





