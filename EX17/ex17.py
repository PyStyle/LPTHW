from sys import argv
# import the argument variable, which lets us specify some info in the command line
from os.path import exists
# os. path used because different operating systems specify files path in
# different ways
# using import to get free code other programmers have written
# "exists" is a function that returns "TRUE" if the path file is valid (i.e.
# file exists and user has permission not "TRUE" -> "FALSE")

script, from_file, to_file = argv
# Need to give name files that u r copying from and copying to in the command
# line when u running this pythn script

print "Copying from %s to %s" % (from_file, to_file)
# display name from which we r copying to file we copy to in terminal

# we could do these two on one line, how?
# indata = open(from_file).read() -> but need to rmv in_file.close() at end
in_file = open(from_file)
# open the from_file and stick that info ito the in_file
indata = in_file.read()
# "in_file" object/variable exists, dot operator says read it (btw function needs
# empty parentheses () as a space for aguments, even if no arguments exist)
# and = says put that text into another object/variable called "in_data"


print "The input file is %d bytes long" % len(indata)
# len = length of the file in bytes

print "Does the output file exist? %r" % exists(to_file)
# exists(to_file) function we imported @2nd line, which gives "TRUE" or "False"
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
# reads whether user hits RETURN or CTRL-C

out_file = open(to_file, 'w')
# take the to_file and opens it or create it, 'w' make it so u can write to it
# default is "read" only, create an object called out_file
out_file.write(indata)
# take the indata and write it to the out_file

print "Alright, all done."

out_file.close()
in_file.close()
# clean up the files that r currently still opened

#One line version
