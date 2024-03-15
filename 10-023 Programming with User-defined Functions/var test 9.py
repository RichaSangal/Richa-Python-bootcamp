import os
os.system('cls' if os.name == 'nt' else 'clear')

"""
def square(length):
    area = length * length
    return area

def rectangle(length, breadth):
    area = length * breadth
    return area

def options():
    print ( "Options")
    print ( "s = prints the area of a square" )
    print ( "r = prints the area of a rectangle" )
    print ( "q = quit" )

choice = "x"

options()
while choice != "q":
    choice= input("Choose from one of the options: ").lower()
    
    if choice == "s":
        length = int(input( "The area of length of the square: "))
        print( f" The length of the square is {square(length)}")
        options()
    
    elif choice == "r":
        length = int(input( "The area of length of the square: "))
        breadth = int(input( "The area of breadth of the square: "))
        print( f" The length of the rectangle is {rectangle(length,breadth)}")
        options()

    elif choice == "q" :
        print ( " You have quit the function" )
    
    else :
        print ( " Input valid option")


"""

num = 10

for i in range(10):
    num = num +1
print ( num )


def add_3_numbers ():
    """
    Takes input of three user defined numbers and adds them up
    
    """
    num1 = int(input( "Enter a number of your choice : "))
    num2 = int(input( "Enter a number of your choice : "))
    num3 = int(input( "Enter a number of your choice : "))

    sum = num1 + num2 + num3

    return sum

var_new=add_3_numbers()

print (f"The total of all the numbers is {var_new}.")