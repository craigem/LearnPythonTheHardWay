"""Learn Python the Hardway, exercise 19"""


def not_your_fathers_function(old_spice_count, cougars_crowding):
    """Defined my own function"""
    print "You have %d bottles of old spice!" % old_spice_count
    print "There are %d cougars crowding..." % cougars_crowding
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Run 1
print "Let's just set the numbers directly:"
not_your_fathers_function(20, 30)

# Run 2
print "Let's set the variables directly from the function:"
OLD_SPICE_COUNT = 10
COUGARS_CROWDING = 50

not_your_fathers_function(OLD_SPICE_COUNT, COUGARS_CROWDING)

# Run 3
print "Do math inside:"
not_your_fathers_function(10 + 20, 5 + 6)

# Run 4
print "Combine the two, variablers and math:"
not_your_fathers_function(OLD_SPICE_COUNT + 100, COUGARS_CROWDING + 1000)

# Run 5
print "Muiltiple the number of cougars by the bottle of old spice:"
not_your_fathers_function(OLD_SPICE_COUNT, OLD_SPICE_COUNT * 2.5)

# Run 6
print "..but we all know Old Spice is repulsive:"
not_your_fathers_function(OLD_SPICE_COUNT, OLD_SPICE_COUNT / 2)

# Run 7
print "Okay, let's OD on the BO:"
not_your_fathers_function(OLD_SPICE_COUNT * 10,
                          COUGARS_CROWDING * OLD_SPICE_COUNT)

# Run 8
print "Right, I'm getting bored now...:"
OLD_SPICE_COUNT = 10
COUGARS_CROWDING = OLD_SPICE_COUNT * 3.5

not_your_fathers_function(OLD_SPICE_COUNT, COUGARS_CROWDING)

# Run 9
print "Running out of ideas and getting repitive:"
OLD_SPICE_COUNT = 10
COUGARS_CROWDING = OLD_SPICE_COUNT / 3.5

not_your_fathers_function(OLD_SPICE_COUNT, COUGARS_CROWDING)

# Run 10
print "Finally I can put this exercise behind me"
OLD_SPICE_COUNT = 10
COUGARS_CROWDING = 50

not_your_fathers_function(OLD_SPICE_COUNT, COUGARS_CROWDING / OLD_SPICE_COUNT)
