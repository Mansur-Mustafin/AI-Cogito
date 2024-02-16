import pygame
from settings import *

class Button:
    def __init__(self, width, height, text='', color=(73, 73, 73), text_color=(255, 255, 255), font_size=30):
        self.x = None
        self.y = None
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, font_size)

    def __str__(self) -> str:
        return self.text

    def draw(self, screen, x_pos, y_pos, mouse_pos):
        self.x = x_pos
        self.y = y_pos

        if self.is_over(mouse_pos):
            button_color = self.text_color
            text_color = self.color
        else :
            button_color = self.color 
            text_color = self.text_color

        # Draw the button rectangle
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, button_color, rect, border_radius=R_BUTTON)

        # Draw the text on the button
        if self.text != '':
            text_surface = self.font.render(self.text, True, text_color)
            screen.blit(text_surface, (self.x + (self.width - text_surface.get_width()) / 2, self.y + (self.height - text_surface.get_height()) / 2))

    def is_over(self, pos):
        if self.x is None : return False

        # Pos is the mouse position as a tuple (x, y)
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False