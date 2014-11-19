"""Exercise 19, Learning Python the Hard Way"""


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """Print the crackers!"""
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
AMOUNT_OF_CHEESE = 10
AMOUNT_OF_CRACKERS = 50

cheese_and_crackers(AMOUNT_OF_CHEESE, AMOUNT_OF_CRACKERS)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variablers and math:"
cheese_and_crackers(AMOUNT_OF_CHEESE + 100, AMOUNT_OF_CRACKERS + 1000)
