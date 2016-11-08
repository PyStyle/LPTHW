##           'Fighting Donald' - A Simple Text Adventure
##                          Version 0.1
##
##                Author: PyStyle - November 2016
##
##  Written as part of Exercise 36 from Learn Python the Hard Way by Z. A.Shaw
##              http://learnpythonthehardway.org
##
##  A simple text adventure which takes a player linearly through a set of
##  rooms.
##  Each room has an obstacle to get past, with one solution
##  and one fail to kill you and the entire world.
##
##  To me this is like one "My first game" adventure, so pls judge on me kindly.
##  Similarities with living or dead persons are purely coincidental.
##
################################################################################

#Import quit
from sys import exit

# Room 1 - Intro room
def start():
    print "\n\tYou wake in a dimly lit room."
    print "\tThere is a door in front of you."
    print "\tAn inscription reads \"Welcome to the Top of the Trump Tower.\""
    print "\tType \"Open door\" if you dare!\n"

    next = raw_input("> ")

#BUG - Typing gibberish no longer leads to death? Why?

    if next == "open" or "Open":
        koch_room()
    elif "exit" in next:
        exit_game()
    else:
        dead("\tYou just caused the Apocalypse without even trying you milquetoast asshole!\n")

# Room 2 - Koch bros sitting with 2 Heckler & Kochs on a bunch of gold
def koch_room():

    print "\n\tYou enter the next room. The door locks behind you."
    print "\tYou see the two Koch Bros in front of another door."
    print "\tThey have a Heckler & Koch in their hand each & sit on a bunch of gold."
    print "\tThe only way through that door is to take the gold."
    print "\tBut how?\n"

    run_away = False

    while True:
        next = raw_input("> ")

        if next == "call Koch Bros":
            print "The Koch Bros just shot you in your face and gave all their gold to Donald!"
            exit_game()
        elif next == "run_away":
            dead("You have just caused the Apocalypse you milquetoast asshole!")
        elif next == "take gold":
            print "\n\tIn a moment of madness, you snatch the gold from the Koch Bros."
            print "\tBefore they could grab the Heckler & Kochs, you throw 2 gold nuggets"
            print "\ton them.\n"
            print "\t'Take that you Kochsuckers!'\n"
            print "\tThe gold nuggets block their gun barrels!\n"

            Gold_taken = True
        elif next == ("open door" or "Open door") and Gold_taken:
            Bernie_room()
        elif next == "exit":
            exit_game()
        else:
            dead("\tThe Donald became POTUS you stupid asshole. This is the End Of World!\n")

# Room 3 - Bernie_room
def Bernie_room():
    print "\n\tYou look around the new room as the sounds of the slamming door"
    print "\techos behind you."
    print "\tYou see a dwarf guarding the next door."
    print "\tIt is Bernie looking at you intently."
    print "\tBernie holds Donalds lost tax returns in his hands. If you give him"
    print "\tyour gold he will hand them out to you."
    print "\tSo what are you gonna do? Keep the gold or give it to Bernie???\n"



    keep_Gold = False

    while True:
        next = raw_input("> ")

        if "talk" in next:
            print "\n\tYou try to reason with Bernie."
            print "\tUnfortunately, Bernie has forgotten his deaf-aid."
            print "\tSo forget it."
            print "\tBernie walks over and smacks you in the head with a Marx"
            print "\tbook. Your face becomes red like the cover of the book."
            print "\tAs you lose conciousness you think to yourself how lucky"
            print "\tyou are that Bernie is weakened by age and you are going "
            print "\tto survive.\n"
            start()
        elif "give gold" in next:
            print "\n\tBernie hands you Donalds tax return. You take them and mail"
            print "\ta snapshot to Julian."
            print "\tJulian publishes everything and the public is shocked."
            print "\tA lot."
            print "\tYou feel like a hero, but only for the moment."
            print "\tBecause, the world is not going to become a better place.\n"
            print "\tIt is going to be the same shitty place it has been before.\n"
            print "\tBut at least things will not become \"worse\" right now.\n"

            Bernie_moved = True
        elif next == ("open door" or "Open door") and Bernie_moved:
            exit_room()
        #elif next != ("open door" or "Open door") and Bernie_moved:
         #   dead("Why did you have to go and say that?")
        elif next == "exit":
            exit_game()
        else:
            dead("You are a greedy snob for keeping the gold!\n")



# Room 5 - Exit room
def exit_room():
    print "\n\tYou open the door and see your way out."
    print "\tAs you walk through the door it slams behind you."
    print "\tAnd then you remember the pile of gold.\n" # add a pause here
    print "\tIn Bernies hands.\n" # add a pause here

    print "\tBut at least he will give the gold to the poor. You hope!\n"
    print "\n\tNow the world is the same shitty place as it has been before.\n"
    print "\n\tBut at least things have not become worse yet.\n"
    print "\n\tDonald got thrown into jail, but Bill became 1st Gentleman now!"
    print "\n\tSame agenda different gender! Hooray!!"

    print "\n\n\t\tTHE END\n"

    exit_game()


# Dead - Tell person they are dead and quit game
def dead(cause):
    print cause, "\n\tYou have just caused the Apocalypse! Now you are dead!\n"
    exit(0)

# Exit - Quit game
def exit_game():
    print "\n\tThanks for playing! \n"
    print "\n\tNext time you better go voting instead of playing shitty games! \n"
    print "\n\tBtw: Great job asshole!"
    exit(0)

#Start - Calls the start function
start()

# Cheat - Brings up solution to room
