class Birds(object):
    def __init__(self, birdType):
        self.type = birdType

    def canFly(self):
        print(self.type + " can fly")

    def cantFly(self):
        print(self.type + " cant fly")

class Raven(Birds):
    def __init__(self, birdName):
        self.type = birdName
        super().__init__(birdName)

class Penguins(Birds):
    def __init__(self, birdName):
        self.type = birdName
        super().__init__(birdName)

bird = Raven("Ravens")
bird.canFly()

bird = Penguins("Penguins")
bird.cantFly()

