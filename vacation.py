nights = int(input("Nights "))
city = raw_input("City ")
days = int(input("Days "))

def hotel_cost():
    60 * "nights"

def plane_ride_cost():
    if city == "London":
        city == 100
    elif city == "Berlin":
        city == 260
    elif city == "New York":
        city == 500

def rental_car_cost():
    cost = 50 * days
    if days >= 3:
        cost -= "10"
    elif days >= 50:
        cost -= "30"

def total_trip_cost():
    total = nights + city + cost
    print(total)
total_trip_cost()
