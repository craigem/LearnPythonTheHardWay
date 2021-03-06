"""Exercise 38, Learning Python the Hard Way"""
TEN_THINGS = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

STUFF = TEN_THINGS.split(' ')
MORE_STUFF = ["Day", "Night", "Song", "Frisbee", "Corn",
              "Banana", "Girl", "Boy"]

while len(STUFF) != 10:
    NEXT_ONE = MORE_STUFF.pop()
    print "Adding: ", NEXT_ONE
    STUFF.append(NEXT_ONE)
    print "There's %d items now." % len(STUFF)

print "There we go: ", STUFF

print "Let's do some things with stuff."

print STUFF[1]
print STUFF[-1]  # whoa! Fancy
print STUFF.pop()
print ' '.join(STUFF)  # what? cool!
print '#'.join(STUFF[3:5])  # super stellar!
