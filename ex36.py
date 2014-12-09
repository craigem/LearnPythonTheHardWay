"""Exercise 36, Learning Python the Hard Way"""
# Import exit from sys so we can exit cleanly:
from sys import exit


def start():
    """Open Game in a room and present options"""
    # You entered a dark and stormy cave.
    print "You have entered a dark and stormy cave..."
    # There is a passage to the left one to the right.
    print "There is a passage to the left and on your right."

    mynext = raw_input("Choose your own adventure: ")

    if mynext == "left":
        # Left will lead to hamster_room()
        hamster_room()
    elif mynext == "right":
        # Right will lead to gerbil_room()
        gerbil_room()
    else:
        # The floor opens up underneath you as Cthulhu rises and swallows
        # you whole.
        dead("The floor opens up underneath you as Cthulhu rises and swallows "
             " you whole.")


# Open the hamster_room and let them know what's in it:
def hamster_room():
    """Let's define the hamster room."""
    print "\n"
    # there's a hamster here.
    print "There's a hamster here."
    # a toothpick
    # a salad sandwich
    print "There's also a salad sandwich and a toothpick."

    mynext = raw_input("What you talkin 'bout Wilis?: ")

    if mynext == "salad sandwich":
        # Choosing the salad sandwich will result in the hamster devouring you
        print "The hamster roars, leaps toward you, tears your head off and " \
              "commences devouring you from the neck down."
        exit(0)
    elif mynext == "toothpick":
        # Choosing the  toothpick will result in hamster slaughter
        print "You pick up the toothpick with a forward somersault before " \
              "stabbing the evil hamster through the heart."
        exit(0)
    else:
        # Choosing an invalid option results in death
        dead("The floor opens up underneath you as Cthulhu rises and "
             "swallows you whole.")

# dead option


def gerbil_room():
    """Open the room and let them know what's in it:"""
    # a gerbil
    print "There's a gerbil here."
    # some dental floss
    print "There's some dental floss..."
    # a stick of celery
    print "...and a stick of celery."

    mynext = raw_input("Which do you choose?: ")

    if mynext == "dental floss":
        # Choosing the dental floss will result in the gerbil assassination.
        print "You cartwheel across to the gerbil, collecting the dental " \
              "floss along the way before strangling the evil little " \
              "bugger from behind."
        exit(0)
    elif mynext == "celery":
        # Choosing celery will result in the gerbil get a free
        # meal of human flesh.
        print "The gerbil lets out a blood curdling cry before leaping " \
              "across the room and locking it's powerful jaw around your " \
              "left big toe as it commences to devour you from the bottom up."
        exit(0)
    else:
        # Choosing an invalid option results in death
        dead("The floor opens up underneath you as Cthulhu rises and "
             "swallows you whole.")


def dead(why):
    """Define death."""
    print why, "Good job!"
    exit(0)

start()
