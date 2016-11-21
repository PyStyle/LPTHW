from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "Welcome to the 'Class of the Last Mediahicans'()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Good luck young 'Mediahican'!", current_scene

        while True:
            print "\n-----"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    def enter(self):
        print "You are dead. Now the entire 'Class of the Last Mediahicans' is "
        print "about to be erased by the 'Big Python' because of your destitue."
        print "May Manitou torture your soul in the happy hunting ground for"
        print "eternity. Howgh!"
        exit(1)

class Saloon(Scene):

    def enter(self):
        print "You wake up in a Saloon with a really bad hangover."
        print "On the table in front of you a huge bottle of firewater is"
        print "provided. The bottle is empty. At the table sits a bunch of"
        print "palefaces. They are all asleep after binge drinking!"
        print "\n"
        print "Your plan to knock them out in a boozy session has worked out."
        print "You can leave the Saloon now to get you a palefaces' horse and"
        print "ride to your village."
        print "Be riding carefully you are still a little drunk!"

        action = raw_input("> ")

        if action == "sleep":
            print "You are such a lazy 'Mediahican'! Your whole Tribe is about to be"
            print "erased by the Big Python because you are such an idle bastard!"
            print "With this kinda attitude you never gonna conquer the Big Python!"
            print "When you will wake up the palefaces probably gonna lynch you"
            print "anyway."
            return 'death'


        elif action == "drink":
            print "You crock! Your whole Tribe is about to be erased by the Big"
            print "Python. And you keep on drinking firewater?!"
            print "You are a disgrace for the 'Tribe of the last Mediahicans'!"
            print "Although 'Mediahicans' are notorious for boozing too much."
            print "By the time you'll wake up, the palefaces probably gonna"
            print "lynch you anyway. Cheers loser!"
            return 'death'


        elif action == "ride":
            print "You get on a horse and gallop out of 'paleface city'."
            print "Although you are sooo hung-over and need some fresh water asap"
            print "set spurs to your horse because time is running out."
            print "\n"
            print "Remember to stop at the creek when you arrive at the plains to"
            print "get some fresh water for you and your horse."
            print "Because you know it is a long-ass ride back to your village."
            print "And try to remain in the saddle although you get dizzy while riding."
            print "A true 'Mediahican' does not know any pain!"
            return 'plains'

        else:
            print "DOES NOT COMPUTE!"
            return 'saloon'



class Plains(Scene):

    def enter(self):
        print "You arrive at the creek. Remember that it is a long-ass way  back"
        print "to your village. Get some fresh water for you and your horse."
        print "But try to drink not too much water because then you will have"
        print "to pee in the plains later."
        print "\n"
        print "As a true 'Mediahican' you should know that peeing in the plains"
        print "is deadly! This is S3RIOUS!"
        print "Try to guess how many drinks of water are appropriate now."
        drinks = "%d" % (randint(1,5))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != drinks and guesses < 6:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]>")

        if guess == drinks:
            print "You and your horse are refreshed."
            print "Get back on the horse. Btw did you not name it yet?"
            print "A true 'Mediahicans' horse needs a name!"
            print "Whatever, do that later. Set spurs to your horse because"
            print "time is running out."
            return 'shaman_tent'
        else:
            print "The horse and you are complete intoxicated with too much"
            print "water. You stop somewhere in the plains to pee."
            print "Suddenly you hear a rustling in the grass."
            print "The 'Big Python' appears and fizzles some codes that you"
            print "Do not understand. You are hearing sounds like SsssModules,"
            print "and SsssClasses and SssssOOP?! Suddenly 'Big Python' just"
            print "swallows you and the horse with its monster gorge."
            print "Shit happens. From OOP to oops."
            return 'death'




class ShamanTent(Scene):

    def enter(self):
        print "You arrive at your village and head directly to the tent of"
        print "the'Mediahicans' Shaman Jonathanou. You enter his tent and hear"
        print "the wise voice of the Shaman saying:"
        print "\n"
        print "'Young Mediahican did you not listen to the old legends of the"
        print "'Big Python'?! It is about the time, that you face the battle."
        print "You are no beginner no more."
        print "Take a puff of the 'Python Pipe' and you will envision what it"
        print "takes to conquer the 'Big Python'!''"
        print "He hands you the Shaman pipe. What are going to do?"
        print "Take a puff or pass?"

        action = raw_input("> ")

        if action == "take a puff":
            print "You walk through wads of smoke and hear the familiar voice "
            print "of Shaman Jonathanou out of the sky: 'Be confident young"
            print "Mediahican you are no beginner no more!''"
            print "\n"
            print "You keep on walking through the smoke although you"
            print "can hardly see anything."
            print "Suddenly you hear that scary fizzle sound again:"
            print "'SssssGet SssssClosssser SssssMart SsssMediahican!'"
            print "Then a big hole appears 10 feet from your moccasins."
            print "You notice the schema of the 'Big Python'."
            print "Your body is shaking like a leaf and your natural"
            print "instincts tell you to run away."
            print "Young Mediahican you just arrived at the Snake Pit."
            return 'snake_pit'

        elif action == "pass":
            print "Yeah we know smoking harms your health."
            print "But a true 'Mediahican' is always ready to sacrifice"
            print "his life for his tribe! You did not learn you lesson yet!"
            print "Although Jonathanou tried to prepare you for this exam."
            print "Fair enough the Shaman will give you another shot."
            print "Please do not disgrace your tribe again."
            print "Jonathanou throws some brazing solder in the fireplace"
            print "and you get demoted back to square one."
            return 'saloon'
        else:
            print "DOES NOT COMPUTE!"
            return "shaman_tent"


class SnakePit(Scene):

    def enter(self):
        print "You stand at the Snake Pit."
        print "Acid fumes and a a fetid, choking odour, the smell of a"
        print "charnel house, grabbs you by the throat!"
        print "The 'Big Python' wriggles out of the Snake Pit"
        print "and stands in attack position."
        print "\n"
        print "Now you have to show what you have learned from all them 'Python'"
        print "drills since you have been become a 'Mediahican'."
        print "The 'Big Python' tries to snag your head, but you duck down."
        print "You jump to the left side and spit out the command to destroy"
        print "the 'Big Python' forever:"
        print "Def destroy_python(eternity):"
        print "python.destroy"
        print "The mighty words of Jonathanou echo in your head: Never forget"
        print "to attach 'Parenthesis' to the 'Dot Operator'!"
        print "\n"
        print "What do you attach?"

        action = raw_input("> ")

        if action == "()":
            print "The 'Big Python' fizzles a last SssssDamned!"
            print "The monster curls to the left and then to the right."
            print "Suddenly you hear a big bang and the 'Big Python' explodes"
            print "and slime covers the whole plas plus your face."
            print "But nevermind! You have mastered the 'Big Python' and saved"
            print "the entire 'Class of the Last Mediahicans'."
            print "Everlasting glory is all but certain for you."
            print "\n"
            print "'Big Python' is destroyed and your Tribe will forever be"
            print " grateful. Manitous sympathy will be for certain from now on."

            return 'finished'

        else:
            print "The 'Big Python' bites of your head."
            return 'death'

class Finished(Scene):
    def enter(self):
        print " You've won young Mediahican! Great Job, Howgh!"
        exit(0)


class Map(object):

    scenes = {
        'saloon' : Saloon(),
        'plains' : Plains(),
        'shaman_tent' : ShamanTent(),
        'snake_pit' : SnakePit(),
        'death' : Death(),
        'finished' : Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('saloon')
a_game = Engine(a_map)
a_game.play()
