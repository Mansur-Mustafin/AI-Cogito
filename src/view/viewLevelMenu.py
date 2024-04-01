from view.view import View
from model.levelMenu import *


class ViewLevelMenu(View):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, menu: LevelMenu) -> None:
        """
        Draws the level Menu
        :param menu: Menu to draw
        :type menu: LevelMenu
        :return: None
        """
        buttons = menu.get_buttons()
        col_width = WIDTH / 4
        col_height = 6*OFFSET + 6*H_BUTTON +100

        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)




        self.draw_rectangle( OFFSET, 6 * OFFSET, col_width- 2*OFFSET, col_height, 10, WHITE_COLOR)
        self.draw_text("3x3", ( 2*OFFSET, 7 * OFFSET), 35)
        for i in range(5):
            buttons[i].draw( self.screen, 2*OFFSET, 10 * OFFSET + i*(H_BUTTON + OFFSET), menu.get_mouse_position())
        
        self.draw_rectangle( OFFSET + col_width, 6 * OFFSET, col_width- 2*OFFSET, col_height, 10, WHITE_COLOR)
        self.draw_text("6x6", ( 2*OFFSET + col_width, 7 * OFFSET), 35)
        for i in range(5):
            buttons[i+5].draw( self.screen, 2*OFFSET + col_width, 10 * OFFSET + i*(H_BUTTON + OFFSET), menu.get_mouse_position())
        
        self.draw_rectangle( OFFSET + 2* col_width, 6 * OFFSET, col_width - 2*OFFSET, col_height, 10, WHITE_COLOR)
        self.draw_text("9x9", ( 2*OFFSET + 2* col_width , 7 * OFFSET), 35)
        for i in range(5):
            buttons[i+10].draw( self.screen, 2*OFFSET + 2* col_width, 10 * OFFSET + i*(H_BUTTON + OFFSET), menu.get_mouse_position())
        
        self.draw_rectangle( OFFSET + 3* col_width, 6 * OFFSET, col_width- 2*OFFSET, col_height, 10, WHITE_COLOR)
        self.draw_text("For AI", ( 2*OFFSET + 3* col_width , 7 * OFFSET), 35)
        for i in range(6):
            buttons[i+15].draw( self.screen, 2*OFFSET + 3 *col_width, 10 * OFFSET + i*(H_BUTTON + OFFSET), menu.get_mouse_position())
        
        self.draw_text("Choose level:", (2 * OFFSET,  OFFSET), 50)
