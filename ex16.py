"""Exercise 16, Learning Python the Hard Way"""
from sys import argv

SCRIPT, FILENAME = argv

print "we're going to erase %r." % FILENAME
print "If you don't wasnt that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
TARGET = open(FILENAME, 'w')

print "Truncating the file.  Goodbye!"
TARGET.truncate()

print "Now I'm going to ask you for three lines."

LINE1 = raw_input("line 1: ")
LINE2 = raw_input("line 2: ")
LINE3 = raw_input("line 3: ")

print "I'm going to write these to the file."

TARGET.write(LINE1)
TARGET.write("\n")
TARGET.write(LINE2)
TARGET.write("\n")
TARGET.write(LINE3)
TARGET.write("\n")

print "And finally, we close it."
TARGET.close()
