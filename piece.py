import numpy
import random

class Piece:
    
    def __init__(self, start, type):
        self.moves = []
        if type == 'default':
            self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                    (-2, -1), (-1, -2), (1, -2), (2, -1)]
        if type == 'random':
            for i in range(8):
                #print('hello')
                self.moves.append((random.randint(-2, 2), random.randint(-2, 2)))
                
        #print(start)
        self.location = start

    def reinit(self, start, type):
        self.moves = []
        if type == 'default':
            self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                    (-2, -1), (-1, -2), (1, -2), (2, -1)]
        if type == 'random':
            for i in range(8):
                #print('hello')
                self.moves.append((random.randint(-2, 2), random.randint(-2, 2)))
                
        #print(start)
        self.location = start



