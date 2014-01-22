# Prompt for the file name
print "What is the fiilename you'd like to read?"
filename = raw_input("> ")

# Set txt to open the filename from argv
txt = open(filename)

# Use txt to print the contents of the file
print "Here's your filename %r:" % filename
print txt.read()

# Prompt the uer to ree-type the file name:
print "Type the filename again:"
file_again = raw_input("> ")

# Use read that file and print the file.
txt_again = open(file_again)

print txt_again.read()
