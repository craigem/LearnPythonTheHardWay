"""Exercise 21, Learning Python the Hard Way"""


def add(aay, bee):
    """Print the sum of aay and bee"""
    print "ADDING %d + %d" % (aay, bee)
    return aay + bee


def subtract(aay, bee):
    """Print the result of the sutraction of aay from bee"""
    print "SUBTRACTING %d - %d" % (aay, bee)
    return aay - bee


def multiply(aay, bee):
    """Print the result of the multiplication of aay and bee"""
    print "MULTIPLYING %d * %d" % (aay, bee)
    return aay * bee


def divide(aay, bee):
    """Print the result of the division of aay by bee"""
    print "DIVIDING %d / %d" % (aay, bee)
    return aay / bee


print "Let's do some math with just functions!"

AGE = add(30, 5)
HEIGHT = subtract(78, 4)
WEIGHT = multiply(90, 2)
IQ = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (AGE, HEIGHT, WEIGHT, IQ)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

WHAT = add(AGE, subtract(HEIGHT, multiply(WEIGHT, divide(IQ, 2))))

print "That becomes: ", WHAT, "Can you do it by hand?"
