# opens the class Parent
class Parent(object):

	# define the override
	def override(self):
		print "PARENT overrride()"

	# define implicit inheritance
	def implicit(self):
		print "PARENT implicit"

	# define the altered inheretance
	def altered(self):
		print "PARENT altered()"

# opens the class Child with inhereitance from Parent
class Child(Parent):

	# define the override
	def override(self):
		print "CHILD override()"

	# define the altered inheretance
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		# Use super to call the altered Parent version
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

# set dad and son
dad = Parent()
son = Child()

# Run each version
dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
