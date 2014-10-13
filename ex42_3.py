## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	print "Altogether Animals!"
	print "=" * 19

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name
		print "%s says: Woof!" % self.name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name
		print "%s says: Meow!" % self.name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name
		print "%s says: Hello!" % self.name

		## Person has-a pet of some kind
		self.pet = None
		print "My name is %s and this is my pet, %s." % (self.name, self.pet)

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## Fish is-a object
class Fish(object):

	def __init__(self, name):
		## ??
		self.name = name
		print "I'm %s the fish!" % self.name

## Salmon is-a fish
class Salmon(Fish):

	def __init__(self, name):
		## ??
		self.name = name
		print "I'm %s the salmon!" % self.name

## Halibut is-a fish
class Halibut(Fish):

	def __init__(self, name):
		## ??
		self.name = name
		print "I'm %s the halibut!" % self.name


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")	

## mary is-a Person
mary = Person("Mary")

## mary's pet is-a satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank's pet is-a rover
frank.pet = rover

## flipper is-a fish
flipper = Fish("flipper")

## crouse is-a Salmon
crouse = Salmon("Crouse")

## harry is-a Halibut
harry = Halibut("Harry")
