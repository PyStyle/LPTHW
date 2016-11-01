def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
# looks ok

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
# looks ok too

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
# Add colon @ end of def print_first_word(words)
# Change "poop" to "pop" word = words.poop(0)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
# Add closing parenthesis to word = words.pop(-1

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
# looks ok

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
# looks ok

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
# looks ok


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# looks okidoki
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""
# looks okidoki too


print "--------------"
print poem
print "--------------"
# looks okidoki tootoo
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
# five = 10 - 2 + 3 - 5 Change last no to 6

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
# Change backslash to / jars = jelly_beans \ 1000


start_point = 10000
beans, jars, crates = secret_formula(start_point)
# Change == in beans, jars, crates == secret_formula(start-point), because ==
# used for boolean (if this equals that then), also change
# secret_formula(start-point) to secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# change jeans to beans print "We'd have %d jeans, %d jars, and %d crates."
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
# print "We'd have %d beans, %d jars, and %d crabapples."
# Change crabapples to crates
# and % secret_formula(start_pont to secret_formula(start_point)

sentence = "All good things come to those who wait."
# sentence = "All god\tthings come to those who weight."
# Change "god" to "good"
# Remove tab command
# Change "weight" to "wait"

words = break_words(sentence)
# words = ex25.break_words(sentence)
# Remove ex25.
sorted_words = sort_words(words)
# sorted_words = ex25.sort_words(words)
# Remove ex25.

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
#.print_first_word(sorted_words)
# Remove . @ beginning
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
# sorted_words = ex25.sort_sentence(sentence)
# Remove ex25.
print sorted_words
# prin sorted_words
# add t to print

print_first_and_last(sentence)
# print_irst_and_last(sentence)
# Add f to first

print_first_and_last_sorted(sentence)
#   print_first_a_last_sorted(senence)
# remove leading spaces
# Change a to and
# Change senence to sentence
