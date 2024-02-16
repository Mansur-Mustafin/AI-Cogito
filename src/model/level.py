import yaml

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
        self.cur_pos = (0, 0)

        print(self.target_pattern)
    
    def getPosition(self):
        return self.cur_pos
    
    def getDimension(self):
        return self.dimension
    
    def getValueAtTarget(self, x, y):
        return self.target_pattern[x][y]
    
    def getValueAtCur(self, x, y):
        return self.current_block[x][y]
    
    def isWinCondition(self):
        return self.current_block == self.target_pattern

    def countMismatchedTiles(self):
        return sum(
        self.current_block[i][j] != self.target_pattern[i][j]
        for i in range(self.dimension)
        for j in range(self.dimension)
    )

    def move(self, direction):

        if direction in self.DIRECTIONS and self.__isValidMove(self.DIRECTIONS[direction]):
            d_x, d_y = self.DIRECTIONS[direction]
            x, y = self.cur_pos
            new_x, new_y = x + d_x, y + d_y

            orig_color = self.current_block[x][y]
            dest_color = self.current_block[new_x][new_y]

            third_color = (self.COLORS - {orig_color, dest_color}).pop()
            
            self.current_block[new_x][new_y] = third_color
            self.cur_pos = (new_x, new_y)
            self.score += 1

    def __isValidMove(self, d_x, d_y):
        new_x = self.cur_pos[0] + d_x
        new_y = self.cur_pos[1] + d_y
        return 0 <= new_x < self.dimension and \
               0 <= new_y < self.dimension and \
               self.current_block[new_x][new_y] != None
