"""Exercise 43, Learning Python the Hard Way"""


class Parent(object):
    """The Parent class is-a object."""
    def override(self):
        """Define the override."""
        print "PARENT override()"


class Child(Parent):
    """The Child class is-a child of the Parent class."""
    def override(self):
        """Define the override."""
        print "CHILD override()"

DAD = Parent()
SON = Child()

DAD.override()
SON.override()
