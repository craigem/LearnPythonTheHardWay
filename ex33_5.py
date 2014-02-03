# 5. Now, write it to use for-loops and range instead. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
# A: At the bottom becomes 6 instead of 5.

numbers = []

def append_numbers(n):
	"""This function will increment the numbers for us."""
	for i in range(0, 6):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

append_numbers(6)

print "The numbers: "

for num in numbers:
	print num
