def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b
# return creates a value that can be assigned to a variable that calls the
# function. That is, it makes the value available but doesn't do anything with
# it on its own.

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"
# first display in the terminal, because the print commands above are in
# function definitions and these functions haven't been called yet.

age = add(30, 5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide(100, 2)
# by calling the functions to assign values to variables, 2 things happen:
# 1. the functionruns, which is why their text appears in the terminal
# 2. the resulting value is assigned to the variable, which is why it can fill
# in the next string

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here's a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# Python observes in the order of operations by doing the innermost parenthesis
# and then working out

print "That becomes:", what, "Can you do it by hand?"
