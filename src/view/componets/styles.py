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
    ALIGNS_TYPES.VERTICAL_CENTER: lambda height: (HEIGHT- height)/2,
    ALIGNS_TYPES.VERTICAL_START: lambda _: 0,
    ALIGNS_TYPES.VERTICAL_END:lambda height: HEIGHT- height,
    ALIGNS_TYPES.HORIZONTAL_CENTER: lambda width: (WIDTH- width)/2,
    ALIGNS_TYPES.HORIZONTAL_START : lambda _: 0,
    ALIGNS_TYPES.HORIZONTAL_END : lambda width: WIDTH -width,
}

class FLOATS_TYPES(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

FLOATS = {
    FLOATS_TYPES.TOP : lambda y, vy: y+vy, 
    FLOATS_TYPES.LEFT : lambda x, vx: x-vx,
    FLOATS_TYPES.RIGHT : lambda x, vx: x+vx,
    FLOATS_TYPES.BOTTOM : lambda y, vy: y+vy,
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




    