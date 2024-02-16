from model.button import Button
from settings import *

class Menu:

    def __init__(self):
        self.buttons = []
        self.__createButtons()
        self.mouse_pos = (WIDTH/2, HEIGHT/2)

    def __createButtons(self):
        self.buttons.append(
            Button(W_BUTTON, H_BUTTON, "Jogar", WHITE_COLOR, BLUE_COLOR, 20)
        )

    def getButtons(self):
        return self.buttons
    
    def move_mouse(self, d_x, d_y):
        new_x = self.mouse_pos[0] + d_x
        new_y = self.mouse_pos[1] + d_y
        self.update_mouse_position(new_x, new_y)


    def update_mouse_position(self, new_x, new_y):
        if self.__isValidPosition(new_x, new_y):
            self.mouse_pos = (new_y, new_x)

    def __isValidPosition(self, x, y):
        return 0 <= x < WIDTH and 0 <= y < HEIGHT