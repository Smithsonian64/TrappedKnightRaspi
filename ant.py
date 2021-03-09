import numpy


class Ant:
    def __init__(self, start):
        self.location = start
        self.direction = self.getdirection('north')

    def getdirection(self, direction):
        if direction == 'north':
            return 3 * numpy.pi / 2
        if direction == 'east':
            return 0
        if direction == 'south':
            return numpy.pi / 2
        if direction == 'west':
            return numpy.pi

    def turnleft(self):
        if self.direction == self.getdirection('east'):
            self.direction = self.getdirection('north')
        else:
            self.direction -= numpy.pi / 2

    def turnright(self):
        if self.direction == self.getdirection('north'):
            self.direction = self.getdirection('east')
        else:
            self.direction += numpy.pi / 2

    def moveforward(self):
        self.location = (int(self.location[0] + numpy.cos(self.direction)), int(self.location[1] + numpy.cos(self.direction + numpy.pi / 2)))

