"""Exercise 14, Learning Python the Hard Way"""
from sys import argv

SCRIPT, USER_NAME = argv
PROMPT = '> '

print "Hi %s, I'm the %s script." % (USER_NAME, SCRIPT)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % USER_NAME
LIKES = raw_input(PROMPT)

print "Where do you live %s?" % USER_NAME
LIVES = raw_input(PROMPT)

print "What kind of computer do you have?"
COMPUTER = raw_input(PROMPT)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (LIKES, LIVES, COMPUTER)
