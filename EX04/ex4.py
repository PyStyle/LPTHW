#full amount of cars
cars = 100
#seats in a car
space_in_a_car = 4.0
#amount of drivers
drivers = 30
#amount of passengers
passengers = 90
#cars minus drivers equal unused cars
cars_not_driven = cars - drivers
#used cars equal amount of drivers
cars_driven = drivers
#total capacity used cars asterisk seats in a car
carpool_capacity = cars_driven * space_in_a_car
#average passenger per car equals passengers slash cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
