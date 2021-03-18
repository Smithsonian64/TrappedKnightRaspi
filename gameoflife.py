import golboard
import numpy
import pygame
import copy
import random


class GameOfLife:
    def __init__(self, screensize, screen):
        self.size = (100, 100)

        self.board = golboard.GOLBoard(self.size, screen)
        self.nextboard = golboard.GOLBoard(self.size, screen)



        self.screen = screen
        # self.colorValues = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 128, 0), (0, 255, 128), (128, 0, 255), (128, 0, 0)]
        # self.rules = self.getrandomrules()

        # self.rules = self.getrandomrules()

        value = numpy.empty((), dtype=object)
        value[()] = (0, 0)

        self.screencoords = numpy.full((self.size[0], self.size[1]), value, dtype=object)

        self.xinterval = 1
        self.yinterval = 1

        self.width = screensize[0]
        self.height = screensize[1]
        self.xoffset = 0
        self.yoffset = 0  # numpy.rint((self.height / self.width) * self.xoffset)

        self.drawgrid()

        self.setrandomcells()

        self.board.squares[50][50] = True
        self.board.squares[51][50] = True
        self.board.squares[51][51] = True

    def makemoves(self):
        while True:

            self.calculateepoch()
            #print(self.board.squares)

            for i in range(1, len(self.board.squares) - 1):
                for j in range(1, len(self.board.squares[i]) - 1):
                    print(self.board.squares[i][j])
                    if self.board.squares[i][j]:

                        pygame.draw.rect(self.screen, (255, 255, 255), (
                            self.screencoords[i][j][0], self.screencoords[i][j][1], int(self.xinterval),
                            int(self.yinterval)))
                        print('coloring:', i, j, 'white')
                    else:
                        pygame.draw.rect(self.screen, (0, 0, 0), (
                            self.screencoords[i][j][0], self.screencoords[i][j][1], int(self.xinterval),
                            int(self.yinterval)))
                    pygame.display.update()

    def calculateepoch(self):
        alivecount = 0
        for i in range(1, len(self.board.squares) - 1):
            for j in range(1, len(self.board.squares[i]) - 1):
                if self.board.squares[i][j + 1]:
                    alivecount += 1
                if self.board.squares[i + 1][j + 1]:
                    alivecount += 1
                if self.board.squares[i][j + 1]:
                    alivecount += 1
                if self.board.squares[i - 1][j + 1]:
                    alivecount += 1
                if self.board.squares[i - 1][j]:
                    alivecount += 1
                if self.board.squares[i - 1][j - 1]:
                    alivecount += 1
                if self.board.squares[i][j - 1]:
                    alivecount += 1
                if self.board.squares[i + 1][j - 1]:
                    alivecount += 1
                if alivecount >= 2 and alivecount <= 3:
                    self.nextboard.squares[i][j] = True
                else:
                    self.nextboard.squares[i][j] = False
        self.board.squares = copy.deepcopy(self.nextboard.squares)

    def setrandomcells(self):
        for i in range(len(self.board.squares)):
            for j in range(len(self.board.squares[i])):

                self.board.squares[i][j] = True

    def drawgrid(self):
        self.xinterval = (self.width - self.xoffset * 2) / (self.size[0])
        self.yinterval = (self.height - self.yoffset * 2) / (self.size[1])

        for i in range(len(self.board.squares)):
            for j in range(len(self.board.squares[0])):
                x = numpy.rint(self.xoffset + i * self.xinterval)
                y = numpy.rint(self.yoffset + j * self.yinterval)
                self.screencoords[i][j] = (x, y)
