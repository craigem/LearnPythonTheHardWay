"""Exercise 31, Learning Python the Hard Way"""
THE_COUNT = [1, 2, 3, 4, 5]
FRUITS = ['apples', 'oranges', 'pears', 'apricots']
CHANGE = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes though a list
for number in THE_COUNT:
    print "This is count %d" % number

# same as above
for fruit in FRUITS:
    print "A fruit of type: %s" % fruit

# also  we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in CHANGE:
    print "I got %r" % i

# we can also build lists, first start with an empty one
ELEMENTS = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    ELEMENTS.append(i)

# now we can print them out too
for i in ELEMENTS:
    print "Element was: %d" % i
