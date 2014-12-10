"""Exercise 42, Learning Python the Hard Way"""


class Animal(object):
    """Animal is-a object (yes, sort of confusing) look @ the extra credit."""
    pass


class Dog(Animal):
    """The Dog class which is-a Animal."""
    def __init__(self, name):
        # ??
        self.name = name


class Cat(Animal):
    """The Cat class which is-a Animal."""
    def __init__(self, name):
        # ??
        self.name = name


class Person(object):
    """The Person class which is-a object."""
    def __init__(self, name):
        # ??
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


class Employee(Person):
    """The employees class which is-a Person."""
    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # ??
        self.salary = salary


class Fish(object):
    """The Fish class which is-a object."""
    pass


class Salmon(Fish):
    """The Salmon class which is-a Fish."""
    pass


class Halibut(Fish):
    """The Halibut class which is-a Fish."""
    pass


# rover is-a Dog
ROVER = Dog("Rover")

# ??
SATAN = Cat("Satan")

# ??
MARY = Person("Mary")

# ??
MARY.pet = SATAN

# ??
FRANK = Employee("Frank", 120000)

# ??
FRANK.pet = ROVER

# ??
FLIPPER = Fish()

# ??
CROUSE = Salmon()

# ??
HARRY = Halibut()
