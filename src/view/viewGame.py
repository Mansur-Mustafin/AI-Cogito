import pygame
from view.view import View
from settings import *

class ViewGame(View):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_screen(self, level):
        self.draw_rectangle(0, 0, WIDTH, HEIGHT, 0, BACKGROUND_COLOR)
        self.draw_right_menu(level)
        
        self.drow_current_board(level)

    
    def draw_right_menu(self, level):
        # background of right menu
        self.draw_rectangle(X_LEFT_MENU, Y_LEFT_MENU, W_LEFT_MENU, H_LEFT_MENU, R_LEFT_MENU, WHITE_COLOR)

        # 3 exemples colors
        self.draw_rectangle(X_3COLORS, Y_3COLORS, W_SQUARE, H_SQUARE, R_SQUARE, RED_COLOR)
        self.draw_rectangle(X_3COLORS + GAP + W_SQUARE, Y_3COLORS, W_SQUARE, H_SQUARE, R_SQUARE, BLUE_COLOR)
        self.draw_rectangle(X_3COLORS + 2*(GAP + W_SQUARE), Y_3COLORS, W_SQUARE, H_SQUARE, R_SQUARE, YELLOW_COLOR)

        # Missmatch ties
        number_in_line = int ((W_LEFT_MENU - 40) / (W_MISS + GAP))
        number_misses = level.countMismatchedTiles()
        x_start = X_LEFT_MENU + OFFSET
        y_start = Y_LEFT_MENU + H_LEFT_MENU - OFFSET - H_MISS
        while(number_misses > 0):
            for i in range(number_in_line):
                self.draw_rectangle(x_start + i*(GAP + W_MISS), y_start, W_MISS, H_MISS, R_MISS, GREEN_COLOR)
                number_misses -= 1
                if number_misses == 0 : break
            y_start -= 2*GAP + H_MISS
        
        self.drow_target_board(level)
        

    def drow_target_board(self, level):
        x_gap = W_SQUARE + GAP
        y_gap = H_SQUARE + GAP
        x_start = X_LEFT_MENU + (W_LEFT_MENU / 2 - level.getDimension() * x_gap / 2) + GAP / 2
        y_start = Y_LEFT_MENU + (H_LEFT_MENU / 2 + level.getDimension() * y_gap / 2) * 0.4
        for i in range(level.getDimension()):
            for j in range(level.getDimension()):
                tile = level.getValueAtTarget(i, j)
                if tile is None:
                    continue
                elif tile == 'r':
                    tile_color = RED_COLOR
                elif tile == 'b':
                    tile_color = BLUE_COLOR
                elif tile == 'y':
                    tile_color = YELLOW_COLOR

                self.draw_rectangle(x_start + i*x_gap, y_start + j*y_gap, W_SQUARE, H_SQUARE, R_SQUARE, tile_color)

    def drow_current_board(self, level):

        scale = int ((min(HEIGHT, WIDTH) - 2*OFFSET) / (H_SQUARE * level.getDimension()))
        x_gap = scale*W_SQUARE + GAP
        y_gap = scale*H_SQUARE + GAP
        x_start = (WIDTH - W_LEFT_MENU - 2*OFFSET) / 2 - (level.getDimension() * x_gap) / 2
        y_start = (HEIGHT - 2*OFFSET) / 2 - (level.getDimension() * y_gap) / 2

        # draw selected aquare
        i, j = level.getPosition()
        self.draw_rectangle(x_start + i*x_gap - 3, y_start + j*y_gap - 3, scale*W_SQUARE + 6, scale*H_SQUARE + 6, R_SQUARE, GREEN_COLOR)

        # draw the board
        for i in range(level.getDimension()):
            for j in range(level.getDimension()):
                tile = level.getValueAtCur(i, j)
                if tile is None:
                    continue
                elif tile == 'r':
                    tile_color = RED_COLOR
                elif tile == 'b':
                    tile_color = BLUE_COLOR
                elif tile == 'y':
                    tile_color = YELLOW_COLOR

                self.draw_rectangle(x_start + i*x_gap, y_start + j*y_gap, scale*W_SQUARE, scale*H_SQUARE, R_SQUARE, tile_color)
        


