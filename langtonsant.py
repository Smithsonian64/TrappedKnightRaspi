import laboard
import pygame
import random
import numpy
from enum import IntEnum


class Colors(IntEnum):
    white = 0
    black = 1
    red = 2
    green = 3
    blue = 4
    yellow = 5
    magenta = 6
    cyan = 7
    orange = 8
    turquoise = 9
    violet = 10
    maroon = 11

class LangtonsAnt:
    def __init__(self, screensize, screen, rules):
        self.size = (100, 100)

        self.board = laboard.LABoard(self.size, screen)
        self.screen = screen
        self.colorValues = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 128, 0), (0, 255, 128), (128, 0, 255), (128, 0, 0)]
        self.rules = self.getrandomrules()

        value = numpy.empty((), dtype=object)
        value[()] = (0, 0)



        self.screencoords = numpy.full((self.size[0], self.size[1]), value, dtype=object)

        self.xinterval = 0
        self.yinterval = 0


        self.width = screensize[0]
        self.height = screensize[1]
        self.xoffset = 0
        self.yoffset = 0#numpy.rint((self.height / self.width) * self.xoffset)

        self.drawgrid()

        print(self.screencoords)

        print(self.rules)

    def makemoves(self):
        while True:
            color = self.getcolor(self.board.ant.location)

            if Colors(color.value).value == len(self.rules) - 1:
                self.board.setcolor(self.board.ant.location, Colors(0))
            else:
                self.board.setcolor(self.board.ant.location, Colors(color.value) + 1)

            if self.rules[color.value] == 'L':
                self.board.ant.turnleft()
            else:
                self.board.ant.turnright()

            pygame.draw.rect(self.screen, self.colorValues[color.value], (self.screencoords[self.board.ant.location[0]][self.board.ant.location[1]][0], self.screencoords[self.board.ant.location[0]][self.board.ant.location[1]][1], int(self.xinterval), int(self.yinterval)))

            self.board.ant.moveforward()

            pygame.display.update()

            if self.board.ant.location[0] >= self.board.size[0] or self.board.ant.location[1] >= self.board.size[1] or \
                    self.board.ant.location[0] < 0 or self.board.ant.location[1] < 0:
                return

    def getcolor(self, index):
        return Colors(self.board.squares[index[0]][index[1]])

    def getrandomrules(self):
        temp = []
        for i in range(random.randint(2, len(self.colorValues))):
            num = random.randint(0, 1)
            if num == 0:
                temp.append('L')
            else:
                temp.append('R')

        return tuple(temp)

    def drawgrid(self):
        self.xinterval = (self.width - self.xoffset * 2) / (self.size[0] - 1)
        self.yinterval = (self.height - self.yoffset * 2) / (self.size[1] - 1)

        for i in range(len(self.board.squares)):
            for j in range(len(self.board.squares[0])):
                x = numpy.rint(self.xoffset + i * self.xinterval)
                y = numpy.rint(self.yoffset + j * self.yinterval)
                self.screencoords[i][j] = (x, y)
