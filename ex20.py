"""Exercise 20, Learning Python the Hard Way"""
from sys import argv

SCRIPT, INPUT_FILE = argv


def print_all(myfile):
    """Print the whole file"""
    print myfile.read()


def rewind(myfile):
    """Rewind to the start of the file"""
    myfile.seek(0)


def print_a_line(line_count, myfile):
    """Print one of the lines"""
    print line_count, myfile.readline()

CURRENT_FILE = open(INPUT_FILE)

print "First let's print the whole file:\n"

print_all(CURRENT_FILE)

print "Now let's rewind, kind of like a tape,"

rewind(CURRENT_FILE)

print "Let's print three lines:"

CURRENT_LINE = 1
print_a_line(CURRENT_LINE, CURRENT_FILE)

CURRENT_LINE = CURRENT_LINE + 1
print_a_line(CURRENT_LINE, CURRENT_FILE)

CURRENT_LINE = CURRENT_LINE + 1
print_a_line(CURRENT_LINE, CURRENT_FILE)
