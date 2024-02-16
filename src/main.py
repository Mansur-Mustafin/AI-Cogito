import pygame, sys
from settings import *
from model.level import Level
from view.viewGame import ViewGame
from view.viewLevelMenu import ViewLevelMenu
from view.viewMainMenu import ViewMainMenu
from model.mainMenu import MainMenu
from model.levelMenu import LevelMenu
from analitics import *
from controller import Controller

class Game:

    def __init__(self) -> None:

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Amado Game')
        self.clock = pygame.time.Clock()
        
        # self.state = Level(2)
        # self.view = ViewGame(self.screen)
        self.state = LevelMenu()
        self.view = ViewLevelMenu(self.screen)
        self.controller = Controller(Level(1))

    def run(self):
        run = True
        while run:
            run = not measureTime(self.controller.move)
            
            self.view.draw_screen(self.state)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()