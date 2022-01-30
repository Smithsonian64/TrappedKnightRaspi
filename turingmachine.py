import pygame
import random
import numpy
import head
import time

class TuringMachine:
    def __init__(self, screensize, screen):
        symbols = numpy.array(
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', '>'])
        states = numpy.array(['store', 'left', 'write', 'right', 'next', 'print'])

        tape = numpy.full(1000, 0, dtype='U')

        percentage = random.randint(0, 100)

        self.screen = screen

        for i in range(len(tape)):
            tape[i] = symbols[random.randint(0, len(symbols) - 1)]
            if random.randint(0, 100) <= percentage:
                tape[i] = '>'

        print(tape)

        self.head = head.Head(screen, symbols, states, tape)



    def runmachine(self):
        duration = random.randint(5, 15)
        starttime = time.time()
        print(duration)
        while True:
            head.Head.runTape(self.head)
            if time.time() - starttime > duration:
                self.screen.fill((0, 0, 0))
                pygame.display.update()
                break




