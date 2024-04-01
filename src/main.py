import sys
from AI.ai import *

from game import Game

'''
if __name__ == "__main__":
    game = Game()
    game.run()
'''

if __name__ == "__main__":
    sys.setrecursionlimit(3000)

    level = Level(21)
    ai = AI(level, AIS.ASTAR, H.MANHATTAN)

    print(ai.moves)
    print(ai.state.time)
