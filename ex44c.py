"""Exercise 43, Learning Python the Hard Way"""


class Parent(object):
    """The Parent class is-a object."""
    def altered(self):
        """Define the altered method."""
        print "PARENT altered()"


class Child(Parent):
    """The Child class is-a child of the Parent class."""
    def altered(self):
        """Define the altered method."""
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

DAD = Parent()
SON = Child()

DAD.altered()
SON.altered()
