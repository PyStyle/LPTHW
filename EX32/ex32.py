the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# for for-loops, structure is similar to "def" and "if"
# with colon at the end of 1st line, then indent
for number in the_count:
    print "This is count %d" % number
    #the 1st variable (right after for) can use any name u like
    # although "i" is common
    # %d because these are number or 'digits'

# same as above
for fruits in fruits:
    # just dont use the same name twice
    print "A fruit of type: %s" % fruits
    # %s because the fruit names are strings

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    # "i" is most common variable name for for-loops
    print "I got %r" % i
    # %r because the data consots of different types



# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    #Range starts @ 1st number  (inclusive) but stops @ 1 less than 2nd no. (exclusive)
    # this is how items in lists are numbered
    # But 0 as 1st no. is default, so this can also be written as 'range(6)'
    # can also specify whether range goes up or down and size of steps
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
    # This adds the numbers to the list one at a time

# now we can print them out too
for i in elements:
    print "ELement was: %d" % i
