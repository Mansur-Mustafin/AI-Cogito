import yaml
from position import Position

class Level:

    DIRECTIONS = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    COLORS = {'r', 'b', 'y'}

    def __init__(self, lvl):
        with open("levels/level" + str(lvl) + ".yaml", 'r') as file:
            level_data = yaml.safe_load(file)
        
        self.dimension = level_data['dimension']
        self.target_pattern = level_data['target_pattern']
        self.current_block = level_data['initial_block']
        self.score = 0
        self.cur_pos = Position(0, 0)
    
    def isWin(self):
        return self.current_block == self.target_pattern
    
    def __isValidMove(self, x , y):
        return 0 <= self.cur_pos.getX() + x < self.dimension and \
               0 <= self.cur_pos.getY() + y < self.dimension
    
    def move(self, direction):

        if direction in Level.DIRECTIONS and self.__isValidMove(Level.DIRECTIONS[direction]):
            self.__move(Level.DIRECTIONS[direction])

        return 
     
    def __move(self, d_x, d_y):
        
        self.cur_pos.updatePosition(d_x, d_y)

        x, y = self.cur_pos.getCoordinates()
        orig_color = self.current_block[x][y]
        dest_color = self.current_block[x + d_x][y + d_y]

        third_color = Level.COLORS.difference({orig_color, dest_color})
        
        self.current_block[x + d_x][y + d_y] = third_color
    



