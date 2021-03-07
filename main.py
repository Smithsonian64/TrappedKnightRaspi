import board
import piece
import pygame
import numpy
import time
import sys
from pygame.locals import *

width = 800
height = 480
size = 100
delay = 0.00
xoffset = 1 
yoffset = numpy.rint((height / width) * xoffset)


value = numpy.empty((), dtype=object)
value[()] = (0, 0)
screencoords = numpy.full((size, size), value, dtype=object)

b = board.Board(size)

screen = pygame.display.set_mode((width, height))

def drawgrid():
    
    xinterval = (width - xoffset * 2) / (size - 1)
    yinterval = (height - yoffset * 2) / (size - 1)
    
    for i in range(len(b.squares)):
        for j in range(len(b.squares[0])):
            x = numpy.rint(xoffset + i * xinterval)
            y = numpy.rint(yoffset + j * yinterval)
            screencoords[i][j] = (x, y)
            #pygame.draw.rect(screen, (255, 255, 255), (x, y, 1, 1))

def makemove():
    lastlocation = b.piece.location
    lowestmove = b.piece.location
    lowestnumber = -1
    for i in range(len(b.piece.moves)):
        testx = b.piece.moves[i][0] + lastlocation[0]
        testy = b.piece.moves[i][1] + lastlocation[1]

        
        
        if b.squares[testx][testy] < lowestnumber or lowestnumber == -1:
            if b.visited[testx][testy] == False:
                lowestnumber = b.squares[testx][testy]
                lowestmove = (testx, testy)
    
    if lowestnumber == -1:
        return


    b.piece.location = lowestmove
    b.visited[lowestmove[0]][lowestmove[1]] = True
    print('moved from', b.getnum(lastlocation), 'to', b.getnum(lowestmove))
    pygame.draw.line(screen, (255,0,0), screencoords[lastlocation[0]][lastlocation[1]], screencoords[b.piece.location[0]][b.piece.location[1]])
    time.sleep(delay)


def main():

    pygame.init()

    screen.fill((0,0,0))
   
    drawgrid()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        #pygame.draw.rect(screen, (0, 0, 255) ,(100, 100, 100, 100))
        makemove()
        pygame.display.update()

    pygame.quit()
    sys.exit(0)
        
        #pygame.draw.rect(screen, BLUE, (0, 0, 100, 100))

        
    



if __name__ == "__main__":
    main()

