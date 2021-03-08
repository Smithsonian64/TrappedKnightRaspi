import board
import piece
import pygame
import numpy
import time
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()

width = 800
height = 480
size = 100
delay = 0.00
xoffset = 1 
yoffset = numpy.rint((height / width) * xoffset)

pygame.mouse.set_visible(False)

value = numpy.empty((), dtype=object)
value[()] = (0, 0)
screencoords = numpy.full((size, size), value, dtype=object)

b = board.Board(size)

origin = b.piece.location

screen = pygame.display.set_mode((width, height))

fontpath = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"


font = pygame.font.Font(fontpath, 30)

def drawgrid():
    
    xinterval = (width - xoffset * 2) / (size - 1)
    yinterval = (height - yoffset * 2) / (size - 1)
    
    for i in range(len(b.squares)):
        for j in range(len(b.squares[0])):
            x = numpy.rint(xoffset + i * xinterval)
            y = numpy.rint(yoffset + j * yinterval)
            screencoords[i][j] = (x, y)
            #pygame.draw.rect(screen, (255, 255, 255), (x, y, 1, 1))

def makemoves():
    print(b.piece.location)
    while True:
        lastlocation = b.piece.location
        lowestmove = b.piece.location
        lowestnumber = -1
        for i in range(len(b.piece.moves)):
            testx = b.piece.moves[i][0] + lastlocation[0]
            testy = b.piece.moves[i][1] + lastlocation[1]

        
       
            if testx >= 100 or testx < 0 or testy >= 100 or testy < 0:
                continue

            if b.squares[testx][testy] < lowestnumber or lowestnumber == -1:
                if b.visited[testx][testy] == False:
                    lowestnumber = b.squares[testx][testy]
                    lowestmove = (testx, testy)
    
        
        if lowestnumber == -1:
            pygame.draw.circle(screen, (0, 255, 0), onscreen(origin), 4)
            pygame.draw.circle(screen,(255, 0, 0), onscreen(lowestmove), 4)
            
            if b.piece.location[0] == size - 1 or b.piece.location[0] == 0 or b.piece.location[1] == size - 1 or b.piece.location[1] == 0:
                text = pygame.font.Font.render(font, 'Trapped by edge!', 1, (255, 255, 255))
            else:
                text = pygame.font.Font.render(font, 'Trapped at square ' + str(b.getnum(lowestmove)), 1, (255, 255, 255))
            pygame.Surface.blit(screen, text, (0, 0))
            pygame.display.update()
            time.sleep(1)
            break



        b.piece.location = lowestmove
        b.visited[lowestmove[0]][lowestmove[1]] = True
        print('moved from', b.getnum(lastlocation), 'to', b.getnum(lowestmove))
        pygame.draw.line(screen, (255,0,255), screencoords[lastlocation[0]][lastlocation[1]], screencoords[b.piece.location[0]][b.piece.location[1]])
        time.sleep(delay)
        pygame.display.update()

    return

def onscreen(x):
    temp = screencoords[x[0]][x[1]]
    return (int(temp[0]), int(temp[1]))

def reinit():
    b.reinit(size)
    b.piece.location = (49, 49)
    lastlocation = (49, 49)
    origin = b.piece.location

    screen.fill((0,0,0))
    pygame.display.update()

def main():


    text = pygame.font.Font(fontpath, 30)
    screen.fill((0,0,0))
   
    drawgrid()
    running = True
    makemoves()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        #pygame.draw.rect(screen, (0, 0, 255) ,(100, 100, 100, 100))
        
        makemoves()
        reinit()
        
        #pygame.display.update()

    pygame.quit()
    sys.exit(0)
        
        #pygame.draw.rect(screen, BLUE, (0, 0, 100, 100))

        
    



if __name__ == "__main__":
    main()

