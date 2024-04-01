from abc import ABC, abstractmethod

import pygame

from settings import *


class View(ABC):
    """
    An abstract base class representing the view in a game.

    Attributes:
        ----------
        screen (pygame.Surface): The main display surface where elements are rendered.
        map_Color (dict): A mapping of color codes to their corresponding RGB values.
    """

    map_Color = {
        'r': RED_COLOR,
        'b': BLUE_COLOR,
        'y': YELLOW_COLOR
    }

    def __init__(self, screen):
        """
        Initializes the View with the specified Pygame screen.

        :param screen: The Pygame screen to render elements on.
        :type screen: pygame.Surface
        """
        self.screen = screen

    @abstractmethod
    def draw_screen(self, state):
        """
        Abstract method to draw the screen. Must be implemented by subclasses.

        :param state: The state of the game to be represented on the screen.
        :return: None
        """
        pass

    def draw_rectangle(self, x: int, y: int, width: int, height: int, border_radius: int,
                       color: tuple[int, int, int]) -> None:
        """
        Draws a rectangle

        :param x: Horizontal position of the top left vertex
        :type x: Int
        :param y: Vertical position of the top left vertex
        :type y: Int
        :param width: Width of the rectangle
        :type width: Int
        :param height: Height of the rectangle
        :type height: Int
        :param border_radius: The radius of the border of the rectangle
        :type border_radius: Int
        :param color: Color of the rectangle represented as a tuple os 3 Ints representing the rgb
        :type color: Tuple[Int,Int,Int]
        :return: None
        """
        rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, color, rect, border_radius=border_radius)

    def draw_text(self, text: str, position: tuple[int, int], font_size: int, color: tuple[int, int, int] = BLACK_COLOR,
                  font_path: str = FONT_PATH) -> None:
        """
        Draws text

        :param text: String text to draw
        :type text : String
        :param position: Position of the text in the screen
        :type position : Tuple[Int,Int]
        :param font_size: Size of the text
        :type font_size : Int
        :param color: Color of the text represented as a tuple os 3 Ints representing the rgb
        :type color : Tuple[int,int,int]
        :param font_path: font of the text to use
        :type font_path : String
        :return: void
        """
        try:
            font = pygame.font.Font(font_path, font_size)
        except Exception as e:
            print(f"[ERROR] loading font: {e}")
            font = pygame.font.SysFont('Arial', font_size)

        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_square_board(self, x: int, y: int, square: dict[tuple[int, int], chr], dimension: int, scale: float = 1) -> None:
        """
        Draws a square board

        :param x: Horizontal position in the screen
        :type x: Int
        :param y: Vertical of the text in the screen
        :type y: Int
        :param square: Board to draw
        :type square: dict[tuple[int, int], chr]
        :param dimension: The dimension of the board (e.g., 8 for 8x8 board).
        :type dimension: Int
        :param scale: Adjust the size of pieces for available space
        :type scale: Float
        :return: void
        """
        x_gap = scale * W_SQUARE + GAP
        y_gap = scale * H_SQUARE + GAP

        for i in range(dimension):
            for j in range(dimension):

                tile = square.get((j, i), 'y')
                if tile is None:
                    continue

                tile_color = self.map_Color.get(tile, BLACK_COLOR)

                self.draw_rectangle(x + i * x_gap, y + j * y_gap, scale * W_SQUARE, scale * H_SQUARE, R_SQUARE,
                                    tile_color)

    def get_screen(self):
        """
        Returns the Pygame screen.

        :return: The current Pygame screen.
        :rtype: pygame.Surface
        """
        return self.screen
