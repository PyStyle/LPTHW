# this one is like your scripts with argv
def print_two(*args):
# define, : colon @ end of 1st line, 4 spaces mean that everything following
# with 4 spaces is a block (u can "run", "call" or "use" a function)
# *args = take all functions and put them  in args as a list 
    arg1, arg2 = args
    # arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    # and display them in this way, %r = replace it with %(...),

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

# A function with no arguments still does sth. It just doesn`t need any variable


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
