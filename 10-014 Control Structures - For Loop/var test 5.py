import os
os.system('cls' if os.name == 'nt' else 'clear')


#for i in range(1,10):
#    print(i)
#    i=i+9
#    print(i)

#print("Example :1")

#num=int(input("Enter a number: "))

#for i in range(0,num):
#    if i%2==0:
#        print(i)
#    else:
#        print("odd number")
"""
print("Example :2")

num=int(input("input a number of your choice: "))

if num%2==0: # if the nuber is even
    star="*"
    for i in range (0,10):
        print(star)
        star=star+"*"

if num%2!=0:
    star="**********"
    for i in range (0,10):
        index=10-i
        print(star[0:index])

"""

"""
#to output a triangle of upside down triangle depending on the inputted number
#

print("Example :3")

num=int(input("input a number of your choice: "))

if num%2==0: # if the nuber is even
    star="*"
    for i in range (0,num):
        print(star)
        star=star+"*"

if num%2!=0: # if the number is odd
    star="**********"
    starlen=len(star)
    if num<=starlen:
        for i in range (0,num):
            index=num-i
            print(star[0:index])
    else:
        if starlen<num:
            difference=num-starlen
            for i in range (0,difference):
                star=star+"*"
            for i in range (0,num):
                index=num-i
                print(star[0:index])
            
"""

"""
print("Example :4")

for x in range (1,10):
    for y in range(1,10):
        print(f"{x}*{y}={x*y}")

"""
"""
# program to make an arrow pattern
        
pattern = "*"

for num in range (1,10) :
    if num<=5:
        print(pattern*num)

    else:
        print((10-num)*pattern)
"""

# program to make reverse arrow
        
#    *        
#   **
#  ***
# ****
#*****
# ****
#  ***
#   **
#    *
        

star = "*"
space = " "

for i in range (1,10):
    if i <= 5:
        print ( space*(5-i) + star*i)

    elif i > 5:

        print ( space*(i-5) + star*(10-i) )


