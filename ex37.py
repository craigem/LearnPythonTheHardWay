# Use each of the operators in ex37_template.mdwn in a small Python 
# program, or as many as you can get done. The key here is to find out what
# the symbol does, make sure you got it right, correct it if you do not, 
# then use it to lock it in.

# from
# import
from sys import exit

# def
# print
# if
# == is equal to comparison
# elif nests an if statement inside and if statement
# else if all expressions are false, run this.
# =	Assignment operator, assigns a value
def start():
	# Opening statement to player
	print "You have entered my dark and stormy python script where I will use" 
	print "all the operators."
	print "Which pill do you want, red or blue? \n"

	next = raw_input("Choose your pill colour: ")

	print "\n"

	# Use if to evaluate responses from the player.
	if next == "red":
	# Red will lead to the red_room()
		red_room()
	elif next == "blue":
	# Blue will lead to the blue_room()
		blue_room()
	else:
	# Summon Keanu
		dead("Your horrendous typing has summoned Keannu, who will bore you with annecdotes from Bill & Ted's excellent adventure for all eternity...")


def red_room():
	# AKA the interesting choice
	print "So you've chosen to enbrace the sometimes painful truth of reality. Good choice."
	print "Let's get serious then, shall we?"
	print "\n"


# %s	String format. The default type for strings
# <		Less than comparison
# >=  greater than or equal to comparison
def blue_room():
	# AKA the soft option
	print "So, you've chosen the blissfull ignorance of illusion."
	print "That's pretty soft, let's see what we can do with that."
	print "\n"
	
	age = raw_input("How old are you? ")
	where = raw_input("What locality do you live in? ")

	print "\n"
	if age < "30":
		# Flatter their youth
		print "Wow, only %s? You are not only young and beautiful but you have wisdom and intellect beyond your years. I wonder if everyone else from %s are as amazing as you?" % (age, where)
	elif age >= "60":
		# Patronise those old enough to feel entitled to it
		print "%s? Really? How does such great wisdom reside in such a youthful visage? There must be something wonderful in the water of %s." % (age, where)
	else:
		# Pander to that middle age insecurity
		print "Wow, you look so much younger than %s and you live in %s! You truly are youthful and exotic." % (age, where)


def dead(why):
	print why, "Nice work nimble fingers!"
	exit(0)

start()
