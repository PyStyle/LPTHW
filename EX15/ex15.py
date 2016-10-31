from sys import argv
# sys = package, import the module orthography (a little bit of extra code from
# the package/system)

script, filename = argv
# filename=textfile this is the argument variable

txt = open(filename)
# create a variable (txt)
# =(put into this variable)
# "open" is a command that reads our text file
# (as long as you put the name of the file in
# the command line when you ran the script)

print "Here`s your file %r:" % filename
#print the content of the file to the console, %r = filename
print txt.read()
#txt is the variable or object and the .(dot)
# is an operator to add a command, "read" in this case
# take this object and do this operation on this object, then read it
# and display it in the terminal
# The parentheses () have to be there but in
# this case there are no arguments to pass

print "Type the filename again:"
# And these do it all over from within the script, take that info we typed
file_again = raw_input("> ")
# take it as raw_input and put into an object called file_again

txt_again = open(file_again)
# open up and out it into text again

print txt_again.read()
# print/display it on the console again

txt.close
txt_again.close
# Also need to close the files
# Use the filename and the dot operator

# study6 =
# Kyans-MBP:LPTHW kyanpur$ python

# >>> f = open ("ex15_sample.txt")
# >>> print f.read()
