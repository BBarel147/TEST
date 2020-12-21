num_dis = int(input("Enter the distance from your destination:"))
time_day = str(input("What time of the day it is?"))
trav_op = str(input("Which traveling option do you prefer?"))
cost_hour = int(input("What is the price of an hour of traveling?"))

bus_pass = 0
omes = 0

if num_dis == 0:
    print("No need for traveling - you are at your destination.")
elif num_dis < 0:
    print("Error")

if time_day == "Morning":
    omes = 3
elif time_day == "Noon":
    omes = 2
elif time_day == "Evening":
    omes = 1
elif time_day != "Morning" and time_day != "Noon" and time_day != "Evening":
    print("Error")

if trav_op == "Private":
    speed = 160 / omes
    time = num_dis / speed
    cost = time * cost_hour
    cost = round(cost)
    time = round(time, 2)
    if cost_hour > 0:
        print("You chose to travel in the car.")
        print("It will take", time, "hours, and it will cost", cost, "shekels.")
    else:
        print("Error")
elif trav_op == "Public":
    if cost_hour > 0:
        print("You chose to travel in public transport.")
        bus_pass = int(input("How many passengers there are on the bus?"))
        if 20 > bus_pass > 0:
            bus_pass = 20
        speed = 180 / (omes + 2)
        speed_bus = (150 - bus_pass) / omes
        if omes == 1:
            speed_bus = 150
        time = num_dis / speed
        time_bus = num_dis / speed_bus
        cost_bus = time_bus * cost_hour
        cost_taxi = (time * cost_hour) + 50
        cost_bus = round(cost_bus)
        cost_taxi = round(cost_taxi)
        time_bus = round(time_bus, 2)
        time = round(time, 2)
        if cost_bus < cost_taxi and time_bus < time:
            print("The best option is the bus")
            print("It will take", time_bus, "hours, and it will cost", cost_bus, "shekels.")
        else:
            print("The best option is the taxi")
            print("It will take", time, "hours, and it will cost", cost_taxi, "shekels.")
    else:
        print("Error")
else:
    print("Error")
