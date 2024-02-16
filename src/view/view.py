from abc import ABC, abstractmethod
import pygame

from settings import *

class View(ABC):
    def __init__(self, screen):
        self.screen = screen

    @abstractmethod
    def draw_screen(self):
        pass

    def draw_rectangle(self, x, y, width, height, border_radius, color):
        rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, color, rect, border_radius=border_radius)

    def draw_text(self, text, position, font_size, color=BLACK_COLOR, font_path=FONT_PATH):
        if font_path:
            font = pygame.font.Font(font_path, font_size)
        else:
            font = pygame.font.SysFont('Arial', font_size)

        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def getScreen(self):
        return self.screen

