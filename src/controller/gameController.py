import pygame, sys

from controller.controller import Controller


class GameController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)
    
    def handle_event(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                print("QUIT")
                return True
            
            elif event.type == pygame.KEYDOWN:
                self.__handle_keydown(event.key)
                return self.state.isWinCondition()
            
            else: return False

    def __handle_keydown(self, key):
        if key in self.KEY_DIRECTIONS:
            self.state.processMove(self.KEY_DIRECTIONS[key])
