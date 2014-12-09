"""Exercise 35, Learning Python the Hard Way"""
from sys import exit


def gold_room():
    """Defines the gold room."""
    print "This room is full of gold. How much do you take?"

    mynext = raw_input("> ")
    if "0" in mynext or "1" in mynext:
        how_much = int(mynext)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    """There be bears in here."""
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        mynext = raw_input("> ")

        if mynext == "take honey":
            dead("the bear looks at you then slaps your face off.")
        elif mynext == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. " \
                  "You can go through it now."
            bear_moved = True
        elif mynext == "taunt_bear" and bear_moved:
            print "The bear gets pissed off and chews your leg off."
        elif mynext == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    """Cthulhu lives here."""
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    mynext = raw_input("> ")

    if "flee" in mynext:
        start()
    elif "head" in mynext:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    """Your funeral procession"""
    print why, "Good job!"
    exit(0)


def start():
    """Defines the start of the game."""
    print "You are in a dark room."
    print "there is a door to your right and left."
    print "Which one do you take?"

    mynext = raw_input("> ")

    if mynext == "left":
        bear_room()
    elif mynext == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
