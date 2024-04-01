import sys
from AI.ai import *

from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()

# if __name__ == "__main__":
#     sys.setrecursionlimit(3000)
#
#     level = Level(6)
#     ai = AI(level, AIS.ASTAR, H.PATTERN)
#
#     print(ai.moves)
#     print(ai.state.time)
