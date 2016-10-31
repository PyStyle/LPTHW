from sys import argv
# adding a module to my code

script, input_file = argv

# create a function to display an entire text file,
# "f" is just a variable name for the file
def print_all(f):
    print f.read()
# dot operator to use the read function

# create a function to go to beginning of a file (i.e. byte 0)
def rewind(f):
    f.seek(0)

# create a function to print out one line, where line_count is the
# line number we want to read, f is the name of the file (from above),
# and readline is a built-in function or method

def print_a_line(line_count, f):
    print line_count, f.readline()

# = assignment operator, defines variable and put in the variable object
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# define current line below, current file in line 24, print 1 line @ a time
current_line = 1
print_a_line(current_line, current_file)

# move to neaxt line by incrementing the variable current_line,
# +1 add another line 
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
