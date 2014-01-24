# Import arv from sys
from sys import argv

script, input_file = argv

# Define the read function
def print_all(f):
	print f.read()

# Define the seek function
def rewind(f):
	f.seek(0)

# Define the line count function
def print_a_line(line_count, f):
	print line_count, f.readline()

# Open the file specified as an argument to the script
current_file = open(input_file)

# Print the whol file
print "First let's print the whole file:\n"

print_all(current_file)

# Use the rewind function to seek back to the start of the file
print "Now let's rewind, kind of like a tape,"

rewind(current_file)

# Set the current line, print it and increment it
print "Let's print three lines:"

current_line = 1 # Seeks set line count to 0, this makes it 1
print_a_line(current_line, current_file)

current_line += 1 # Increments line count to 2
print_a_line(current_line, current_file)

current_line += 1 # Increment line count to 3
print_a_line(current_line, current_file)
