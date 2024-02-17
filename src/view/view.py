from abc import ABC, abstractmethod
import pygame

from settings import *

class View(ABC):

    map_Color = {
        'r' : RED_COLOR,
        'b' : BLUE_COLOR,
        'y' : YELLOW_COLOR
    }

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

    def draw_square_board(self, x, y, x_gap, y_gap, square, scale = 1):
        
        # TODO check is state is Level!
        dimension = len(square)

        for i in range(dimension):
            for j in range(dimension):

                tile = square[j][i]

                if tile is None: continue

                tile_color = self.map_Color.get(tile, BLACK_COLOR)

                self.draw_rectangle(x + i*x_gap, y + j*y_gap, scale*W_SQUARE, scale*H_SQUARE, R_SQUARE, tile_color)


    def getScreen(self):
        return self.screen

