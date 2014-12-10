"""Exercise 42.3, Learning Python the Hard Way"""


class Animal(object):
    """Animal is-a object (yes, sort of confusing) look @ the extra credit."""
    print "Altogether Animals!"
    print "=" * 19


class Dog(Animal):
    """Dog is-a Animal"""
    def __init__(self, name):
        # ??
        self.name = name
        print "%s says: Woof!" % self.name


class Cat(Animal):
    """Cat is-a Animal"""
    def __init__(self, name):
        # ??
        self.name = name
        print "%s says: Meow!" % self.name


class Person(object):
    """Person is-a object"""
    def __init__(self, name):
        # ??
        self.name = name
        print "%s says: Hello!" % self.name

        # Person has-a pet of some kind
        self.pet = None
        print "My name is %s and this is my pet, %s." % (self.name, self.pet)


class Employee(Person):
    """Employee is-a Person"""
    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # ??
        self.salary = salary


class Fish(object):
    """Fish is-a object"""
    def __init__(self, name):
        # ??
        self.name = name
        print "I'm %s the fish!" % self.name


class Salmon(Fish):
    """Salmon is-a fish"""
    def __init__(self, name):
        # ??
        self.name = name
        print "I'm %s the salmon!" % self.name


class Halibut(Fish):
    """Halibut is-a fish"""
    def __init__(self, name):
        # ??
        self.name = name
        print "I'm %s the halibut!" % self.name


# rover is-a Dog
ROVER = Dog("Rover")

# Satan is-a Cat
SATAN = Cat("Satan")

# mary is-a Person
MARY = Person("Mary")

# mary's pet is-a satan
MARY.pet = SATAN

# frank is-a Employee
FRANK = Employee("Frank", 120000)

# frank's pet is-a rover
FRANK.pet = ROVER

# flipper is-a fish
FLIPPER = Fish("Flipper")

# crouse is-a Salmon
CROUSE = Salmon("Crouse")

# harry is-a Halibut
HARRY = Halibut("Harry")
