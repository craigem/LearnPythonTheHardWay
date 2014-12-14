"""Exercise 43, Learning Python the Hard Way"""
# Gothons from Planet Percal #25
#
# "Aliens have invaded a space ship and our hero has to go through a maze of
# rooms defeating them so he can escape into an escape pod to the planet below.
# The game will be morelike a Zork or Adventure type game with test outputs and
# funny ways to die. The game will invlove an engine that runs a map full if
# rooms or scenes. Each room will print its own description when the player
# enters it and then tell then engine what room to rub netx out of the map."
#
# Death
# =====
# This is when the player dies and should be something funny
# Central Corridor
# ================
# This is the starting point and has a Gothon already standing there they have
# to defeat with a joke before continuing
# Laser Weapon Armory
# ===================
# This is where the hero gets a neutron bomb to blow up the ship before getting
# to the escape pod. It has a keypad he has to guess the number for.
# The Bridge
# ==========
# Another battle scene with a Gothon where the hero places the bomb
# Escape Pod
# ==========
# Where the hero escapes but only after guessing the right esape pod.
#
# * Alien
# * Player
# * Ship
# * Maze

# Import requirements
from sys import exit
from random import randint


class Scene(object):
    """Default scene object"""
    def enter(self):
        """Define what happens when the default scene is entered."""
        print "This scene is not yet configured. Subclass it and " \
            "implement enter()."
        exit(1)


class Engine(object):
    """The game engine"""
    def __init__(self, scene_map):
        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        """Play the current scene."""
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene

    while True:
        print "\n--------"
        next_scene_name = current_scene.enter()
        print "next scene", next_scene_name
        current_scene = self.scene_map.next_scene(next_scene_name)
        print "map returns new scene", current_scene


class Death(Scene):
    """The death scene."""
    quips = [
        "You died. You kinda suck at this.",
        "Your mum would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):
    """The central corridor."""
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and"
        print "destroyed your entire crew. You are the last surviving member"
        print "and your last mission is to get the neutron destruct bomb from"
        print "the Weapons Armoury, put it in the bridge, and blow the ship"
        print "up after getting into an escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons"
        print "Armoury when a Gothon jumps out, red scaly skin, dark grimy"
        print "teeth, and evil clown costume flowing around his hate filled"
        print "body. He's blocking the door to the Armoury and about to pull"
        print "a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank your blaster and fire it at the"
            print "Gothon. His clown costume is flowing and moving around his"
            print "body, which throws off your aim. your laser hits his"
            print "costume but misses him entirely. This completely ruins his"
            print "brand new costume his mother bought him, which makes him"
            print "fly into an insane rage and blast you repeatedly in the"
            print "face until you are dead. Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide"
            print "right as the Gothon's blaster cranks a laser past your"
            print "head. In the middle of your artful dodge your foot slips"
            print "and you bang your head on the metal wall and pass out. You"
            print "wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learth Gothon insults in the " \
                  "academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, " \
                  "fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then bursts out " \
                  "laughing and can't move."
            print "While he's laughing you run up and shoot him square in " \
                  "the head"
            print "putting him down, then jump through the Weapon Armoury " \
                  "door."
            print 'laser_weapon_armory'
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    """The laser weapon armory scene."""
    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the"
        print "room for more Gothons that might be hiding. It's dead quiet,"
        print "too quiet. You stand up and run to the far side of the room and"
        print "find the neutron bomb in it's container. There's a keypad lock"
        print "on the box and you need the code to get the bomb out. If you"
        print "get the code wrong 10 times then the lock closes forever and"
        print "you can't get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess not in (code, '169') and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess in [code, '169']:
            print "The container clicks open and the seal breaks, letting gas"
            print "out. You grab the neutron bomb and run as fast as you can"
            print "to the Bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up"
            print "the ship from their ship and you die."
            return 'death'


class TheBridge(Scene):
    """The bridge scene."""
    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"


class EscapePod(Scene):
    """The escape pod scene."""
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) not in (good_pod, 0):
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"

            return 'finished'


class Map(object):
    """The map object."""
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armoury': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        """Define the next scene."""
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
        return val

    def opening_scene(self):
        """Define the opening scene."""
        return self.next_scene(self.start_scene)

# * Gothon
# * Planet

A_MAP = Map('central_corridor')
A_GAME = Engine(A_MAP)
A_GAME.play()
