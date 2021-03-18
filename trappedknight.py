import tkboard
import piece
import pygame
import numpy
import time
import sys
from pygame.locals import *


class TrappedKnight:
    def __init__(self, screensize, screen):
        pygame.init()
        pygame.font.init()

        pygame.mouse.set_visible(False)

        self.screen = screen



        self.size = 100
        self.delay = 0.01
        self.xoffset = 1
        self.width = screensize[0]
        self.height = screensize[1]
        self.yoffset = numpy.rint((self.height / self.width) * self.xoffset)



        pygame.mouse.set_visible(False)

        value = numpy.empty((), dtype=object)
        value[()] = (0, 0)
        self.screencoords = numpy.full((self.size, self.size), value, dtype=object)

        self.b = tkboard.TKBoard(self.size)

        self.origin = self.b.piece.location

        origin = self.b.piece.location

        screen = pygame.display.set_mode((self.width, self.height))

        fontpath = "FreeMono.ttf"

        self.font = pygame.font.Font(fontpath, 30)
        self.drawgrid()


    def drawgrid(self):
        xinterval = (self.width - self.xoffset * 2) / (self.size - 1)
        yinterval = (self.height - self.yoffset * 2) / (self.size - 1)

        for i in range(len(self.b.squares)):
            for j in range(len(self.b.squares[0])):
                x = numpy.rint(self.xoffset + i * xinterval)
                y = numpy.rint(self.yoffset + j * yinterval)
                self.screencoords[i][j] = (x, y)
                # pygame.draw.rect(screen, (255, 255, 255), (x, y, 1, 1))

    def makemoves(self):
        # print(b.piece.location)
        while True:
            lastlocation = self.b.piece.location
            lowestmove = self.b.piece.location
            lowestnumber = -1
            for i in range(len(self.b.piece.moves)):
                testx = self.b.piece.moves[i][0] + lastlocation[0]
                testy = self.b.piece.moves[i][1] + lastlocation[1]

                if testx >= 100 or testx < 0 or testy >= 100 or testy < 0:
                    continue

                if self.b.squares[testx][testy] < lowestnumber or lowestnumber == -1:
                    if self.b.visited[testx][testy] == False:
                        lowestnumber = self.b.squares[testx][testy]
                        lowestmove = (testx, testy)


            if lowestnumber == -1:
                pygame.draw.circle(self.screen, (0, 255, 0), self.onscreen(self.origin), 4)
                pygame.draw.circle(self.screen, (255, 0, 0), self.onscreen(lowestmove), 4)

                if self.b.piece.location[0] == self.size - 1 or self.b.piece.location[0] == 0 or self.b.piece.location[1] == self.size - 1 or \
                        self.b.piece.location[1] == 0:
                    text = pygame.font.Font.render(self.font, 'Trapped by edge!', 1, (255, 255, 255))
                else:
                    text = pygame.font.Font.render(self.font, 'Trapped at square ' + str(self.b.getnum(lowestmove)), 1,
                                                       (255, 255, 255))
                pygame.Surface.blit(self.screen, text, (0, 0))
                pygame.display.update()
                time.sleep(1)
                break

            self.b.piece.location = lowestmove
            self.b.visited[lowestmove[0]][lowestmove[1]] = True
            # print('moved from', b.getnum(lastlocation), 'to', b.getnum(lowestmove))
            pygame.draw.line(self.screen, (255, 0, 255), self.screencoords[lastlocation[0]][lastlocation[1]], self.screencoords[self.b.piece.location[0]][self.b.piece.location[1]])
            time.sleep(self.delay)
            pygame.display.update()
        self.reinit()
        return

    def onscreen(self, x):
            temp = self.screencoords[x[0]][x[1]]
            return (int(temp[0]), int(temp[1]))

    def reinit(self):
        self.b.reinit(self.size)
        self.b.piece.location = (49, 49)
        lastlocation = (49, 49)
        origin = self.b.piece.location

        self.screen.fill((0, 0, 0))
        pygame.display.update()

