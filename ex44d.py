"""Exercise 43, Learning Python the Hard Way"""


class Parent(object):
    """Opens the class Parent."""
    def override(self):
        """define the override."""
        print "PARENT overrride()"

    def implicit(self):
        """define implicit inheritance"""
        print "PARENT implicit"

    def altered(self):
        """define the altered inheretance"""
        print "PARENT altered()"


class Child(Parent):
    """opens the class Child with inhereitance from Parent"""
    # define the override
    def override(self):
        print "CHILD override()"

    # define the altered inheretance
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        # Use super to call the altered Parent version
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

# set DAD and SON
DAD = Parent()
SON = Child()

# Run each version
DAD.implicit()
SON.implicit()

DAD.override()
SON.override()

DAD.altered()
SON.altered()
