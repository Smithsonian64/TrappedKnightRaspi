import numpy
import piece
import pygame
import sys

class Board:
    def __init__(self, size):
        self.size = size
        self.squares = self.makespiral(size)
        self.visited = numpy.full((size, size), False, dtype=bool)
        self.visited[int(numpy.floor(size / 2 - 1))][int(numpy.floor(size / 2 - 1))] = True
        self.piece = piece.Piece((int(numpy.floor(size / 2) - 1), int(numpy.floor(size / 2) - 1)), 'random')
        
        
        #print(self.squares)
        #print(sys.getrecursionlimit())
        #print(self.visited)
   
    def reinit(self, size):
        self.visited = numpy.full((size, size), False, dtype=bool)
        self.visited[int(numpy.floor(size / 2 - 1))][int(numpy.floor(size / 2 - 1))] = True
        self.piece.reinit((int(numpy.floor(size / 2) - 1), int(numpy.floor(size / 2) - 1)), 'random')

    def getnum(self, location):
        return self.squares[location[0]][location[1]]


    def makespiral(self, size):
        
         
        numbers = numpy.arange(1, size * size + 1)
        array = numbers.reshape(size, size)


        nrows, ncols = array.shape
        idx = numpy.arange(nrows * ncols).reshape(nrows, ncols)[::-1]
        spiral_idx = []
        while idx.size:
            spiral_idx.append(idx[0])

            idx = idx[1:]

            idx = idx.T[::-1]

        spiral_idx = numpy.hstack(spiral_idx)

        spiral = numpy.empty_like(array)
        spiral.flat[spiral_idx] = array.flat[::-1]
        return spiral





