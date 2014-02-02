i = 0
numbers = []

def append_numbers(n):
    """This function will increment the numbers for us."""
    global i
    while i < n:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

append_numbers(6)

print "The numbers: "

for num in numbers:
	print num
