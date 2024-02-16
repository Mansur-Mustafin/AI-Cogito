import pygame, sys

from controller.controller import Controller

from view.viewGame import ViewGame
from view.viewLevelMenu import ViewLevelMenu
from view.viewMainMenu import ViewMainMenu

from model.mainMenu import MainMenu
from model.levelMenu import LevelMenu
from model.level import Level



class MenuController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                print("QUIT")
                return self.EXIT
            
            elif event.type == pygame.MOUSEMOTION:
                self.state.update_mouse_position(event.pos)
                return None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = self.state.getPressedButton()

                if button is None : return None
                else: return self.hadle_pressed_button(button)

    def hadle_pressed_button(self, button):
        pass




class MainMenuController(MenuController):

    def __init__(self, state, view):
        super().__init__(state, view)
 
    def hadle_pressed_button(self, button):
        if str(button) == "Jogar":
            self.state = LevelMenu()
            self.view = ViewLevelMenu(self.view.getScreen())
            return self.CHANGE_LEVEL
        else: 
            print("TODO: ", button)
            return False




class LevelMenuController(MenuController):

    def __init__(self, state, view):
        super().__init__(state, view)
    
    def hadle_pressed_button(self, button):
        lvl = str(button).split(' ')[1]
        self.state = Level(lvl)
        self.view = ViewGame(self.view.getScreen())
        return self.CHANGE_GAME
