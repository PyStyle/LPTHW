class Chatter(object):
    def start(self, start_emotion):
        self.emotion = start_emotion
        print "Hello there, how are you doing?“
        userinput = raw_input(">")
        while userinput != "quit":
            if "angry" in userinput:
                self.emotion = Angry()
            elif "silly" in userinput:
                self.emotion = Coy()
            elif "hello" in userinput:
                self.emotion = Welcoming()
            response = self.emotion.respond(userinput)
            print response
            userinput = raw_input(">")



class Emotion(object):
    pass
class Angry(Emotion):
    pass

class Welcoming(Emotion):
    def respond(self, userinput):
        if "good" in userinput:
            return "I'm so glad that you are good."
        elif "bad" in userinput:
            return "That's such a shame"
        else:
            return "Tell me how you 're doing"'"

class Coy(Emotion):
    pass

#Start the program
from random import choice
emotions = Welcoming(), Angry(), Coy()
startemo = choice(emotions)
App = Chatter()
App.start(startemo)
