import board
import piece
import pygame
import numpy
import time
import sys
from pygame.locals import *
import trappedknight

screensize = (800, 480)


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(screensize)
    screen.fill((0, 0, 0))
    pygame.display.update()

    tk = trappedknight.TrappedKnight((800, 480), screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        tk.makemoves()
        tk.drawgrid()
        tk.reinit()

        # pygame.display.update()

    pygame.quit()
    sys.exit(0)

    # pygame.draw.rect(screen, BLUE, (0, 0, 100, 100))


if __name__ == "__main__":
    main()
