import os
os.system('cls' if os.name == 'nt' else 'clear')


# program to input 3 lengths of triangle and output the area

import math


len1=float(input("Enter length 1 of triangle: "))
len2=float(input("Enter length 2 of triangle: "))
len3=float(input("Enter length 3 of triangle: "))

# calculating area 
s=(len1+len2+len3)/2
area=math.sqrt((s*(s-len1)*(s-len2)*(s-len3)))
print(round(area,2))