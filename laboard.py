import numpy
import pygame
import ant



class LABoard:
    def __init__(self, size, screen):

        self.screen = screen
        self.size = size
        self.squares = numpy.full((size[0], size[1]), 0)
        self.ant = ant.Ant((int(numpy.floor(size[0] / 2)), int(numpy.floor(size[1] / 2))))

        #for i in range(size[0]):
         #   for j in range(size[1]):
          #      pygame.draw.rect(screen, (255, 255, 255), (i, j, 1, 1))



    def setcolor(self, index, color):
        self.squares[index[0]][index[1]] = color
