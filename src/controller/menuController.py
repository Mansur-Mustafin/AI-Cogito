import pygame, sys

from controller.controller import Controller


class MenuController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)
    
    def handle_event(self):
        pass

    def handle_mouse_motion(self, new_pos):
        self.state.update_mouse_position(new_pos)


class MainMenuController(MenuController):

    def __init__(self, state, view):
        super().__init__(state, view)
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                print("QUIT")
                return True
            
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event.pos)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = self.state.getPressedButton()

                if button is None : return False

                print(button)
                return False


class LevelMenuController(MenuController):

    def __init__(self, state, view):
        super().__init__(state, view)
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                print("QUIT")
                return True
            
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event.pos)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = self.state.getPressedButton()

                if button is None : return False

                print(button)
                return False