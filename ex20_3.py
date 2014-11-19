"""Learn Python the Hard Way, exercise 20"""
# Import arv from sys
from sys import argv

SCRIPT, INPUT_FILE = argv


def print_all(myfile):
    """Define the read function"""
    print myfile.read()


def rewind(myfile):
    """Define the seek function"""
    myfile.seek(0)


def print_a_line(line_count, myfile):
    """Define the line count function"""
    print line_count, myfile.readline()

# Open the file specified as an argument to the script
CURRENT_FILE = open(INPUT_FILE)

# Print the whol file
print "First let's print the whole file:\n"

print_all(CURRENT_FILE)

# Use the rewind function to seek back to the start of the file
print "Now let's rewind, kind of like a tape,"

rewind(CURRENT_FILE)

# Set the current line, print it and increment it
print "Let's print three lines:"

CURRENT_LINE = 1  # Seeks set line count to 0, this makes it 1
print_a_line(CURRENT_LINE, CURRENT_FILE)

CURRENT_LINE += 1  # Increments line count to 2
print_a_line(CURRENT_LINE, CURRENT_FILE)

CURRENT_LINE += 1  # Increment line count to 3
print_a_line(CURRENT_LINE, CURRENT_FILE)
