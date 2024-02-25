from settings import WIDTH, HEIGHT
from enum import Enum, auto
from .theme import *


VW = WIDTH/100
VH = HEIGHT/100

class ALIGNS_TYPES(Enum):
    VERTICAL_CENTER = auto()
    VERTICAL_START = auto()
    VERTICAL_END = auto()
    HORIZONTAL_CENTER = auto()
    HORIZONTAL_START = auto()
    HORIZONTAL_END = auto()

ALIGNS = {
    ALIGNS_TYPES.VERTICAL_CENTER: lambda self: (self.y == None) if  (HEIGHT- self.height)/2 else self.y,
    ALIGNS_TYPES.VERTICAL_START: lambda self: (self.y == None) if 0 else self.y,
    ALIGNS_TYPES.VERTICAL_END:lambda self: (self.y == None) if HEIGHT- self.height else self.y,
    ALIGNS_TYPES.HORIZONTAL_CENTER: lambda self:  (self.x == None) if (WIDTH- self.width)/2 else self.x,
    ALIGNS_TYPES.HORIZONTAL_START : lambda self: (self.x == None) if 0 else self.x,
    ALIGNS_TYPES.HORIZONTAL_END : lambda self: (self.x == None) if WIDTH - self.width else self.x,
}

class FLOATS_TYPES(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

FLOATS = {
    FLOATS_TYPES.TOP : lambda self, vy: self.y+vy, 
    FLOATS_TYPES.LEFT : lambda self, vx: self.x-vx,
    FLOATS_TYPES.RIGHT : lambda self, vx: self.x+vx,
    FLOATS_TYPES.BOTTOM : lambda self, vy: self.y+vy,
}

class STYLES(Enum):
    ALIGNS = auto()
    FLOATS = auto()
    BACKGROUND = auto()
    TEXT_COLOR = auto()
    FONT_SIZE = auto()

class Styles():
    def __init__(self, styles) -> None:
        self.defaul()
        if(styles[STYLES.ALIGNS]): self.aligns = styles[STYLES.ALIGNS]
        if(styles[STYLES.FLOATS]): self.floats = styles[STYLES.FLOATS]
        if(styles[STYLES.BACKGROUND]): self.background = styles[STYLES.BACKGROUND]
        if(styles[STYLES.TEXT_COLOR]): self.textColor = styles[STYLES.TEXT_COLOR]
        if(styles[STYLES.FONT_SIZE]): self.fontSize = styles[STYLES.FONT_SIZE]

    def defaul(self):
        self.aligns = []
        self.floats = []
        self.background = BACKGROUND_COLOR
        self.textColor = BLACK_COLOR
        self.fontSize = 13




    