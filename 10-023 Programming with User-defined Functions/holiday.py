import os
os.system('cls' if os.name == 'nt' else 'clear')

# task is to calculate total holiday cost including hotel cost, flight cost, car rental cost
# take input from users on destination, no of days of stay
# create dictionaries for flight costs

print (" This program will help calculate the total holiday cost. ")


def options():
    """
    This function calculates the total hotel costs based on the number of nights

    """ 
    
    print (" This program can be used for below destinations only. ")
    print (" Greece ")
    print (" Spain ")
    print (" Srilanka ")
    print (" Chicago ")


def hotel_cost(num_nights): 
    """
    This function calculates the total hotel costs based on the number of nights

    """     
    hotel_dict={"greece":250 , "spain":200 , "srilanka":80 , "chicago":150}
    total_hotel_cost= hotel_dict[city_flight] * num_nights
    return total_hotel_cost
        

def plane_cost (city_flight) :
    """
    This function calculates the total flight costs based on the city

    """ 
    flight_cost_dict = {"greece":100 , "spain":100 , "srilanka":550 , "chicago":450}
    total_flight_cost = flight_cost_dict [city_flight]
    return total_flight_cost


def car_rental ( rental_days ) :
    """
    This function calculates the car rental cost based on the number of days and city visited

    """ 
    carrental_cost_dict = {"greece":50 , "spain":50 , "srilanka":10 , "chicago":20}
    total_rental_cost = carrental_cost_dict  [ city_flight ] * rental_days
    return total_rental_cost


def total_holiday_cost ():
    """
    This function calculates the total cost for flight, hotel and car rental

    """ 
    total_holiday_cost_cal = hotel_cost(num_nights) + plane_cost(city_flight)+ car_rental(rental_days)
    return total_holiday_cost_cal
        

dest = ["greece","spain","srilanka","chicago"]

options()

# get input from user. Use while, try and except for error handling.

while True:
 
    city_flight = input("Enter the city you are flying to : ").lower().strip()

    if city_flight in dest:
           
        while True:

            try: 
                num_nights = int(input ("Enter the number of nights you plan to stay : "))
                print ("Thats a perfect number of days for a holiday.")
                break
            except:
                print (" Thats not an integer. Please try again.")
        
        while True:

            try: 
                rental_days  = int(input (" The no of days you need to hire a car :"))

                if rental_days > num_nights:
                    raise Exception (" The car hire days cannot be more the duration of stay. Try again")
                
                print ("Thats a perfect number of days to rent a car.")

                print ( f"The total cost of your holiday in {city_flight.capitalize()} for {num_nights} nights is £{total_holiday_cost()}.")

                break

            except ValueError:
                print (" Thats not an integer. Please try again.")
                
            
            except Exception as e:
                print (e)

    
    
    else :
        print("Your destinations doesnt match to our list. Please try again")
        options()
        continue
    
    break

         


    
        
        

