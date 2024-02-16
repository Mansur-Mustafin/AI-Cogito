import pygame
from view.view import View
from settings import *

class ViewMenu(View):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, menu):
        center_x = (WIDTH - W_BUTTON) / 2 

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, (255, 255, 255))

        for button in menu.getButtons():
            button.draw(self.screen, center_x, 100)
