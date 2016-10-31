from sys import argv
# sys = package(library), import the module orthography
#(a little bit of extra code from the package/system)

script, filename = argv
# scrpitname, filename=textfile this is the argument variable
# need to include command line when u run python script
# If you r writing/appending then a new file will b created with that name (if 1
#does not already exist)

# the following code is about modifying objects

print "We're going to erase %r." % filename
# print = stuff that shows up in the terminal

print "If you don't want that, hit CTRL_C ( ^C)."
print "If you do want that, hit RETURN."

raw_input("?")
# prompts ?, waits for our input

print "Opening the file..."
target = open(filename, 'w')
# takes filename, w = write, opens the file (accessible to do sth with it),
# feed this into a target

print "Truncating the file.  Goodbye!"
target.truncate()
# truncating the file, what is in there is gon b erased

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# prompts the 3 lines we type in

print "I#m going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target = object, command write = take any info we type in and write info
# into the text file
# go down to the next line/linebreak

print "And finally, we close it."
target.close()
# write and reas, truncate and close are examples of commands
# (methods or functions for an object e.g. target)
