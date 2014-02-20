# Use each of the operators in ex37_template.mdwn in a small Python 
# program, or as many as you can get done. The key here is to find out what
# the symbol does, make sure you got it right, correct it if you do not, 
# then use it to lock it in.

# from
# import
from sys import exit
from subprocess import call
import datetime

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
		dead("\n\a\a\aYour horrendous typing has summoned Keannu, who will bore you with annecdotes from Bill & Ted's excellent adventure for all eternity...")


def red_room():
	# AKA the interesting choice
	print "So you've chosen to enbrace the sometimes painful truth of reality. Good choice."
	print "Let's get serious then, shall we?"
	print "\n"
	
	next = raw_input("Would you like a glass of milk? ")

	# Process their response
	if next == "yes":
	# yes will summon apt-get moo:
		call(["apt-get", "moo"])
	elif next == "no":
	# no will take you to the red pill level 2
		red_pill_l2()
	else:
	# Summon Keanu
		dead("\n\a\a\aYour horrendous typing has summoned Keannu, who will bore you with annecdotes from Bill & Ted's excellent adventure for all eternity...")

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

# Set the value of now
now = datetime.datetime.now()

# [ ] list
# * Multiplication
# <= less than or equal to comparison
# \" Escapes the " character
#\t ASCII Horizontal Tab
#\v ASCII Vertical Tab
def red_pill_l2():
	# Bring in some numbers and add them to an array
	age = raw_input("\nBefore we begin, how old are you? ")
	# This sets up code to be called by exec later to calulate their year of birth
	useexec = compile('year_of_birth = now.year - %s' % age, '<string>', 'exec') 
	exec useexec
	print "Your age is: %s" % age
	print "Your year of birth %d" % year_of_birth
	print "Creating rpl2list..."
	rpl2list = [age, year_of_birth]
	print "rpl2list contains: %s" % rpl2list
	for i in rpl2list:
		print "This is number: %s" % i
	del rpl2list[1]
	if year_of_birth == 1984:
		print "\nBig brother is watching you."
	# This needs fixing
	# Still needs fixing
	months = (age * 12)
	print "You've seen %s months." % months
	if age <= "16":
		dead("\t \vYou're \"too young\" to be using this!")

	

def dead(why):
	print why, "Nice work nimble fingers!"
	exit(0)

# Start the program
start()
