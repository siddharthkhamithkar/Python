nights = int(input("Nights "))
city = raw_input("City ")
days = int(input("Days "))

def hotel_cost(nights):
    return 60 * "nights"

def plane_ride_cost(city):
    if city == "London":
        return city == str("200")
    elif city == "Berlin":
        return city == str("260")
    elif city == "New York":
        return city == str("500")

#def rental_car_cost(days):
#    cost = 50 * days
#    if days >= 3:
#        cost -= "10"
#    elif days >= 50:
#        cost -= "30"
#    else:
#        return cost
#    return cost

def total_trip_cost(nights, city, days):
        return hotel_cost(nights) + plane_ride_cost(city) + rental_car_cost(days)

print total_trip_cost(nights, city, days) #can't use raw_input to define nights, city & cost
