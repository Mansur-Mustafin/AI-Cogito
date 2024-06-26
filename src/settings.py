"""
File: settings.py
Description: This module defines various constants and settings used throughout the game.
"""

from pygame import USEREVENT
from enum import Enum, auto

ASTAR_WEIGHT = 1

# define display characteristics
WIDTH = 1280
HEIGHT = 720
FPS = 60
LEVELS_DIR = "levels/"
FONT_PATH = "assets/Comfortaa-Regular.ttf"
MUSIC_PATH = "assets/background_music.mp3"
BUTTON_SOUND = "assets/button_pressed.mp3"

# define ai settings
WAITING_TIME = 1000
TIMER_EVENT = USEREVENT + 1

# define used colors in game:
BACKGROUND_COLOR = (255, 255, 255)
WHITE_COLOR = (230, 230, 230)
RED_COLOR = (255, 99, 99)
BLUE_COLOR = (100, 100, 255)
YELLOW_COLOR = (255, 235, 98)
GREEN_COLOR = (74, 200, 73)
BLACK_COLOR = (0, 0, 0)

# define view GAME
GAP = 3
OFFSET = 25
W_SQUARE = 30
H_SQUARE = 30
R_SQUARE = 6

Y_LEFT_MENU = 25
W_LEFT_MENU = int(WIDTH / 256 * 85)
X_LEFT_MENU = WIDTH - Y_LEFT_MENU - W_LEFT_MENU
H_LEFT_MENU = HEIGHT - Y_LEFT_MENU - Y_LEFT_MENU
R_LEFT_MENU = 23

X_3COLORS = X_LEFT_MENU + 20
Y_3COLORS = Y_LEFT_MENU + 20

W_MISS = 15
H_MISS = 42
R_MISS = 6

# define view MENU
W_BUTTON = 250
H_BUTTON = 50
R_BUTTON = 20

ARROW_W = 40
ARROW_H = 40
ARROW_R = 20
ARROW_FONT_S = 30

ICONS_SIZE = 50
VIEW_ACTIONS_X = 270
VIEW_ACTIONS_Y = 15
ACTIONS_SPACE = 50

QUIT_X = 1075
QUIT_Y = 620


class Command(Enum):
    EXIT = auto()
    CHANGE_GAME_PLAYER = auto()
    CHANGE_GAME_PC = auto()
    CHANGE_MAIN = auto()
    CHANGE_LEVEL = auto()
    CHANGE_END = auto()
    CHANGE_HUERISTIC = auto()
