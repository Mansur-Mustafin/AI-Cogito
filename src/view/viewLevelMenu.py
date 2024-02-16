import pygame
from view.view import View
from settings import *

class ViewLevelMenu(View):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, menu):
        x = 25
        y = 50
        n_buttons_column = int ((HEIGHT - 50) / (H_BUTTON + 60))
        buttons = menu.getButtons()

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)
        
        while buttons != []:
            for i in range(min(n_buttons_column, len(buttons))):
                button = buttons[i]
                if button.is_over(menu.getMousePosition()):
                    button.draw(self.screen, x, y, True)
                else :
                    button.draw(self.screen, x, y)
                y += 60
            x += W_BUTTON
            y = 50
            buttons = buttons[min(n_buttons_column, len(buttons)):]

