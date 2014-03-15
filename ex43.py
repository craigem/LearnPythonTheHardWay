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

# * Scene
#   - enter
class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

# * Engine
class Engine(object):

	def __init__(self, scene_map):
		print "Engine __init__ has scene_map", scene_map
		self.scene_map = scene_map

#   - play
	def play(self):
		current_scene = self.scene_map.opening_scene()
		print "Play's first scene". current_scene

		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			print "next scene", next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name)
			print "map returns new scene", current_scene

#   * Death
class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mum would be proud...is she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

#   * Central Corridor
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bobmb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."

		action = RAW_INPUT("> ")

		if action == "shoot!":
			print "Quick on the draw you yank your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. your laser hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'

		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your arfyul dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wale up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'

		elif action == "tell a joke":
			print "Lucky for you they made you learth Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then bursts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			print 'laser_weapon_armory'

			else:
				print "DOES NOT COMPUTE!"
				return 'central_corridor'

#   * Laser Weapon Armory
class LaserWeaponArmory(Scene):

	def enter(self):
		pass

#   * The Bridge
class TheBridge(Scene):

	def enter(self):
		pass

#   * Escape Pod
class EscapePod(Scene):

	def enter(self):
		pass

# * Map
class Map(object):

	def __init__(self, start_scsene):
		pass

#   - next_scene
	def next_scene(self, scene_name):
		pass

#   - opening_scene
	def opening_scene(self):
		pass

# * Gothon
# * Planet

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
