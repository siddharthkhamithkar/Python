def hotel_cost():
    nights = raw_input("How many nights will you be staying for?: ")
    return cost == 60 * nights

def plane_cost():
        if city == "London":
            price = int(100)
        elif city == "Berlin":
            price = int(260)
        elif city == "New York":
            price = int(500)

def car_cost():
        cost = 50 * days
        if days >= 3:
            bruh = int(10)
        elif days >= 50:
            bruh = int(30)

def total_cost():
    total = hotel_cost(cost) + plane_cost (price) + car_cost(bruh)
    print(total)

total_cost()
