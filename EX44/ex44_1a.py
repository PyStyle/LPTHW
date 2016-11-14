class Dozenten(object):

    def override(self):
        print "Dozenten denken nur an ihr Fach!()"

class Student(Dozenten):

    def override(self):
        print "Studenten denken nur an ihre Freizeit!()"

Sender = Dozenten()
Empfaenger = Student()

Sender.override()
Empfaenger.override()
