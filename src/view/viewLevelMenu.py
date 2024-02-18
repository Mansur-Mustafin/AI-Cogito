import pygame
from view.view import View
from settings import *
from model.levelMenu import *

class ViewLevelMenu(View):
    def __init__(self, screen):
        super().__init__(screen)

    '''
    Draws the level Menu
    :param menu: Menu to draw
    :type menu: LevelMenu
    :return: None 
    '''
    def draw_screen(self, menu:LevelMenu) -> None:
        x = 25
        y = 150
        n_buttons_column = int ((HEIGHT - y - 25) / (H_BUTTON + 10))
        buttons = menu.getButtons()

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)
        
        while buttons != []:
            for i in range(min(n_buttons_column, len(buttons))):
                button = buttons[i]
                button.draw(self.screen, x, y, menu.getMousePosition())
                y += 60
                
            x += W_BUTTON * 0.8
            y = 150
            buttons = buttons[min(n_buttons_column, len(buttons)):]
        
        self.draw_text("Choose level difficulty:", (2*OFFSET, 2*OFFSET), 50)

