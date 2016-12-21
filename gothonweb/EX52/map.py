class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = self.paths.get('*')
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
death = Scene("Death", "death", "you died",
"""
You are dead. Now the entire 'Class of the Last Mediahicans' is
about to be erased by the 'Big Python' because of your destitue.
May Manitou torture your soul in the happy hunting ground for
eternity. Howgh!
""")

saloon = Scene("Saloon", "saloon",
"""
You wake up in a Saloon with a really bad hangover.
On the table in front of you a huge bottle of firewater is
provided. The bottle is empty. At the table sits a bunch of
palefaces. They are all asleep after binge drinking!
Your plan to knock them out in a boozy session has worked out.
You can leave the Saloon now to get you a palefaces' horse and
ride to your village.
Be riding carefully you are still a little drunk!
""")

plains = Scene("Plains", "plains",
"""
You arrive at the creek. Remember that it is a long-ass way  back
to your village. Get some fresh water for you and your horse.
But try to drink not too much water because then you will have
to pee in the plains later.
As a true 'Mediahican' you should know that peeing in the plains
is deadly! This is S3RIOUS!
Try to guess how many drinks of water are appropriate now.
""")

shaman_tent = Scene("shaman_tent", "Shaman_Tent",
"""
You arrive at your village and head directly to the tent of
the'Mediahicans' Shaman Jonathanou. You enter his tent and hear
the wise voice of the Shaman saying:
'Young Mediahican did you not listen to the old legends of the
'Big Python'?! It is about time, that you face the battle.
You are no beginner no more.
Take a puff of the 'Python Pipe' and you will envision what it
takes to conquer the 'Big Python'!'
He hands you the Shaman pipe. What are going to do?
Take a puff or pass?
""")

snake_pit = Scene("Snake_Pit", "snake_pit",
"""
You stand at the Snake Pit.
Acid fumes and a a fetid, choking odour, the smell of a
charnel house, grabbs you by the throat!
The 'Big Python' wriggles out of the Snake Pit
and stands in attack position.
Now you have to show what you have learned from all them 'Python'
drills since you have been become a 'Mediahican'.
The 'Big Python' tries to snag your head, but you duck down.
You jump to the left side and spit out the command to destroy
the 'Big Python' forever:
Def destroy_python(eternity):
python.destroy
The mighty words of Jonathanou echo in your head: Never forget
to attach 'Parenthesis' to the 'Dot Operator'!
What do you attach?
""")

sleepy_loser = Scene("Sleep", "sleep",
"""
You are such a lazy 'Mediahican'! Your whole Tribe is about to be
erased by the Big Python because you are such an idle bastard!
With this kinda attitude you never gonna conquer the Big Python!
When you will wake up the palefaces probably gonna lynch you
anyway.
""")

drunk_loser = Scene("Drunkie", "Drunk_Loser", "drunk_loser",
"""
You crock! Your whole Tribe is about to be erased by the 'Big
Python'. And you keep on drinking firewater?!
You are a disgrace for the 'Tribe of the last Mediahicans'!
Although 'Mediahicans' are notorious for boozing too much.
By the time you'll wake up, the palefaces probably gonna lynch you anyway.
Cheers loser!
""")

finished = Scene("Finished", "You won",
"""
The 'Big Python' fizzles a last SssssDamned!
The monster curls to the left and then to the right.
Suddenly you hear a big bang and the 'Big Python' explodes
and slime covers the whole plas plus your face.
But nevermind! You have mastered the 'Big Python' and saved
the entire 'Class of the Last Mediahicans'.
Everlasting glory is all but certain for you.
'Big Python' is destroyed and your Tribe will forever be grateful.
Manitous sympathy will be for certain from now on...
You've won young Mediahican! Great Job, Howgh!
""")

#Define the action commands available in each scene
saloon.add_paths({
    'sleep': sleepy_loser,
    'drink': drunk_loser,
    'ride': plains
})

plains.add_paths({
    '3': shaman_tent,
    '*': death
})

shaman_tent.add_paths({
    'take a puff': snake_pit,
    'pass': death
})

snake_pit.add_paths({
    '()':finished
    '*': death
})
# Make some useful variables to be used in the web application
SCENES = {
    death.urlname: death,
    saloon.urlname: saloon,
    plains.urlname: plains
    shaman_tent.urlname: shaman_tent
    snake_pit.urlname: snake_pit
    sleepy_loser.urlname: sleepy_loser
    drunk_loser.urlname: drunk_loser
    finished.urlname: finished
}
START = saloon
