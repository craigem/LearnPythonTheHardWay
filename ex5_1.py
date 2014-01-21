# -- coding: utf-8 --

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
#Print the weight and convert to centimeters
print "He's %d inches, %d centimeters tall." % (height, height * 2.54)
#Print the weight and convert to kilos
print "He's %d pounds, %d kilos heavy." % (weight, weight * 0.4535)
print "ACtually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
