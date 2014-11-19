"""Exercise 24, Learning Python the Hard Way"""
print "Let's practive everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t \
    tabs.'

POEM = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "--------------"
print POEM
print "--------------"


FIVE = 10 - 2 + 3 - 6
print "This should be five: %s" % FIVE


def secret_formula(started):
    """Secret forumula for calculating the number of jars, bean and crates"""
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = JARS / 100
    return jelly_beans, jars, crates


START_POINT = 10000
BEANS, JARS, CRATES = secret_formula(START_POINT)

print "With a starting point of: %d" % START_POINT
print "We'd have %d beans, %d jars, and %d crates." % (BEANS, JARS, CRATES)

START_POINT = START_POINT / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(
    START_POINT)
