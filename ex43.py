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
		pass

#   - play
	def play(self):
		pass

#   * Death
class Death(Scene):

	def enter(self):
		pass

#   * Central Corridor
class CentralCorridor(Scene):

	def enter(self):
		pass

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
