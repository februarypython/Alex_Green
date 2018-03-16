class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def display_health(self):
        print self.health

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("dog", 150)
    
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__("dragon", 170)
    
    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        super(Dragon, self).display_health()
        print "i am a dragon"

frog = Animal("Frog", 100)
Dog1 = Dog()
Dragon1 = Dragon()
Cat = Animal("cat", 200)

frog.walk().walk().walk().run().run().display_health()
Dog1.walk().walk().walk().run().run().pet().display_health()
Dragon1.fly().fly().display_health()
Cat.walk().fly().pet().display_health() #pet and fly do not work for cat/animal class.
