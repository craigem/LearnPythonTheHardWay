"""Exercise 43, Learning Python the Hard Way"""


class Parent(object):
    """Opens the class Parent."""
    def override(self):
        """define the override."""
        print "PARENT override()"

    def implicit(self):
        """define implicit inheritance"""
        print "PARENT implicit"

    def altered(self):
        """define the altered inheritance"""
        print "PARENT altered()"


class Child(Parent):
    """opens the class Child with inheritance from Parent"""
    # define the override
    def override(self):
        print "CHILD override()"

    # define the altered inheritance
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
