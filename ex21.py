"""Exercise 21, Learning Python the Hard Way"""
def add(a, b):
    """Print the sum of a and b"""
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    """Print the result of the sutraction of a from b"""
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    """Print the result of the multiplication of a and b"""
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    """Print the result of the division of a by b"""
    print "DIVIDING %d / %d" % (a, b)
    return a / b


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
