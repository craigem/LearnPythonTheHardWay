"""Exercise 17, Learning Python the Hard Way"""
from sys import argv
from os.path import exists

SCRIPT, FROM_FILE, TO_FILE = argv

print "Copyng from %s to %s" % (FROM_FILE, TO_FILE)

# we could do these two on one line too, how?
IN_FILE = open(FROM_FILE)
INDATA = IN_FILE.read()

print "THe input file is %d bytes long" % len(INDATA)

print "Does the output file exist? %r" % exists(TO_FILE)
print "Ready, hit RETURN to continue, CTLRL-C to abort."
raw_input()

OUT_FILE = open(TO_FILE, 'w')
OUT_FILE.write(INDATA)

print "Alright, all done."

OUT_FILE.close()
IN_FILE.close()
