# -- coding: utf-8 --

# Set the initial variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the x and y variables
print x
print y

# Inlcude thw x and y variables inside strings
print "I said: %r." % x
print "I also said:'%s'." % y

# Set the joke variables
hilarious = False
joke_evaluation = "Isn't this joke so funny?! %r"

# Print the joke variables
print joke_evaluation % hilarious

# Set and print two more varibles just for the sake of it.
w = "This is the left sode of..."
e = "a string with a right side."

print w + e
