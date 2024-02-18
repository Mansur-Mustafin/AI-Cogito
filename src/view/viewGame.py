from view.view import View
from settings import *


class ViewGame(View):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, level: int) -> None:
        """
        Draws the game screen
        :param level: The level to draw
        :type level: Level
        :return: None
        """
        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)
        self.draw_right_menu(level)
        self.draw_current_board(level)

    def draw_right_menu(self, level: int) -> None:
        """
        Draws the right menu of the game screen
        :param level: The level to draw
        :type level: Level
        :return: None
        """

        # background of right menu
        self.draw_rectangle(X_LEFT_MENU, Y_LEFT_MENU, W_LEFT_MENU, H_LEFT_MENU, R_LEFT_MENU, WHITE_COLOR)

        # 3 examples colors
        self.draw_rectangle(X_3COLORS, Y_3COLORS, W_SQUARE, H_SQUARE, R_SQUARE, RED_COLOR)
        self.draw_rectangle(X_3COLORS + GAP + W_SQUARE, Y_3COLORS, W_SQUARE, H_SQUARE, R_SQUARE, BLUE_COLOR)
        self.draw_rectangle(X_3COLORS + 2 * (GAP + W_SQUARE), Y_3COLORS, W_SQUARE, H_SQUARE, R_SQUARE, YELLOW_COLOR)

        # score
        self.draw_text(f"Score: {str(level.get_score())}", (X_3COLORS + 5 * W_SQUARE, Y_3COLORS), H_SQUARE)

        # Missmatch ties
        number_in_line = int((W_LEFT_MENU - 40) / (W_MISS + GAP))
        number_misses = level.count_mismatched_tiles()
        x_start = X_LEFT_MENU + OFFSET
        y_start = Y_LEFT_MENU + H_LEFT_MENU - OFFSET - H_MISS
        while number_misses > 0:
            for i in range(number_in_line):
                self.draw_rectangle(x_start + i * (GAP + W_MISS), y_start, W_MISS, H_MISS, R_MISS, GREEN_COLOR)
                number_misses -= 1
                if number_misses == 0: break
            y_start -= 2 * GAP + H_MISS

        # target board
        self.draw_target_board(level)

        # instructions
        self.draw_text(f"Use ← ↑ ↓ → to move", (X_LEFT_MENU + OFFSET, HEIGHT / 2 + 2 * OFFSET), 25)

    def draw_target_board(self, level: int) -> None:
        """
        Draws the target board
        :param level: The level to draw
        :type level: Level
        :return: None
        """
        x_gap = W_SQUARE + GAP
        y_gap = H_SQUARE + GAP
        x_start = X_LEFT_MENU + (W_LEFT_MENU / 2 - level.get_dimension() * x_gap / 2) + GAP / 2
        y_start = Y_LEFT_MENU + (H_LEFT_MENU / 2 + level.get_dimension() * y_gap / 2) * 0.4

        self.draw_square_board(x_start, y_start, level.get_target_board())

    def draw_current_board(self, level: int) -> None:
        """
        Draws the current board
        :param level: The level to draw
        :type level: Level
        :return: None
        """
        scale = ((min(HEIGHT, WIDTH) - 2 * OFFSET) / ((H_SQUARE + GAP) * level.get_dimension()))
        x_gap = scale * W_SQUARE + GAP
        y_gap = scale * H_SQUARE + GAP
        x_start = (WIDTH - W_LEFT_MENU - 2 * OFFSET) / 2 - (level.get_dimension() * x_gap) / 2
        y_start = HEIGHT / 2 - (level.get_dimension() * y_gap) / 2

        # draw selected square
        i, j = level.get_position()
        self.draw_rectangle(x_start + i * x_gap - 3, y_start + j * y_gap - 3, scale * W_SQUARE + 6,
                            scale * H_SQUARE + 6, R_SQUARE, GREEN_COLOR)

        # draw the board
        self.draw_square_board(x_start, y_start, level.get_current_board(), scale)
