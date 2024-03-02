from view.view import View
from settings import *
from model.mainMenu import MainMenu
from .componets.buttons import *

class ViewMainMenu(View):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, menu: MainMenu) -> None:
        """
        Draws the Main Menu
        :param menu: Menu to draw
        :type menu: MainMenu
        :return: None
        """
        center_x = (WIDTH - W_BUTTON) / 2 - 400  # 400 - offset
        y = 150
        mouse_pos = menu.get_mouse_position()
        buttons = menu.get_buttons()

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)
        draw_button(buttons[0], self.screen, mouse_pos, center_x, y )
    

        y += 200

        for button in buttons[1:]:
            draw_button(button, self.screen,mouse_pos, center_x, y )
            #button.draw(self.screen, center_x, y, mouse_pos)
            y += 60

        self.draw_text("Cogito Game", (WIDTH * 0.55, 2 * OFFSET), 50)

        w_square = 150
        # super mal
        self.draw_rectangle(WIDTH * 0.55, 2 * OFFSET + 100, w_square, w_square, 18, BLUE_COLOR)
        self.draw_rectangle(WIDTH * 0.55 + w_square, 2 * OFFSET + 100 + w_square, w_square, w_square, 18, RED_COLOR)
        self.draw_rectangle(WIDTH * 0.55 + 2 * w_square, 2 * OFFSET + 100 + 2 * w_square, w_square, w_square, 18, YELLOW_COLOR)
