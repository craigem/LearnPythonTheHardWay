"""Exercise 8, Learning Python the Hard Way"""
# -- coding: utf-8 --

FORMATTER = "%r %r %r %r"

print FORMATTER % (1, 2, 3, 4)
print FORMATTER % ("one", "two", "three", "four")
print FORMATTER % (True, False, False, True)
print FORMATTER % (FORMATTER, FORMATTER, FORMATTER, FORMATTER)
print FORMATTER % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
