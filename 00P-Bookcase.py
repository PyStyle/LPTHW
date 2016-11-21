


# Define the classes
class Bookcase(object):
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def _str_(self):
        return self.prettyprint()

        def prettyprint(self):
            return "A Generic Bookcase"

class Billy(Bookcase):
    def _init_(self, width, height):
        super(Billy, self)._init_(width, height)

        # Overridden method
        def prettyprint(self):
            pretty = "A Billy Bookcase with dimension &d x %d cm"
            return pretty % (self.width, self.height)

class Hemnes(Bookcase):
    def _init_(self, width, height):
        super(Hemnes, self)._init_(width, height)

    # overriden method
    def prettyprint(self):
        pretty = "A Fany Hemnes Bookcase with dimensions %d x %d cm"
        return pretty % (self.width, self.height)

# Make an instance of the classes
gen = Bookcase(50, 100)
bil = Billy(80, 120)
hem = Hemnes(200, 180)

# Call one of the functions (methods) inside the instanceprint hem.prettyprint()
print hem.prettyprint ()
# Other useful things
print "Type:\n %r\n %r\n %r" % (type(gen), type(bil), type(hem))
print "Raw:\n %r\n %r\n %r" % (gen, bil, hem)
print "Pretty:\n %s\n %s\n %s" % (gen, bil, hem)
print "Is Instance of Billy?: ", isinstance(gen, Billy)
print "Is Instance of Billy?: ", isinstance(bil, Billy)
print "Is Instance of Billy?: ", isinstance(hem, Billy)
