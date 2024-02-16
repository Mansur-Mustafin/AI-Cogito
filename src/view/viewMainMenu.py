import pygame
from view.view import View
from settings import *

class ViewMainMenu(View):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, menu):
        center_x = (WIDTH - W_BUTTON) / 2 - 400 # 400 - offset
        y = 150
        mouse_pos = menu.getMousePosition()
        buttons = menu.getButtons()

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)

        buttons[0].draw(self.screen, center_x, y, mouse_pos) # Jogar button

        y += 200

        for button in buttons[1:]:
            button.draw(self.screen, center_x, y, mouse_pos)
            y += 60
        
        self.draw_text("Amado Game", (WIDTH * 0.55, 2*OFFSET), 50)

        w_square = 150
        # super mal
        self.draw_rectangle(WIDTH * 0.55, 2*OFFSET + 100, w_square, w_square, 18, BLUE_COLOR)
        self.draw_rectangle(WIDTH * 0.55 + w_square, 2*OFFSET + 100 + w_square, w_square, w_square, 18, RED_COLOR)
        self.draw_rectangle(WIDTH * 0.55 + 2*w_square, 2*OFFSET + 100 + 2*w_square, w_square, w_square, 18, YELLOW_COLOR)
    