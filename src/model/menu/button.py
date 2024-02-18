import pygame


class Button:
    def __init__(self, x, y, width, height, text='', color=(73, 73, 73), text_color=(255, 255, 255), font_size=30):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, font_size)

    def __str__(self) -> str:
        return self.text

   
    """
    Checks if the mouse is over the button
    :param mouse_pos: the position of the mouse
    :type mouse_pos: Tuple[Int,Int]
    :return: True if the mouse is over the button, false otherwise
    :rtype: Bool
    """

    def is_over(self, mouse_pos: tuple[int, int]) -> bool:
        if self.x is None: return False

        # Pos is the mouse position as a tuple (x, y)
        if self.x < mouse_pos[0] < self.x + self.width and \
                self.y < mouse_pos[1] < self.y + self.height:
            return True
        return False
