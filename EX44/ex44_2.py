class Parent(object):

    def altered(self):
        print "Parent altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

das = Parent()
son = Child()

das.altered()
son.altered()
