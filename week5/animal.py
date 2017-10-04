

class Animal(object):
    def __init__(self, name, health=10):
        self.name = name 
        self.health = health 
    def walk(self):
        print "{} is walking...".format(self.name)
        self.health -= 1
        return self
    def run(self): 
        print "{} is running...".format(self.name)
        self.health -= 5
        return self
    def displayHealth(self): 
        print "{}'s health is now at {}.".format(self.name, self.health)

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        print"petting {}...".format(self.name)
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        print "{} is flying...".format(self.name)
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a dragon!"


Cat = Animal("Zoomer", 9)
Cat.run().walk().displayHealth()

Sparky = Dog("Sparky")
Sparky.displayHealth()
Sparky.walk().walk().walk().run().run().pet().displayHealth()

Smokey = Dragon("Smokey")
Smokey.walk().fly().displayHealth()

ardvark = Animal("Artimus")
ardvark.walk().walk().displayHealth().fly()