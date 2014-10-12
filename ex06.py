"""Exercise 6, Learning Python the Hard Way"""
# -- coding: utf-8 --

# Set the initial variables
X = "There are %d types of people." % 10
BINARY = "binary"
DO_NOT = "don't"
Y = "Those who know %s and those who %s." % (BINARY, DO_NOT)

# Print the x and y variables
print X
print Y

# Inlcude the x and y variables inside strings
print "I said: %r." % X
print "I also said:'%s'." % Y

# Set the joke variables
HILARIOUS = False
JOKE_EVALUATION = "Isn't this joke so funny?! %r"

# Print the joke variables
print JOKE_EVALUATION % HILARIOUS

# Set and print two more varibles just for the sake of it.
W = "This is the left sode of..."
E = "a string with a right side."

print W + E
