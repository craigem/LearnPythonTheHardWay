# 3. Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.
# 4. Rewrite the script again to use this function to see what effect that has.

i = 0
increment = 1
numbers = []

def append_numbers(n):
	"""This function will increment the numbers for us."""
	global i
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

append_numbers(6)

print "The numbers: "

for num in numbers:
	print num
