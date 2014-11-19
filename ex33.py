"""Exercise 33, Learning Python the Hard Way"""
i = 0
NUMBERS = []

while i < 6:
    print "At the top i is %d" % i
    NUMBERS.append(i)

    i = i + 1
    print "Numbers now: ", NUMBERS
    print "At the bottom i is %d" % i


print "The numbers: "

for num in NUMBERS:
    print num
