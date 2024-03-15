import os
os.system('cls' if os.name == 'nt' else 'clear')


star="*****"
starlen=len(star)
index=1

# program to print out a pattern of stars
#run the for loop to run the program many times to print in multiple rows

for i in range (0,10):

# use if and elif to check the conditions and print 2 separate triangles
    
    if i<=starlen:
        print (star[0:i])
        
        
    elif i>starlen:
        print(star[0:starlen-index])
        index=index+1

    

