import os
os.system('cls' if os.name == 'nt' else 'clear')

# define variables and use if condition with and operators to check conditions

time_swim=float(input("Enter the total minutes taken to swim: "))
time_cycle=float(input("Enter the total minutes taken to cycle: "))
time_run=float(input("Enter the total minutes taken to run: "))
totaltime=time_swim+time_cycle+time_run
print(totaltime)

if totaltime>=0 and totaltime<=100:
    print("Provincial colors")

elif totaltime>=101 and totaltime<=105:
    print("Provincial half colours")

elif totaltime>=106 and totaltime<=110:
    print("Provincial scroll")

elif totaltime>111:
    print("No award")

