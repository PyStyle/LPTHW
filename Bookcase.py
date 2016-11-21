# Blueprint for pumping out new bookcases
class Bookcase(objects):
    # this is where you set up a new instance
    def_init_(self, w, h):
        print "Initializing a new bookcase"
        self.width = w
        self.height = h

# Here's how you make a bookcase from the Blueprint
a = Bookcase(10, 200)
