"""Exercise 4, Learning Python the Hard Way"""
# Set the initial variable values
CARS = 100
SPACE_IN_A_CAR = 4.0
DRIVERS = 30
PASSENGERS = 90

# Calculate the number of cars not driven
CARS_NOT_DRIVEN = CARS - DRIVERS

# Set the number of cars driven to be the number of drivers available
CARS_DRIVEN = DRIVERS

# Calculate the car pool capacity by multiplying the number of cars driven by
# the number of spaces available
CARPOOL_CAPACITY = CARS_DRIVEN * SPACE_IN_A_CAR

# Calculate the average number of passengers in each car
AVERAGE_PASSENGERS_PER_CAR = PASSENGERS / CARS_DRIVEN

# Print the results
print "There are", CARS, "cars available."
print "There are only", DRIVERS, "drivers available."
print "There will be", CARS_NOT_DRIVEN, "empty cars today."
print "We can transport", CARPOOL_CAPACITY, "people today."
print "We have", PASSENGERS, "to carpool today."
print "We need to put about", AVERAGE_PASSENGERS_PER_CAR, "in each car."
