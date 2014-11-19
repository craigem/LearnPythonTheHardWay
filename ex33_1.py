"""Exercise 33, Learning Python the Hard Way"""
i = 0
NUMBERS = []


def append_numbers(nnn):
    """This function will increment the numbers for us."""
    global i
    while i < nnn:
        print "At the top i is %d" % i
        NUMBERS.append(i)

        i = i + 1
        print "Numbers now: ", NUMBERS
        print "At the bottom i is %d" % i

append_numbers(6)

print "The numbers: "

for num in NUMBERS:
    print num
