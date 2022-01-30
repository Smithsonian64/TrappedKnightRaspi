import golboard
import numpy
import pygame
import copy
import random
import time

class GameOfLife:
    def __init__(self, screensize, screen):
        self.size = (100, 100)

        self.board = golboard.GOLBoard(self.size, screen)
        self.nextboard = golboard.GOLBoard(self.size, screen)

        self.screen = screen

        self.screencoords = numpy.full((self.size[0], self.size[1]), 0, dtype='i,i,i')

        self.xinterval = 1
        self.yinterval = 1

        self.width = screensize[0]
        self.height = screensize[1]
        self.xoffset = 0
        self.yoffset = 0  # numpy.rint((self.height / self.width) * self.xoffset)

        self.drawgrid()

        self.setrandomcells()
        #self.setRPentomino()
        #self.setAcorn()
        self.starttime = time.time()
        self.duration = random.randint(5, 15)

    def makemoves(self):

        colorvalue = 0
        while True:

            self.nextboard.squares = copy.deepcopy(self.board.squares)

            for i in range(1, len(self.board.squares) - 1):
                for j in range(1, len(self.board.squares[i]) - 1):
                    currentSquare = self.board.squares[i][j]
                    colorvalue = self.screencoords[i][j][2]
                    alivecount = 0
                    if self.board.squares[i][j + 1]:
                        alivecount += 1
                    if self.board.squares[i + 1][j + 1]:
                        alivecount += 1
                    if self.board.squares[i + 1][j]:
                        alivecount += 1
                    if self.board.squares[i + 1][j - 1]:
                        alivecount += 1
                    if self.board.squares[i][j - 1]:
                        alivecount += 1
                    if self.board.squares[i - 1][j - 1]:
                        alivecount += 1
                    if self.board.squares[i - 1][j]:
                        alivecount += 1
                    if self.board.squares[i - 1][j + 1]:
                        alivecount += 1

                    if colorvalue > 0:
                        if colorvalue < 5:
                            self.screencoords[i][j][2] = 0
                        else:
                            self.screencoords[i][j][2] -= 5


                    if (not currentSquare and alivecount == 3):
                        self.nextboard.squares[i][j] = True
                        self.screencoords[i][j][2] = 255

                    if currentSquare and (alivecount != 2 and alivecount != 3):
                        self.nextboard.squares[i][j] = False

                    if currentSquare:
                        self.screencoords[i][j][2] = 255


                    if colorvalue >= 0:
                        pygame.draw.rect(self.screen, (0, colorvalue, colorvalue), (
                            self.screencoords[i][j][0], self.screencoords[i][j][1], int(self.xinterval),
                            int(self.yinterval+1)))

            self.board.squares = copy.deepcopy(self.nextboard.squares)

            pygame.display.update()

            if time.time() - self.starttime > self.duration:
                self.screen.fill((0, 0, 0))
                pygame.display.update()
                return

    def setrandomcells(self):
        for i in range(len(self.board.squares)):
            for j in range(len(self.board.squares[i])):
                if random.randrange(0, 100) % 2 == 0:
                    self.board.squares[i][j] = True

    def setRPentomino(self):
        self.board.squares[50][50] = True
        self.board.squares[49][50] = True
        self.board.squares[50][49] = True
        self.board.squares[50][51] = True
        self.board.squares[51][51] = True

    def setAcorn(self):
        self.board.squares[70][50] = True
        self.board.squares[71][50] = True
        self.board.squares[71][52] = True
        self.board.squares[73][51] = True
        self.board.squares[74][50] = True
        self.board.squares[75][50] = True
        self.board.squares[76][50] = True

    def drawgrid(self):
        self.xinterval = (self.width - self.xoffset * 2) / (self.size[0])
        self.yinterval = (self.height - self.yoffset * 2) / (self.size[1])

        for i in range(len(self.board.squares)):
            for j in range(len(self.board.squares[0])):
                x = numpy.rint(self.xoffset + i * self.xinterval)
                y = numpy.rint(self.yoffset + j * self.yinterval)
                self.screencoords[i][j] = (x, y, 0)
