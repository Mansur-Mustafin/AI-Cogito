from view.view import View
from model.levelMenu import *
from model.endMenu import EndMenu


class ViewEndMenu(View):
    """
    This class is responsible for drawing the end menu screen in the game.
    """

    def __init__(self, screen):
        """
        Initializes the ViewEndMenu with the specified Pygame screen.

        :param screen: The Pygame screen to render elements on.
        :type screen: pygame.Surface
        """
        super().__init__(screen)

    def draw_screen(self, menu: EndMenu) -> None:
        """
        Renders the end menu screen

        :param menu: Menu to draw
        :type menu: EndMenu
        :return: None
        """
        x = (WIDTH - W_BUTTON) / 2
        y = 450
        n_buttons_column = int((HEIGHT - y - 25) / (H_BUTTON + 10))
        buttons = menu.get_buttons()

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, WHITE_COLOR)

        self.draw_rectangle((WIDTH - 21 * 30) / 2 - 30, 2 * OFFSET - 15, 21 * 30 + 35, 650, 25, BACKGROUND_COLOR)

        while buttons:
            for i in range(min(n_buttons_column, len(buttons))):
                button = buttons[i]
                button.draw(self.screen, x, y, menu.get_mouse_position())
                y += 60

            x += W_BUTTON * 0.8
            y = 150
            buttons = buttons[min(n_buttons_column, len(buttons)):]

        score = "Score: " + str(menu.level.score)
        time = f"Time: {str(menu.level.time)[0:7]}s"
        if menu.level.is_win_condition():
            self.draw_text("You have won the game", ((WIDTH - 21 * 30) / 2, 2 * OFFSET), 50)
        else:
            self.draw_text("You have lost the game", ((WIDTH - 21 * 30) / 2, 2 * OFFSET), 50)
        self.draw_text(score, ((WIDTH - W_BUTTON) / 2, 300), 30)
        self.draw_text(time, ((WIDTH - W_BUTTON) / 2, 350), 30)
