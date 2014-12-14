"""Exercise 43, Learning Python the Hard Way"""


class Parent(object):
    """Define the Parent object."""
    def implicit(self):
        """It's implicit!"""
        print "PARENT implicit()"


class Child(Parent):
    """Child class is-a child of the Parent class"""
    pass

DAD = Parent()
SON = Child()

DAD.implicit()
SON.implicit()
