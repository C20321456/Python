class Birds(object):
    def __init__(self, birdType):
        self.birdtype = birdType

    def canFly(self):
        print(self.birdtype + " can fly")

    def cantFly(self):
        print(self.birdtype + " cant fly")


class Raven(Birds):
    def __init__(self, birdName):
        self.birdtype = birdName

        super().__init__(birdName)

class Penguins(Birds):
    def __init__(self, birdName):
        self.birdtype = birdName
        
        super().__init__(birdName)

bird = Raven("Ravens")
bird.canFly()

bird = Penguins("Penguins")
bird.cantFly()

