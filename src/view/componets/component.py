from .styles import *
import pygame

class Component ():
    def __init__(self,width =0 ,height = 0, style: Styles = Styles({}), x = None, y = None) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.styles = style
        self.apply_styles()

    def apply_styles (self):
        for align in self.styles.aligns:
            ALIGNS[align](self)

        for float, dv in self.styles.floats:
            FLOATS[float](self, dv)

    def draw(self, screen):
        self.draw_rectangle(screen,self.x, self.y, self.width, self.height, self.styles.border, self.styles.background)

    def draw_rectangle(self,screen, x: int, y: int, width: int, height: int, border_radius: int,
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
        pygame.draw.rect(screen, color, rect, border_radius=border_radius)
    
