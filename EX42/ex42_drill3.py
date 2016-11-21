## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    voice = "I am a dangerous, I bite the hand that feeds me."

    def __init__(self, name):
        ## Animal has-a name
        self.name = name

    def talk(self):
        print Animal.voice

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    def setAttr(self, attr):
        Dog.voice = attr

    def getAttr(self):
        print Dog.voice

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

	def setAttr(self, attr):
		Cat.voice = attr

	def getAttr(self):
		print Cat.voice


## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is-a Person hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a Pet named satan
mary.pet = satan

## Frank is-a Employee (with value 120000?)
frank = Employee("Frank", 120000)

## Frank has-a pet named rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

rover.talk()
rover.setAttr("bark bark I'm a Ruff Ryder like DMX")
rover.getAttr()

satan.talk()
satan.setAttr("meoow meooow I'm a Smoove Criminal like Catwoman")
satan.getAttr()