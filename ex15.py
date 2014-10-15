"""Exercise 15, Learning Python the Hard Way"""
# Import argv from the sys module
from sys import argv

# Set the variables to be taken from argv
SCRIPT, FILENAME = argv

# Set txt to open the filename from argv
TXT = open(FILENAME)

# Use txt to print the contents of the file
print "Here's your filename %r:" % FILENAME
print TXT.read()

# Prompt the uer to ree-type the file name:
print "Type the filename again:"
FILE_AGAIN = raw_input("> ")

# Use read that file and print the file.
TXT_AGAIN = open(FILE_AGAIN)

print TXT_AGAIN.read()
