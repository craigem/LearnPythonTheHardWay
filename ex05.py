"""Exercise 5, Learning Python the Hard Way"""
# -- coding: utf-8 --

NAME = 'Zed A. Shaw'
AGE = 35 # not a lie
HEIGHT = 74 # inches
WEIGHT = 180 # lbs
EYES = 'Blue'
TEETH = 'White'
HAIR = 'Brown'

print "Let's talk about %s." % NAME
print "He's %r inches tall." % HEIGHT
print "He's %d pounds heavy." % WEIGHT
print "ACtually that's not too heavy."
print "He's got %s eyes and %s hair." % (EYES, HAIR)
print "His teeth are usually %s depending on the coffee." % TEETH

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % \
    (AGE, HEIGHT, WEIGHT, AGE + HEIGHT + WEIGHT)
