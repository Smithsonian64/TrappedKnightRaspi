import numpy
import pygame
import ant



class GOLBoard:
    def __init__(self, size, screen):

        self.screen = screen
        self.size = size
        self.squares = numpy.full((size[0], size[1]), False)



    def setcolor(self, index, color):
        self.squares[index[0]][index[1]] = color
