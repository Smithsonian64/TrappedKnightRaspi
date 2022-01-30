import pygame
import time
import random

class Head:
    def __init__(self, screen, symbols, states, tape):
        self.screen = screen
        self.symbols = symbols
        self.states = states
        self.tape = tape
        self.tapeIndex = 0
        self.stateIndex = 0
        self.register = ''
        self.currentState = ''

        self.tapeSlice = ''

        self.output = ''

        fontpath = "FreeMono.ttf"

        self.font = pygame.font.Font(fontpath, 30)
        self.font1 = pygame.font.Font(fontpath, 20)

    # 'store', 'write', 'stop', 'left', 'right', 'next', 'previous', 'print'

    def runTape(self):

        self.currentState = self.states[self.stateIndex]
        while True:

            if self.tape[self.tapeIndex] == '>':
                self.executeNext()
                # print(self.currentState)
                return

            if self.tape[self.tapeIndex] == '<':
                self.executePrevious()
                # print(self.currentState)
                return

            if self.currentState == 'store':
                self.executeStore()
            if self.currentState == 'write':
                self.executeWrite()
            if self.currentState == 'left':
                self.executeLeft()
            if self.currentState == 'right':
                self.executeRight()
            if self.currentState == 'next':
                self.executeNext()
            if self.currentState == 'print':
                self.executePrint()

            # print(self.tapeIndex)
            # print(self.tape.size)

            # print(self.currentState)
            # print(self.register)

            text = pygame.font.Font.render(self.font, 'current state: ' + self.currentState, 1, (255, 255, 255))
            text1 = pygame.font.Font.render(self.font1, 'output: ' + str(self.output), 1, (255, 255, 255))
            text2 = pygame.font.Font.render(self.font, 'Head read: ' + self.tape[self.tapeIndex], 1, (255, 255, 255))
            self.getTapeSlice()
            text3 = pygame.font.Font.render(self.font, self.tapeSlice, 1, (255, 255, 255))
            self.screen.fill((0, 0, 0))
            pygame.Surface.blit(self.screen, text, (0, 0))
            pygame.Surface.blit(self.screen, text2, (0, 50))
            pygame.Surface.blit(self.screen, text1, (0, 100))
            pygame.Surface.blit(self.screen, text3, (0, 250))

            pygame.draw.rect(self.screen, (0, 255, 255), (323, 250, 20, 30), 2)

            pygame.display.update()
            #time.sleep(1000)

            #print(self.tape)


    def executeStore(self):
        self.register = self.tape[self.tapeIndex]
        self.executeRight()

    def executeWrite(self):
        self.tape[self.tapeIndex] = self.register
        self.executeRight()
        self.executeNext()

    def executeLeft(self):
        if self.tapeIndex == 0:
            self.tapeIndex = self.tape.size - 1
        else:
            self.tapeIndex -= 1

    def executeRight(self):
        if self.tapeIndex + 1 == self.tape.size:
            self.tapeIndex = 0
        else:
            self.tapeIndex += 1

    def executeNext(self):
        if self.stateIndex + 1 == self.states.size:
            self.stateIndex = 0
        else:
            self.stateIndex += 1

        self.currentState = self.states[self.stateIndex]
        self.executeRight()

    def executePrevious(self):
        if self.stateIndex == 0:
            self.stateIndex = self.states.size - 1
        else:
            self.stateIndex -= 1

        self.currentState = self.states[self.stateIndex]
        self.executeRight()

    def executePrint(self):
        if len(self.output) >= 50:
            self.output = ''
        # print(self.register)
        self.executeRight()
        self.output += self.register
        self.executeNext()

    def getTapeSlice(self):
        self.tapeSlice = ''
        for i in range(self.tapeIndex - 19, self.tapeIndex + 19):
            if i < 0:
                self.tapeSlice += self.tape[len(self.tape) + i]
            elif i >= len(self.tape):
                self.tapeSlice += self.tape[len(self.tape) - i]
            else:
                self.tapeSlice += self.tape[i]
