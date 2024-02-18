import pygame
from view.view import View
from model.levelMenu import *
from theme import *
from  .consts import *

class ViewMenu(View):
    def __init__(self, screen):
        super().__init__(screen)


    """
    Draws the button
    :param screen: the screen where the button is going to be drawn
    :param x_pos: the horizontal position of the button
    :type x_pos: Int
    :param y_pos: the vertical position of the button
    :type y_pos: int
    :param mouse_pos: the position of the mouse
    :type mouse_pos: Tuple[Int,Int]
    :return: None
    """

    def draw_button(self, button:Button, mouse_pos: tuple[int, int]) -> None:

        if button.is_over(mouse_pos):
            button_color = button.text_color
            text_color = button.color
        else:
            button_color = button.color
            text_color = button.text_color

        # Draw the button rectangle
        rect = pygame.Rect(button.x, button.y, button.width, button.height)
        pygame.draw.rect(self.screen, button_color, rect, border_radius=R_BUTTON)

        # Draw the text on the button
        if button.text != '':
            text_surface = button.font.render(button.text, True, text_color)
            self.screen.blit(text_surface, (button.x + (button.width - text_surface.get_width()) / 2,
                                       button.y + (button.height - text_surface.get_height()) / 2))
