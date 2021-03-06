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
#%f  Displays the number as a fixed point number.
#\'  Escapes the ' character
#\b  ASCII Backspace
#\\  Escapes the \ character
#+   Addition
#-   Subtraction
#!=  is not equal to comparison
#/   Division
#//  Truncating division
#**  Exponentiation (power) operator
#!=  is not equal to comparison
def red_pill_l2():
	# Bring in some numbers and add them to an array
	age = int(raw_input("\nBefore we begin, how old are you? "))
	# This sets up code to be called by exec later to calulate their year of birth
	useexec = compile('year_of_birth = now.year - %s' % age, '<string>', 'exec') 
	exec useexec
	print "Your age is: %f" % age
	print "Your year of birth %d" % year_of_birth
	print "Creating rpl2list..."
	rpl2list = [age, year_of_birth]
	print "rpl2list contains: %s" % rpl2list
	for i in rpl2list:
		print "This is number: %d" % i
	del rpl2list[1]
	if year_of_birth == 1984:
		print "\nBig brother is watching you."
	# This needs fixing
	months = (age * 12)
	print "You\'ve seen %s months." % months
	if age <= 16:
		dead("\t \vYou're \"too young\" to be using this!")
	# Now I'm going to backspace a line just because
	print "What\b is happening\b to\b this\b sentence\b? \\b gone wild."
	num1 = int(raw_input("\nNow pick a number: "))
	num2 = int(raw_input("Pick another number: "))
	num3 = num1 + num2
	num4 = num1 - num2
	num5 = num1 / num2
	num6 = num1 // num2
	num7 = num1 ** num2
	gt = num1 > num2
	if num1 != num2:
		print "This is just an excuse for me to play with some maths."
		print "Addition: %d + %d = %d" % (num1, num2, num3)
		print "Subtraction: %d - %d = %d" % (num1, num2, num4)
		print "Division: %d / %d = %d" % (num1, num2, num5)
		print "Truncating Division: %d // %d = %d" % (num1, num2, num6)
		print "Exponention: %d ** %d = %d" % (num1, num2, num7)
		# Fix this
		if num1 > num2:
			print "By how much is %d > %d? %d" % (num1, num2, gt)

def dead(why):
	print why, "Nice work nimble fingers!"
	exit(0)

# Start the program
start()
