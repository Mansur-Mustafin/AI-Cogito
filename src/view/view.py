from abc import ABC, abstractmethod
import pygame

class View(ABC):
    def __init__(self, screen):
        self.screen = screen

    @abstractmethod
    def draw_screen(self):
        pass

    def draw_rectangle(self, x, y, width, height, border_radius, color):
        rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, color, rect, border_radius=border_radius)

