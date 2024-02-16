import pygame
from view.view import View
from settings import *

class ViewMainMenu(View):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, menu):
        center_x = (WIDTH - W_BUTTON) / 2 - 400 # 400 - offset
        y = 150
        buttons = menu.getButtons()

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)

        buttons[0].draw(self.screen, center_x, y) # Jogar button
        y += 200

        for button in buttons[1:]:
            if button.is_over(menu.getMousePosition()):
                button.draw(self.screen, center_x, y, True)
            else :
                button.draw(self.screen, center_x, y)
            
            y += 60
