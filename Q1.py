#super() is a function in Python that makes class inheritance more manageable and extensible.
# the function returns a temporary object that allows refrence to a parent class

class Animal(object):
    def __init__(self, animalName):
        self.name = animalName

    def eat(self):
        print(self.name + " is eating")

    def walk(self):
        print(self.name + " is walking")

    def roar(self):
        print(self.name + " is roaring") 


class Dog(Animal):
    def __init__(self, dogName):
        self.name = dogName
        super().__init__(dogName)

    def giveTreat(self):
        super().eat()

    def goForWalk(self):
        super().walk()

class Bird(Animal):
    def __init__(self, birdName):
        self.name = birdName
        super().__init__(birdName)

    def giveSeeds(self):
        super().eat()

class Lion(Animal):
    def __init__(self, lionName):
        self.name = lionName
        super().__init__(lionName)

dog = Dog("Rex")
dog.giveTreat()
dog.goForWalk()

bird = Bird("Gizmo")
bird.giveSeeds()

safari_Lion = Lion("Haster")
safari_Lion.roar()


