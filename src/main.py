import pygame, sys
from settings import *
from level import Level
from controller import Controller
from analitics import *


class Game:

    def __init__(self) -> None:

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Amado Game')
        self.clock = pygame.time.Clock()
        self.controller = Controller(Level(1))

    def run(self):
        run = True
        while run:
            run = not measureTime(self.controller.move)
            
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()