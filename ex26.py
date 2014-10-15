"""Exercise 26, Learning Python the Hard Way"""
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t \
    tabs.'

POEM = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print POEM
print "--------------"

FIVE = 10 - 2 + 3 - 6
print "This should be five: %s" % FIVE

def secret_formula(started):
    """Secret forumula for calculating the number of jars, bean and crates"""
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


START_POINT = 10000
BEANS, JARS, CRATES = secret_formula(START_POINT)

print "With a starting point of: %d" % START_POINT
print "We'd have %d beans, %d jars, and %d crates." % (BEANS, JARS, CRATES)

START_POINT = START_POINT / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(
    START_POINT)


SENTENCE = "All good things come to those who wait."

import ex25

WORDS = ex25.break_words(SENTENCE)
SORTED_WORDS = ex25.sort_words(WORDS)

print_first_word(WORDS)
print_last_word(WORDS)
print_first_word(SORTED_WORDS)
print_last_word(SORTED_WORDS)
SORTED_WORDS = ex25.sort_sentence(SENTENCE)
print SORTED_WORDS

print_first_and_last(SENTENCE)

print_first_and_last_sorted(SENTENCE)
