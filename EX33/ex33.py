i = 0
numbers = []
# Creates an empty list (similar to an array in other languages )

# For while-loops, structure is similar to 'def', 'if' and
# 'for'-loops with colon at end of 1st line, then indent

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    # Can also be written as i += 1
    # Note: In other languages you can write 'I++' but that
    # doesn`t work in Python
    # On the last loop, the increment raises i to 6 but
    # it doesn`t get added to the list or get printed because
    # it happens after the print and append but before the
    # loop returns to 'while i < 6' which stops the loop
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers:"

for num in numbers:
    print num
# for-loop goes through the numbers list and prints each one
