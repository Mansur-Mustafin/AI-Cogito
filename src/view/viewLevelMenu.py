from view.viewMenu import ViewMenu
from model.levelMenu import *
from theme import *
from  .consts import *

class ViewLevelMenu(ViewMenu):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, menu: LevelMenu) -> None:
        """
        Draws the level Menu
        :param menu: Menu to draw
        :type menu: LevelMenu
        :return: None
        """

        #n_buttons_column = int((HEIGHT - y - 25) / (H_BUTTON + 10))
        buttons = menu.get_buttons()
        mouse_pos = menu.get_mouse_position()
        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)

        for button in buttons:
            self.draw_button( button, mouse_pos)

 
        self.draw_text("Choose level difficulty:", (2 * OFFSET, 2 * OFFSET), 50)
