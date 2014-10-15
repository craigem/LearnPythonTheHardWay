"""Exercise 29, Learning Python the Hard Way"""
PEOPLE = 20
CATS = 30
DOGS = 15


if PEOPLE < CATS:
    print "Too many cats! The world is doomed!"

if PEOPLE > CATS:
    print "Not many cats! The world is asved!"

if PEOPLE < DOGS:
    print "The world is drooled on!"

if PEOPLE > DOGS:
    print "The world is dry!"


DOGS += 5

if PEOPLE >= DOGS:
    print "People are greater than or equal to dogs."

if PEOPLE <= DOGS:
    print "People are less than or equal to dogs."


if PEOPLE == DOGS:
    print "People are dogs."
