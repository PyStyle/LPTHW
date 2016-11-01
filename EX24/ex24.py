print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# Line is in single quotes_> need to be escaped with a backslash. Blank
# spaces after newlines and tabs print as such.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# Triple quotes for extended text, as well as new line & tab commands.


print "--------------"
print poem
print "--------------"
# displays dashes, poem and dashes again


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
# These are the variable names within the function, known as local variables
# (opposed to "global variables").
# They can be different outside the function.


start_point = 10000
beans, jars, crates = secret_formula(start_point)
# This calls the function and fills the three variables.
# "Beans" instead of "jelly beans", could name variables whatever u wanted.
# The function just fills them in with the return values in order they r listed.

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# Here we use the variable names as defined oabove and NOT as in the functions.

start_point = start_point / 10
# Reassigns start_point with a new value based on the old one.
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
# This version calls on the function and fills in the values directly
# without creating intermediate variables outside the function.
