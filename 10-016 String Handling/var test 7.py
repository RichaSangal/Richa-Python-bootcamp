import os
os.system('cls' if os.name == 'nt' else 'clear')
"""
print("Example 1")

num_build = " "
i = 0

while i<=50:
    if i%2==0:
        num_build=num_build + str(i)+" "
    i=i+1

print (num_build)

"""

print("Example 2")

num_build = []
i = 0

while i <= 50:
    if i%2 == 0:
        num_build.append(str(i))
    i = i+1
    
print(" ".join(num_build))