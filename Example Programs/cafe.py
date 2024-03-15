import os
os.system('cls' if os.name == 'nt' else 'clear')

# program to calculate total stock worth with information stores in different dictionaries

menu = [ "apples", "bag", "banana", "pencil", "bottle" ]

stock = { "apples":2, "bag":4,"banana":2,"pencil":4,"bottle":2 }

price = { "apples":3, "bag":4,"banana":5,"pencil":6,"bottle":7 }

total_stock_cost = []

# run loop to access dictionaries 

for item in menu :
    
    total_stock_cost.append(stock [item] * price [item])

print ( f"The total cost of all the items in the shop is £{sum(total_stock_cost)}")