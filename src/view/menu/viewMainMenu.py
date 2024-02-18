from view.menu.viewMenu import ViewMenu
from model.menu.menu import Menu
from theme import *
from  ..consts import *

class ViewMainMenu(ViewMenu):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, menu: Menu) -> None:
        """
        Draws the Main Menu
        :param menu: Menu to draw
        :type menu: MainMenu
        :return: None
        """
        mouse_pos = menu.get_mouse_position()
        buttons = menu.get_buttons()

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)

        for button in buttons:
            self.draw_button( button, mouse_pos)

        self.draw_text("Amado Game", (WIDTH * 0.55, 2 * OFFSET), 50)

        w_square = 150
        # super mal
        self.draw_rectangle(WIDTH * 0.55, 2 * OFFSET + 100, w_square, w_square, 18, BLUE_COLOR)
        self.draw_rectangle(WIDTH * 0.55 + w_square, 2 * OFFSET + 100 + w_square, w_square, w_square, 18, RED_COLOR)
        self.draw_rectangle(WIDTH * 0.55 + 2 * w_square, 2 * OFFSET + 100 + 2 * w_square, w_square, w_square, 18, YELLOW_COLOR)
