# Import exit from sys so we can exit cleanly:
from sys import exit

# Open Game in a room and present options
def start():
	# You entered a dark and stormy cave.
	print "You have entered a dark and stormy cave..."
	# There is a passage to the left one to the right.
	print "There is a passage to the left and on your right."

	next = raw_input("Choose your own adventure: ")

	if next == "left":
	# Left will lead to hamster_room()
		hamster_room()
	elif next == "right":
	# Right will lead to gerbil_room()
		gerbil_room()
	else:
	# The floor opens up underneath you as Cthulu rises and swallows you whole.
		dead("The floor opens up underneath you as Cthulu rises and swallows you whole.")


# Open the hamster_room and let them know what's in it:
def hamster_room():
	print "\n"
	# there's a hamster here.
	print "There's a hamster here."
	# a toothpick
	# a salad sandwich
	print "There's also a salad sandwich and a toothpick."

	next = raw_input("What you talkin 'bout Wilis?: ")

	if next == "salad sandwich":
	# Choosing the salad sandwich will result in the hamster devouring you
		print "The hamster roars, leaps toward you, tears your head off and commences devouring you from the neck down."
		exit(0)
	elif next == "toothpick":
	# Choosing the  toothpick will result in hmaster slaughter
		print "You pick up the toothpick with a forward summersault before stabbing the evil hamster through the heart."
		exit(0)
	else:
	# Choosing an invalid option results in death
		dead("The floor opens up underneath you as Cthulu rises and swallows you whole.")

# dead option

# Open the room and let them know what's in it:
def gerbil_room():
	# a gerbil
	print "There's a gerbil here."
	# some dental floss
	print "There's some dental floss..."
	# a stick of celery
	print "...and a stick of celery."

	next = raw_input("Which do you choose?: ")

	if next == "dental floss":
	# Choosing the dental floss will result in the gerbil assasination.
		print "You cartwheel across to the gerbil, collecting the dental floss along the way before strangling the evil little bugger from behind."
		exit(0)
	elif next == "celery":
	# Choosing celery will result in the gerbil get a free meal of human flesh.
		print "The gerbil lets out a blood curdling cry before leaping across the room and locking it's powerful jaw around your left big toe as it commences to devour you from the bottom up."
		exit(0)
	else:
	# Choosing an invalid option results in death
		dead("The floor opens up underneath you as Cthulu rises and swallows you whole.")

def dead(why):
	print why, "Good job!"
	exit(0)

start()
