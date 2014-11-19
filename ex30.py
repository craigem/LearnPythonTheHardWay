"""Exercise 26, Learning Python the Hard Way"""
PEOPLE = 30
CARS = 40
BUSES = 15


if CARS > PEOPLE:
    print "We should take the cars."
elif CARS < PEOPLE:
    print "We should not take the cars."
else:
    print "We can't decide."

if BUSES > CARS:
    print "That's too manny buses."
elif BUSES < CARS:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if PEOPLE > BUSES:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
