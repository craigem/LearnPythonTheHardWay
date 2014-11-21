"""Exercise 33, Learning Python the Hard Way"""
# 3. Add another variable to the function arguments that you can pass in that
# lets you change the + 1 on line 8 so you can change how much it increments by
# 4. Rewrite the script again to use this function to see what effect that has.

i = 0
INCREMENT = 1
NUMBERS = []


def append_numbers(nbr):
    """This function will increment the numbers for us."""
    global i
    while i < nbr:
        print "At the top i is %d" % i
        NUMBERS.append(i)

        i = i + INCREMENT
        print "Numbers now: ", NUMBERS
        print "At the bottom i is %d" % i

append_numbers(6)

print "The numbers: "

for num in NUMBERS:
    print num
