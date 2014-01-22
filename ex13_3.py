# -- coding: utf-8 --

# Import argv from sys
from sys import argv

# Get some user input
pants = raw_input("Are you wearing pants? ")

# Set the variable to argv
script, first, second, third = argv

# Print them.

print "The script is called:", script
print "Your first variable is:", first
print "Yout second variable is:", second
print "Your third variable is:", third
print "Your pants status is:", pants
