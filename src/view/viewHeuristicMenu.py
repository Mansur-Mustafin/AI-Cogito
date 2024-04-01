from view.view import View
from model.levelMenu import *


class ViewHeuristicMenu(View):
    """
    This class is responsible for drawing the heuristic menu screen in the game.
    """
    def __init__(self, screen):
        """
        Initializes the ViewHeuristicMenu with the specified Pygame screen.

        :param screen: The Pygame screen to render elements on.
        :type screen: pygame.Surface
        """
        super().__init__(screen)

    def draw_screen(self, menu: LevelMenu) -> None:
        """
        Draws the level Menu

        :param menu: Menu to draw
        :type menu: LevelMenu
        :return: None
        """
        x = 25
        y = 150
        n_buttons_column = int((HEIGHT - y - 25) / (H_BUTTON + 10))
        buttons = menu.get_buttons()

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)

        while buttons:
            for i in range(min(n_buttons_column, len(buttons))):
                button = buttons[i]
                button.draw(self.screen, x, y, menu.get_mouse_position())
                y += 60

            x += W_BUTTON * 0.8
            y = 150
            buttons = buttons[min(n_buttons_column, len(buttons)):]

        self.draw_text("Choose heuristic for AI algorithm:", (2 * OFFSET, 2 * OFFSET), 50)
