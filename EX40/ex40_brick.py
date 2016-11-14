class Dozenten(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def lied_an_den_dozenten(self):
        for line in self.lyrics:
            print line

botschaft_1 = lied_an_den_dozenten(["We don't need no education",
                                       "We don't need no thought control",
                                       "No dark sarcasm in the classroom"])

botschaft_2 = lied_an_den_dozenten(["Teachers leave them kids alone",
                                          "Hey! Teacher! Leave them kids alone!",
                                          "All in all, it's just another brick in the wall",
                                          "All in all, you're just another brick in the wall"])

botschaft_1.lied_an_den_dozenten()
botschaft_2.lied_an_den_dozenten()
