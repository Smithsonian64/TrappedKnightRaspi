import numpy

class Piece:
    
    def __init__(self, start):
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                (-2, -1), (-1, -2), (1, -2), (2, -1)]
        print(start)
        self.location = start



