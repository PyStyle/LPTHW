print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a spooky NSA Agent staring at your smartphone. What do you do?"
    print "1. Run out of the room."
    print "2. Scream at the NSA Agent 'Go and fuck yourself!'."

    bear = raw_input(">")

    if bear == "1":
        print "The Agent hacks your smartphone. Good job!"
    elif bear == "2":
        print "The Agent hacks your bank account. Good job!"
    else:
        print "Well, doing %s is probably better. Agent runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthuhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity =="2":
        print "You body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall in a knife and die. Good job!"
