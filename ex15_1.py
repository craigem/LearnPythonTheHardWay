# Import argv from the sys module
from sys import argv

# Set the variables to be taken from argv
script, filename = argv

# Set txt to open the filename from argv
txt = open(filename)

# Use txt to print the contents of the file
print "Here's your filename %r:" % filename
print txt.read()
