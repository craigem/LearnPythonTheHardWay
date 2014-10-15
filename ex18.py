"""Exercise 18, Learning Python the Hard Way"""
# this one is like your scripts with argv
def print_two(*args):
    """Take two arguments and print them"""
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    """Take two arguments and print them"""
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    """Take one arguments and print it"""
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    """Take no arguments and print statement"""
    print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
