"""Exercise 31, Learning Python the Hard Way"""
print (
    "You enter a dark room with two doors. Do you go through door #1 or "
    "door #2?")

DOOR = raw_input("> ")

if DOOR == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    BEAR = raw_input("> ")

    if BEAR == "1":
        print "The bear eats your face off. Good job!"
    elif BEAR == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % BEAR

elif DOOR == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    INSANITY = raw_input("> ")

    if INSANITY == "1" or INSANITY == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
