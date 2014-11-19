# Define the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# Run the function and seed the values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# Seed variables before using them as input to the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Use math to seed the variable values
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# Use math and variables to seed the function:
print "And we can combine the two, variablers and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
