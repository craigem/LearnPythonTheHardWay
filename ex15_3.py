# Import argv from the sys module
from sys import argv

# Set the variables to be taken from argv
script, filename = argv

# Set txt to open the filename from argv
txt = open(filename)

# Use txt to print the contents of the file
print "Here's your filename %r:" % filename
print txt.read()
# Now close the file
txt.close()

# Prompt the uer to ree-type the file name:
print "Type the filename again:"
file_again = raw_input("> ")

# Use read that file and print the file.
txt_again = open(file_again)

print txt_again.read()
# now close this file too
txt_again.close()
