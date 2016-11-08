people = 20
cats = 30
dogs = 15

# For if statements, structure is similar to "def."
# with colon @ end of 1st line, then indent

if people < cats:
    print "Too many cats! The world is doomed!"
# 20 < 30 == TRUE, displays "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"
# 20 > 30 == FALSE, no display

if people < dogs:
    print "The world is drooled on!"
# 20 < 15 == FALSE, no display

if people > dogs:
    print "The world is dry!"
# 20 > 15 == TREU, this displays


dogs += 5

# dogs = 15 + 5 = 20
# This is a method for incrementing numbers
# It is equivalent to "dogs = dogs + 5"
# You can also use -=, *=, \=, etc.

if people >= dogs:
    print "People are greater than or equal to dogs."
# 20 >= 20 == TRUE, so displays

if people <= dogs:
    print "People are less than equal to dogs."
# 20<= 20 == TRUE, so displays again


if people == dogs:
    print "People are dogs."
