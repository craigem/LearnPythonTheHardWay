"""Exercise 33, Learning Python the Hard Way"""
# 5. Now, write it to use for-loops and range instead. Do you need the
# incrementation in the middle any more? What happens if you do not get rid of
# it?
# A: At the bottom becomes 6 instead of 5.

NUMBERS = []


def append_numbers(nbr):
    """This function will increment the numbers for us."""
    for i in range(0, 6):
        print "At the top i is %d" % i
        NUMBERS.append(i)

        print "Numbers now: ", NUMBERS
        print "At the bottom i is %d" % i

append_numbers(6)

print "The numbers: "

for num in NUMBERS:
    print num
