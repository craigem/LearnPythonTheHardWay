#Set the initial variable values
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

#Calculate the number of cars not driven
cars_not_driven = cars - drivers

#Set the number of cars driven to be the number of drivers available
cars_driven = drivers

#Calculate the car pool capacity by multiplying the number of car driven by the number of spaces available
carpool_capacity = cars_driven * space_in_a_car

#Calculate the average number of passengers in each car
average_passengers_per_car = passengers / cars_driven

#Print the results
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
