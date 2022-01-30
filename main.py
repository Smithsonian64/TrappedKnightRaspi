import tkboard
import piece
import pygame
import numpy
import time
import sys
from pygame.locals import *
import trappedknight
import langtonsant
import gameoflife
import turingmachine
import random

screensize = (800, 480)


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(screensize)
    screen.fill((0, 0, 0))
    pygame.display.update()

    #tk = trappedknight.TrappedKnight((800, 480), screen)
    #la = langtonsant.LangtonsAnt((800, 480), screen, 'RRLLLRLLLRRR')
    #gol = gameoflife.GameOfLife((800, 480), screen)
    #tm = turingmachine.TuringMachine((800, 480), screen)

    running = True

    while running:
        index = random.randint(0, 3)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        if index == 0:
            tk = trappedknight.TrappedKnight((800, 480), screen)
            tk.makemoves()
        elif index == 1:
            la = langtonsant.LangtonsAnt((800, 480), screen, 'RRLLLRLLLRRR')
            la.makemoves()
        elif index == 2:
            gol = gameoflife.GameOfLife((800, 480), screen)
            gol.makemoves()
        elif index == 3:
            tm = turingmachine.TuringMachine((800, 480), screen)
            tm.runmachine()


        # pygame.display.update()

    pygame.quit()
    sys.exit(0)

    # pygame.draw.rect(screen, BLUE, (0, 0, 100, 100))


if __name__ == "__main__":
    main()
