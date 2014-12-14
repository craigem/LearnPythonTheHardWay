"""Exercise 44, Learning Python the Hard Way"""


class Other(object):
    """The class Other is-a object"""
    def override(self):
        """Define the override method."""
        print "OTHER override()"

    def implicit(self):
        """Define the implicit method."""
        print "OTHER implicit"

    def altered(self):
        """Define the altered method."""
        print "OTHER altered()"


class Child(object):
    """The class Child is-a object."""
    def __init__(self):
        self.other = Other()

    def implicit(self):
        """Define the implicit method."""
        self.other.implicit()

    def override(self):
        """Define the override method."""
        print "CHILD override()"

    def altered(self):
        """Define the altered method."""
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

SON = Child()

SON.implicit()
SON.override()
SON.altered()
